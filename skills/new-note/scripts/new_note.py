#!/usr/bin/env python3
"""Create a Main Note in an Obsidian vault's Inbox, following its Unique Note Creator settings.

Usage: new_note.py --title TITLE [--tag TAG ...] [--vault PATH] [--body-stdin]

Prints the new note's path. On failure, exits non-zero with the reason on stderr.
"""
import argparse
import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

ID_FORMAT = "%Y%m%d%H%M"
# Inbox notes are `{id}`, filed notes `{cabinet}.{id}`; both carry the same timestamp.
NOTE_TIMESTAMP = re.compile(r"^(?:\d{3}\.)?(\d{12})$")
TEMPLATER_TAG = re.compile(r"<%[*_-]?\s*(.*?)\s*[_-]?%>", re.S)
DATE_CALL = re.compile(r"""^tp\.(file\.creation_date|date\.now)\(\s*(?:['"]([^'"]*)['"])?\s*\)$""")
DATE_DEFAULTS = {"file.creation_date": "YYYY-MM-DD HH:mm", "date.now": "YYYY-MM-DD"}
MOMENT_TO_STRFTIME = [("YYYY", "%Y"), ("MM", "%m"), ("DD", "%d"), ("HH", "%H"), ("mm", "%M"), ("ss", "%S")]
YAML_NEEDS_QUOTES = re.compile(r"""^[\s\-?:,\[\]{}#&*!|>'"%@`]|[:#]\s|\s#|\s$|^$""")


def fail(message):
    print(message, file=sys.stderr)
    sys.exit(1)


def yaml_string(value):
    # json.dumps output is a valid YAML double-quoted scalar.
    return json.dumps(value, ensure_ascii=False) if YAML_NEEDS_QUOTES.search(value) else value


def taken_timestamps(vault):
    taken = set()
    for path in vault.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(vault).parts):
            continue
        match = NOTE_TIMESTAMP.match(path.stem)
        if match:
            taken.add(match.group(1))
    return taken


def render_templater(text, note_id, now):
    unknown = []

    def render(match):
        expr = match.group(1)
        if expr == "tp.file.title":
            return note_id
        date = DATE_CALL.match(expr)
        if date:
            fmt = date.group(2) or DATE_DEFAULTS[date.group(1)]
            for token, directive in MOMENT_TO_STRFTIME:
                fmt = fmt.replace(token, directive)
            return now.strftime(fmt)
        unknown.append(expr)
        return ""

    return TEMPLATER_TAG.sub(render, text), unknown


def fill_frontmatter(lines, title, tags):
    """Fill the empty `title:`, first empty alias, and first empty tag the template leaves."""
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        key = re.match(r"^(title|aliases|tags):\s*$", line)
        next_is_empty_item = i + 1 < len(lines) and re.match(r"^(\s*)-\s*$", lines[i + 1])
        if key and key.group(1) == "title":
            out.append(f"title: {yaml_string(title)}")
        elif key and next_is_empty_item and key.group(1) == "aliases":
            out += [line, f"{next_is_empty_item.group(1)}- {yaml_string(title)}"]
            i += 1
        elif key and next_is_empty_item and key.group(1) == "tags" and tags:
            out += [line] + [f"{next_is_empty_item.group(1)}- {yaml_string(t)}" for t in tags]
            i += 1
        else:
            out.append(line)
        i += 1
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--title", required=True)
    parser.add_argument("--tag", action="append", default=[])
    parser.add_argument("--vault", default=".")
    parser.add_argument("--body-stdin", action="store_true", help="read the note body from stdin")
    args = parser.parse_args()

    title = args.title.strip()
    if not title:
        fail("The title is empty. Ask the user for the note's title.")

    vault = Path(args.vault).expanduser().resolve()
    if not (vault / ".obsidian").is_dir():
        fail(f"{vault} is not an Obsidian vault (no .obsidian/ folder). Ask the user for the vault path and pass it as --vault.")

    settings_path = vault / ".obsidian" / "zk-prefixer.json"
    try:
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        fail(f"Can't read {settings_path}. The Unique Note Creator core plugin isn't set up; ask the user which folder new notes go in and which template they use.")
    folder, template = settings.get("folder", "").strip(), settings.get("template", "").strip()
    if not folder or not template:
        fail(f"{settings_path} has no {'folder' if not folder else 'template'} set. Ask the user for it.")

    template_path = vault / f"{template}.md"
    if not template_path.is_file():
        fail(f"Template not found: {template_path}. Ask the user which template to use.")

    now = datetime.now()
    taken = taken_timestamps(vault)
    stamp = now
    while stamp.strftime(ID_FORMAT) in taken:
        stamp += timedelta(minutes=1)
    note_id = stamp.strftime(ID_FORMAT)

    rendered, unknown = render_templater(template_path.read_text(encoding="utf-8"), note_id, now)
    lines = rendered.rstrip("\n").split("\n")
    if lines and lines[0] == "---" and "---" in lines[1:]:
        end = lines.index("---", 1)
        lines = fill_frontmatter(lines[: end + 1], title, args.tag) + lines[end + 1 :]

    body = sys.stdin.read().strip() if args.body_stdin else ""
    content = "\n".join(lines) + f"\n\n# {title}\n\n" + (body + "\n" if body else "")

    note_path = vault / folder / f"{note_id}.md"
    note_path.parent.mkdir(parents=True, exist_ok=True)
    with note_path.open("x", encoding="utf-8") as f:
        f.write(content)

    for expr in unknown:
        print(f"Warning: left a Templater field empty that this script can't render: <% {expr} %>", file=sys.stderr)
    print(note_path)


if __name__ == "__main__":
    main()

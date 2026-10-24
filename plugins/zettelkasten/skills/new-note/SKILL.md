---
name: new-note
description: Capture a new idea as a Zettelkasten note (Main Note) in the Obsidian vault's Inbox, where the user reviews it before filing it into a cabinet. Use this whenever the user asks for a note for their zettelkasten ("I want a note for my zettelkasten", "create a note titled X for my zettelkasten"), or otherwise wants to capture an idea, concept, quote, or learning as a note, card, or zettel, in English or Spanish, even if they don't mention the Inbox. Not for journal entries, meeting notes, blog posts, book notes, or filing or moving notes that already exist.
---

# New note in the Inbox

The vault runs an Antinet-style Zettelkasten. Every new note lands in the Inbox first, and the user files it into a numbered cabinet by hand. That review is deliberate: it's where they decide where the idea belongs and what it connects to. So this skill only creates the note, and leaves filing, moving, renaming and indexing to the user.

## 1. Get the title

A note holds one idea, and its title names that idea. If the user didn't give a title, ask for it and nothing else. If what they gave holds several ideas, say so and ask which one this note is for, since each idea gets its own note.

## 2. Create the note

Run `scripts/new_note.py` from this skill's base directory, with the vault as the working directory:

```sh
python3 <skill-dir>/scripts/new_note.py --title "<title>" --tag "<tag>" --body-stdin <<'EOF'
<body>
EOF
```

Pass `--tag` once per tag the user gave, and leave it out if they gave none. Leave out `--body-stdin` and the heredoc if there's no body.

The script reads the Inbox folder and template from the vault's Unique Note Creator settings (`.obsidian/zk-prefixer.json`), picks a timestamp ID no other note in the vault uses, renders the template's Templater fields (Templater doesn't run on files created outside Obsidian), and prints the new note's path. Using it keeps every note consistent with the ones Obsidian creates.

If it exits with an error, the message says what's missing. Ask the user for that. If they give a vault path, pass it as `--vault`. If it prints a warning about a Templater field it couldn't render, tell the user which field was left empty.

## 3. The body

Write only what the user gave you. Don't add ideas, examples or explanations of your own. Writing a note in your own words is how this method turns reading into understanding, and any sentence the user didn't write is one they'd have to check and rewrite during review. Fixing typos and turning their words into a short list is fine. If they gave only a title, leave the body empty.

Keep the language the user wrote in. The vault mixes Spanish and English, and English technical terms usually stay in English.

## 4. Sources

Cite sources as footnotes at the end of the body, the way the existing notes do:

```markdown
Los LLMs no recuerdan nada entre conversaciones. [^1]

[^1]: [[Antinet Zettelkasten - Scott Scheper]]
```

- **A book or article:** link its note by exact filename, which you can find with `find . -name "<title>*.md" -not -path "./.*"`. A wikilink to a filename that doesn't exist creates an empty note when clicked, so if there's no match, write the plain title and tell the user.
- **Another Zettelkasten note:** link by filename with its title as the display name, e.g. `[[600.202602232212|LLMs are Stateless]]`. Check the ID belongs to the note you mean, and never link a note to itself.
- **A URL:** paste it as-is.

## 5. Report

Reply with the new note's path in one line. Don't offer to file or index it; the user does that during review.

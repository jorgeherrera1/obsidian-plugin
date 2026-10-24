# antinet

A Claude Code plugin with skills for running an Antinet-style Zettelkasten in an Obsidian vault.

## Skills

- **new-note**: creates a Main Note in the vault's Inbox for you to review. It reads the Inbox folder and template from Obsidian's Unique Note Creator settings and never files the note for you.

## Use

Requires Python 3 and a vault with the Unique Note Creator core plugin set up.

```sh
git clone https://github.com/jorgeherrera1/obsidian-plugin.git
cd /path/to/your/vault
claude --plugin-dir /path/to/obsidian-plugin
```

Then ask: "Create a note titled … for my zettelkasten".

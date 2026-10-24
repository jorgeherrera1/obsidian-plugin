# zettelkasten

A Claude Code and Cursor plugin with skills for running an Antinet-style Zettelkasten in an Obsidian vault.

## Skills

- **new-note**: creates a Main Note in the vault's Inbox for you to review. It reads the Inbox folder and template from Obsidian's Unique Note Creator settings and never files the note for you.

## Install

Requires Python 3 and a vault with the Unique Note Creator core plugin set up.

### Claude Code

```sh
claude plugin marketplace add jorgeherrera1/obsidian-plugin
claude plugin install zettelkasten@jorgeherrera1
```

### Cursor

Import this repository as a team marketplace (Dashboard → Settings → Plugins), then install `zettelkasten` from it.

To try it without a marketplace, copy `plugins/zettelkasten` to `~/.cursor/plugins/local/zettelkasten` and reload the window.

## Use

Open your vault and ask: "Create a note titled … for my zettelkasten".

## Develop

The plugin lives in `plugins/zettelkasten`. Load it from a clone without installing:

```sh
cd /path/to/your/vault
claude --plugin-dir /path/to/obsidian-plugin/plugins/zettelkasten
```

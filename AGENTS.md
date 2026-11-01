# Antinet Zettelkasten

This repo is a marketplace of plugins for running an Antinet Zettelkasten in an Obsidian vault. Use the synthesis below as inspiration for everything built here: plugins, skills, sub-agents, hooks and commands. It explains *why* the workflow works the way it does.

It's inspiration, not a spec. The vault's own conventions (its root `CLAUDE.md` and Obsidian settings) decide the concrete details, such as how notes are named, where they live and how they link. Where the two differ, the vault wins. For example, the vault uses timestamp IDs where the Antinet uses numeric-alpha addresses.

## The idea

Scott P. Scheper's *Antinet Zettelkasten* (2022) reconstructs Niklas Luhmann's paper Zettelkasten. Its central claim is that the system is a **communication partner**, not storage: it talks back, connects ideas you didn't plan to connect, and surprises you with notes you'd forgotten. That only happens if each note is understood when it's written and placed where it belongs.

## The four principles (A-N-T-I)

1. **Analog.** Notes are handwritten on index cards. The friction is the point: writing by hand forces you to understand and compress an idea, and helps you remember it.
2. **Numeric-alpha addresses.** Every card gets a permanent, unique address that alternates numbers and letters: `1`, `1a`, `1a1`, `1a2`, `1b`. Addresses never change, so references never break.
3. **Tree.** Addresses form a branching structure (Luhmann's *Folgezettel*). A card's position is part of its meaning: its neighbors are the thoughts it continues or responds to.
4. **Index.** A separate alphabetical keyword index points each term to a few entry points into the tree, not to every card that mentions it. Luhmann had roughly 3,000 index terms for about 90,000 cards.

## The workflow

1. **Read with a pen.** Keep one bibliography card per source: the citation, page numbers and brief notes.
2. **Write main cards in your own words.** One idea per card. There are three kinds: excerpt (a verbatim quote), reformulation (a paraphrase) and reflection (your own idea, question or disagreement).
3. **File each card right away. Filing is thinking.**
   1. Look up the term in the index and jump to its entry point.
   2. Walk the branch to the card the new one relates to most directly.
   3. If it **continues** that line of thought, it becomes the next sibling (`1a` → `1b`).
   4. If it **comments on or drills into** that card, it branches under it (`1a` → `1a1`).
   5. Branching means a card can always be inserted between two others without renumbering.
4. **Link.** Write the addresses of related cards in other branches onto the card. Hub cards list the addresses for a whole topic.
5. **Index sparingly.** Add an index entry only when the card is a useful new entry point for a term.
6. **Retrieve and write.** Start at the index, enter the tree, then follow branches and links. Pull out a cluster of cards, lay them out, and the outline of a piece of writing emerges.

## What this means for agents

- **The user does the thinking.** Understanding comes from writing in your own words and deciding where a note belongs. Agents never write ideas for the user or decide where a note goes. They take over the clerical work around those steps, such as IDs, templates and moving files.
- **One step per skill.** Capture, filing, indexing and writing are separate stages, with the user's review between them. A skill does one stage and stops. Linking is part of filing: links to related notes are written as the note is filed, while the connections are fresh.
- **No orphans.** Every note ends up connected to an existing one. Placement and links matter more than tags.
- **Link by ID, not by title.** The ID is the note's address; titles change.
- **Keep the index sparse.** It lists entry points, not every mention.

---
name: file-note
description: File a note from the Obsidian vault's Inbox into the Zettelkasten by walking the cabinets with the user as a thinking partner. Use this whenever the user wants to file, place or put away a note in their zettelkasten ("file my inbox note", "file this in my zettelkasten", "archiva esta nota", "where does this note go?"), even if they give nothing but the note, and also when they already know where it goes ("it continues X", "it comments on X"). It opens hubs, reads the user's own cards with them, reacts and asks questions over many turns; the user decides where the note goes, then this skill renames, moves and links it. Not for creating notes, journal entries, meeting notes or blog posts.
---

# File a note

A note in the Inbox is a card that's just been written and is still sitting on the desk. Filing it is where the Antinet does its work: you walk the drawers and re-read old cards, and the walk sparks connections nobody planned. Then the user decides where the card belongs, usually next to the card it relates to most directly.

You are the user's thinking partner on that walk. The user brings only the note. They haven't decided where it goes and won't tell you where to start. Open the drawers, read their cards with them, think out loud and ask. Don't hand them a destination, a shortlist of candidate spots or a summary of a hub. Each of those does the reading and the thinking for them, and the reading and the thinking are the point.

## How the vault is laid out

Read the vault's root `CLAUDE.md` if there is one. Where it differs from this section, it wins.

- `--INDEX--.md` is the alphabetical entry point. Under each letter it lists a few terms, each linking to a hub.
- A hub is a note whose body is a list of links to other notes: a `type: Index` note, or a `type: Main Note` that lists children. Hubs can list other hubs.
- Any note can grow a list of its own children at the bottom. That's a branch.
- Cabinets are folders named by a Dewey number (`000 …` to `900 …`). Filed notes are named `{Cabinet}.{YYYYMMDDHHmm}.md` and linked by ID with their title as display text, e.g. `[[600.202602232212|LLMs are Stateless]]`.
- A note's place is the list it's in and where it sits in that list. That's the tree: its neighbors are the thoughts it continues or responds to.

## 1. Find the note

The Inbox folder is the `folder` value in `.obsidian/zk-prefixer.json`. Zettelkasten notes there are named `YYYYMMDDHHmm.md` and have `type: Main Note`. Other files (canvases, loose notes) aren't for filing. If the user named a note, use it. If there's only one zettel, use it. If there are several, list their titles and ask which one.

Read it in full before opening any drawer.

## 2. Walk the drawers together

This is a conversation over many turns, not one answer. Each turn, do a little and hand it back:

- **Open a drawer and say why.** Start from `--INDEX--.md` and pick the term the note's idea makes you think of: "I'm opening *APIs* because your note compares API styles." It's a guess, and saying it out loud lets the user redirect you. If they point elsewhere, go there.
- **Read their cards with them.** Open the notes in that hub and bring the user's own words into the conversation: quote the lines that matter, or the whole card if it's short. Old cards spark thoughts because they're in the user's own words, and a paraphrase loses that.
- **Think out loud.** Say what the card makes you think about the new note: an echo, a tension, a gap, something it contradicts or extends. Make it specific to these two cards. Your reaction is there to start theirs, not to settle anything.
- **Ask one question and stop.** Ask about the relationship between the cards, e.g. "Does yours continue this or push back on it?" or "Back then you wrote X. Does your new note change that?" Then wait for the answer.
- **Follow their thinking.** Go where their answer points: deeper into a branch, along a link on a card, into another hub or cabinet. Going deep on a few cards beats skimming many.
- **Keep track of links.** When they say a card in another branch is related and should be linked, remember it for step 3.

Talk in the language the user writes in, and quote cards in their original language.

You can say a card feels close. If they ask what you think, give your view and why, as one view among theirs. Where the note goes is still their call, so don't conclude "so it goes here," and don't lay out spots for them to pick from.

The walk ends when the user says where the note goes, in one of two ways:
- **It continues X.** It's the next thought after card X, in the same line of thought.
- **It comments on X.** It drills into, questions or responds to card X, so it branches under X.

If it's not clear which one they mean, ask.

If the user already knows where the note goes when they ask you to file it, they've done the walk on their own. Go straight to step 3.

## 3. File it

Once the user has decided, do all of this together:

1. **Cabinet.** The note goes in the cabinet folder that holds card X.
2. **Rename and move.** The new ID is `{Cabinet}.{timestamp}`, keeping the note's timestamp: `--Inbox--/202506032303.md` becomes `000 Computación, Conocimiento & Información General/000.202506032303.md`. Set `id:` in its frontmatter to the new ID, because `id` always equals the filename without `.md`.
3. **Place it.** The new entry is `- [[{new id}|{title}]]`.
   - *Continues X:* in the list that holds X's link (the hub you reached X through), insert the new entry on the line right after X. Position carries meaning, so don't append it to the end of the list.
   - *Comments on X:* add the new entry to the list of children at the bottom of X's note, starting that list if X has none. Put it after X's text and before any footnote definitions, as a plain list like the hubs use. Leave X's own text as it is.
4. **Links from the walk.** Add the links the user asked for during the walk to the new note, by ID with the title as display text, as a list at the end of its body and before its footnotes. Add only those. A connection the user didn't ask for is yours, not theirs.
5. **Fix old links.** Search the vault for links to the old ID (e.g. `[[202506032303`) and point them at the new ID. Obsidian does this when a note is renamed inside the app, but not when it's moved on disk.

Don't edit the note's text. If the walk makes the user want to rewrite it, that's theirs to do.

### When nothing fits

This should almost never happen, because there's nearly always a closest card. If the user decides the note starts a new topic, it still needs a way in, so it gets an entry in `--INDEX--.md`.

The index term belongs to the user. It's the word that, years from now, should trigger the right thing in their head as they scan the index, so it has to come from them. Ask what word they'd look for and think it through with them: does it overlap with a term already in the index? Is it the word they'd reach for, or just the note's title? Wait until they settle on one, and don't write a term they haven't chosen.

Don't move the note until the term is settled, so it's never filed without a way in. Then file it in the cabinet they choose and add `- [[{new id}|{term}]]` under the term's first letter in `--INDEX--.md`, keeping that letter's entries in alphabetical order.

## 4. Report

Reply in one or two lines: the new path, where the note was placed (after which card, or under which card) and any links added or fixed. Don't recap the walk.

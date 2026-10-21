# Briefings — AI Instructions

One-off briefings on AI, ML, security, data analytics and dev topics. Each one covers a single concept, incident or technique in a few minutes of reading. Published free by SophiArch at `https://sophiarch.github.io/Briefings/` and links back to [lms.sophiarch.com](https://lms.sophiarch.com).

This repo sits in the `SophiArchSite.code-workspace`. Brand, voice and audience rules come from `../SophiArchSite/.claude/branding.md` and `../SophiArchSite/CLAUDE.md`: adult professionals, plain and direct language, Dracula palette.

## Layout

- `<Topic>/<Name>.md` is the source, a Marp deck. Topic folders use PascalCase (`Agent`, `Cybersecurity`, `Development`, ...). File names use `Snake_Case`.
- `<Topic>/<Name>.html` and `<Topic>/<Name>.pdf` are the exported copies, committed next to the source. GitHub Pages serves the HTML.
- Images go in `<Topic>/Images/`.
- `README.md` is generated. Don't edit it by hand: change `front.md` (intro) or `bottom.md` (footer) and regenerate.

## Deck front matter

Copy it from an existing deck (for example `Agent/AI_Agent_as_Data_Scientist.md`): `marp: true`, `theme: dracula`, `size: 16:9`, `paginate: true`, `author`, a `header` with the briefing title, and the footer `© <year> SophiArch [lms.sophiarch.com](https://lms.sophiarch.com)`.

## Workflow

1. Write or edit the `.md` deck. The `marp_gen` skill handles slide drafts and `excalidraw-skill` handles diagrams.
2. Export it to `.html` and `.pdf` beside the source.
3. Rebuild the index with `uv run src/index.py`. It picks up every `.html` under a topic folder.
4. Commit the source, the exports and `README.md` together.

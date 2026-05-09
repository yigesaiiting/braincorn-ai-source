# AI_README — Codex Execution Spec

This repository is the Braincorn knowledge vault.

Codex should treat this repo as a layered knowledge system, not a flat note dump.

## Operating principle

Always prefer:

1. read existing knowledge
2. update the smallest correct page
3. preserve source hierarchy
4. avoid rewriting raw inputs
5. leave a clear trail of changes

## Vault layers

- `00_Inbox/` — temporary intake only
- `10_Raw/` — raw source material; do not rewrite unless explicitly asked
- `20_Wiki/` — durable knowledge pages
- `30_Projects/` — active workstreams and project context
- `40_Decisions/` — judgments, decisions, and postmortems
- `50_Outputs/` — reports, PRDs, essays, reviews, deliverables
- `90_System/` — rules, prompts, templates, guides, navigation

## Read order

When answering a question or making an edit, read in this order:

1. The relevant index pages
2. The most specific existing page
3. Related project / decision pages
4. Related outputs
5. Raw sources only if verification is needed

Recommended index pages:

- `20_Wiki/Index.md`
- `30_Projects/Index.md`
- `40_Decisions/Index.md`
- `50_Outputs/Index.md`
- `90_System/Index.md`

## Writing rules

- Do not rewrite `10_Raw/` unless explicitly asked.
- If a formal page is needed, write to the appropriate layer:
  - concept/company/person/playbook/product → `20_Wiki/`
  - ongoing initiative → `30_Projects/`
  - judgment / postmortem → `40_Decisions/`
  - finished deliverable → `50_Outputs/`
- Use YAML frontmatter for formal pages whenever possible.
- Use Obsidian wiki-links for internal references.
- If information is uncertain, label it `需要验证`.
- If information is missing, label it `资料不足`.

## Market-content rules

For market or trading material, always separate:

- facts
- inference
- catalysts
- risks
- trade plan / observation
- conditions not suitable for entry

## XingYu-content rules

For XingYu-related material, always separate:

- user insights
- product features
- growth paths
- partnerships
- execution SOPs
- current bottleneck

## Decision rules

When a new judgment appears, capture it in `40_Decisions/` and link it back to:

- the relevant wiki page
- the relevant project page
- the relevant output, if any

## Output rules

If you produce a report, PRD, essay, outline, or review:

- store it in `50_Outputs/`
- backlink to the pages it updates
- if a lasting conclusion emerged, also update the relevant wiki or decision page

## Editing discipline

- Make the smallest correct change.
- Avoid unrelated refactors.
- Preserve existing formatting and frontmatter unless there is a reason to update it.
- Do not delete content unless explicitly requested or clearly broken.
- If a rename/move is needed, preserve discoverability with redirect notes or aliases when appropriate.

## File naming

- Keep existing vault naming conventions when possible.
- Prefer `Index.md` for index pages.
- Prefer descriptive names for durable notes.
- For dated decisions and outputs, include the date in the filename.

## Required response structure

When Codex answers using this vault, prefer:

1. Conclusion
2. Evidence
3. Risks / caveats
4. Next actions

## If you discover new durable knowledge

After answering, determine whether the result should be reflected in:

- a `20_Wiki/` page
- a `30_Projects/` page
- a `40_Decisions/` page
- a `50_Outputs/` page

If yes, update the smallest relevant page.

## Helpful entry points

- `90_System/Vault Map.md`
- `90_System/README.md`
- `90_System/使用说明.md`
- `90_System/Git 使用说明.md`


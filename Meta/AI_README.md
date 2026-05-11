# Braincorn Vault AI Execution Spec

This file is the formal AI operating manual for the Braincorn vault.

## Entry points

Read these first:

1. `README.md`
2. `INDEX.md`
3. `Meta/README.md`
4. `Meta/Index.md`

Then follow the relevant section index:

- `Wiki/Index.md`
- `Projects/Index.md`
- `Resolutions/Index.md`
- `Outputs/Index.md`
- `Meta/AI_Workflows/Index.md`
- `Meta/Knowledge_Rules/Index.md`
- `Meta/Prompts/Index.md`
- `Meta/Templates/Index.md`

## Operating principle

Always prefer:

1. read existing knowledge
2. update the smallest correct page
3. preserve source hierarchy
4. avoid rewriting raw inputs
5. leave a clear trail of changes

## Root entry policy

- `README.md`, `INDEX.md`, and `AI_README.md` at the vault root are thin shims.
- Their job is to route readers and tools into `Meta/`.
- The substantive rules live in this file and the other `Meta/` pages.

## Vocabulary map

- **Resolutions** = personal judgments, decisions, reversals, tradeoffs, and postmortems
- **Meta** = rules, workflows, templates, indexes, and vault operating instructions
- **Projects** = active workstreams and ongoing initiatives
- **Wiki** = durable reusable knowledge
- **Raw** = source material and capture logs
- **Outputs** = finished deliverables and reviews

## Vault layers

- `Inbox/` — temporary intake only
- `Raw/` — raw source material; do not rewrite unless explicitly asked
- `Wiki/` — durable knowledge pages
- `Projects/` — active workstreams and project context
- `Projects/Daily_Plans/` — daily work plans
- `Resolutions/` — resolutions, judgments, reversals, and postmortems
- `Outputs/` — reports, PRDs, essays, reviews, deliverables
- `Outputs/Daily_Reports/` — daily reports
- `Meta/` — rules, prompts, templates, guides, navigation

## Read order

When answering a question or making an edit, read in this order:

1. `README.md`
2. `INDEX.md`
3. The relevant section index
4. The most specific existing page
5. Related project / resolution pages
6. Related outputs
7. Raw sources only if verification is needed

## Writing rules

- Do not rewrite `Raw/` unless explicitly asked.
- If a formal page is needed, write to the appropriate layer:
  - concept/company/person/playbook/product → `Wiki/`
  - ongoing initiative → `Projects/`
  - resolution / postmortem → `Resolutions/`
  - finished deliverable → `Outputs/`
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

## Resolution rules

When a new resolution appears, capture it in `Resolutions/` and link it back to:

- the relevant wiki page
- the relevant project page
- the relevant output, if any

## Output rules

If you produce a report, PRD, essay, outline, or review:

- store it in `Outputs/`
- backlink to the pages it updates
- if a lasting conclusion emerged, also update the relevant wiki or resolution page

## Daily workflow

- Write daily work plans in `Projects/Daily_Plans/`
- Write daily reports in `Outputs/Daily_Reports/`
- Keep the day’s plan and report linked to each other when possible

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
- For dated resolutions and outputs, include the date in the filename.

## Required response structure

When answering using this vault, prefer:

1. Conclusion
2. Evidence
3. Risks / caveats
4. Next actions

## If you discover new durable knowledge

After answering, determine whether the result should be reflected in:

- a `Wiki/` page
- a `Projects/` page
- a `Resolutions/` page
- a `Outputs/` page

If yes, update the smallest relevant page.

## Helpful entry points

- `README.md`
- `INDEX.md`
- `Meta/README.md`
- `Meta/Index.md`
- `Meta/Vault Map.md`
- `Meta/使用说明.md`
- `Meta/Git 使用说明.md`

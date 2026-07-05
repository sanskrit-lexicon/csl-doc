# csl-doc

_Created: 22-06-2026 · Last updated: 05-07-2026_

The Cologne Digital Sanskrit Dictionaries span 40+ dictionaries, each with
its own scan-source quirks, markup conventions, and installation history —
too much for tribal knowledge alone. csl-doc is the project's **Sphinx-built
documentation site**: the maintainers' and contributors' reference for how
each dictionary was digitized, how the local dev environment is set up, and
how new dictionaries (LRV, ABCH, AP, …) get added to the docs.

This is genuinely a thin, docs-only repo — there is no application logic
here, only a Sphinx `source/` tree and its generated `build/` output. That
is by design, not a gap.

## Structure

| Path | Role |
|---|---|
| [source/](source) | Sphinx documentation source (`.rst` files, `conf.py`) |
| [build/](build) | Generated HTML output of `sphinx-build` |
| [Makefile](Makefile) / [make.bat](make.bat) | Standard Sphinx build entry points |
| [readme_dev.md](readme_dev.md) | Full dev-environment setup log (Windows/XAMPP, virtualenv, sphinx versions) |
| [readme_dev_ap.md](readme_dev_ap.md) | Same, specifically for adding the AP dictionary's docs |
| [move_images.py](move_images.py) | Utility to relocate images into the Sphinx source tree |

## Usage example — the real CI/build command, read from source

This repo has no CI workflow file; the actual documented build command
(copied verbatim from [readme_dev.md](readme_dev.md), not invented) is:

```bash
# be sure the 'myenv' virtualenv is activated, csl-doc is the current directory
sphinx-build -b html source build
```

That regenerates `build/index.html` from the `.rst` sources under
`source/`. Adding a new dictionary's docs follows the same pattern
documented for LRV and ABCH in [readme_dev.md](readme_dev.md): drop the
front/end-matter PDFs, add an `index.rst` entry, write the dictionary's
`.rst` page, rebuild, push.

## Issues overview

Snapshot 2026-05-29: **2** open, **4** closed.

| Milestone | Open | Closed | Total |
|---|---:|---:|---:|
| User Experience | 1 | 0 | 1 |
| Developer Experience | 1 | 0 | 1 |

Open by type: enhancement 1 · documentation 1. By severity: minor 1 · trivial 1.

## GitHub issue conventions

Follows the [Cologne tooling-repo taxonomy](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-tooling-runbook.md):

- **17 type labels** across 5 categories
- **4 severity levels**: trivial, minor, major, critical
- **5 milestones**: API Stability, User Experience, Data Quality, Developer Experience, Community
- **Domain labels** scoped to web-frontend: `domain:ui`, `domain:routing`, `domain:i18n`, `domain:rendering`
- **Org Project**: [Tooling Roadmap](https://github.com/orgs/sanskrit-lexicon/projects/9)

See [CLAUDE.md](CLAUDE.md) for full definitions.

---

_Dr. Mārcis Gasūns_

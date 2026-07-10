# csl-doc

_Created: 22-06-2026 · Last updated: 11-07-2026_

The Cologne Digital Sanskrit Dictionaries span 40+ dictionaries, each with
its own scan-source quirks, markup conventions, and installation history —
too much for tribal knowledge alone. csl-doc is the project's **Sphinx-built
documentation site**: the maintainers' and contributors' reference for how
each dictionary was digitized, how the local dev environment is set up, and
how new dictionaries (LRV, ABCH, AP, …) get added to the docs.

This is a thin, docs-only repo — there is no application logic here, only a
Sphinx [`source/`](https://github.com/sanskrit-lexicon/csl-doc/tree/main/source)
tree and its generated
[`build/`](https://github.com/sanskrit-lexicon/csl-doc/tree/main/build) output.
That is by design, not a gap. (Note: the mechanical tooling-runbook once tagged
this repo `web-frontend`; it hosts no front-end — it is documentation.)

Beyond the prose docs, the repo also holds the **`csldoc` front-matter scans**
(dictionary title pages, prefaces, abbreviation lists). Those scans are an
upstream data source: they feed the
[`/cologne-preface-ocr`](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-tooling-runbook.md)
workflow and the `prefaces_*` OCR-staging repos (e.g. `prefaces_ieg` over the
IEG scans). See
[`Uprava/PROJECT_INTERLINKS.md`](https://github.com/gasyoun/Uprava/blob/main/PROJECT_INTERLINKS.md)
for the full data-flow map.

## Structure

| Path | Role |
|---|---|
| [source/](https://github.com/sanskrit-lexicon/csl-doc/tree/main/source) | Sphinx documentation source — `conf.py` plus one `.rst` page per dictionary under [source/dictionaries/](https://github.com/sanskrit-lexicon/csl-doc/tree/main/source/dictionaries) |
| [build/](https://github.com/sanskrit-lexicon/csl-doc/tree/main/build) | Generated HTML output of `sphinx-build` |
| [Makefile](https://github.com/sanskrit-lexicon/csl-doc/blob/main/Makefile) / [make.bat](https://github.com/sanskrit-lexicon/csl-doc/blob/main/make.bat) | Standard Sphinx build entry points |
| [readme_dev.md](https://github.com/sanskrit-lexicon/csl-doc/blob/main/readme_dev.md) | Full dev-environment setup log (Windows/Gitbash, virtualenv, Sphinx versions) |
| [readme_dev_ap.md](https://github.com/sanskrit-lexicon/csl-doc/blob/main/readme_dev_ap.md) | Same, specifically for adding the AP dictionary's docs |
| [move_images.py](https://github.com/sanskrit-lexicon/csl-doc/blob/main/move_images.py) | Utility to relocate images into the Sphinx source tree |

## Build

The documented build command (copied verbatim from
[readme_dev.md](https://github.com/sanskrit-lexicon/csl-doc/blob/main/readme_dev.md),
not invented) — with the `myenv` virtualenv activated and `csl-doc` as the
current directory:

```bash
sphinx-build -b html source build
```

That regenerates `build/index.html` from the `.rst` sources under `source/`.
Adding a new dictionary's docs follows the same pattern documented for LRV and
ABCH in
[readme_dev.md](https://github.com/sanskrit-lexicon/csl-doc/blob/main/readme_dev.md):
drop the front/end-matter PDFs, add an `index.rst` entry, write the
dictionary's `.rst` page, rebuild, push.

## CI

Two GitHub Actions workflows run on this repo (there is no Sphinx build check
in CI — the build is run locally per the section above):

- [readme-guard.yml](https://github.com/sanskrit-lexicon/csl-doc/blob/main/.github/workflows/readme-guard.yml)
  — fails a PR only if a hand-maintained `<!-- BEGIN/END MANUAL: … -->` README
  block present on the base branch is dropped; a no-op while no such block
  exists.
- [dependabot-auto-merge.yml](https://github.com/sanskrit-lexicon/csl-doc/blob/main/.github/workflows/dependabot-auto-merge.yml)
  — hands-off approve + squash-merge of Dependabot PRs once checks pass.

## Issues overview

Snapshot 2026-07-11: **2** open, **4** closed.

| Milestone | Open | Closed | Total |
|---|---:|---:|---:|
| User Experience | 1 | 0 | 1 |
| Developer Experience | 1 | 0 | 1 |

Open by type: enhancement 1 · documentation 1. By severity: minor 1 · trivial 1.

## GitHub issue conventions

Follows the [Cologne tooling-repo taxonomy](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-tooling-runbook.md):

- **9 type labels**: `bug`, `feature`, `enhancement`, `performance`, `tech-debt`, `security`, `documentation`, `infrastructure`, `question`
- **4 severity levels**: trivial, minor, major, critical
- **5 milestones**: API Stability, User Experience, Data Quality, Developer Experience, Community
- **Domain labels** scoped to this repo's docs/rendering, e.g. `domain:rendering`
- **Org Project**: [Tooling Roadmap](https://github.com/orgs/sanskrit-lexicon/projects/9)

See [CLAUDE.md](https://github.com/sanskrit-lexicon/csl-doc/blob/main/CLAUDE.md) for full definitions.

---

_Dr. Mārcis Gasūns_

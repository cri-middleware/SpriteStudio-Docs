# AGENTS.md

This file provides guidance to coding agents when working with code in this repository.

## What this repo is

A **documentation portal** (MkDocs + Material) for the SpriteStudio SDK and its official
players. It is a lightweight hub, **not** a mirror of each player's docs: every player keeps
its own site in its own repository. This portal hosts only the unified entry point and the
**cross-cutting** material that belongs to no single player — the landing page, the ecosystem
overview, shared SDK concepts, the format specification, and licensing.

Consequence for edits: player pages under `docs/*/players/` are intentionally **thin** — a
short description plus links out to that player's own docs and GitHub repo. Do not expand them
into full player documentation; that content lives in the player's own repository.

## Commands

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r docs/requirements.txt

.venv/bin/mkdocs serve           # live preview at http://127.0.0.1:8000
.venv/bin/mkdocs build --strict  # exactly what CI runs; fails on broken links / missing nav
```

Always validate with `.venv/bin/mkdocs build --strict` before finishing — CI (`.github/workflows/pages.yml`)
runs the same command on every PR and blocks merge on any broken internal link or nav mismatch.
Deployment is **manual**: publishing is triggered by running the workflow (`workflow_dispatch`),
which builds the site and deploys it via the GitHub Pages deployment API (OIDC) — no `gh-pages`
branch and no `contents: write`. Merging to `main` does **not** auto-publish.

## Architecture & conventions

- **Folder-based i18n** (`mkdocs-static-i18n`, `docs_structure: folder`). Every page exists
  twice: `docs/en/<path>` and `docs/ja/<path>`. When you add, move, or rename a page, do it in
  **both** `en/` and `ja/`, or the strict build breaks. English is the default/fallback locale.
- **Navigation is defined once** in `mkdocs.yml` under `nav:` using locale-relative paths (e.g.
  `players/unity.md`, no `en/` or `ja/` prefix). Japanese nav labels come from the
  `plugins.i18n.languages` → `nav_translations` map, **not** from the file tree — add a matching
  `nav_translations` entry whenever you introduce a new nav title.
- **Content lives in three folders** under each locale: `overview/` (ecosystem, platform
  choice, feature support, browser demos, and the asset-conversion overview + standalone tools),
  `sdk/` (canonical cross-player concepts, glossary, format spec, shared limitations, porting), and
  `players/` (thin entry pages) — plus `index.md`, `support.md`, and `license.md` at the locale
  root. Note: `nav` surfaces `overview/` under **two** top-level sections — 🗺️ Overview and
  🔄 Converting Assets — so a new Overview page can belong to either.
- **Cross-cutting claims must be sourced from the sibling repos**, since this portal owns no
  code. `sdk/limitations.md` summarizes the SDK's Player Porting Guide (`libs/ssruntime/docs`,
  *Introduction → Limitations*); `overview/feature-support.md` reports only what each player's
  own docs state, and says so — do not infer support or non-support that no repo documents.
- **No facts that need tracking across repos.** Version numbers, engine/runtime requirement
  tables, per-project license identifiers, and schema-compatibility matrices are deliberately
  *not* hosted here: they would have to be chased across seven repositories. Let each project
  state them in its own docs and link out instead.
- **Internal links are relative file paths** ending in `.md` (e.g. `../sdk/concepts.md`), which
  is what `--strict` validates. External player docs are absolute `https://…` URLs. Link sibling
  repos at the **repository root**, not `blob/main/...` paths into their docs — SSPlayerForGodot,
  SSPlayerForRenPy, and SSPlayerForUnity default to `develop` and `main` may not carry `docs/`,
  so such a link 404s silently (`--strict` validates internal links only).
- **"Coming soon" gating**: player docs sites, live demos, and the hosted `ssconverter-web`
  are GitHub Pages URLs (`cri-middleware.github.io/…`) that 404 until each is deployed, so those
  outbound links are neutralized to plain **"coming soon" / "準備中"** text (no hyperlink) in
  both locales. `github.com/cri-middleware/…` **repo** links stay live as forward-links. When a
  site ships, restore its link in `en/` and `ja/` together.
- **Landing page cards** (`index.md`) use Material "grid cards" — they depend on the
  `attr_list`, `md_in_html`, and `pymdownx.emoji` markdown extensions already configured in
  `mkdocs.yml`. Icon shortcodes like `:material-unity:` render to SVG via those extensions.
- **Pinned toolchain**: `docs/requirements.txt` versions are deliberately pinned and kept in
  sync with the per-player repos (SSPlayerForUnity, SSPlayerForRenPy). Bump intentionally.

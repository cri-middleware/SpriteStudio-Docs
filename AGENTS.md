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
python -m venv .venv && source .venv/bin/activate
pip install -r docs/requirements.txt

mkdocs serve           # live preview at http://127.0.0.1:8000
mkdocs build --strict  # exactly what CI runs; fails on broken links / missing nav
```

Always validate with `mkdocs build --strict` before finishing — CI (`.github/workflows/docs.yml`)
runs the same command and blocks merge on any broken internal link or nav mismatch. On push to
`main`, CI also runs `mkdocs gh-deploy` to publish to the `gh-pages` branch.

## Architecture & conventions

- **Folder-based i18n** (`mkdocs-static-i18n`, `docs_structure: folder`). Every page exists
  twice: `docs/en/<path>` and `docs/ja/<path>`. When you add, move, or rename a page, do it in
  **both** `en/` and `ja/`, or the strict build breaks. English is the default/fallback locale.
- **Navigation is defined once** in `mkdocs.yml` under `nav:` using locale-relative paths (e.g.
  `players/unity.md`, no `en/` or `ja/` prefix). Japanese nav labels come from the
  `plugins.i18n.languages` → `nav_translations` map, **not** from the file tree — add a matching
  `nav_translations` entry whenever you introduce a new nav title.
- **Content lives in three areas** under each locale: `overview/` (ecosystem, platform choice,
  conversion), `sdk/` (canonical cross-player concepts, format spec, porting guide), and
  `players/` (thin entry pages).
- **Internal links are relative file paths** ending in `.md` (e.g. `../sdk/concepts.md`), which
  is what `--strict` validates. External player docs are absolute `https://…` URLs.
- **Landing page cards** (`index.md`) use Material "grid cards" — they depend on the
  `attr_list`, `md_in_html`, and `pymdownx.emoji` markdown extensions already configured in
  `mkdocs.yml`. Icon shortcodes like `:material-unity:` render to SVG via those extensions.
- **Pinned toolchain**: `docs/requirements.txt` versions are deliberately pinned and kept in
  sync with the per-player repos (SSPlayerForUnity, SSPlayerForRenPy). Bump intentionally.

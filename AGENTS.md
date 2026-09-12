# AGENTS.md

## Operating rules

*   Keep changes scoped to the requested task.
*   Do not commit, push, or open PRs unless the user explicitly asks.
*   Before editing, read enough surrounding context to know what a page owns and what links into
    it; if the read tool truncated a file, read the remaining ranges first.
*   Follow the style of the file you touch, and **edit `en/` and `ja/` in the same turn** — a
    change that lands in one locale is the defect this repo produces most.
*   After editing, run `scripts/build-docs.sh` with no arguments. It is the only validation there
    is: nothing builds the docs on a pull request.
*   **This portal owns no code**, so every claim is sourced from a sibling repo. The invariants are
    *Conventions* and *Traps* below — update this file when one of them changes.

## What this repo is

A Zensical **documentation portal** for the SpriteStudio SDK and its official players: the unified
entry point plus the **cross-cutting** material belonging to no single player. Every player keeps
its own site in its own repository, so `docs/*/players/` pages stay **thin** — a short description
and links out, never full player documentation.

## Commands

```bash
scripts/prepare-docs.sh            # .venv + the pinned toolchain
scripts/build-docs.sh              # English, then Japanese into site/ja — both --strict
scripts/build-pages.sh serve=yes   # ... then serve the published tree on :8000
zensical serve [-f mkdocs.ja.yml]  # unwrapped: live preview of one locale at a time
```

The first two also ship as `.ps1`; all take `key=value` options and `--help`.

- **Order matters**: the English build clears `site/`, which contains `site/ja`. `serve` validates
  nothing — `serve --strict` is accepted and does nothing.
- **Deployment is manual** — `.github/workflows/pages.yml` on `workflow_dispatch` alone (merging
  to `main` publishes nothing), calling these same scripts. So `scripts/*.sh` are production
  tooling: keep them executable (mode `100755`) and working with no options.

## Conventions

- **Everything twice.** Every page exists as `docs/en/<path>` and `docs/ja/<path>`. There is no
  fallback locale: a page missing from `docs/ja/` is a nav entry pointing at nothing.
- **Content lives in three folders** per locale, each mapping to exactly one nav section:
  `overview/` → 🗺️ Overview, `players/` → 🎮 Players & Tools, `sdk/` → 🛠️ SDK & Development, and
  `index.md` / `support.md` / `license.md` at the root → ℹ️ About. Keep it one-to-one.
- **Every `players/` page answers four questions in order** (from
  `SpriteStudio-SDK/MAINTAINING_PLAYERS.md`): what you install, how a `.sspj` becomes a `.ssab`,
  how it gets on screen, where to read next (three links at most). An admonition above them names
  the shape — **editor-first** (Unity, Godot) or **code-first**. Nothing goes above question 1.
  Depart only where the host collides with it and say why there: `converter.md` is a conversion
  tool, `wgpu.md` answers question 1 with a table. A missing docs site is not such a case.
- **Sources**: `sdk/limitations.md` from the SDK's Player Porting Guide (`libs/ssruntime/docs`,
  *Introduction → Limitations*), `overview/player-differences.md` from each player's own docs.
- **One fact, one page** — link instead of restating. `sdk/concepts.md` owns what the core
  **provides**, `sdk/limitations.md` what it does **not** plus every all-player constraint,
  `overview/player-differences.md` **only what differs between players**, `overview/conversion.md`
  how the project files map onto what conversion emits, `sdk/glossary.md` what each extension *is*.
  Two shapes follow. `sdk/limitations.md` keeps **one altitude**: four `##` buckets (playback,
  what the player supplies, rendering, shipping), every constraint a `###` inside one — a fact
  promoted to `##` is the bug. `overview/player-differences.md` is a **one-line-per-player table
  over one `###` per player**; an overgrown cell belongs in the section, not in both.
- **No facts that need tracking across repos**: version numbers, requirement tables, per-project
  license identifiers, schema matrices. Let each project state them and link out.
- **Internal links are relative `.md` paths** (`../sdk/concepts.md`) — that is what `--strict`
  validates. Link sibling repos at the repository root. A moved page needs a `redirect_maps:` entry
  under the `redirects` plugin in `mkdocs.base.yml`, relative to `docs_dir`: one entry covers both.
- **"Coming soon" gating**: `cri-middleware.github.io/…` URLs 404 until deployed, so those
  outbound links are plain **"coming soon" / "準備中"** text, no hyperlink, while `github.com/…`
  repo links stay live. The three `ssconverter-web` addresses in
  `overview/convert-with-a-standalone-tool.md` are the **one exception** (link + 🚧 + marker); do
  not extend it without asking.
- **🚧 marks anything pending publication** — a card, a table cell or a list item as readily as a
  sentence — immediately before the pending phrase (`Docs (🚧 coming soon)`), not in front of the
  whole entry, and never marks a technical constraint. `en` and `ja` carry the same marks file for
  file — a locale with fewer is the bug. In `sdk/limitations.md`, `##` headings carry an emoji,
  `###` none.

## Traps: `--strict` validates internal links and nothing else

- **A YAML sequence must be defined in exactly one of the three configs.** Zensical's `INHERIT`
  *concatenates* sequences where MkDocs replaces them, so `nav` in the base as well as a locale
  config renders the English nav followed by the Japanese one. Shared sequences (`theme.palette`,
  `theme.features`, `plugins`, `markdown_extensions`, `extra.alternate`) live in `mkdocs.base.yml`
  only; per-locale ones (`nav`, `extra.social`) in the locale configs only, `nav` written twice over
  locale-relative paths (`players/unity.md`), structurally identical, labels translated. Mappings
  deep-merge, so scalar overrides like `theme.language` are safe.
- **Deep-link a sibling repo with `blob/HEAD/…`, never `blob/main/…`** — the family is split
  between `main` and `develop`, so a hard-coded branch 404s silently in half of them. **From
  `docs/ja/`, link the `.ja.md` counterpart** where one exists (`20_limitations.ja.md`,
  `README.ja.md`, `SCHEMA.ja.md`), or that directory's `README.ja.md`.
- **A repository added to the portal needs a row on three surfaces** — a card in `index.md`, a row
  in `license.md`, a row in `support.md` — in both locales, plus the `nav` entry and the
  `players/` page. Nothing validates the two tables.
- **`LICENSE.md` holds the licence text and nothing else.** GitHub scores the whole file against
  known texts, and one `SPDX-License-Identifier:` line costs ~6 points of similarity — enough to
  flip the repo to "Other". The translation lives in `LICENSE.ja.md`; do not merge them back.
- **`.github/ISSUE_TEMPLATE/config.yml` mirrors `SUPPORT.md`** — blank issues off, the forum and
  Help Center links repeating what SUPPORT.md routes. Change one, change the other.
- **No `edit_uri`**, here or in the player repos: nothing validates a branch name and the family
  is split. Do not reintroduce it without checking each repo's default branch.
- **Do not adopt `zensical.toml` or Zensical-only syntax**; the configs are valid MkDocs configs.
  The `pymdownx.emoji` block names a module Zensical never imports — it keeps the MkDocs build
  working, is inert here, and must not be "fixed".
- **`docs/requirements.txt` pins `zensical`** — bump in step with every sibling that builds with
  Python (SDK, Unity, Godot, Ren'Py, Flutter, wgpu, SSConverterGUI). SSPlayerForWeb and
  SSPlayerForReactNative use VitePress; SSProjectGenerator has no docs site.

Everything else is commented at the point of use — the three configs and both `overrides/`
templates cover per-locale `site_url` / `assets/` / `extra.social` and their own workarounds.

# AGENTS.md

## Operating rules

*   Keep changes scoped to the requested task.
*   Do not commit, push, or open PRs unless the user explicitly asks.
*   Before editing, read enough surrounding context to know what a page owns and what links into
    it; if the read tool truncated a file, read the remaining ranges first.
*   Follow the style of the file you touch, and **edit `en/` and `ja/` in the same turn** — a
    change that lands in one locale is the defect this repo produces most.
*   After editing, run `scripts/build-docs.sh`. It is the only validation there is: nothing
    builds the docs on a pull request.
*   **This portal owns no code**, so every claim is sourced from a sibling repo. Update this file
    when one of the invariants below changes.

## What this repo is

A Zensical **documentation portal** for the SpriteStudio SDK and its official players: the entry
point plus the **cross-cutting** material belonging to no single player. Every player documents
itself, so `docs/*/players/` pages stay **thin** — a short description and links out.

## Commands

```bash
scripts/prepare-docs.sh            # .venv + the pinned toolchain
scripts/build-docs.sh              # English, then Japanese into site/ja — both --strict
scripts/build-pages.sh serve=yes   # ... then serve the published tree on :8000
zensical serve [-f mkdocs.ja.yml]  # unwrapped: live preview of one locale at a time
```

All three also ship as `.ps1`; each takes `key=value` options and `--help`. **Order matters**: the
English build clears `site/`, which contains `site/ja`. `serve` validates nothing — `--strict` is
accepted and ignored. Merging publishes nothing: deployment is `workflow_dispatch` alone, calling
these same scripts, so keep `scripts/*` mode `100755` and working with no options.

## Conventions

- **Everything twice.** Every page exists as `docs/en/<path>` and `docs/ja/<path>`. There is no
  fallback locale: a page missing from `docs/ja/` is a nav entry pointing at nothing.
- **Three folders per locale, one nav section each**: `overview/` → 🗺️ Overview, `players/` →
  🎮 Players & Tools, `sdk/` → 🛠️ SDK & Development, and `index.md` / `support.md` / `license.md`
  at the root → ℹ️ Support & License. Keep it one-to-one.
- **Every `players/` page answers four questions in order** (from
  `SpriteStudio-SDK/MAINTAINING_PLAYERS.md`): what you install, how a `.sspj` becomes a `.ssab`,
  how it gets on screen, where to read next (three links at most). An admonition above them names
  the shape — **editor-first** (Unity, Godot) or **code-first**; nothing goes above question 1.
  Depart only where the host collides with it, and say why there (`converter.md` is a conversion
  tool; `wgpu.md` answers question 1 with a table). A missing docs site is not such a case.
- **One fact, one page** — link instead of restating. `sdk/concepts.md` owns what the core
  **provides**; `sdk/limitations.md` what it does **not**, plus every all-player constraint;
  `overview/player-differences.md` **only what differs between players**; `overview/conversion.md`
  how project files map onto what conversion emits; `sdk/glossary.md` what each extension *is*.
  The first comes from the SDK's Player Porting Guide (`libs/ssruntime/docs`, *Introduction →
  Limitations*), the second from each player's own docs.
- **Two of those keep a fixed shape.** `sdk/limitations.md` holds **one altitude**: four `##`
  buckets (playback, what the player supplies, rendering, shipping), every constraint a `###`
  inside one — a fact promoted to `##` is the bug. `overview/player-differences.md` is a
  **one-line-per-player table over one `###` per player**; an overgrown cell belongs in one.
- **No facts that need tracking across repos**: version numbers, requirement tables, per-project
  license identifiers, schema matrices. Let each project state them and link out.
- **🚧 marks anything pending publication** — a card, a table cell or a list item as readily as a
  sentence — immediately before the pending phrase (`Docs (🚧 coming soon)`), not in front of the
  whole entry, and never on a technical constraint. `en` and `ja` carry the same marks file for
  file. In `sdk/limitations.md`, `##` headings carry an emoji, `###` none.

## Traps: `--strict` validates internal links and nothing else

- **A YAML sequence must be defined in exactly one of the three configs.** Zensical's `INHERIT`
  *concatenates* sequences where MkDocs replaces them, so `nav` in the base as well as a locale
  config renders the English nav followed by the Japanese one. `theme.palette`, `theme.features`,
  `plugins`, `markdown_extensions` and `extra.alternate` live in `mkdocs.base.yml` only; `nav` and
  `extra.social` in the locale configs only, `nav` written twice over locale-relative paths,
  structurally identical, labels translated. Mappings deep-merge, so `theme.language` is safe.
- **Internal links are relative `.md` paths** (`../sdk/concepts.md`) — that is what `--strict`
  checks. Link siblings at their repo root; a moved page needs a `redirect_maps:` entry.
- **`cri-middleware.github.io/…` URLs 404 until deployed**, so those outbound links are plain
  **"coming soon" / "準備中"** text, no hyperlink, while `github.com/…` repo links stay live. Two
  pages link the address anyway: the three `ssconverter-web` addresses in
  `overview/convert-with-a-standalone-tool.md` (link + 🚧 + marker), and every row of
  `overview/try-it.md`, covered by that page's 🚧 admonition. Do not extend either without asking.
- **Deep-link a sibling repo with `blob/HEAD/…`, never `blob/main/…`** — the family is split
  between `main` and `develop`, so a hard-coded branch 404s silently in half of them. **From
  `docs/ja/`, link the `.ja.md` counterpart** where one exists (`20_limitations.ja.md`,
  `README.ja.md`, `SCHEMA.ja.md`), or that directory's `README.ja.md`.
- **A repository added to the portal needs five edits per locale** — a card in `index.md`, a row
  in `license.md`, a row in `support.md`, the `nav` entry, the `players/` page. Nothing checks them.
- **`LICENSE.md` holds the licence text and nothing else.** GitHub scores the whole file against
  known texts, and one `SPDX-License-Identifier:` line costs ~6 points of similarity — enough to
  flip the repo to "Other". The translation lives in `LICENSE.ja.md`; do not merge them back.
- **`.github/ISSUE_TEMPLATE/config.yml` mirrors `SUPPORT.md`** — change one, change the other.
- **No `edit_uri`**, here or in the player repos: nothing validates a branch name.
- **Do not adopt `zensical.toml` or Zensical-only syntax**; the configs are valid MkDocs configs.
  The `pymdownx.emoji` block names a module Zensical never imports: inert here, and not a bug.
- **`docs/requirements.txt` pins `zensical`** — bump in step with every sibling that builds with
  Python (SDK, Unity, Godot, Ren'Py, Flutter, wgpu, SSConverterGUI). SSPlayerForWeb and
  SSPlayerForReactNative use VitePress; SSProjectGenerator has no docs site.

Everything else is commented where it is used — the three configs and both `overrides/` templates.

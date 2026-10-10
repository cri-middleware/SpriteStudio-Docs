# SpriteStudio-Docs — AI Agent Guide

## Operating rules

*   Keep changes scoped to the requested task. Unrequested hardening is a suggestion, not a commit; a defect
    you actually hit in the code you touched is not — fix it, or say plainly why you did not.
*   Do not commit, push, or open PRs unless the user explicitly asks.
*   Before editing, read enough surrounding context to understand callers and invariants, the ones below
    included. If the read tool truncated a file, read the remaining ranges first.
*   Follow the existing style of the file you touch (naming, type usage, control flow, error handling).
*   **Anything that exists twice changes twice** — a page and its translation, a `.sh` and its `.ps1`. A
    change that lands in one half is the defect this family produces most.
*   **Never break a line between two Japanese characters**: Chrome draws that break as a visible space.
*   **Finish by running this repository's checks**: `scripts/build-docs.sh`, both locales. Nothing builds
    the docs on a pull request, so it is the only gate there is. Read what a run says it verified rather
    than its exit code — several checks here pass, or skip themselves, when a prerequisite is missing.
*   **Do not restate here what another file owns.** The table below says which file that is; a fact that
    belongs to none of them goes where it will be seen to go stale.
*   **This portal owns no code**, so every claim is sourced from a sibling repository. Update this file when
    one of the invariants below changes.

## What this repo is

A Zensical **documentation portal** for the SpriteStudio SDK and its official players: the entry
point plus the **cross-cutting** material belonging to no single player. Every player documents
itself in its own repository, so `docs/*/players/` pages stay **thin** — a short description and
links out, never full player documentation.

## Where each answer is written

| Question | File |
|---|---|
| How to set up, build and check the site, and the rules for writing a page | [CONTRIBUTING.md](./CONTRIBUTING.md) |
| What each script does and takes | that script's `--help` |
| How the site is published | [RELEASING.md](./RELEASING.md), maintainers only |
| What a `players/` page owes its reader | `SpriteStudio-SDK/MAINTAINING_PLAYERS.md` |
| Why a YAML sequence may live in only one config | the header comment of `mkdocs.base.yml` |
| Everything else about a config or a template | the comment at the point of use |

## Invariants

- **Three folders per locale, one nav section each**: `overview/` → 🗺️ Overview, `players/` →
  🎮 Players & Tools, `sdk/` → 🛠️ SDK & Development, and `index.md` / `support.md` / `license.md`
  at the root → ℹ️ Support & License. Keep it one-to-one.
- **Every `players/` page answers four questions in order** (from `MAINTAINING_PLAYERS.md`): what
  you install, how a `.sspj` becomes a `.ssab`, how it gets on screen, where to read next (three
  links at most). An admonition above them names the shape — **editor-first** (Unity, Godot) or
  **code-first**; nothing goes above question 1. Depart only where the host collides with it, and
  say why there (`converter.md` is a conversion tool; `wgpu.md` answers question 1 with a table).
  A missing docs site is not such a case.
- **One fact, one page** — link instead of restating. `sdk/concepts.md` owns what the core
  **provides**; `sdk/limitations.md` what it does **not**, plus every all-player constraint —
  technical constraints only, since work not built yet belongs in a ROADMAP (text and 9-slice
  parts, which no player draws, are the one exception); `overview/player-differences.md` **only
  what differs between players**; `overview/conversion.md`
  how project files map onto what conversion emits; `sdk/glossary.md` what each extension *is*.
  `sdk/concepts.md` follows the SDK's Player Porting Guide (`libs/ssruntime/docs`, its table of
  contents), `sdk/limitations.md` the guide's *Introduction → Limitations*, and
  `overview/player-differences.md` each player's own docs.
- **Two of those keep a fixed shape.** `sdk/limitations.md` holds **one altitude**: four `##`
  buckets (playback, what the player supplies, rendering, shipping), every constraint a `###`
  inside one — a fact promoted to `##` is the bug. `overview/player-differences.md` is a
  **one-line-per-player table over one `###` per player**; an overgrown cell belongs in one. In
  `sdk/limitations.md`, `##` headings carry an emoji, `###` none.
- **Every page reads as published** — a sibling repository, its GitHub Pages site and its Releases
  are linked as live, never marked 🚧, "coming soon" or "準備中", and a registry a package is not on
  goes unmentioned. `en` and `ja` carry the same links file for file.
- **A repository added to the portal needs five edits per locale** — a card in `index.md`, a row
  in `license.md`, a row in `support.md`, the `nav` entry, the `players/` page — plus one entry in
  `llmstxt.sections` of `mkdocs.base.yml`, once for both locales. Nothing checks it.
- **`LICENSE.md` holds the licence text and nothing else.** GitHub scores the whole file against
  known texts, and one `SPDX-License-Identifier:` line costs ~6 points of similarity — enough to
  flip the repo to "Other". The translation lives in `LICENSE.ja.md`; do not merge them back.
- **`.github/ISSUE_TEMPLATE/config.yml` mirrors `SUPPORT.md`** — change one, change the other.
- **No `edit_uri`**, here or in the player repos: nothing validates a branch name.
- **Do not adopt `zensical.toml` or Zensical-only syntax**; the configs are valid MkDocs configs.
  The `pymdownx.emoji` block names a module Zensical never imports: inert here, and not a bug.

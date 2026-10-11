# SpriteStudio-Docs — AI Agent Guide

## Operating rules

*   Keep changes scoped to the requested task. Unrequested hardening is a suggestion, not a commit; a defect
    you actually hit in the code you touched is not — fix it, or say plainly why you did not.
*   Before editing, read enough surrounding context to understand callers and invariants, the ones below
    included.
*   **Anything that exists twice changes twice** — a page and its translation, a `.sh` and its `.ps1`.
    Missing one half is this family's most common defect.
*   **Never break a line between two Japanese characters**; Chrome renders the break as a space.
*   **Finish with this repository's checks**: `scripts/build-docs.sh`, both locales, the build CI runs.
    Read what a run says it verified, not its exit code — several checks pass, or skip themselves, without
    a prerequisite.
*   **Do not restate what another file owns**; the table below says which file. A fact no file owns goes
    where its staleness will be noticed.
*   **This portal owns no code**: every claim is sourced from a sibling repository.

## What this repo is

A Zensical documentation portal for the SpriteStudio SDK and its official players: the entry point,
plus the cross-cutting material no single player owns. Each player documents itself in its own
repository, so `docs/*/players/` pages stay thin — a short description and links out.

## Where each answer is written

| Question | File |
|---|---|
| Setup, build and checks, and the rules for writing a page | [CONTRIBUTING.md](./CONTRIBUTING.md) |
| Publishing the site, maintainers only | [RELEASING.md](./RELEASING.md) |
| What a `players/` page owes its reader | `SpriteStudio-SDK/MAINTAINING_PLAYERS.md` |
| What a script takes | its `--help` |

## Invariants

*   **Three folders per locale, one nav section each**, one-to-one: `overview/` → 🗺️ Overview, `players/`
    → 🎮 Players & Tools, `sdk/` → 🛠️ SDK & Development, and the root's `index.md` / `support.md` /
    `license.md` → ℹ️ Support & License.
*   **A `players/` page answers four questions in order**: what you install, how a `.sspj` becomes a
    `.ssab`, how it gets on screen, and where to read next (three links at most). An admonition above them
    names the shape — **editor-first** (Unity, Godot) or **code-first** — and nothing else precedes
    question 1. Depart only where the host collides with the shape, and say why on the page
    (`converter.md`, `wgpu.md`); a missing docs site is not such a case.
*   **One fact, one page; link instead of restating.** `sdk/concepts.md` owns what the core provides,
    following the Player Porting Guide's contents. `sdk/limitations.md` owns what it does not, and every
    all-player technical constraint, following the guide's Limitations; unbuilt work belongs in a ROADMAP,
    except text and 9-slice parts. `overview/player-differences.md` owns only what differs between players,
    `overview/conversion.md` how project files map onto conversion output, and `sdk/glossary.md` what each
    extension is.
*   **`sdk/limitations.md` holds one altitude**: four `##` buckets with emoji (playback, what the player
    supplies, rendering, shipping), and every constraint a `###` without one inside a bucket.
    **`overview/player-differences.md` is a one-line-per-player table over one `###` per player**; an
    overgrown cell moves into its `###`.
*   **A repository added to the portal needs five edits per locale** — a card in `index.md`, rows in
    `license.md` and `support.md`, the `nav` entry and the `players/` page — plus one `llmstxt.sections`
    entry in `mkdocs.base.yml`. Nothing checks it.
*   **`LICENSE.md` holds the licence text and nothing else**: GitHub scores the whole file, and an
    `SPDX-License-Identifier:` line costs enough similarity to flip it to "Other". The translation stays in
    `LICENSE.ja.md`.
*   **`.github/ISSUE_TEMPLATE/config.yml` mirrors `SUPPORT.md`.**
*   **No `edit_uri`**, here or in the player repos: nothing validates a branch name.
*   **No `zensical.toml` and no Zensical-only syntax**; the configs stay valid MkDocs. The
    `pymdownx.emoji` block names a module Zensical never imports — inert, not a bug.

# AGENTS.md

This file provides guidance to coding agents when working with code in this repository.

## What this repo is

A **documentation portal** ([Zensical](https://zensical.org)) for the SpriteStudio SDK and its
official players. It is a lightweight hub, **not** a mirror of each player's docs: every player keeps
its own site in its own repository. This portal hosts only the unified entry point and the
**cross-cutting** material that belongs to no single player — the landing page, the ecosystem
overview, shared SDK concepts, the format specification, and licensing.

Consequence for edits: player pages under `docs/*/players/` are intentionally **thin** — a
short description plus links out to that player's own docs and GitHub repo. Do not expand them
into full player documentation; that content lives in the player's own repository.

## Commands

```bash
scripts/prepare-docs.sh                             # .venv + the pinned toolchain
scripts/build-docs.sh                               # English then Japanese, both strict
scripts/build-pages.sh serve=yes                    # ... the published tree, on :8000
```

`scripts/*.ps1` are the PowerShell twins, and every one of these scripts takes `key=value`
options and `--help`, like the ones in the player repos: `prepare-docs.sh python=py
force=yes`, `build-docs.sh locale=ja venv=.venv`. The `-docs` suffix is deliberate: the
player repos carry same-named scripts for their own build steps, so the name says which one
this is. What the first two wrap is only this:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r docs/requirements.txt

# One build per locale. English first: it clears site/, which contains site/ja.
.venv/bin/zensical build --strict
.venv/bin/zensical build -f mkdocs.ja.yml --strict
```

`serve` is deliberately **not** wrapped — it validates nothing, serves one locale at a time,
and has nothing worth defaulting:

```bash
.venv/bin/zensical serve                            # live preview of English
.venv/bin/zensical serve -f mkdocs.ja.yml           # ... or of Japanese
```

`scripts/build-pages.sh` is the third script and the published site: the two above, run for
you, then a static server over `site/`. That server is the point of it, and the one thing
`zensical serve` cannot do — both locales at once, so the header language selector resolves
and every link is the link a reader clicks. It builds nothing of its own; this portal's site
is the docs and nothing else. The name is the family's: in the repos whose site carries a
playable demo or an API reference, `build-pages` carries those too.

Always validate with **both** builds before finishing — `scripts/build-docs.sh` with no
arguments does exactly that. **This is the only validation there is** — nothing builds the docs
on a pull request, so a broken internal link is not caught for you. Running it locally is the
gate. `mkdocs.base.yml` also sets `strict: true`, so a plain `build` fails the same way; the
explicit flag is kept inside `build-docs.sh` and in the commands above because it is what the
docs everywhere tell people to run. `serve`, by contrast, validates nothing — `zensical serve --strict` is
accepted and currently does nothing.

Building only the English locale is the easy mistake here: the English build clears `site/`,
and `site/ja` lives inside it, so afterwards the Japanese site does not exist at all — a
`site/` you then serve or upload is English-only. `build-docs.sh locale=en` says so on the way
out; plain `build-docs.sh` avoids it.

Deployment is **manual**: `.github/workflows/pages.yml` triggers on `workflow_dispatch` alone.
Running it calls `scripts/prepare-docs.sh` and then `scripts/build-pages.sh prepare=no serve=no`
— the same scripts you run locally, deliberately, so that the locale order and the `--strict`
flag are defined in one place rather than drifting between a workflow nothing PR-tests and a
README nobody re-reads.
The publish therefore aborts rather than deploying a dead link, and deploys via the GitHub
Pages deployment API (OIDC) — no `gh-pages` branch and no `contents: write`. Merging to `main`
does **not** auto-publish. The sibling player repos publish on `release: published` +
`workflow_dispatch`; this portal cuts no releases, so dispatch is the whole story here.

Consequence: `scripts/*.sh` are now production tooling. Keep them executable (git records
mode `100755`), and keep `build-pages.sh` — with the `build-docs.sh` it calls — working with
no options beyond the two the workflow passes: that invocation is what publishes the site.

## Architecture & conventions

- **One locale, one config.** Every page exists twice — `docs/en/<path>` and `docs/ja/<path>` —
  and each locale is built from its own config file. `mkdocs.yml` builds English to `site/`,
  `mkdocs.ja.yml` builds Japanese to `site/ja/`, and both inherit the shared settings from
  `mkdocs.base.yml`. When you add, move, or rename a page, do it in **both** `en/` and `ja/`.
  There is no fallback locale any more: a page missing from `docs/ja/` is not silently served in
  English, it is a nav entry pointing at nothing.
- **The three-config split has one rule: a YAML sequence must be defined in exactly one of the
  three files.** Zensical's `INHERIT` *concatenates* parent and child sequences where MkDocs
  replaces them. Put `nav` in the base as well as a locale config and the Japanese site renders
  the English navigation followed by the Japanese one; do it with `extra.social` and the footer
  grows six icons. Mappings deep-merge in both tools, so scalar overrides like `theme.language`
  are safe. Shared sequences (`theme.palette`, `theme.features`, `plugins`,
  `markdown_extensions`, `extra.alternate`) therefore live in `mkdocs.base.yml` and nowhere else;
  per-locale ones (`nav`, `extra.social`) live in the locale configs and never in the base.
- **Navigation is defined twice**, once per locale config, using locale-relative paths (e.g.
  `players/unity.md`, no `en/` or `ja/` prefix). The two trees must stay structurally identical;
  only the labels differ, and they are written directly in each language rather than looked up
  from a translation map. This replaced `nav_translations`, which no longer exists.
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
- **One fact, one page.** The three cross-cutting pages have deliberately disjoint jobs, and link
  to each other instead of restating: `sdk/concepts.md` owns what the shared core **provides**
  (the canonical feature list), `sdk/limitations.md` owns what it **does not do** plus every
  all-player constraint (the runtime-vs-player responsibility table, drawing and blending caveats,
  sequence playback, browser and asset requirements), and `overview/feature-support.md` owns
  **only what differs between players**. Keep the blend-mode discussion there stated as mechanism,
  with the per-player enumeration confined to the table. Restating a fact on a second page is how
  the text-part responsibilities once drifted into being documented backwards — link instead.
- **No facts that need tracking across repos.** Version numbers, engine/runtime requirement
  tables, per-project license identifiers, and schema-compatibility matrices are deliberately
  *not* hosted here: they would have to be chased across every sibling repository. Let each
  project state them in its own docs and link out instead.
- **Internal links are relative file paths** ending in `.md` (e.g. `../sdk/concepts.md`), which
  is what `--strict` validates. External player docs are absolute `https://…` URLs. Link sibling
  repos at the **repository root**; when you must point at a file inside one, use
  `blob/HEAD/...`, never `blob/main/...` — most sibling repos default to `develop`, so a
  `main` path 404s silently (`--strict` validates internal links only) while `HEAD` always
  resolves to whatever that repo's default branch is. **From `docs/ja/`, link the `.ja.md`
  counterpart** where the sibling repo publishes one — the SDK ships `.ja.md` beside most of
  its guide pages (`20_limitations.ja.md`, `README.ja.md`, `SCHEMA.ja.md`). Sending a Japanese
  reader to the English original is the kind of drift `--strict` cannot see. Where only a
  directory would do, point at that directory's `README.ja.md` instead.
- **"Coming soon" gating**: player docs sites, live demos, and the hosted `ssconverter-web`
  are GitHub Pages URLs (`cri-middleware.github.io/…`) that 404 until each is deployed, so those
  outbound links are neutralized to plain **"coming soon" / "準備中"** text (no hyperlink) in
  both locales. `github.com/cri-middleware/…` **repo** links stay live as forward-links. When a
  site ships, restore its link in `en/` and `ja/` together. **One deliberate exception**: the
  three `ssconverter-web` addresses in `overview/convert-with-a-standalone-tool.md` *are*
  hyperlinked — link + 🚧 + the "coming soon" / "準備中" marker, which is the pattern the sibling
  repo READMEs use for the same situation. Their address is already fixed by the publishing repo
  (`SSPlayerForWeb`'s `scripts/build-ssconverter-pages.sh`), so it is worth handing readers a
  clickable forward-link rather than an address they must copy. They still 404 today: leave them
  linked anyway, and do not extend the hyperlink pattern to another "coming soon" without asking.
- **Landing page cards** (`index.md`) use "grid cards" — they depend on the `attr_list` and
  `md_in_html` markdown extensions already configured in `mkdocs.base.yml`. Icon shortcodes like
  `:material-unity:` and `:simple-rust:` render to SVG. Note that the `pymdownx.emoji` block
  still names `material.extensions.emoji`, a module Zensical does not ship: Zensical resolves
  icons itself and never imports it. The block is kept because it is what makes the same configs
  build under MkDocs, and it is inert otherwise — do not "fix" it by pointing it somewhere else.
- **Site metadata and chrome** — the "everything twice" rule applies unevenly here, so check
  which side of it a given setting falls on before duplicating or sharing it:
    - `overrides/main.html` (`theme.custom_dir`) emits the Open Graph / Twitter Card tags the
      theme omits, **and repairs the page title**: Zensical never sets `page.is_homepage`, so
      its own `base.html` titles the landing page "SpriteStudio Docs - SpriteStudio Docs". The
      override derives the flag from `page.url` instead and overrides the `htmltitle` block, so
      the tab, the `og:` card and the Twitter card all read from one value. It still consults
      `page.is_homepage` first, so the workaround retires itself if Zensical starts setting it.
      **One template serves both locales** — `config.site_name`, `config.site_description` and
      `config.theme.language` come from whichever locale config is building. Localize by adding
      a per-locale config override, not by branching in the template.
    - **Each locale ships its own `assets/`.** `theme.favicon` resolves against the site root,
      and each locale now *has* its own root (`site/` and `site/ja/`), so the file exists twice:
      `docs/en/assets/favicon.svg` and `docs/ja/assets/favicon.svg`. There is no shared
      `docs/assets/` any more — a file there would sit outside both `docs_dir`s and never be
      copied anywhere.
    - **`site_url` is per locale** and the ja one must keep its `ja/` suffix: `page.canonical_url`
      and therefore `og:url` are built from it. Inheriting the English value would advertise
      every Japanese page under its English address.
    - **Footer social icons are defined twice**, in `mkdocs.yml` and `mkdocs.ja.yml` (the labels
      are translated; the icons and links are not). Add or reorder an icon in both, or the two
      footers diverge. Keep `twitter:site` in `overrides/main.html` in sync with the X link.
    - **The header language selector is rebuilt by `overrides/partials/alternate.html`** so
      that switching language keeps the reader on the page they are on. `mkdocs-static-i18n`
      used to rewrite those links per page; nothing does once the locales are separate builds,
      and the stock partial emits `alt.link` verbatim, sending everyone to the other locale's
      home page. The override derives the href from `page.url` instead, which is why
      `extra.alternate[].link` in `mkdocs.base.yml` holds a locale *subpath* (`""`, `ja/`)
      rather than a URL, and why each locale config carries `extra.site_root_prefix`. Known
      gap: the `<link rel="alternate" hreflang>` tags in `<head>` still point at each locale
      root — they sit inside the theme's `site_meta` block, and overriding that would mean
      copying thirty lines Zensical may change. `serve` still shows one locale at a time, so
      the selector only works against a build of both; README says how.
- **There is deliberately no `edit_uri`**, here or in the player repos, so no "edit this page"
  button renders. It is a branch name nothing validates — `--strict` does not look at it — and
  it was already wrong in three of the five sibling players, pointing at `main` where the
  default branch is `develop`. `edit/HEAD/…` would remove the branch name but could not be
  verified: the web editor redirects anonymous requests to a login page whether the ref is
  valid or not. The footer repo link and CONTRIBUTING.md route corrections instead. Do not
  reintroduce it without checking each repo's default branch.
- **Pinned toolchain**: `docs/requirements.txt` pins `zensical` deliberately — bump
  intentionally. The pins are **no longer kept in sync with the per-player repos**: this portal
  is the first to move off MkDocs + Material for MkDocs (which its own authors put into
  maintenance mode), and the players follow one at a time. Restore the sync rule once they have.
- **The configs are still valid MkDocs configs, deliberately.** `pip install mkdocs-material`
  and `mkdocs build --strict -f mkdocs.yml` builds the same site, which is what makes the
  migration reversible and lets you diff the two engines when something looks off. Do not adopt
  `zensical.toml` or any Zensical-only config syntax while that is still worth keeping — and
  note Zensical's own docs currently advise existing projects against the `.toml` switch.
- **Known Zensical gaps** worth not re-discovering: `page.is_homepage` is never set (worked
  around in `overrides/main.html`); `serve --strict` is accepted but does nothing; there is no
  multi-locale build, which is the whole reason for the three-config split; and the theme's own
  chrome icons are Lucide rather than Material, so a page renders three fewer inline SVGs than
  the MkDocs build did. Content icons are unaffected.

# Contributing to SpriteStudio-Docs

Thank you for your interest in improving the SpriteStudio documentation portal! Corrections, clarifications, and translation fixes are all welcome.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [What belongs in this repository](#what-belongs-in-this-repository)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Environment](#development-environment)
- [Documentation Standards](#documentation-standards)

## Code of Conduct
Please refer to [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

## What belongs in this repository

This is a **portal**, not a mirror. Every player keeps its own documentation site in its own repository, and this repository hosts only the unified entry point plus the **cross-cutting** material that belongs to no single player: the landing page, the ecosystem overview, the platform chooser, feature support, shared SDK concepts, the format specification, shared limitations, the glossary, support routing, and licensing.

Consequences for a contribution:

- **Player-specific content goes to that player's repository.** The pages under `docs/*/players/` are intentionally thin - a short description plus links out. Please do not grow them into full player documentation.
- **Cross-cutting claims must be sourced from the sibling repositories.** This portal owns no code, so a statement about what a player supports must come from that player's own docs (or the SDK's). Please do not infer support - or the lack of it - that no repository documents. Where nothing is documented, say so.

## How Can I Contribute?

### Reporting problems
Open a [GitHub Issue](https://github.com/cri-middleware/SpriteStudio-Docs/issues) for a wrong or outdated description, a broken link, a missing translation, or a build failure. Problems with a player's own behavior belong in that player's repository - see [SUPPORT.md](./SUPPORT.md).

### Pull Requests
1. Fork the repository and create your branch from `main`.
2. Make the change in **both** `docs/en/` and `docs/ja/` (see below).
3. Run `mkdocs build --strict` locally - this is exactly what CI runs.
4. Submit a Pull Request targeting `main` with a clear description. Use [Conventional Commits](https://www.conventionalcommits.org/) (e.g. `docs: …`).

Note that merging does **not** publish. Deployment is manual: a maintainer runs the `Publish docs via GitHub Pages` workflow (`workflow_dispatch`).

## Development Environment

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r docs/requirements.txt

.venv/bin/mkdocs serve           # live preview at http://127.0.0.1:8000
.venv/bin/mkdocs build --strict  # what CI runs; fails on broken links / nav mismatches
```

On Windows, use `py -m venv .venv` and `.\.venv\Scripts\mkdocs`.

The toolchain versions in `docs/requirements.txt` are pinned deliberately and kept in sync with the per-player documentation sites - please bump them intentionally, not incidentally.

## Documentation Standards

### Both languages, always
The site uses folder-based i18n: every page exists twice, as `docs/en/<path>` and `docs/ja/<path>`. When you add, move, or rename a page, **do it in both** - otherwise the strict build fails. English is the default and fallback locale.

If you can only write one language confidently, say so in the PR; a maintainer can help with the other side rather than let the two drift.

### Navigation lives in `mkdocs.yml`
The `nav:` tree is defined once, with locale-relative paths (`sdk/glossary.md`, no `en/` or `ja/` prefix). Japanese navigation labels come from `plugins.i18n.languages` → `nav_translations`, **not** from the file tree - add a matching entry whenever you introduce a new nav title.

### Links
- **Internal links** are relative file paths ending in `.md` (e.g. `../sdk/concepts.md`). `--strict` validates these.
- **Links into sibling repositories** should target the repository (or a path that exists on its default branch). Avoid deep `blob/main/...` links to documentation files: several players keep their docs on `develop`, so such a link can 404 silently - `--strict` only validates internal links.
- **Pre-launch sites** (player documentation sites, live demos, the hosted converter) are neutralized to plain "coming soon" / "準備中" text until each is deployed. When one ships, restore its link in `en/` and `ja/` together.

### Writing
- Prefer material that stays true. Version numbers, requirement tables, and other facts that need tracking across seven repositories age badly in a portal - let each project state those in its own docs, and link out instead.
- Match the surrounding page: sentence-case headings with a leading emoji, tables for comparisons, and `!!!` admonitions (Material) for notes and warnings.
- Keep the two locales structurally identical - same headings, same tables, same links - so future edits can be applied to both in one pass.

---
Contributions to this project are considered to be made under the terms of the project's [LICENSE.md](./LICENSE.md).

---

# SpriteStudio-Docs への貢献

SpriteStudio ドキュメントポータルの改善にご関心をお寄せいただきありがとうございます。誤りの修正、説明の改善、翻訳の修正など、どれも歓迎します。

## 行動規範
[CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) を参照してください。

## このリポジトリが扱う範囲

ここは**ポータル**であり、各 Player ドキュメントのミラーではありません。各 Player のドキュメントはそれぞれのリポジトリのサイトで管理され、このリポジトリが持つのは統一された入口と、どの Player にも属さない**横断的な**情報だけです（ランディングページ、エコシステム概要、プラットフォームの選び方、機能サポート状況、共通の SDK コンセプト、フォーマット仕様、共通の制限事項、用語集、サポート窓口の振り分け、ライセンス）。

貢献にあたっての帰結:

- **Player 固有の情報は、その Player のリポジトリへ。** `docs/*/players/` 配下のページは意図的に薄く保っています（短い説明と外部リンクのみ）。ここを本格的な Player ドキュメントに育てないでください。
- **横断的な記述は兄弟リポジトリを出典とすること。** このポータルはコードを持たないため、ある Player が何に対応しているかという記述は、その Player 自身（または SDK）のドキュメントに基づく必要があります。どのリポジトリにも記載のない対応可否を推測しないでください。記載がない場合は、その旨を書いてください。

## 貢献の方法

### 問題の報告
記述の誤りや古い情報、リンク切れ、翻訳の欠落、ビルドの失敗は [GitHub Issues](https://github.com/cri-middleware/SpriteStudio-Docs/issues) へ。各 Player の動作に関する問題は該当 Player のリポジトリへお願いします（[SUPPORT.md](./SUPPORT.md) 参照）。

### プルリクエスト
1. リポジトリを fork し、`main` からブランチを作成してください。
2. `docs/en/` と `docs/ja/` の **両方** を変更してください（下記参照）。
3. ローカルで `mkdocs build --strict` を実行してください。CI と同じ検証です。
4. `main` を対象に、変更内容を明確に記載した PR を作成してください。コミットは [Conventional Commits](https://www.conventionalcommits.org/)（例: `docs: …`）に従ってください。

マージしても **公開はされません**。デプロイは手動で、メンテナーが `Publish docs via GitHub Pages` ワークフロー（`workflow_dispatch`）を実行します。

## 開発環境

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r docs/requirements.txt

.venv/bin/mkdocs serve           # http://127.0.0.1:8000 でライブプレビュー
.venv/bin/mkdocs build --strict  # CI と同じ検証。リンク切れや nav の不整合で失敗します
```

Windows では `py -m venv .venv` と `.\.venv\Scripts\mkdocs` を使用してください。

`docs/requirements.txt` のバージョンは各 Player のドキュメントサイトと揃えて意図的に固定しています。更新はついでではなく、意図をもって行ってください。

## ドキュメントの規約

### 常に両言語
フォルダー方式の i18n を使っており、すべてのページは `docs/en/<path>` と `docs/ja/<path>` の 2 か所に存在します。ページの追加・移動・リネームは **必ず両方** に行ってください。片方だけだと strict ビルドが失敗します。英語が既定かつフォールバックのロケールです。

片方の言語しか自信がない場合は、その旨を PR に書いてください。両者が乖離するくらいなら、メンテナーがもう一方を補います。

### ナビゲーションは `mkdocs.yml`
`nav:` はロケール相対のパス（`sdk/glossary.md` のように `en/` や `ja/` を付けない）で一度だけ定義します。日本語のナビ名はファイルツリーではなく `plugins.i18n.languages` → `nav_translations` から取得されるため、新しいナビ項目を追加したら対応するエントリーも追加してください。

### リンク
- **内部リンク**は `.md` で終わる相対パス（例: `../sdk/concepts.md`）。`--strict` が検証します。
- **兄弟リポジトリへのリンク**は、リポジトリ自体（または既定ブランチに存在するパス）を指してください。ドキュメントファイルへの `blob/main/...` の深いリンクは避けてください。docs を `develop` で管理している Player があり、気付かないまま 404 になります（`--strict` は内部リンクしか検証しません）。
- **公開前のサイト**（各 Player のドキュメントサイト、ライブデモ、ホスト版コンバーター）は、公開されるまでリンクにせず「coming soon」「準備中」の文字列にしています。公開されたら `en/` と `ja/` の両方でリンクに戻してください。

### 書き方
- 長く正しくあり続ける情報を優先してください。バージョン番号や要件表など、7 つのリポジトリを追跡し続ける必要がある情報はポータルでは古くなりやすいものです。各プロジェクト自身のドキュメントに任せ、こちらからはリンクしてください。
- 周囲のページに合わせてください。見出しは先頭に絵文字、比較は表、注意書きは Material の `!!!` 記法。
- 2 つのロケールは構造を同一に保ってください（同じ見出し、同じ表、同じリンク）。以後の編集を一度に両方へ適用できます。

---
本プロジェクトへの貢献は、プロジェクトの [LICENSE.md](./LICENSE.md) に同意したものとみなされます。

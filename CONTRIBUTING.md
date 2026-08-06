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
3. Build **both locales** locally - `.venv/bin/zensical build --strict` then `.venv/bin/zensical build -f mkdocs.ja.yml --strict`. **Nothing builds the docs on a pull request**, so this is the only validation there is - a broken link or a nav entry pointing at a missing page is not caught for you (see [Development Environment](#development-environment)).
4. Submit a Pull Request targeting `main` with a clear description. Use [Conventional Commits](https://www.conventionalcommits.org/) (e.g. `docs: …`).

Note that merging does **not** publish. Deployment is manual: a maintainer runs the `Publish docs via GitHub Pages` workflow (`workflow_dispatch`).

## Development Environment

macOS / Linux (bash):

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r docs/requirements.txt

.venv/bin/zensical serve                            # live preview of English at http://127.0.0.1:8000
.venv/bin/zensical serve -f mkdocs.ja.yml           # ... or of Japanese (stop the other one first)

# The gate. Nothing checks a PR. English first: it clears site/, which contains site/ja.
.venv/bin/zensical build --strict
.venv/bin/zensical build -f mkdocs.ja.yml --strict
```

Windows (PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\python -m pip install -r docs/requirements.txt

.\.venv\Scripts\zensical serve                      # live preview of English at http://127.0.0.1:8000
.\.venv\Scripts\zensical serve -f mkdocs.ja.yml     # ... or of Japanese (stop the other one first)

# The gate. Nothing checks a PR. English first: it clears site/, which contains site/ja.
.\.venv\Scripts\zensical build --strict
.\.venv\Scripts\zensical build -f mkdocs.ja.yml --strict
```

The toolchain versions in `docs/requirements.txt` are pinned deliberately - please bump them intentionally, not incidentally. This portal runs on [Zensical](https://zensical.org) while the sibling player repositories are still on MkDocs + Material for MkDocs, so the pins are no longer kept in step with theirs.

`serve` does not validate links, and it renders one locale, so the header's language selector 404s there - see the [README](./README.md#previewing-the-language-selector) for how to preview both locales together.

## Documentation Standards

### Both languages, always
The site uses folder-based i18n: every page exists twice, as `docs/en/<path>` and `docs/ja/<path>`. When you add, move, or rename a page, **do it in both** - otherwise the strict build fails. English is the default and fallback locale.

If you can only write one language confidently, say so in the PR; a maintainer can help with the other side rather than let the two drift.

### Navigation lives in the two locale configs
There is a `nav:` tree in `mkdocs.yml` (English) and another in `mkdocs.ja.yml` (Japanese). Both use locale-relative paths (`sdk/glossary.md`, no `en/` or `ja/` prefix) and the two must stay identical in structure - only the labels differ, written directly in the language rather than looked up from a translation map. Add a page to one and forget the other, and that page simply never appears in that locale's navigation.

Settings shared by both locales live in `mkdocs.base.yml`, which the two inherit. One rule governs what may go where: **a YAML sequence must be defined in exactly one of the three files.** Zensical's `INHERIT` concatenates sequences rather than replacing them, so a `nav` in the base as well as a locale config renders both navigations, one after the other.

### Links
- **Internal links** are relative file paths ending in `.md` (e.g. `../sdk/concepts.md`). `--strict` validates these.
- **Links into sibling repositories** should target the repository itself. When you must point at a file inside one, write `blob/HEAD/...` rather than `blob/main/...`: most sibling repositories default to `develop`, so a `main` path can 404 silently - `--strict` only validates internal links - while `HEAD` always resolves to that repository's default branch.
- **Pre-launch sites** (player documentation sites, live demos, the hosted converter) are GitHub Pages URLs that 404 until each is deployed, so they are neutralized to plain "coming soon" / "準備中" text. This applies to those **sites only** - `github.com/cri-middleware/…` repository links stay live as forward-links. When a site ships, restore its link in `en/` and `ja/` together.

### Writing
- Prefer material that stays true. Version numbers, requirement tables, and other facts that need tracking across every sibling repository age badly in a portal - let each project state those in its own docs, and link out instead.
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
3. ローカルで **両ロケール** をビルドしてください（`.venv/bin/zensical build --strict` のあと `.venv/bin/zensical build -f mkdocs.ja.yml --strict`）。**プルリクエストではドキュメントは一切ビルドされません**。これが唯一の検証で、リンク切れや、存在しないページを指す nav エントリーは自動では検出されません（[開発環境](#開発環境) 参照）。
4. `main` を対象に、変更内容を明確に記載した PR を作成してください。コミットは [Conventional Commits](https://www.conventionalcommits.org/)（例: `docs: …`）に従ってください。

マージしても **公開はされません**。デプロイは手動で、メンテナーが `Publish docs via GitHub Pages` ワークフロー（`workflow_dispatch`）を実行します。

## 開発環境

macOS / Linux (bash):

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r docs/requirements.txt

.venv/bin/zensical serve                            # 英語を http://127.0.0.1:8000 でライブプレビュー
.venv/bin/zensical serve -f mkdocs.ja.yml           # 日本語の場合（先に別のものを停止）

# 唯一の検証。PR では何も検証されません。site/ を消去する英語ビルドを先に。
.venv/bin/zensical build --strict
.venv/bin/zensical build -f mkdocs.ja.yml --strict
```

Windows (PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\python -m pip install -r docs/requirements.txt

.\.venv\Scripts\zensical serve                      # 英語を http://127.0.0.1:8000 でライブプレビュー
.\.venv\Scripts\zensical serve -f mkdocs.ja.yml     # 日本語の場合（先に別のものを停止）

# 唯一の検証。PR では何も検証されません。site/ を消去する英語ビルドを先に。
.\.venv\Scripts\zensical build --strict
.\.venv\Scripts\zensical build -f mkdocs.ja.yml --strict
```

`docs/requirements.txt` のバージョンは意図的に固定しています。更新はついでではなく、意図をもって行ってください。このポータルは [Zensical](https://zensical.org) を使っていますが、兄弟の Player リポジトリはまだ MkDocs + Material for MkDocs のため、バージョンを揃える運用は現在は行っていません。

`serve` はリンクを検証せず、1ロケールしか配信しないため、ヘッダーの言語セレクターは 404 になります。両ロケールをまとめてプレビューする方法は [README](./README.ja.md#言語切り替えのプレビュー) を参照してください。

## ドキュメントの規約

### 常に両言語
フォルダー方式の i18n を使っており、すべてのページは `docs/en/<path>` と `docs/ja/<path>` の 2 か所に存在します。ページの追加・移動・リネームは **必ず両方** に行ってください。片方だけだと strict ビルドが失敗します。英語が既定かつフォールバックのロケールです。

片方の言語しか自信がない場合は、その旨を PR に書いてください。両者が乖離するくらいなら、メンテナーがもう一方を補います。

### ナビゲーションは2つのロケール設定に
`nav:` は `mkdocs.yml`（英語）と `mkdocs.ja.yml`（日本語）にそれぞれあります。どちらもロケール相対のパス（`sdk/glossary.md` のように `en/` や `ja/` を付けない）を使い、構造は完全に一致させてください。異なるのはラベルだけで、翻訳マップを介さず各言語で直接書きます。片方に追加してもう片方を忘れると、そのロケールのナビにはそのページが現れません。

両ロケール共通の設定は `mkdocs.base.yml` にあり、2つの設定ファイルがこれを継承します。どこに何を書けるかは1つのルールで決まります — **YAML の配列は3ファイルのうち必ず1つにだけ定義すること。** Zensical の `INHERIT` は配列を置き換えではなく連結するため、base とロケール設定の両方に `nav` を置くと、2つのナビが続けて描画されます。

### リンク
- **内部リンク**は `.md` で終わる相対パス（例: `../sdk/concepts.md`）。`--strict` が検証します。
- **兄弟リポジトリへのリンク**は、リポジトリ自体を指してください。リポジトリ内のファイルを直接指す必要がある場合は、`blob/main/...` ではなく `blob/HEAD/...` と書いてください。多くの兄弟リポジトリは既定ブランチが `develop` のため、`main` を指すパスは気付かないまま 404 になります（`--strict` は内部リンクしか検証しません）。`HEAD` は常にそのリポジトリの既定ブランチへ解決されます。
- **公開前のサイト**（各 Player のドキュメントサイト、ライブデモ、ホスト版コンバーター）は、デプロイされるまで 404 になる GitHub Pages の URL のため、リンクにせず「coming soon」「準備中」の文字列にしています。対象は**これらのサイトのみ**で、`github.com/cri-middleware/…` のリポジトリへのリンクは先行リンクとして有効なままにします。サイトが公開されたら `en/` と `ja/` の両方でリンクに戻してください。

### 書き方
- 長く正しくあり続ける情報を優先してください。バージョン番号や要件表など、すべての兄弟リポジトリを追跡し続ける必要がある情報はポータルでは古くなりやすいものです。各プロジェクト自身のドキュメントに任せ、こちらからはリンクしてください。
- 周囲のページに合わせてください。見出しは先頭に絵文字、比較は表、注意書きは Material の `!!!` 記法。
- 2 つのロケールは構造を同一に保ってください（同じ見出し、同じ表、同じリンク）。以後の編集を一度に両方へ適用できます。

---
本プロジェクトへの貢献は、プロジェクトの [LICENSE.md](./LICENSE.md) に同意したものとみなされます。

# Contributing to SpriteStudio-Docs

> [!IMPORTANT]
> We are not accepting pull requests until a Contributor License Agreement (CLA) is in place. Issues remain open for bug reports and requests.

Thank you for your interest in improving the SpriteStudio documentation portal! Corrections, clarifications, and translation fixes are all welcome.

## Code of Conduct
Please refer to [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

## What belongs in this repository

This is a **portal**, not a mirror. Every player keeps its own documentation site in its own repository, and this repository hosts only the unified entry point plus the **cross-cutting** material that belongs to no single player: the landing page, the ecosystem overview, the platform chooser, the differences between players, shared SDK concepts, the format specification, shared limitations, the glossary, support routing, and licensing.

Consequences for a contribution:

- **Player-specific content goes to that player's repository.** The pages under `docs/*/players/` are intentionally thin - a short description plus links out. Please do not grow them into full player documentation.
- **Cross-cutting claims must be sourced from the sibling repositories.** This portal owns no code, so a statement about what a player supports must come from that player's own docs (or the SDK's). Please do not infer support - or the lack of it - that no repository documents. Where nothing is documented, say so.

## How Can I Contribute?

### Reporting problems
Open a [GitHub Issue](https://github.com/cri-middleware/SpriteStudio-Docs/issues) for a wrong or outdated description, a broken link, a missing translation, or a build failure. Problems with a player's own behavior belong in that player's repository - see [SUPPORT.md](./SUPPORT.md).

### Pull Requests
1. Fork the repository and create your branch from `main`.
2. Make the change in **both** `docs/en/` and `docs/ja/` (see below).
3. Build **both locales** locally - `scripts/build-docs.sh` (or `scripts\build-docs.ps1`) does exactly that, in the order that works. A pull request's CI runs the same build, so a broken link or a nav entry pointing at a missing page fails the PR as well; building first finds it sooner (see [Development Environment](#development-environment)).
4. Submit a Pull Request targeting `main` with a clear description. Use [Conventional Commits](https://www.conventionalcommits.org/) (e.g. `docs: …`).

Note that merging does **not** publish. Deployment is manual: a maintainer runs the `Publish docs via GitHub Pages` workflow (`workflow_dispatch`).

## Development Environment

You need Python 3.11 or later, Zensical's minimum. The `python3` that macOS ships is older, so point the script at a newer one: `scripts/prepare-docs.sh python=python3.13`.

```bash
scripts/prepare-docs.sh          # once: .venv + the pins in docs/requirements.txt
scripts/build-docs.sh            # English then Japanese, both --strict: what CI runs
scripts/build-pages.sh serve=yes # the published tree, both locales -> http://localhost:8000/
```

Both locales, English first: the English build clears `site/`, and the Japanese site lives inside it at `site/ja`, so an English-only build leaves no Japanese site at all. `mkdocs.base.yml` sets `strict: true`, so a broken internal link or a nav entry pointing at a missing page fails the build. `build-pages.sh serve=yes` serves both locales from one server, the only way to see the header's language selector resolve. `pages.yml`'s build job **is** that script, so a publish builds exactly what a local run with the same options builds, and a change to `prepare-docs.sh` or `build-pages.sh` is a change to the publish: keep them executable (mode `100755`). `.ps1` twins on Windows, `key=value` options and `--help` on every script.

`zensical serve` previews one locale as you write, and validates nothing, `--strict` or not:

```bash
.venv/bin/zensical serve                    # English at http://127.0.0.1:8000
.venv/bin/zensical serve -f mkdocs.ja.yml   # Japanese; stop the other one first
```

On Windows the executable is `.\.venv\Scripts\zensical`.

The toolchain versions in `docs/requirements.txt` are pinned deliberately - please bump them intentionally, not incidentally, and **in step with the sibling repositories**. Every sibling that builds its docs with Python - the SDK, Unity, Godot, Ren'Py, Flutter, wgpu, SSConverterGUI - pins the same [Zensical](https://zensical.org) version this repository does, so a bump here is a bump everywhere. (SSPlayerForWeb and SSPlayerForReactNative build with VitePress and have no pin to match.) Bump to a release uploaded at least seven days earlier: a release is likeliest to be yanked, or found compromised, in its first days, and pip run with a seven-day cooldown (`PIP_UPLOADED_PRIOR_TO=P7D`) does not install a younger one. If the new version raises its `Requires-Python`, raise `MIN_PYTHON` in `scripts/prepare-docs.sh` and `.ps1` with it.

## Documentation Standards

### Both languages, always
The site uses folder-based i18n: every page exists twice, as `docs/en/<path>` and `docs/ja/<path>`. When you add, move, or rename a page, **do it in both** - otherwise the strict build fails. There is no fallback locale: each locale is a separate build over its own `docs_dir`, so a page missing from `docs/ja/` is not quietly served in English, it is a nav entry pointing at nothing.

If you can only write one language confidently, say so in the PR; a maintainer can help with the other side rather than let the two drift.

### Navigation lives in the two locale configs
There is a `nav:` tree in `mkdocs.yml` (English) and another in `mkdocs.ja.yml` (Japanese). Both use locale-relative paths (`sdk/glossary.md`, no `en/` or `ja/` prefix) and the two must stay identical in structure - only the labels differ, written directly in the language rather than looked up from a translation map. Add a page to one and forget the other, and that page simply never appears in that locale's navigation.

Settings shared by both locales live in `mkdocs.base.yml`, which the two inherit. One rule governs what may go where: **a YAML sequence must be defined in exactly one of the three files.** Zensical's `INHERIT` concatenates sequences rather than replacing them, so a `nav` in the base as well as a locale config renders both navigations, one after the other.

### Links
- **Internal links** are relative file paths ending in `.md` (e.g. `../sdk/concepts.md`). `--strict` validates these.
- **Links into sibling repositories** should target the repository itself. When you must point inside one, write `blob/HEAD/...` for a file and `tree/HEAD/...` for a directory, never a branch name: the sibling repositories default to `main` or `develop` with no pattern to follow, so a branch path can 404 silently - `--strict` only validates internal links - while `HEAD` always resolves to that repository's default branch.
- **Write every page as published.** A sibling repository, its GitHub Pages site (a player's docs, a demo) and its Releases are linked as live, with no 🚧, "coming soon" or "準備中". A registry a package is not on (pub.dev, crates.io) goes unmentioned: name the route that exists. Change `en/` and `ja/` together.

### Writing
- Prefer material that stays true. Version numbers, requirement tables, and other facts that need tracking across every sibling repository age badly in a portal - let each project state those in its own docs, and link out instead.
- Match the surrounding page: sentence-case headings with a leading emoji, tables for comparisons, and `!!!` admonitions (Material) for notes and warnings.
- Keep the two locales structurally identical - same headings, same tables, same links - so future edits can be applied to both in one pass.

---
Contributions to this project are considered to be made under the terms of the project's [LICENSE.md](./LICENSE.md).

---

# SpriteStudio-Docs への貢献

> [!IMPORTANT]
> コントリビューターライセンス契約（CLA）の準備が整うまで、プルリクエストは受け付けていません。バグ報告や要望は引き続き Issue で受け付けています。

SpriteStudio ドキュメントポータルの改善にご関心をお寄せいただきありがとうございます。誤りの修正、説明の改善、翻訳の修正など、どれも歓迎します。

## 行動規範
[CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) を参照してください。

## このリポジトリが扱う範囲

ここは**ポータル**であり、各 Player ドキュメントのミラーではありません。各 Player のドキュメントはそれぞれのリポジトリのサイトで管理され、このリポジトリが持つのは統一された入口と、どの Player にも属さない**横断的な**情報だけです（ランディングページ、エコシステム概要、プラットフォームの選び方、Player ごとの違い、共通の SDK コンセプト、フォーマット仕様、共通の制限事項、用語集、サポート窓口の振り分け、ライセンス）。

貢献にあたっての帰結:

- **Player 固有の情報は、その Player のリポジトリへ。** `docs/*/players/` 配下のページは意図的に薄く保っています（短い説明と外部リンクのみ）。ここを本格的な Player ドキュメントに育てないでください。
- **横断的な記述は兄弟リポジトリを出典とすること。** このポータルはコードを持たないため、ある Player が何に対応しているかという記述は、その Player 自身（または SDK）のドキュメントに基づく必要があります。どのリポジトリにも記載のない対応可否を推測しないでください。記載がない場合は、その旨を書いてください。

## 貢献の方法

### 問題の報告
記述の誤りや古い情報、リンク切れ、翻訳の欠落、ビルドの失敗は [GitHub Issues](https://github.com/cri-middleware/SpriteStudio-Docs/issues) へ。各 Player の動作に関する問題は該当 Player のリポジトリへお願いします（[SUPPORT.md](./SUPPORT.md) 参照）。

### プルリクエスト
1. リポジトリを fork し、`main` からブランチを作成してください。
2. `docs/en/` と `docs/ja/` の **両方** を変更してください（下記参照）。
3. ローカルで **両ロケール** をビルドしてください。`scripts/build-docs.sh`（または `scripts\build-docs.ps1`）が正しい順序で両方をビルドします。プルリクエストの CI も同じビルドを実行するので、リンク切れや、存在しないページを指す nav エントリーがあれば PR も失敗します。先に手元でビルドすれば、早く気付けます（[開発環境](#開発環境) 参照）。
4. `main` を対象に、変更内容を明確に記載した PR を作成してください。コミットは [Conventional Commits](https://www.conventionalcommits.org/)（例: `docs: …`）に従ってください。

マージしても **公開はされません**。デプロイは手動で、メンテナーが `Publish docs via GitHub Pages` ワークフロー（`workflow_dispatch`）を実行します。

## 開発環境

Python 3.11 以上が必要です（Zensical の要件）。macOS に同梱の `python3` はこれより古いので、新しいものをスクリプトに指定してください: `scripts/prepare-docs.sh python=python3.13`。

```bash
scripts/prepare-docs.sh          # 一度だけ: .venv と docs/requirements.txt のピン
scripts/build-docs.sh            # 英語 → 日本語の順に --strict でビルド。CI と同じビルド
scripts/build-pages.sh serve=yes # 公開ツリー、両ロケール -> http://localhost:8000/
```

必ず両ロケールを、英語を先にビルドします。英語ビルドは `site/` を消去し、日本語サイトはその内側（`site/ja`）に出力されるため、英語だけをビルドすると日本語サイトは残らず消えます。`mkdocs.base.yml` が `strict: true` を設定しているので、内部リンク切れや、存在しないページを指す nav エントリーがあるとビルドは失敗します。`build-pages.sh serve=yes` は両ロケールを 1 つのサーバーで配信します。ヘッダーの言語セレクターの動作を確認できるのはこの方法だけです。`pages.yml` のビルドジョブは**このスクリプト**なので、公開でビルドされるものは、同じオプションで手元でビルドしたものと一致します。`prepare-docs.sh` と `build-pages.sh` への変更は公開への変更でもあるため、実行権限（モード `100755`）を保ってください。Windows は `.ps1` 版を使い、どのスクリプトも `key=value` 形式のオプションと `--help` を取ります。

執筆中は `zensical serve` で 1 ロケールをプレビューできます。`--strict` を付けても何も検証しません。

```bash
.venv/bin/zensical serve                    # 英語を http://127.0.0.1:8000 で
.venv/bin/zensical serve -f mkdocs.ja.yml   # 日本語（先にもう一方を停止）
```

Windows では実行ファイルは `.\.venv\Scripts\zensical` です。

`docs/requirements.txt` のバージョンは意図的に固定しています。更新はついでではなく、意図をもって、かつ**兄弟リポジトリと足並みを揃えて**行ってください。Python でドキュメントをビルドする兄弟リポジトリ（SDK・Unity・Godot・Ren'Py・Flutter・wgpu・SSConverterGUI）は、このリポジトリと同じ [Zensical](https://zensical.org) のバージョンを固定しているため、ここでの更新は全リポジトリでの更新を意味します（SSPlayerForWeb と SSPlayerForReactNative は VitePress のため対象外です）。更新先は、アップロードから 7 日以上たったリリースにしてください。取り下げられたり侵害が見つかったりするのは公開直後の数日が最も多く、7 日のクールダウン（`PIP_UPLOADED_PRIOR_TO=P7D`）を設定した pip はそれより新しいリリースを入れません。新しい版が `Requires-Python` を引き上げたら、`scripts/prepare-docs.sh` と `.ps1` の `MIN_PYTHON` も合わせて引き上げてください。

## ドキュメントの規約

### 常に両言語
フォルダー方式の i18n を使っており、すべてのページは `docs/en/<path>` と `docs/ja/<path>` の 2 か所に存在します。ページの追加・移動・リネームは **必ず両方** に行ってください。片方だけだと strict ビルドが失敗します。フォールバックのロケールはありません。ロケールごとに `docs_dir` の異なる別のビルドなので、`docs/ja/` に無いページが英語で代替表示されることはなく、リンク先の無い nav エントリーになります。

片方の言語しか自信がない場合は、その旨を PR に書いてください。両者が乖離するくらいなら、メンテナーがもう一方を補います。

### ナビゲーションは2つのロケール設定に
`nav:` は `mkdocs.yml`（英語）と `mkdocs.ja.yml`（日本語）にそれぞれあります。どちらもロケール相対のパス（`sdk/glossary.md` のように `en/` や `ja/` を付けない）を使い、構造は完全に一致させてください。異なるのはラベルだけで、翻訳マップを介さず各言語で直接書きます。片方に追加してもう片方を忘れると、そのロケールのナビにはそのページが現れません。

両ロケール共通の設定は `mkdocs.base.yml` にあり、2つの設定ファイルがこれを継承します。どこに何を書けるかは1つのルールで決まります — **YAML の配列は3ファイルのうち必ず1つにだけ定義すること。** Zensical の `INHERIT` は配列を置き換えではなく連結するため、base とロケール設定の両方に `nav` を置くと、2つのナビが続けて描画されます。

### リンク
- **内部リンク**は `.md` で終わる相対パス（例: `../sdk/concepts.md`）。`--strict` が検証します。
- **兄弟リポジトリへのリンク**は、リポジトリ自体を指してください。リポジトリ内を直接指す必要がある場合は、ブランチ名を書かず、ファイルなら `blob/HEAD/...`、ディレクトリなら `tree/HEAD/...` と書いてください。兄弟リポジトリの既定ブランチは `main` と `develop` が混在しており、ブランチ名を書いたパスは気付かないまま 404 になります（`--strict` は内部リンクしか検証しません）。`HEAD` は常にそのリポジトリの既定ブランチへ解決されます。
- **公開済みとして書きます。** 兄弟リポジトリ、その GitHub Pages のサイト（Player のドキュメント、デモ）、Releases は公開されているものとしてリンクし、🚧・「coming soon」・「準備中」は付けません。パッケージが載っていないレジストリ（pub.dev、crates.io）には触れず、実際にある入手経路を書きます。`en/` と `ja/` は一緒に変えてください。

### 書き方
- 長く正しくあり続ける情報を優先してください。バージョン番号や要件表など、すべての兄弟リポジトリを追跡し続ける必要がある情報はポータルでは古くなりやすいものです。各プロジェクト自身のドキュメントに任せ、こちらからはリンクしてください。
- 周囲のページに合わせてください。見出しは先頭に絵文字、比較は表、注意書きは Material の `!!!` 記法。
- 2 つのロケールは構造を同一に保ってください（同じ見出し、同じ表、同じリンク）。以後の編集を一度に両方へ適用できます。

---
本プロジェクトへの貢献は、プロジェクトの [LICENSE.md](./LICENSE.md) の条件の下で行われたものとみなされます。

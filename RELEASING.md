# Publishing SpriteStudio-Docs

Maintainers only. Contributors do not run any of this — see [CONTRIBUTING.md](./CONTRIBUTING.md).

## Publishing the site

Anyone with the Write role on this repository can publish: a publish is one workflow run, so nothing depends on whose machine starts it. You need `gh` (run `gh auth login` once) and the docs toolchain from [CONTRIBUTING.md](./CONTRIBUTING.md#development-environment). The commands are bash; on Windows, run them in PowerShell, with `scripts\build-pages.ps1` in place of the `.sh`.

The portal cuts no releases — no version, no tag, no Release. A publish is a run of `pages.yml`: it builds the site from the branch it was started on and replaces the whole published site with the result. Nothing else starts it, and merging a pull request publishes nothing, so `main` can hold merged changes the site does not show yet.

### 1. Read what main will publish

Nothing builds a pull request, so the merges in `main` have never been built together. Build `main` the way the workflow does and read the result in a browser: both locales, and the language selector on a page other than the home page.

```bash
git switch main && git pull --ff-only
scripts/build-pages.sh serve=yes    # http://localhost:8000/; Ctrl-C to stop
```

### 2. Run the workflow from main

```bash
gh workflow run pages.yml --ref main
gh run watch                        # the run takes a few seconds to appear
```

Always from `main`: nothing in the workflow stops a run started on another branch from publishing that branch. **Run workflow** on the Actions page offers `main` by default. The build is `--strict`, so a broken internal link fails the run before anything is deployed, and the site stays as it was.

### 3. Check the live site

Open <https://cri-middleware.github.io/SpriteStudio-Docs/> and <https://cri-middleware.github.io/SpriteStudio-Docs/ja/>, and switch language on a page other than the home page.

## Undoing a publish

A publish replaces the whole site, so undoing one is publishing again: revert the change on `main` through a pull request, then go back to step 1. A run that failed deployed nothing; fix the cause on `main` and run it again.

<br>

---

# SpriteStudio-Docs の公開手順

維持者向けです。コントリビューターがこの手順を実行することはありません（[CONTRIBUTING.md](./CONTRIBUTING.md) を参照してください）。

## サイトの公開

このリポジトリの Write ロールを持つ人なら誰でも公開できます。公開はワークフローの実行 1 回なので、誰の手元から始めても結果は変わりません。必要なのは `gh`（最初に一度 `gh auth login`）と、[CONTRIBUTING.md](./CONTRIBUTING.md#開発環境) の docs ツールチェーンです。コマンドは bash で書いています。Windows では PowerShell で、`.sh` の代わりに `scripts\build-pages.ps1` を実行してください。

ポータルはリリースを切りません。バージョンもタグも Release もありません。公開とは `pages.yml` の実行のことで、実行を始めたブランチからサイトをビルドし、公開中のサイト全体をその結果で置き換えます。ほかに公開を始めるものは無く、プルリクエストをマージしても何も公開されないので、`main` にはサイトにまだ出ていないマージ済みの変更があり得ます。

### 1. main が公開するものを読む

プルリクエストではビルドが走らないため、`main` に入ったマージは一度も一緒にビルドされていません。ワークフローと同じ方法で `main` をビルドし、結果をブラウザで読みます。両ロケールと、トップページ以外のページでの言語セレクターです。

```bash
git switch main && git pull --ff-only
scripts/build-pages.sh serve=yes    # http://localhost:8000/ 。Ctrl-C で停止
```

### 2. main からワークフローを実行する

```bash
gh workflow run pages.yml --ref main
gh run watch                        # run が一覧に出るまで数秒かかる
```

必ず `main` から実行します。別のブランチから始めた実行がそのブランチを公開するのを、ワークフローは止めません。Actions ページの **Run workflow** は既定で `main` を選びます。ビルドは `--strict` なので、内部リンクが切れていれば何もデプロイされないまま実行が失敗し、サイトはそのまま残ります。

### 3. 公開されたサイトを確かめる

<https://cri-middleware.github.io/SpriteStudio-Docs/> と <https://cri-middleware.github.io/SpriteStudio-Docs/ja/> を開き、トップページ以外のページで言語を切り替えます。

## 公開の取り消し

公開はサイト全体を置き換えるので、取り消しはもう一度公開することです。`main` でその変更をプルリクエストで revert し、手順 1 に戻ります。失敗した実行は何もデプロイしていません。原因を `main` で直してから、もう一度実行します。

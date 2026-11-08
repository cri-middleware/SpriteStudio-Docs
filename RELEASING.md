# Publishing SpriteStudio-Docs

Maintainers only. Contributors do not run any of this — see [CONTRIBUTING.md](./CONTRIBUTING.md).

## Publishing the site

Anyone with the Write role on this repository can publish: a publish is one workflow run, so nothing depends on whose machine starts it. You need `gh` 2.87 or later (run `gh auth login` once) and the docs toolchain from [CONTRIBUTING.md](./CONTRIBUTING.md#development-environment).

Every command block runs as written in a new shell; **a person** reads the local preview and sorts ScanCode matches in step 1, and decides step 2 (publishing to production). The blocks are bash. zsh runs them too; run `setopt interactive_comments` once there so `#` comments in pasted blocks are ignored. On Windows, run them in Git Bash, except the local preview, which runs in PowerShell with `scripts\build-pages.ps1` in place of the `.sh`. Step 1 switches branches, so run it in a clean checkout.

The portal cuts no releases — no version, no tag, no Release. A publish is a run of `pages.yml`: it builds the site from the branch it was started on and replaces the whole published site with the result. Nothing else starts it, and merging a pull request publishes nothing, so `main` can hold merged changes the site does not show yet.

### 1. Read what main will publish

Build `main` the way the workflow does and read the result in a browser: both locales, and the language selector on a page other than the home page.

```bash
git switch main && git pull --ff-only
scripts/build-pages.sh prepare=yes serve=yes    # http://localhost:8000/; Ctrl-C to stop
```

Then scan `main` for copyright and license notices copied from others. `provenance.yml` runs ScanCode, which finds them. **A person sorts what it finds.** A notice of the earlier SpriteStudio Players and SDK is our own. Anything else is rewritten, unless its license, read at its source, is compatible with BSD-3-Clause and the notice that license asks for is kept. Fix it by a pull request into `main`, and run the block again.

```bash
RUN=$(gh workflow run provenance.yml --ref main | sed 's|.*/||') &&
  gh run watch "${RUN:?}" --exit-status &&
  gh run download "${RUN:?}" -n provenance -D "qa/$RUN" &&
  cat "qa/$RUN/summary.md"
```

### 2. Run the workflow from main

**A person decides when to publish.**

```bash
RUN=$(gh workflow run pages.yml --ref main | sed 's|.*/||') &&
  gh run watch "${RUN:?}" --exit-status
```

Always from `main`: a run started on another branch fails at its first step and deploys nothing. **Run workflow** on the Actions page offers `main` by default. The build is `--strict`, so a broken internal link fails the run before anything is deployed, and the site stays as it was.

### 3. Check the live site

Open <https://cri-middleware.github.io/SpriteStudio-Docs/> and <https://cri-middleware.github.io/SpriteStudio-Docs/ja/>, and switch language on a page other than the home page. Then check the external links, which no build does: `ci.yml` runs the link check along with the build. A broken link fails the run, and the block then prints the log of the step that failed, which names the link.

```bash
RUN=$(gh workflow run ci.yml --ref main | sed 's|.*/||') &&
  gh run watch "${RUN:?}" --exit-status ||
  { gh run view "${RUN:?}" --log-failed; false; }
```

## Undoing a publish

A publish replaces the whole site, so undoing one is publishing again: revert the change on `main` through a pull request, then go back to step 1. A run that failed deployed nothing; fix the cause on `main` and run it again.

<br>

---

# SpriteStudio-Docs の公開手順

維持者向けです。コントリビューターがこの手順を実行することはありません（[CONTRIBUTING.md](./CONTRIBUTING.md) を参照してください）。

## サイトの公開

このリポジトリの Write ロールを持つ人なら誰でも公開できます。公開はワークフローの実行 1 回なので、誰の手元から始めても結果は変わりません。必要なのは `gh` 2.87 以降（最初に一度 `gh auth login`）と、[CONTRIBUTING.md](./CONTRIBUTING.md#開発環境) の docs ツールチェーンです。

各コマンドブロックは新しいシェルでそのまま実行できます。手順 1 のローカルプレビューの確認と ScanCode 検出結果の仕分け、手順 2（本番環境への公開の判断）は**人が行います**。ブロックは bash で書いています。zsh でも動きます。その場合は、貼り付けたブロック内の `#` コメントが無視されるよう、最初に一度 `setopt interactive_comments` を実行してください。Windows では Git Bash で実行します。ただしローカルプレビューは PowerShell で、`.sh` の代わりに `scripts\build-pages.ps1` を実行します。手順 1 はブランチを切り替えるため、クリーンなチェックアウトで実行してください。

ポータルはリリースを切りません。バージョンもタグも Release もありません。公開とは `pages.yml` の実行のことで、実行を始めたブランチからサイトをビルドし、公開中のサイト全体をその結果で置き換えます。ほかに公開を始めるものは無く、プルリクエストをマージしても何も公開されないので、`main` にはサイトにまだ出ていないマージ済みの変更があり得ます。

### 1. main が公開するものを読む

ワークフローと同じ方法で `main` をビルドし、結果をブラウザで読みます。両ロケールと、トップページ以外のページでの言語セレクターです。

```bash
git switch main && git pull --ff-only
scripts/build-pages.sh prepare=yes serve=yes    # http://localhost:8000/ 。Ctrl-C で停止
```

続けて、他者の著作権表示やライセンスの記述が紛れ込んでいないかを、`main` で照合します。`provenance.yml` は ScanCode でそれを見つけます。**見つかったものは人が仕分けます。** 以前の SpriteStudio の Player・SDK の表示は、自社のものです。それ以外は書き直します。残せるのは、出所で確かめたライセンスが BSD-3-Clause と両立し、そのライセンスが求める表示を残すときだけです。直すときは、プルリクエストで `main` を直し、このブロックをもう一度実行します。

```bash
RUN=$(gh workflow run provenance.yml --ref main | sed 's|.*/||') &&
  gh run watch "${RUN:?}" --exit-status &&
  gh run download "${RUN:?}" -n provenance -D "qa/$RUN" &&
  cat "qa/$RUN/summary.md"
```

### 2. main からワークフローを実行する

**公開の実行は人が判断します。**

```bash
RUN=$(gh workflow run pages.yml --ref main | sed 's|.*/||') &&
  gh run watch "${RUN:?}" --exit-status
```

必ず `main` から実行します。別のブランチから始めた実行は最初のステップで失敗し、何もデプロイしません。Actions ページの **Run workflow** は既定で `main` を選びます。ビルドは `--strict` なので、内部リンクが切れていれば何もデプロイされないまま実行が失敗し、サイトはそのまま残ります。

### 3. 公開されたサイトを確かめる

<https://cri-middleware.github.io/SpriteStudio-Docs/> と <https://cri-middleware.github.io/SpriteStudio-Docs/ja/> を開き、トップページ以外のページで言語を切り替えます。続けて、どのビルドも確かめない外部リンクを確認します。`ci.yml` はビルドとあわせてリンクチェックを実行します。リンクが切れていれば run は失敗し、ブロックが失敗したステップのログを表示します。切れたリンクはそのログに出ます。

```bash
RUN=$(gh workflow run ci.yml --ref main | sed 's|.*/||') &&
  gh run watch "${RUN:?}" --exit-status ||
  { gh run view "${RUN:?}" --log-failed; false; }
```

## 公開の取り消し

公開はサイト全体を置き換えるので、取り消しはもう一度公開することです。`main` でその変更をプルリクエストで revert し、手順 1 に戻ります。失敗した実行は何もデプロイしていません。原因を `main` で直してから、もう一度実行します。

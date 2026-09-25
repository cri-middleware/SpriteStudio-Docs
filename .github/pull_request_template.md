<!--
Thanks for contributing! See CONTRIBUTING.md for the constraints this project works under
(both locales, claims sourced from the sibling repositories, links into them through `HEAD`).
CONTRIBUTING.md に本プロジェクトの制約が記載されています。日本語でも英語でも構いません。
-->

## What does this change? / 変更内容

<!-- What it does and why. Link any related issue: Fixes #123 -->

## How was it verified? / 検証方法

<!--
Which checks ran, and on what. If you could not run them, say so —
that is useful information, not a problem.
実行した確認と環境。実行できなかった場合はその旨をお書きください。
-->

- [ ] `scripts/build-docs.sh` — builds `en` and `ja` with `--strict`; nothing builds the docs on a pull request
- [ ] `scripts/build-pages.sh serve=yes` — checked the pages and the language selector in a browser
- [ ] Not run — see notes below / 未実行（理由は下記）

**Environment / 環境:** OS, and bash or PowerShell

## Checklist

- [ ] Scoped to one thing. Unrelated fixes are easier to review as their own PR.
- [ ] Follows the style of the files it touches.
- [ ] Docs updated if behaviour changed.
- [ ] Anything that exists twice changed twice — a page and its translation, a `.sh` and its `.ps1`.
- [ ] `docs/en/` and `docs/ja/` both changed, and `nav` in both `mkdocs.yml` and `mkdocs.ja.yml`.
- [ ] Every claim comes from a sibling repository; nothing is inferred.
- [ ] Links into sibling repositories use `blob/HEAD/` or `tree/HEAD/`, never a branch name.
- [ ] 🚧 sits immediately before the pending phrase, with the same marks in both locales.

## Anything reviewers should know? / レビュー時の注意点

<!-- Trade-offs you made, alternatives you rejected, parts you are unsure about. -->

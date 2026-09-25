# Security Policy

## Supported Versions

This repository builds a static documentation site from `main`. Fixes are made on `main`.

## Reporting a Vulnerability

**Please do not open a public GitHub Issue for a security problem.** Report it privately through the
official inquiry form:

👉 [**CRI Middleware Inquiry Form (English)**](https://www.webtech.co.jp/contact/en.html)

The English form has no file upload. If you need to send a reproduction, use the
[Japanese Help Center form](https://www.webtech.co.jp/help/ja/spritestudio7/inquiries/ssplayer_tool/),
which takes a zip of up to 8 MB.

Please include:

- What the impact is — script injected into a page, a compromised build dependency, a leaked secret.
- The page, file or workflow involved, and the steps that show the problem.

We will confirm receipt, tell you whether we can reproduce it, and let you know when a fix ships.
Please give us a chance to release that fix before disclosing publicly.

### Which repository to report to

This portal only documents the SpriteStudio players and the SDK. A vulnerability in one of them is
reported through the same form; name the repository, and it will be routed.

## Scope Notes

This repository is documentation: Markdown pages, the site configuration, and the scripts and workflow
that build it and publish it to GitHub Pages. Anything in the published site or its build that could harm
a reader or a maintainer is in scope — a page that runs injected script, a build dependency that has been
compromised, a workflow that exposes a secret.

---

# セキュリティポリシー

## サポート対象バージョン

本リポジトリは `main` から静的なドキュメントサイトをビルドします。修正は `main` に対して行います。

## 脆弱性の報告

**セキュリティに関する問題は、公開の GitHub Issue に投稿しないでください。** 再現データ（8 MB までの zip ファイル）の添付も可能なヘルプセンターより、非公開でご報告ください。

👉 [**ヘルプセンター（お問い合わせフォーム）**](https://www.webtech.co.jp/help/ja/spritestudio7/inquiries/ssplayer_tool/)

ご報告には以下を含めてください。

- 影響の内容（ページへのスクリプト混入、ビルド依存の侵害、秘密情報の漏洩など）
- 関係するページ、ファイル、またはワークフローと、問題を示す手順

受領の確認、再現可否、修正版の公開時期についてご連絡します。修正を公開するまでの間、公表をお待ちいただけますようお願いします。

### 報告先リポジトリの判断

本ポータルは SpriteStudio の各 Player と SDK を紹介するドキュメントです。それらの脆弱性も同じフォームからご報告ください。対象のリポジトリ名を添えていただければ、こちらで振り分けます。

## 既知の注意点

本リポジトリはドキュメントです。Markdown のページ、サイトの設定、そしてサイトをビルドして GitHub Pages へ公開するスクリプトとワークフローから成ります。公開されたサイトやそのビルドのうち、読者やメンテナーに害を及ぼしうるもの（スクリプトが混入したページ、侵害されたビルド依存、秘密情報を漏らすワークフローなど）が対象です。

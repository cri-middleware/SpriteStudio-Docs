[**English**](./README.md) | [**日本語**](./README.ja.md)

# SpriteStudio Docs

SpriteStudio SDK と公式 Player 群のドキュメント**ポータル**です。

このリポジトリは軽量なハブです。各 Player のドキュメントを**再ホストはしません** - Player のドキュメントはそれぞれのリポジトリのサイトで管理されています。ここが提供するのは統一された入口と、どの Player にも属さない横断的な情報です。

- 製品カードを並べたランディングページ
- [エコシステム概要](docs/ja/overview/ecosystem.md)と[プラットフォームの選び方](docs/ja/overview/choose-your-platform.md)
- [アセットの変換](docs/ja/overview/conversion.md)と[スタンドアロンツールでの変換](docs/ja/overview/convert-with-a-standalone-tool.md)
- [Player ごとの違い](docs/ja/overview/player-differences.md)と、共通ランタイムの[制限事項](docs/ja/sdk/limitations.md)
- 共通の [SDK コンセプト](docs/ja/sdk/concepts.md)、[用語集](docs/ja/sdk/glossary.md)、[フォーマット仕様](docs/ja/sdk/format-spec.md)、[移植ガイドへの案内](docs/ja/sdk/porting.md)
- [サポート窓口の振り分け](docs/ja/support.md)と共通のライセンス情報

公開先: <https://cri-middleware.github.io/SpriteStudio-Docs/ja/>

## 構成

```
docs/
  en/ , ja/          # ロケールごとに1フォルダー、ロケールごとに1設定ファイル
    assets/          # favicon（ロケールごとにコピーを持ちます）
    index.md         # ランディングページ（製品カード）
    overview/        # ecosystem, choose-your-platform, player-differences,
                     #   try-it, conversion, convert-with-a-standalone-tool,
                     #   ai-assistants
    sdk/             # concepts, glossary, format-spec, limitations, porting
                     #   （横断的な正典）
    players/         # 各 Player のドキュメントへリンクする薄い入口ページ
    support.md
    license.md
  requirements.txt
scripts/
  prepare-docs.{sh,ps1}       # venv の作成と、バージョン固定したツールチェーンの導入
  build-docs.{sh,ps1}         # 両ロケールを正しい順序で strict ビルド
  build-pages.{sh,ps1}        # 上の 2 つを実行し site/ を配信。workflow が呼ぶもの
mkdocs.base.yml               # 両ロケール共通の設定
mkdocs.yml                    # 英語   -> site/
mkdocs.ja.yml                 # 日本語 -> site/ja/
.github/workflows/ci.yml      # プルリクエストごとと毎週のビルド（strict）
.github/workflows/pages.yml   # ビルド（strict）＋ GitHub Pages へのデプロイ
```

すべてのページは `en/` と `ja/` の**両方**に存在し、各ロケールはそれぞれの設定ファイルからビルドされます。`mkdocs.yml` と `mkdocs.ja.yml` は `mkdocs.base.yml` から共通設定を継承し、差分だけを持ちます — ドキュメントディレクトリ、出力先、サイト URL、言語、そしてその言語で書いたナビゲーションと `llms.txt` の目次です。

サイトの生成には [Zensical](https://zensical.org)（MkDocs + Material for MkDocs の後継。開発チームは同じ）を使用しています。設定ファイルは MkDocs の設定としても有効なままなので、エンジンを比較したい場合は `mkdocs-material` でも同じサイトをビルドできます。

## 貢献について

誤りの修正、説明の改善、翻訳の修正を歓迎します。手順、サイトのビルドとプレビューの方法、ドキュメントの規約は [CONTRIBUTING.md](./CONTRIBUTING.md) を参照してください。参加にあたっては[行動規範](./CODE_OF_CONDUCT.md)が適用されます。質問や不具合の報告先は [SUPPORT.md](./SUPPORT.md) をご覧ください。

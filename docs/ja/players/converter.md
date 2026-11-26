---
description: "SpriteStudio のプロジェクト（.sspj）を公式 Player 向けに変換するデスクトップアプリ、SSConverter GUI。SpriteStudio は、手持ちのイラストにボーン・メッシュ・エフェクトを付けて動かす 2D アニメーションツールです。"
---

# 🖥️ SSConverter GUI

`libssconverter` をラップした **デスクトップアプリ**（Tauri）です。CLI を使わずに `.sspj`
プロジェクトをランタイム用アセットへ変換できます。配布しているビルドは **macOS と Windows**
です。Linux では SDK の `ssconverter-cli` を使ってください（ウィンドウが無いだけで、同じ
`libssconverter` です）。

- **入手:** [GitHub Releases](https://github.com/cri-middleware/SSConverterGUI/releases)
- **使い方:** [スタンドアロンツールで変換する](../overview/convert-with-a-standalone-tool.md)
- **ドキュメント:** <https://cri-middleware.github.io/SSConverterGUI/ja/>
- **リポジトリ:** <https://github.com/cri-middleware/SSConverterGUI>

再生ではなく変換のためのツールなので、このページには Player のページのようなインストール・変換・再生の手順はありません。出力フォルダは、Player がアセットを読み込む場所へコピーしてください。場所は各 Player のクイックスタートにあり、[プラットフォームの選び方](../overview/choose-your-platform.md) から辿れます。これらのアセットが供給される変換パイプラインについては [SDK コンセプト](../sdk/concepts.md) を参照してください。

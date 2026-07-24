# 📱 SSPlayerForFlutter

**Flutter** アプリで SpriteStudio 7（`.ssab`）アニメーションを再生します。`ssplayer_flutter`
パッケージの `SpriteStudioView` ウィジェットが共有 Rust ランタイム（`libssruntime`）を
`dart:ffi` 経由で駆動し、`Canvas.drawVertices` で描画するため、Flutter の各ターゲットで通常の
ウィジェットと同様に合成できます。[Flame](https://flame-engine.org/) アダプター（`ssplayer_flame`）、
`.sspj` を `.ssab` に変換する同梱の `ssconvert` CLI、編集内容を実行中のアプリへ反映するライブ
リロードも備えています。パッケージは pub.dev には未公開のため、当面は GitHub Releases の
バンドルからインストールしてください。

- **ドキュメント:** _準備中_
- **リポジトリ:** <https://github.com/cri-middleware/SSPlayerForFlutter>

Player の比較は [プラットフォームの選び方](../overview/choose-your-platform.md) を、
全 Player 共通の変換／再生パイプラインは [SDK コンセプト](../sdk/concepts.md) を参照してください。

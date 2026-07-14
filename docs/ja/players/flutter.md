# 📱 SSPlayerForFlutter

**Flutter** アプリで SpriteStudio 7（`.ssab`）アニメーションを再生します。`SpriteStudioView`
ウィジェットが共有 Rust ランタイム（`libssruntime`）を `dart:ffi` 経由で駆動し、
`Canvas.drawVertices` で描画するため、Flutter の各ターゲットで通常のウィジェットと同様に
合成できます。同梱の Dart 製コンバーター（`ssconverter_dart` / `ssconvert` CLI）で
`.sspj` を `.ssab` に変換できます。

!!! warning "開発初期"
    🧪 SSPlayerForFlutter は**開発中**（alpha、`ssruntime_dart 7.0.0-alpha.x` を基盤）で、
    **pub.dev には未公開**です。現時点で基本的な再生は動作しますが、応用機能（パーツカラー・
    マスク・メッシュ変形・エフェクト・インスタンス）は実装中です。API・パッケージ構成は
    変更される可能性があります。

- **リポジトリ:** <https://github.com/cri-middleware/SSPlayerForFlutter>

Player の比較は [プラットフォームの選び方](../overview/choose-your-platform.md) を、
全 Player 共通の変換／再生パイプラインは [SDK コンセプト](../sdk/concepts.md) を参照してください。

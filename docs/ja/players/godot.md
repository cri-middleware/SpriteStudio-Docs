# 🕹️ SSPlayerForGodot

**Godot Engine** でネイティブに SpriteStudio アニメーションを描画します。`libssruntime` を
基盤とし、2 つの形態で提供されます。

- **GDExtension** - エンジンの再ビルド不要で導入できるバイナリアドオン。
- **カスタムモジュール** - Godot 本体に組み込んでビルドする、より密な統合方式。

アニメーションのサウンド（`ssaudio`）イベントをエンジンのオーディオで再生でき、独自の
オーディオバックエンドへ差し替えるフックも備えます。

- **ドキュメント:** <https://cri-middleware.github.io/SSPlayerForGodot/>
- **リポジトリ:** <https://github.com/cri-middleware/SSPlayerForGodot>

Player の比較は [プラットフォームの選び方](../overview/choose-your-platform.md) を、
全 Player 共通の変換／再生パイプラインは [SDK コンセプト](../sdk/concepts.md) を参照してください。

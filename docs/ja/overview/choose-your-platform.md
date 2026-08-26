# 🧭 プラットフォームの選び方

対象ランタイムに合ったものを選んでください。名前は各ページの概要へ、右列はそれぞれの
詳しい情報へリンクしています。

| 動かしたい対象 | 使用するもの | 詳細 |
|---|---|---|
| Unity ゲーム | **[SSPlayerForUnity](../players/unity.md)** | ドキュメント（準備中） |
| **ブラウザ** - PixiJS・WebGL | **[SSPlayerForWeb](../players/web.md)**（Player コレクション） | ドキュメント（準備中） |
| **ブラウザ** - WebGPU | **[SSPlayerForWgpu](../players/wgpu.md)**（`@spritestudio/ssplayer-wgpu`） | ドキュメント（準備中） |
| **RPG ツクール MZ** | **[SSPlayerForWeb](../players/web.md)**（`ssplayer-rmmz`） | ドキュメント（準備中） |
| **TyranoScript / TyranoBuilder** のビジュアルノベル | **[SSPlayerForWeb](../players/web.md)**（`ssplayer-tyranoscript` / `ssplayer-tyranobuilder`） | ドキュメント（準備中） |
| Godot ゲーム | **[SSPlayerForGodot](../players/godot.md)** | ドキュメント（準備中） |
| **Bevy** ゲーム | **[SSPlayerForWgpu](../players/wgpu.md)**（`ssplayer-wgpu-bevy`） | ドキュメント（準備中） |
| **Flutter** アプリ | **[SSPlayerForFlutter](../players/flutter.md)** | ドキュメント（準備中） |
| Ren'Py ビジュアルノベル | **[SSPlayerForRenPy](../players/renpy.md)** | ドキュメント（準備中） |
| エンジンを使わず自分で描画する **Rust** / **C・C++** アプリケーション | **[SSPlayerForWgpu](../players/wgpu.md)** | ドキュメント（準備中） |
| **React Native** アプリ | **[SSPlayerForReactNative](../players/react-native.md)** | ドキュメント（準備中） |
| 独自の Player ・組み込みを作りたい | **SpriteStudio-SDK** | [Player の移植](../sdk/porting.md) |

Player ごとの統合の成熟度は [プレイヤーごとの違い](./player-differences.md) と各 Player のページに
記載しており、この表では重複して書きません。

`.sspj` の変換だけしたい場合は、Player ではなくスタンドアロンツールを選びます。

| 変換したい環境 | 使用するもの | 詳細 |
|---|---|---|
| ウェブ（ブラウザ） | **[SSPlayerForWeb](../players/web.md)**（`ssconverter-web`） | 試す（準備中） |
| デスクトップ - GUI | **[SSConverterGUI](../players/converter.md)** | ドキュメント（準備中） |
| デスクトップ - CLI | **SpriteStudio-SDK**（`ssconverter-cli`） | [使い方](./convert-with-a-standalone-tool.md) |

## ✅ すべてのプラットフォームに共通

- **変換ステップ**（`.sspj` -> ランタイムアセット `.ssab` / `.ssqb` ＋テクスチャ）はどこでも
  同じです。パイプラインは
  [SDK コンセプト](../sdk/concepts.md)、変換方法（インポート時の自動変換・GUI・CLI・ブラウザ）は
  [アセットの変換](./conversion.md) を参照してください。
- 対応機能（ボーン、メッシュ／デフォーム、パーティクル、拡張ブレンド、マスク）は
  共通コアが担うため、機能セット自体はどこでも同じです。エンジンごとに残る差分は
  [プレイヤーごとの違い](./player-differences.md)、すべての Player に共通する制約は
  [共通の制限事項](../sdk/limitations.md) を参照してください。
- ライセンスは共通です。[ライセンス](../license.md) を参照してください。

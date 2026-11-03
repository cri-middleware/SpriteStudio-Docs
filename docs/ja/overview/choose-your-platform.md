# 🧭 プラットフォームの選び方

対象ランタイムに合ったものを選んでください。名前は各ページの概要へ、右列はそれぞれの詳しい情報へリンクしています。

| 動かしたい対象 | 使用するもの | 詳細 |
|---|---|---|
| Unity ゲーム | **[SpriteStudio Player for Unity](../players/unity.md)** | [ドキュメント](https://cri-middleware.github.io/SSPlayerForUnity/ja/) |
| **ブラウザ** - PixiJS・WebGL | **[SpriteStudio Player for Web](../players/web.md)**（Player コレクション） | [ドキュメント](https://cri-middleware.github.io/SSPlayerForWeb/ja/) |
| **ブラウザ** - WebGPU | **[SpriteStudio Player for wgpu](../players/wgpu.md)**（`@spritestudio/ssplayer-wgpu`） | [ドキュメント](https://cri-middleware.github.io/SSPlayerForWgpu/ja/start/web/) |
| **RPG ツクール MZ** | **[SpriteStudio Player for Web](../players/web.md)**（`ssplayer-rmmz`） | [ドキュメント](https://cri-middleware.github.io/SSPlayerForWeb/ja/usage/rmmz) |
| **TyranoScript / ティラノビルダー** のビジュアルノベル | **[SpriteStudio Player for Web](../players/web.md)**（`ssplayer-tyranoscript` / `ssplayer-tyranobuilder`） | ドキュメント: [TyranoScript](https://cri-middleware.github.io/SSPlayerForWeb/ja/usage/tyrano) / [ティラノビルダー](https://cri-middleware.github.io/SSPlayerForWeb/ja/usage/tyranobuilder) |
| Godot ゲーム | **[SpriteStudio Player for Godot](../players/godot.md)** | [ドキュメント](https://cri-middleware.github.io/SSPlayerForGodot/ja/) |
| **Bevy** ゲーム | **[SpriteStudio Player for wgpu](../players/wgpu.md)**（`ssplayer-bevy`） | [ドキュメント](https://cri-middleware.github.io/SSPlayerForWgpu/ja/start/bevy/) |
| **Flutter** アプリ | **[SpriteStudio Player for Flutter](../players/flutter.md)** | [ドキュメント](https://cri-middleware.github.io/SSPlayerForFlutter/ja/) |
| **Flame** 製のゲーム | **[SpriteStudio Player for Flutter](../players/flutter.md)**（`ssplayer_flame`） | [ドキュメント](https://cri-middleware.github.io/SSPlayerForFlutter/ja/guide/flame/) |
| Ren'Py ビジュアルノベル | **[SpriteStudio Player for Ren'Py](../players/renpy.md)** | [ドキュメント](https://cri-middleware.github.io/SSPlayerForRenPy/ja/) |
| エンジンを使わず自分で描画する **Rust** / **C・C++** アプリケーション | **[SpriteStudio Player for wgpu](../players/wgpu.md)** | [ドキュメント](https://cri-middleware.github.io/SSPlayerForWgpu/ja/) |
| **React Native** アプリ | **[SpriteStudio Player for React Native](../players/react-native.md)** | [ドキュメント](https://cri-middleware.github.io/SSPlayerForReactNative/ja/) |
| 独自の Player・組み込みを作りたい | **SpriteStudio-SDK** | [Player の移植](../sdk/porting.md) |

Player ごとの統合の成熟度は [Player ごとの違い](./player-differences.md) と各 Player のページに記載しており、この表では重複して書きません。

`.sspj` の変換だけしたい場合は、Player ではなくスタンドアロンツールを選びます。

| 変換したい環境 | 使用するもの | 詳細 |
|---|---|---|
| ウェブ（ブラウザ） | **[SpriteStudio Player for Web](../players/web.md)**（`ssconverter-web`） | [試す](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) |
| デスクトップ - GUI（macOS / Windows） | **[SSConverter GUI](../players/converter.md)** | [ドキュメント](https://cri-middleware.github.io/SSConverterGUI/ja/) |
| デスクトップ - CLI | **SpriteStudio-SDK**（`ssconverter-cli`） | [使い方](./convert-with-a-standalone-tool.md) |

## ✅ すべてのプラットフォームに共通

- **変換ステップ**（`.sspj` -> ランタイムアセット `.ssab` / `.ssqb` ＋テクスチャ）はどこでも同じです。パイプラインは
  [SDK コンセプト](../sdk/concepts.md)、変換方法（Player による変換・GUI・CLI・ブラウザ）は
  [アセットの変換](./conversion.md) を参照してください。
- 対応機能（ボーン、メッシュ／デフォーム、パーティクル、拡張ブレンド、マスク）は共通コアが担うため、機能セット自体はどこでも同じです。エンジンごとに残る差分は
  [Player ごとの違い](./player-differences.md)、すべての Player に共通する制約は
  [共通の制限事項](../sdk/limitations.md) を参照してください。
- ライセンスは共通です。[ライセンス](../license.md) を参照してください。

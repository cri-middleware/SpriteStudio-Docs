# 🧭 プラットフォームの選び方

対象ランタイムに合ったものを選んでください。名前は各ページの概要へ、右列はそれぞれの
詳しい情報へリンクしています。

| 動かしたい対象 | 使用するもの | 詳細 |
|---|---|---|
| Unity ゲーム | **[SSPlayerForUnity](../players/unity.md)** | ドキュメント（準備中） |
| **ブラウザ** - PixiJS・WebGL | **[SSPlayerForWeb](../players/web.md)**（Player コレクション） | ドキュメント（準備中） |
| **RPG ツクール MZ**・**TyranoScript** - 🧪 実験的（alpha） | **[SSPlayerForWeb](../players/web.md)**（`ssplayer-webgl` のアダプター） | ドキュメント（準備中） |
| Godot ゲーム | **[SSPlayerForGodot](../players/godot.md)** | ドキュメント（準備中） |
| **Flutter** アプリ | **[SSPlayerForFlutter](../players/flutter.md)** | ドキュメント（準備中） |
| Ren'Py ビジュアルノベル | **[SSPlayerForRenPy](../players/renpy.md)** | ドキュメント（準備中） |
| 独自の Player ・組み込みを作りたい | **SpriteStudio-SDK** | [Player の移植](../sdk/porting.md) |

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
  共通コアが担うため、プラットフォーム間で一貫しています。
- ライセンスは共通です。[ライセンス](../license.md) を参照してください。

# 🧭 プラットフォームの選び方

対象ランタイムに合った Player を選んでください。各項目はそれぞれの詳細ドキュメントへリンクしています。

| 動かしたい対象 | 使用するもの | ドキュメント / リポジトリ |
|---|---|---|
| Unity ゲーム | **SSPlayerForUnity** | [ドキュメント](https://cri-middleware.github.io/SSPlayerForUnity/) |
| **ブラウザ** - PixiJS・WebGL・**RPG ツクール MZ**・**TyranoScript** | **SSPlayerForWeb**（Player コレクション） | [ドキュメント](https://cri-middleware.github.io/SSPlayerForWeb/) |
| Godot ゲーム | **SSPlayerForGodot** | [ドキュメント](https://cri-middleware.github.io/SSPlayerForGodot/) |
| **Flutter** アプリ - 🧪 開発初期 | **SSPlayerForFlutter** | [GitHub](https://github.com/cri-middleware/SSPlayerForFlutter) |
| Ren'Py ビジュアルノベル | **SSPlayerForRenPy** | [ドキュメント](https://cri-middleware.github.io/SSPlayerForRenPy/) |
| ウェブ（ブラウザ）で `.sspj` を変換したい | **SSPlayerForWeb**（`ssconverter-web`） | [試す](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) |
| デスクトップで `.sspj` を変換したい - GUI | **SSConverterGUI** | [GitHub](https://github.com/cri-middleware/SsConverterGUI) |
| デスクトップで `.sspj` を変換したい - CLI | **SpriteStudio-SDK**（`ssconverter-cli`） | [GitHub](https://github.com/cri-middleware/SpriteStudio-SDK) |
| 独自の Player ・組み込みを作りたい | **SpriteStudio-SDK** | [Player の移植](../sdk/porting.md) |

## ✅ すべてのプラットフォームに共通

- **変換ステップ**（`.sspj` -> ランタイムアセット `.ssab` / `.ssqb` ＋テクスチャ）はどこでも
  同じです。パイプラインは
  [SDK コンセプト](../sdk/concepts.md)、変換方法（インポート時の自動変換・GUI・CLI・ブラウザ）は
  [アセットの変換](./conversion.md) を参照してください。
- 対応機能（ボーン、メッシュ／デフォーム、パーティクル、拡張ブレンド、マスク）は
  共通コアが担うため、プラットフォーム間で一貫しています。
- ライセンスは共通です。[ライセンス](../license.md) を参照してください。

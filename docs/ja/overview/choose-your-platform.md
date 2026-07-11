# 🧭 プラットフォームの選び方

対象ランタイムに合った Player を選んでください。各項目はそれぞれの詳細ドキュメントへリンクしています。

| 動かしたい対象 | 使用するもの | ドキュメント |
|---|---|---|
| Unity ゲーム | **SSPlayerForUnity** | [ドキュメント](https://cri-middleware.github.io/SSPlayerForUnity/) |
| **ブラウザ** - PixiJS・スタンドアロン WebGL・**TyranoScript** | **SSPlayerForWeb**（Player コレクション） | [ドキュメント](https://cri-middleware.github.io/SSPlayerForWeb/) |
| Godot ゲーム | **SSPlayerForGodot** | [ドキュメント](https://cri-middleware.github.io/SSPlayerForGodot/) |
| Ren'Py ビジュアルノベル | **SSPlayerForRenPy** | [ドキュメント](https://cri-middleware.github.io/SSPlayerForRenPy/) |
| デスクトップで `.sspj` を変換したいだけ - GUI | **SSConverterGUI** | [GitHub](https://github.com/cri-middleware/SsConverterGUI) |
| デスクトップで `.sspj` を変換したいだけ - CLI | **SpriteStudio-SDK**（`ssconverter-cli`） | [GitHub](https://github.com/cri-middleware/SpriteStudio-SDK) |
| ウェブ（ブラウザ）で `.sspj` を変換したいだけ | **SSPlayerForWeb**（`ssconverter-web`） | [試す](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) |
| 独自の Player ・組み込みを作りたい | **SpriteStudio-SDK** | [Player の移植](../sdk/porting.md) |

## ✅ すべてのプラットフォームに共通

- **変換ステップ**（`.sspj` -> ランタイムアセット）はどこでも同じです。
  [SDK コンセプト](../sdk/concepts.md) を参照してください。変換は
  [コンバーター GUI](../players/converter.md) か、各 Player に同梱される
  `ssconverter-cli` で行えます。
- 対応機能（ボーン、メッシュ／デフォーム、パーティクル、拡張ブレンド、マスク）は
  共通コアが担うため、プラットフォーム間で一貫しています。
- ライセンスは共通です。[ライセンス](../license.md) を参照してください。

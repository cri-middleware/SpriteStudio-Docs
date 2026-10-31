# 🔘 UI 統合

SpriteStudio のアニメーションは、アプリの UI ツールキットのボタンそのものにできます。Unity なら uGUI の `Button`、Godot なら `BaseButton`、Flutter ならいつもの `InkWell` や `ElevatedButton` です。そのツールキットのボタンなので、クリック、キーボードのフォーカス、無効の状態、読み上げはほかのボタンと同じように働き、アニメーションがボタンのいまの状態を見せます。

▶️ [ライブデモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/pixi/ui.html) - PixiJS アプリで Ringo のサンプルが描くボタンが 2 つ。片方は指定したパーツでだけポインタを受けます。

## ✨ できること

- **ツールキットのボタンそのもの。** イベント、フォーカスとキーボード操作、無効の状態はツールキットのものがそのまま使えます。作り直すものがないので、ほかの UI にそのままなじみます。
- **どの状態の見た目も SpriteStudio で作る。** 1 つのアニメーションに、状態の名前のラベル（`normal`・`hover`・`pressed`・`disabled` など）を置くと、ボタンはその状態のあいだ、その区間をループ再生します。状態ごとの見た目はコードではなくエディタで決まります。ラベルのない状態は代わりの区間に、最後はアニメーション全体に落ちるので、ループするだけのアニメーションでもボタンとして動きます。手持ちのアニメーションを状態に割り当てることもできます。
- **絵の上だけでクリックを受ける。** 形の不揃いなボタンでは、ポインタを受けるパーツを指定すると、ボタンの箱のほかの場所では受けなくなります。
- **Reduced motion（動きを減らす設定）。** 有効にすると、どの状態も区間の最初のフレームで止まります。`reduced_motion` ラベルを置けば、待機中の状態は代わりに穏やかなループを再生できます。
- **読み上げ。** 読み上げる名前はボタンに渡します。アニメーション自体は装飾として扱われます。
- **1 つのアニメーションを表のどの Player でも。** 下の表の Player はどれも同じ規約（同じ状態のラベル、同じ代わりの区間）に従うので、ボタンとして作ったアニメーションはそのどれでもボタンとして動きます。

## 🎮 使える場所

| Player | なるボタン | 詳細 |
|---|---|---|
| **[Unity](../players/unity.md)** | uGUI の `Button` か `Toggle`: **SpriteStudio Button** / **SpriteStudio Toggle**（アセンブリ `SpriteStudio.UI`） | [ガイド](https://cri-middleware.github.io/SSPlayerForUnity/ja/workflow/ui_buttons/) |
| **[Web](../players/web.md)** - PixiJS | `@pixi/ui` の `ButtonContainer`: `SSButton`（`@spritestudio/ssplayer-pixi-ui`） | [ガイド](https://cri-middleware.github.io/SSPlayerForWeb/ja/usage/pixi-ui) |
| **[Godot](../players/godot.md)** | `BaseButton`: `SpriteStudioButton` | [ガイド](https://cri-middleware.github.io/SSPlayerForGodot/ja/workflow/ui_buttons/) |
| **[Flutter](../players/flutter.md)** | `statesController` を受け取るボタン（`InkWell`・`ElevatedButton` など）を `SpriteStudioStateView`（`package:ssplayer_flutter/ui.dart`）で描く | [ガイド](https://cri-middleware.github.io/SSPlayerForFlutter/ja/guide/buttons/) |
| **[Ren'Py](../players/renpy.md)** | `imagebutton` と同じ Ren'Py のボタン: `SSButton` | [ガイド](https://cri-middleware.github.io/SSPlayerForRenPy/ja/buttons/) |
| **[React Native](../players/react-native.md)** | ビューを覆う `<Pressable>`: `<SpriteStudioButton>`（`react-native-spritestudio-ui`） | [ガイド](https://cri-middleware.github.io/SSPlayerForReactNative/ja/usage/ui) |

自分で Player を作る場合、どの Player も従う規約は SDK の Player 移植ガイドの [UI 統合](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/libs/ssruntime/docs/50_features/80_ui_integration.ja.md)の章です。[Player の移植](../sdk/porting.md)もご覧ください。

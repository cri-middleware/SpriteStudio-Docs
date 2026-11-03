# 🎚️ モーションブレンド

1 体のキャラクターで複数のアニメーションを同時に再生し、切れ目なく移り変われます。下で歩き、その上に狙いのポーズを重ね、単発のリアクションをクロスフェードで入れる、といった具合です。どのアニメーションも、アーティストが SpriteStudio で個別に作ったものです。組み合わせは Player が実行時に行うので、組み合わせを変えても書き出し直しは要らず、`.ssab` も変わりません。

▶️ ライブデモ: [PixiJS](https://cri-middleware.github.io/SSPlayerForWeb/examples/pixi/blend.html)・[WebGL](https://cri-middleware.github.io/SSPlayerForWeb/examples/webgl/blend.html) - 1 体のキャラクターでのクロスフェードと重ね合わせをキーで操作でき、各トラックの状態が絵の横に出ます。

## ✨ できること

- **カットではなくクロスフェード。** 待機から攻撃へ、1 フレームで切り替えずに一瞬かけて移ります。
- **アニメーションを重ねる。** アニメーションはトラックに積みます。歩きに足を引きずる動きを重ねる、何にでもまばたきや手振りを重ねる、といった使い方です。トラックごとに強さがあるので、半分の強さで重ねたり、フェードインやフェードアウトさせたりできます。
- **1 つのトラックで 2 つのアニメーションを混ぜる。** 歩きから走りへのブレンドのように、重みで混ぜ合わせます。
- **値でトラックを動かす。** トラックを再生せずに再生位置を自分で動かせば、トラッキングの値に合わせて顔の向きを変えるといったことができます。
- **位相をそろえて始める。** トラックに載せるアニメーションを、track 0 のアニメーションがいる位置から始められるので、歩幅の半ばにいる歩きに走りを重ねると、走りも自分の歩幅の半ばから始まります。
- **キャラクター全体で 1 つの時計。** 一時停止・再開・停止はすべてのトラックにまとめて効きます。

組み合わせるアニメーションは 1 つの `.ssab` に入っている必要があり、パーツがどのセルを表示するかなど一部の属性は、混ぜられずにメインのアニメーションに従います。詳しくは [共通の制限事項](../sdk/limitations.md) にあります。

## 🎮 使える場所

| Player | 呼ぶもの | 詳細 |
|---|---|---|
| **[Unity](../players/unity.md)** | `SpriteStudioPlayer` と `SpriteStudioGraphic` のメソッド（どちらも同じ） | [ガイド](https://cri-middleware.github.io/SSPlayerForUnity/ja/workflow/motion_blending/) |
| **[Web](../players/web.md)** | `ssplayer-pixi`・`ssplayer-webgl`・RPG ツクール MZ の `SSPlayer` のメソッド。MZ のプラグインコマンド **SSトラック設定**・**SSトラックフェード**・**SSトラック解除**。TyranoScript の `[ss_track]`・`[ss_track_fade]`・`[ss_track_clear]` タグと `[ss_play]` の `transition=` | [ガイド](https://cri-middleware.github.io/SSPlayerForWeb/ja/customize/motion-blending) |
| **[Godot](../players/godot.md)** | `SpriteStudioPlayer2D` のメソッド | [ガイド](https://cri-middleware.github.io/SSPlayerForGodot/ja/workflow/motion_blending/) |
| **[Flutter](../players/flutter.md)** | `SpriteStudioPlayer` のメソッド | [ガイド](https://cri-middleware.github.io/SSPlayerForFlutter/ja/guide/motion-blending/) |
| **[Ren'Py](../players/renpy.md)** | `ss_crossfade`・`ss_set_track_animation` などの `ss_*` のトラック操作 | [ガイド](https://cri-middleware.github.io/SSPlayerForRenPy/ja/usage/#mixing-animations) |
| **[wgpu](../players/wgpu.md)** | Rust の `SSPlayer`、C の `ss_player_*`、JavaScript の `SsPlayerWeb`、Bevy の `SsTrackCommand` | [ガイド](https://cri-middleware.github.io/SSPlayerForWgpu/ja/guide/motion-blending/) |
| **[React Native](../players/react-native.md)** | クロスフェードは `transitionMs` プロパティだけでコード不要。それ以外は Player のトラック操作 | [ガイド](https://cri-middleware.github.io/SSPlayerForReactNative/ja/usage/motion-blending) |

自分で Player を作る場合、どの行も同じ仕組み（トラック、強さと重み、track 0 が特別な理由）に基づいています。その説明は SDK の Player 移植ガイドの [アニメーションミキシング](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/libs/ssruntime/docs/50_features/10_animation_mixing.ja.md)の章にあります。[Player の移植](../sdk/porting.md)もご覧ください。

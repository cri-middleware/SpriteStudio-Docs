# 🧥 実行時にキャラクターを変える

SpriteStudio のアニメーションは決まった映像ではありません。再生中に、ゲームやアプリからパーツに物を付けたり、描画に使う絵を差し替えたり、パーツ 1 つの色・セル・表示を変えたりできます。装備、着せ替え、色違い、被ダメージの点滅、HP バーといった用途に、SpriteStudio から書き出し直さずに使えます。

▶️ ライブデモ: [Override Layer API デモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/override/)では、Ringo のサンプルを再生したまま、パーツ単位のカラー・表示・セルの上書きを 1 つずつ切り替え、各ステップの呼び出しを画面に出します。

## 🎯 パーツに追従させる

自分で用意したものをパーツに付けると、毎フレームそのパーツと一緒に動き、回転し、拡大縮小します。手に持たせる武器、銃口のエフェクト、頭上の HP バーなどです。追従させるのはエンジンが描くノード・ウィジェット・ビューなので、エンジンで表示できるものなら何でも構いません。

メッシュ（スキン）パーツには直接追従できません。絵はボーンのスキニングで動きますが、パーツ自身の変換はセットアップ時の位置に残るためです。SpriteStudio でその位置に NULL パーツかボーンパーツを足し、そちらに追従させてください。

## 🧥 テクスチャを差し替える

再生中に、セルマップが描画に使う画像を差し替えます。着せ替え、色違い、装備、パーツを組み合わせたアバターなどです。アーティストがタイムラインで指定するテクスチャ変更とは違い、いつ差し替えるかはコードが決めます。セルの位置とサイズはそのまま残るので、新しい画像は元の画像と同じサイズ・同じレイアウトにしてください。変換後に[画像だけを差し替える](./conversion.md#プロジェクトの構成と変換後の対応)ときと同じ決まりです。

## 🎨 パーツを上書きする

アニメーションのキーの上から、パーツ 1 つの色、表示するセル、表示するかどうかを指定します。ダメージで赤く染める、アクセサリーを隠す、顔のセルを差し替える、といった使い方です。下ではアニメーションが再生を続け、上書きを解除するとパーツはアニメーションの指定に戻ります。

## 🎮 使える場所

| Player | パーツに追従 | テクスチャの差し替え | パーツの上書き |
|---|---|---|---|
| **[Unity](../players/unity.md)** | [ガイド](https://cri-middleware.github.io/SSPlayerForUnity/ja/workflow/usage_scripting/#パーツトラッキング指定パーツへの追従) | [ガイド](https://cri-middleware.github.io/SSPlayerForUnity/ja/workflow/usage_scripting/#動的テクスチャ差し替えセルマップの差し替え--着せ替え) | [ガイド](https://cri-middleware.github.io/SSPlayerForUnity/ja/workflow/usage_scripting/#パーツオーバーライドパーツカラー--セル--表示指定) |
| **[Web](../players/web.md)** | [ガイド](https://cri-middleware.github.io/SSPlayerForWeb/ja/customize/part-following) | [ガイド](https://cri-middleware.github.io/SSPlayerForWeb/ja/customize/texture-replacement) | [ガイド](https://cri-middleware.github.io/SSPlayerForWeb/ja/customize/part-overrides) |
| **[Godot](../players/godot.md)** | [ガイド](https://cri-middleware.github.io/SSPlayerForGodot/ja/workflow/usage_scripting/#パーツトラッキング指定パーツへの追従) | [ガイド](https://cri-middleware.github.io/SSPlayerForGodot/ja/workflow/usage_scripting/#動的テクスチャ差し替え-アバターの着せ替え) | [ガイド](https://cri-middleware.github.io/SSPlayerForGodot/ja/workflow/usage_scripting/#パーツオーバーライドパーツカラー--セル--表示指定) |
| **[Flutter](../players/flutter.md)** | [ガイド](https://cri-middleware.github.io/SSPlayerForFlutter/ja/guide/part-following/) | [ガイド](https://cri-middleware.github.io/SSPlayerForFlutter/ja/guide/textures/) | [ガイド](https://cri-middleware.github.io/SSPlayerForFlutter/ja/guide/part-overrides/) |
| **[Ren'Py](../players/renpy.md)** | [ガイド](https://cri-middleware.github.io/SSPlayerForRenPy/ja/usage/#5-パーツトラッキング指定パーツへの追従) | [ガイド](https://cri-middleware.github.io/SSPlayerForRenPy/ja/usage/#7-テクスチャの動的差し替え着せ替え--表情差分) | [ガイド](https://cri-middleware.github.io/SSPlayerForRenPy/ja/usage/#6-パーツオーバーライドパーツカラー--セル--表示指定) |
| **[wgpu](../players/wgpu.md)** | [ガイド](https://cri-middleware.github.io/SSPlayerForWgpu/ja/guide/part-overrides/#パーツに追従させる) | [ガイド](https://cri-middleware.github.io/SSPlayerForWgpu/ja/guide/texture-replacement/) | [ガイド](https://cri-middleware.github.io/SSPlayerForWgpu/ja/guide/part-overrides/) |
| **[React Native](../players/react-native.md)** | [ガイド](https://cri-middleware.github.io/SSPlayerForReactNative/ja/usage/parts#following-a-part) | [ガイド](https://cri-middleware.github.io/SSPlayerForReactNative/ja/usage/textures#replacing-a-texture) | [ガイド](https://cri-middleware.github.io/SSPlayerForReactNative/ja/usage/parts) |

自分で Player を作る場合、SDK の Player 移植ガイドでは、[パーツオーバーライド](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/libs/ssruntime/docs/50_features/20_part_overrides.ja.md)、[外部リソースとテクスチャ](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/libs/ssruntime/docs/50_features/30_external_resources.ja.md)、API 規約の[パーツの読み出し](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/libs/ssruntime/docs/20_design/30_api_conventions.ja.md#9-パーツの読み出し)の節で扱っています。[Player の移植](../sdk/porting.md)もご覧ください。

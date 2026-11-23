# 🎬 SpriteStudio Docs

**SpriteStudio SDK** と公式 Player 群のドキュメントポータルです。

[SpriteStudio](https://www.webtech.co.jp/spritestudio/) は 2D アニメーション制作ツールです。このポータルは、SpriteStudio アニメーションを再生するすべての公式ランタイムと、そのための変換ツールへの入口です。これらはすべて共通の Rust コア **SpriteStudio-SDK** の上に構築されています。

どれを使うか迷ったら [プラットフォームの選び方](./overview/choose-your-platform.md) を、全体像は [エコシステム](./overview/ecosystem.md) をご覧ください。

▶️ まず動かして確かめたい方は [ブラウザで試す](./overview/try-it.md) へ - インストール不要のライブデモとホスト型コンバーターがあります。

## 🎮 Player・ツール

<div class="grid cards" markdown>

-   :material-unity: __Unity__

    ---

    ワールド空間にも uGUI の Canvas にも描け、Canvas ではボタンやトグルにもなります。Burst ジョブと SIMD で最適化した Rust コアがメッシュを組み、GC アロケーションなしで動きます。

    :octicons-arrow-right-24: [概要](./players/unity.md) |
    [ドキュメント](https://cri-middleware.github.io/SSPlayerForUnity/ja/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForUnity)

-   :material-web: __Web（Player コレクション）__

    ---

    依存ゼロの `<ss-player>` タグから PixiJS、RPG ツクール MZ・TyranoScript・ティラノビルダーまで、環境に合わせて選べる Player 群です。`<video>` と違って自由に拡大縮小でき、操作にも反応します。ブラウザで完結する変換ツール（ssconverter-web）も入っています。

    :octicons-arrow-right-24: [概要](./players/web.md) |
    [ドキュメント](https://cri-middleware.github.io/SSPlayerForWeb/ja/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForWeb)

-   :simple-godotengine: __Godot__

    ---

    `SpriteStudioPlayer2D` をいつものノードとしてシーンに置け、GDExtension ならエンジンを再ビルドせずに入ります。ポーズ計算は SIMD で最適化した Rust コアが担い、大量のキャラクターでも滑らかです。

    :octicons-arrow-right-24: [概要](./players/godot.md) |
    [ドキュメント](https://cri-middleware.github.io/SSPlayerForGodot/ja/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForGodot)

-   :simple-flutter: __Flutter__

    ---

    普通のウィジェットとして配置・変形・クリップでき、Flame のゲームにも載せられます。描画は Flutter 自身のレンダラが行い、WebView も動画のデコードも使いません。

    :octicons-arrow-right-24: [概要](./players/flutter.md) |
    [ドキュメント](https://cri-middleware.github.io/SSPlayerForFlutter/ja/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForFlutter)

-   :material-drama-masks: __Ren'Py__

    ---

    `show` 1 行で普通の画像と同じように使え、セリフに合わせて口パクします。オープニングや動く背景など、動画（ムービー）の軽量な代替にもなります。

    :octicons-arrow-right-24: [概要](./players/renpy.md) |
    [ドキュメント](https://cri-middleware.github.io/SSPlayerForRenPy/ja/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForRenPy)

-   :simple-rust: __wgpu（Rust・C / C++・WebGPU）__

    ---

    Rust・Bevy から C/C++・ブラウザまで、1 つの wgpu レンダラーで動きます。GPU はホストのものを借りるだけなので、egui や Bevy など既存の wgpu アプリの中に同居できます。

    :octicons-arrow-right-24: [概要](./players/wgpu.md) |
    [ドキュメント](https://cri-middleware.github.io/SSPlayerForWgpu/ja/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForWgpu)

-   :simple-react: __React Native__

    ---

    普通のビューとして使え、描画はネイティブコードが Skia で行います。フレームごとに頂点が JavaScript を通ることも、React が再レンダーすることもありません。

    :octicons-arrow-right-24: [概要](./players/react-native.md) |
    [ドキュメント](https://cri-middleware.github.io/SSPlayerForReactNative/ja/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForReactNative)

-   :material-file-swap: __SSConverter GUI__

    ---

    `.sspj` プロジェクトをランタイム用アセットへ変換するデスクトップアプリ。

    :octicons-arrow-right-24: [概要](./players/converter.md) |
    [ドキュメント](https://cri-middleware.github.io/SSConverterGUI/ja/) |
    [GitHub](https://github.com/cri-middleware/SSConverterGUI)

-   :material-cog: __SpriteStudio-SDK__

    ---

    全 Player の基盤となる共通 Rust コア（`libssruntime` / `libssconverter`）。新規エンジン向けの **Player 移植ガイド**を同梱。

    :octicons-arrow-right-24: [コンセプト](./sdk/concepts.md) |
    [移植](./sdk/porting.md) |
    [ドキュメント](https://cri-middleware.github.io/SpriteStudio-SDK/ja/) |
    [GitHub](https://github.com/cri-middleware/SpriteStudio-SDK)

</div>

✨ 再生のほかに、[モーションブレンド](./overview/motion-blending.md)・[UI 統合](./overview/ui-integration.md)・[実行時にキャラクターを変える](./overview/runtime-changes.md)にも対応しています。

🎨 手元に SpriteStudio プロジェクトがない場合は、CRI Middleware が無償の[サンプルデータ](https://www.webtech.co.jp/help/ja/spritestudio7/download/sample/)を公開しています - キャラクター・エフェクト・UI などの `.sspj` 一式がそろっており、そのまま[変換](./overview/conversion.md)にかけられます。

!!! note "このポータルについて"
    **SDK を直接使う方・新しい Player を作る方**は
    [SDK・開発者向け](./sdk/concepts.md) を参照してください。

    **困ったとき・不具合を見つけたとき**は [サポート](./support.md) へ。報告先のリポジトリや問い合わせ窓口を振り分けています。

    各 Player の詳細ドキュメントはそれぞれのリポジトリで管理されています。このポータルはその入口であり、どの Player にも属さない**横断的な情報**を集約します。

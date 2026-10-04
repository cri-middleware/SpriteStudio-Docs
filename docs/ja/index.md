# 🎬 SpriteStudio Docs

**SpriteStudio SDK** と公式 Player 群のドキュメントポータルです。

[SpriteStudio](https://www.webtech.co.jp/spritestudio/) は 2D アニメーション制作ツールです。このポータルは、SpriteStudio アニメーションを再生するすべての公式ランタイム・ツールへの入口です。これらはすべて共通の Rust コア **SpriteStudio-SDK** の上に構築されています。

どれを使うか迷ったら [プラットフォームの選び方](./overview/choose-your-platform.md) を、全体像は [エコシステム](./overview/ecosystem.md) をご覧ください。

▶️ まず動かして確かめたい方は [ブラウザで試す](./overview/try-it.md) へ - インストール不要のライブデモとホスト型コンバーターがあります。

🎨 手元に SpriteStudio プロジェクトがない場合は、CRI Middleware が無償の[サンプルデータ](https://www.webtech.co.jp/help/ja/spritestudio7/download/sample/)を公開しています - キャラクター・エフェクト・UI などの `.sspj` 一式がそろっており、そのまま[変換](./overview/conversion.md)にかけられます。

## 🎮 Player・ツール

<div class="grid cards" markdown>

-   :material-unity: __Unity__

    ---

    Unity Engine 上で SpriteStudio アニメーションを再生。Job System で高速動作します。

    [:octicons-arrow-right-24: 概要](./players/unity.md) |
    ドキュメント（🚧 準備中） |
    [GitHub](https://github.com/cri-middleware/SSPlayerForUnity)

-   :material-web: __Web（Player コレクション）__

    ---

    ブラウザ向け Player 群（PixiJS・フレームワーク非依存 WebGL・RPG ツクール MZ・TyranoScript・
    TyranoBuilder）と、クライアントサイド変換ツール（ssconverter-web）のコレクション。

    [:octicons-arrow-right-24: 概要](./players/web.md) |
    ドキュメント（🚧 準備中） |
    [GitHub](https://github.com/cri-middleware/SSPlayerForWeb)

-   :simple-godotengine: __Godot__

    ---

    Godot でネイティブに描画。GDExtension とカスタムモジュールの両方で提供。

    [:octicons-arrow-right-24: 概要](./players/godot.md) |
    ドキュメント（🚧 準備中） |
    [GitHub](https://github.com/cri-middleware/SSPlayerForGodot)

-   :simple-flutter: __Flutter__

    ---

    `SpriteStudioView` ウィジェットで Flutter アプリに SpriteStudio アニメーションを再生。

    [:octicons-arrow-right-24: 概要](./players/flutter.md) |
    ドキュメント（🚧 準備中） |
    [GitHub](https://github.com/cri-middleware/SSPlayerForFlutter)

-   :material-drama-masks: __Ren'Py__

    ---

    Ren'Py 製ビジュアルノベルに SpriteStudio キャラクターを組み込みます。

    [:octicons-arrow-right-24: 概要](./players/renpy.md) |
    ドキュメント（🚧 準備中） |
    [GitHub](https://github.com/cri-middleware/SSPlayerForRenPy)

-   :simple-rust: __wgpu（Rust・C / C++）__

    ---

    wgpu で描画する Player。wgpu が WebGPU・Vulkan・DX12・Metal の違いを吸収するため、同じ Player がどのバックエンドでも動きます。

    [:octicons-arrow-right-24: 概要](./players/wgpu.md) |
    ドキュメント（🚧 準備中） |
    [GitHub](https://github.com/cri-middleware/SSPlayerForWgpu)

-   :simple-react: __React Native__

    ---

    React Native アプリで SpriteStudio アニメーションを再生します。`<SpriteStudioView>`
    コンポーネントを配置するだけで、描画は Skia 経由でネイティブ側が担当します。

    [:octicons-arrow-right-24: 概要](./players/react-native.md) |
    ドキュメント（🚧 準備中） |
    [GitHub](https://github.com/cri-middleware/SSPlayerForReactNative)

-   :material-file-swap: __コンバーター GUI__

    ---

    `.sspj` プロジェクトをランタイム用アセットへ変換するデスクトップアプリ。

    [:octicons-arrow-right-24: 概要](./players/converter.md) |
    ドキュメント（🚧 準備中） |
    [GitHub](https://github.com/cri-middleware/SSConverterGUI)

-   :material-cog: __SpriteStudio-SDK__

    ---

    全 Player の基盤となる共通 Rust コア（`libssruntime` / `libssconverter`）。新規エンジン向けの **Player 移植ガイド**を同梱。

    [:octicons-arrow-right-24: コンセプト](./sdk/concepts.md) |
    [移植](./sdk/porting.md) |
    [GitHub](https://github.com/cri-middleware/SpriteStudio-SDK)

</div>

!!! note "このポータルについて"
    **Player を使う方**は上のカードから。[プラットフォームの選び方](./overview/choose-your-platform.md)で最適な Player が分かり、各 Player は自身の詳細ドキュメントへリンクします。

    **SDK を直接使う方・新しい Player を作る方**は
    [SDK・開発者向け](./sdk/concepts.md) を参照してください。

    **困ったとき・不具合を見つけたとき**は [サポート](./support.md) へ。報告先のリポジトリや問い合わせ窓口を振り分けています。

    各 Player の詳細ドキュメントはそれぞれのリポジトリで管理されています。このポータルはその入口であり、どの Player にも属さない**横断的な情報**を集約します。

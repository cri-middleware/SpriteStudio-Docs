# ▶️ ブラウザで試す

SpriteStudio の変換と再生を、**インストール不要・設定なし**でその場で確認できます。ここに挙げたものはすべてブラウザ内で完結します。各項目は対応 Player の公式サイトでホストされており、このページはそのリンクを集めたものです。

## 🔄 ブラウザで変換する

**[ssconverter-web](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/)** は `.sspj` を
`.ssab` に変換します。処理は WebAssembly でローカル（ブラウザ内）だけで完結し、ファイルがサーバーへアップロードされることは一切ありません。手順やデスクトップ／CLI 版については
[スタンドアロンツールで変換する](./convert-with-a-standalone-tool.md) を参照してください。

## 🎮 ライブ Player デモ

| デモ | Player | 内容 |
|---|---|---|
| [PixiJS デモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/pixi/) | **[SpriteStudio Player for Web](../players/web.md)**（`@spritestudio/ssplayer-pixi`） | PixiJS v8 アプリでの再生。`.ssab`＋`.png` の入った**ディレクトリを D&D** すると自分のアニメをプレビューできます。 |
| [WebGL デモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/webgl/) | **[SpriteStudio Player for Web](../players/web.md)**（`@spritestudio/ssplayer-webgl`） | フレームワーク非依存の `<ss-player>` Web Component。`.ssab`＋`.png` の**ディレクトリを D&D** して自分のアニメをプレビュー。 |
| [Override Layer API デモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/override/) | **[SpriteStudio Player for Web](../players/web.md)**（`@spritestudio/ssplayer-pixi`） | Ringo のサンプルを再生したまま、パーツ単位のカラー・表示・セルの上書きを 1 つずつ切り替えながら繰り返す自走デモ。各ステップの呼び出しが画面に出ます。 |
| [RPG ツクール MZ デモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/rmmz/) | **[SpriteStudio Player for Web](../players/web.md)**（`@spritestudio/ssplayer-rmmz`） | SpriteStudio アニメを正しい Z 順で表示するサンプル MZ プロジェクト。 |
| [TyranoScript デモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/tyranoscript/) | **[SpriteStudio Player for Web](../players/web.md)**（`@spritestudio/ssplayer-tyranoscript`） | TyranoScript のノベルゲームで、`[ss_*]` タグから SpriteStudio アニメを再生。 |
| [Ren'Py デモ](https://cri-middleware.github.io/SSPlayerForRenPy/demo/) | **[SpriteStudio Player for Ren'Py](../players/renpy.md)** | 同梱の SpriteStudio アニメを Ren'Py Web で再生。 |
| [Flutter デモ](https://cri-middleware.github.io/SSPlayerForFlutter/demo/flutter/) | **[SpriteStudio Player for Flutter](../players/flutter.md)**（`ssplayer_flutter`） | Flutter の Web ビルドで動く `SpriteStudioView` ウィジェット。同じ `libssruntime` の wasm 上で全描画種別を再生。 |
| [Flame デモ](https://cri-middleware.github.io/SSPlayerForFlutter/demo/flame/) | **[SpriteStudio Player for Flutter](../players/flutter.md)**（`ssplayer_flame`） | 同じ再生を `SpriteStudioComponent` として Flame のゲームループから駆動。 |
| [WebGPU デモ](https://cri-middleware.github.io/SSPlayerForWgpu/demo/) | **[SpriteStudio Player for wgpu](../players/wgpu.md)**（`@spritestudio/ssplayer-wgpu`） | js API、`<ss-player-webgpu>` カスタム要素単体、それを他の要素と重ねて 1 ページに並べたもの（`GPUDevice` は 1 つ）、そして `partTransform` でパーツに DOM マーカーを追従させるもの。 |

Flutter の 2 つのデモは同 Player の Web ターゲットで動作します。Web ターゲットは同 Player のドキュメント上 developer preview の位置づけです。WebGPU デモには WebGPU 対応ブラウザが必要です。

**自分のアニメをプレビューしたい場合**、デモが受け取るのは `.ssab`＋`.png` なので、先に `.sspj` を変換してください。上記のブラウザ版コンバーターでも、
[スタンドアロンツール](./convert-with-a-standalone-tool.md) でも構いません。全体の流れは [アセットの変換](./conversion.md) にまとまっています。手元にプロジェクトがない場合は、無償の[サンプルデータ](https://www.webtech.co.jp/help/ja/spritestudio7/download/sample/)がそのまま使えます。

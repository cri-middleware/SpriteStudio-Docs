# ▶️ ブラウザで試す

SpriteStudio の変換と再生を、**インストール不要・設定なし**でその場で確認できます。ここに挙げたものはすべてブラウザ内で完結します。各項目は対応 Player の公式サイトでホストされており、このページはそのリンクを集めたものです。

## 🔄 ブラウザで変換する

| ツール | 内容 |
|---|---|
| [ssconverter-web](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) | `.sspj` を `.ssab` に変換。処理は WebAssembly でローカル（ブラウザ内）だけで完結し、ファイルがサーバーへアップロードされることは一切ありません。 |

手順やデスクトップ／CLI 版については [スタンドアロンツールで変換する](./convert-with-a-standalone-tool.md) を参照してください。

## 🎮 ライブ Player デモ

### [SpriteStudio Player for Web](../players/web.md)

| デモ | パッケージ | 内容 |
|---|---|---|
| [PixiJS デモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/pixi/) | `@spritestudio/ssplayer-pixi` | PixiJS アプリでの再生。`.ssab`＋`.png` の入った**ディレクトリを D&D** すると自分のアニメをプレビューできます。 |
| [WebGL デモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/webgl/) | `@spritestudio/ssplayer-webgl` | フレームワーク非依存の WebGL レンダラー。`.ssab`＋`.png` の**ディレクトリを D&D** して自分のアニメをプレビュー。 |
| [パーツ上書きデモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/override/) | `@spritestudio/ssplayer-pixi` | Ringo のサンプルを再生したまま、パーツ単位でカラー・表示・セルを変えます。[実行時にキャラクターを変える](./runtime-changes.md) もご覧ください。 |
| [PixiJS UI デモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/pixi/ui.html) | `@spritestudio/ssplayer-pixi-ui` | Ringo のサンプルが描く `@pixi/ui` のボタンが 2 つ。[UI 統合](./ui-integration.md) もご覧ください。 |
| [モーションブレンドデモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/pixi/blend.html) | `@spritestudio/ssplayer-pixi` | 1 体のキャラクターでのクロスフェード、加算の重ね合わせ、2 本目のトラック。[モーションブレンド](./motion-blending.md) もご覧ください。 |
| [RPG ツクール MZ デモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/rmmz/) | `@spritestudio/ssplayer-rmmz` | SpriteStudio アニメを正しい Z 順で表示するサンプル MZ プロジェクト。 |
| [TyranoScript デモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/tyranoscript/) | `@spritestudio/ssplayer-tyranoscript` | TyranoScript のノベルゲームで、`[ss_*]` タグから SpriteStudio アニメを再生。 |

### [SpriteStudio Player for Flutter](../players/flutter.md)

| デモ | パッケージ | 内容 |
|---|---|---|
| [Flutter デモ](https://cri-middleware.github.io/SSPlayerForFlutter/demo/flutter/) | `ssplayer_flutter` | Flutter の Web ビルドで動く `SpriteStudioView` ウィジェット。 |
| [Flame デモ](https://cri-middleware.github.io/SSPlayerForFlutter/demo/flame/) | `ssplayer_flame` | 同じ再生を `SpriteStudioComponent` として Flame のゲームループから駆動。 |

これらのデモは同 Player の Web ターゲットで動作します。

### [SpriteStudio Player for Ren'Py](../players/renpy.md)

| デモ | 内容 |
|---|---|
| [Ren'Py デモ](https://cri-middleware.github.io/SSPlayerForRenPy/demo/) | 同梱の SpriteStudio アニメを Ren'Py Web で再生。 |

### [SpriteStudio Player for wgpu](../players/wgpu.md)

| デモ | パッケージ | 内容 |
|---|---|---|
| [WebGPU デモ](https://cri-middleware.github.io/SSPlayerForWgpu/demo/) | `@spritestudio/ssplayer-wgpu` | JavaScript の API と `<ss-player-webgpu>` カスタム要素。`.ssab`＋`.png` の**ディレクトリを D&D** して自分のアニメをプレビュー。 |

WebGPU 対応ブラウザが必要です。

## 📂 自分のアニメをプレビューする

PixiJS・WebGL・WebGPU のデモが受け取るのは `.ssab`＋`.png` のフォルダ（PixiJS と WebGL のデモは embedded の `.ssab` 1 ファイルも可）なので、先に `.sspj` を変換してください。上記のブラウザ版コンバーターでも、[スタンドアロンツール](./convert-with-a-standalone-tool.md) でも構いません。全体の流れは [アセットの変換](./conversion.md) にまとまっています。手元にプロジェクトがない場合は、無償の[サンプルデータ](https://www.webtech.co.jp/help/ja/spritestudio7/download/sample/)がそのまま使えます。

## ➡️ 次に読む

[プラットフォームの選び方](./choose-your-platform.md) で、自分のエンジンに合う Player と、インストールから最初の表示までの手順が分かります。

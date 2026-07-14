# ▶️ ブラウザで試す

SpriteStudio の変換と再生を、**インストール不要・設定なし**でその場で確認できます。ここに
挙げたものはすべてブラウザ内で完結します。各項目は対応 Player のリポジトリでホストされており、
このページはそのリンクを集めたものです。

## 🔄 ブラウザで変換する

**[ssconverter-web](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/)** は `.sspj` を
`.ssab` に変換します。処理は WebAssembly でローカル（ブラウザ内）だけで完結し、ファイルが
サーバーへアップロードされることは一切ありません。手順やデスクトップ／CLI 版については
[エディタなしで変換する](./convert-without-an-editor.md) を参照してください。

## 🎮 ライブ Player デモ

| デモ | Player | 内容 |
|---|---|---|
| [PixiJS デモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/pixi/) | **SSPlayerForWeb**（`ssplayer-pixi`） | PixiJS v8 アプリでの再生。`.ssab`＋`.png` の入った**ディレクトリを D&D** すると自分のアニメをプレビューできます。 |
| [WebGL デモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/webgl/) | **SSPlayerForWeb**（`ssplayer-webgl`） | フレームワーク非依存の `<ss-player>` Web Component。`.ssab`＋`.png` の**ディレクトリを D&D** して自分のアニメをプレビュー。 |
| [RPG ツクール MZ デモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/rmmz/) | **SSPlayerForWeb**（`ssplayer-rmmz`） | SS アニメを正しい Z 順で表示するサンプル MZ プロジェクト。 |
| [TyranoScript デモ](https://cri-middleware.github.io/SSPlayerForWeb/examples/tyrano/) | **SSPlayerForWeb**（`ssplayer-tyrano`） | TyranoScript / TyranoBuilder のノベルゲームで SpriteStudio アニメを再生。 |
| [Ren'Py デモ](https://cri-middleware.github.io/SSPlayerForRenPy/demo/) | **SSPlayerForRenPy** | 同梱の SpriteStudio アニメを Ren'Py Web で再生。 |

各 Player の詳しい説明は [Web（Player コレクション）](../players/web.md)・[Ren'Py](../players/renpy.md) の各ページを参照してください。

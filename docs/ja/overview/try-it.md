# ▶️ ブラウザで試す

SpriteStudio の変換と再生を、**インストール不要・設定なし**でその場で確認できます。ここに
挙げたものはすべてブラウザ内で完結します。各項目は対応 Player の公式サイトでホストされており、
このページはそのリンクを集めたものです。

!!! info "準備中"
    これらのデモとホスト型コンバーターは、各 Player のサイトと同時に公開されます。以下の
    リンクはその時点で有効になります。

## 🔄 ブラウザで変換する

**ssconverter-web** は `.sspj` を
`.ssab` に変換します。処理は WebAssembly でローカル（ブラウザ内）だけで完結し、ファイルが
サーバーへアップロードされることは一切ありません。手順やデスクトップ／CLI 版については
[スタンドアロンツールで変換する](./convert-with-a-standalone-tool.md) を参照してください。

## 🎮 ライブ Player デモ

| デモ | Player | 内容 |
|---|---|---|
| PixiJS デモ（準備中） | **[SSPlayerForWeb](../players/web.md)**（`@spritestudio/ssplayer-pixi`） | PixiJS v8 アプリでの再生。`.ssab`＋`.png` の入った**ディレクトリを D&D** すると自分のアニメをプレビューできます。 |
| WebGL デモ（準備中） | **[SSPlayerForWeb](../players/web.md)**（`@spritestudio/ssplayer-webgl`） | フレームワーク非依存の `<ss-player>` Web Component。`.ssab`＋`.png` の**ディレクトリを D&D** して自分のアニメをプレビュー。 |
| RPG ツクール MZ デモ（準備中） | **[SSPlayerForWeb](../players/web.md)**（`@spritestudio/ssplayer-rmmz`） | SS アニメを正しい Z 順で表示するサンプル MZ プロジェクト。 |
| TyranoScript デモ（準備中） | **[SSPlayerForWeb](../players/web.md)**（`@spritestudio/ssplayer-tyranoscript`） | TyranoScript のノベルゲームで、`[ss_*]` タグから SpriteStudio アニメを再生。 |
| Ren'Py デモ（準備中） | **[SSPlayerForRenPy](../players/renpy.md)** | 同梱の SpriteStudio アニメを Ren'Py Web で再生。 |

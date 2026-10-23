# 🕹️ SpriteStudio Player for Godot

**Godot Engine** でネイティブに SpriteStudio アニメーションを描画します。`libssruntime` を基盤としています。

!!! tip "エディタで始まる - 最初のフレームまでコードは不要"
    アドオンをコピーし、`.sspj` をエディタにドラッグし、ノードを置いてアセットを割り当てるだけです。GDScript からの制御も可能ですが、ここまでには必要ありません。

**1. 何を入れるか** -
[最新の Release](https://github.com/cri-middleware/SSPlayerForGodot/releases/latest) の Assets にある `ssplayer-godot-extension-<Godot のバージョン>.zip` を取り、中の `addons` フォルダを Godot プロジェクトのルートにコピーします。Player の形態は次の 2 つです。

- **GDExtension** - Release に入っている、エンジンの再ビルド不要で導入できるバイナリアドオン。
- **カスタムモジュール** - ソースから Godot 本体に組み込んでビルドする、より密な統合方式。

**2. `.sspj` -> `.ssab`** - `.sspj` をファイルマネージャーから、アドオンの **SS Importer** ドックへドラッグ&ドロップします。プロジェクトの中で変換されるため、別途ツールを入れる必要はありません。

**3. どう画面に出すか** - 変換された `.ssab` を 2D ビューポートへドロップします。最初のアニメーションを選んだ `SpriteStudioPlayer2D` ノードが置かれ、シーンを実行すると再生されます。

フォルダを含めた手順は、README の[クイックスタート](https://github.com/cri-middleware/SSPlayerForGodot/blob/HEAD/README.ja.md#-gdextension-を用いたクイックスタート)にあります。

## ➡️ 次に読む

- [ドキュメント](https://cri-middleware.github.io/SSPlayerForGodot/ja/)
- [リポジトリ](https://github.com/cri-middleware/SSPlayerForGodot)
- [プラットフォームの選び方](../overview/choose-your-platform.md) - 他の Player との比較

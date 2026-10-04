# 🕹️ SpriteStudio Player for Godot

**Godot Engine** でネイティブに SpriteStudio アニメーションを描画します。`libssruntime` を基盤としています。

!!! tip "エディタで始まる - 最初のフレームまでコードは不要"
    アドオンをコピーし、`.sspj` をエディタにドラッグし、ノードを置いてアセットを割り当てるだけです。GDScript からの制御も可能ですが、ここまでには必要ありません。

**1. 何を入れるか** -
[GitHub Releases](https://github.com/cri-middleware/SSPlayerForGodot/releases) の `addons`
フォルダを、Godot プロジェクトのルートにコピーします。対応は Godot 4.7 系です。Player の形態は次の 2 つです。

- **GDExtension** - Release に入っている、エンジンの再ビルド不要で導入できるバイナリアドオン。
- **カスタムモジュール** - ソースから Godot 本体に組み込んでビルドする、より密な統合方式。

**2. `.sspj` -> `.ssab`** - `.sspj` を Godot エディタにドラッグ&ドロップします。アドオンの
SS Import Dock がその場で変換するため、別途ツールを入れる必要はありません。

**3. どう画面に出すか** - `SpriteStudioPlayer2D` ノードを追加し、**Ssab**
プロパティに `.ssab` を割り当てます。

## ➡️ 次に読む

- **ドキュメント** - 🚧 *準備中*
- [リポジトリ](https://github.com/cri-middleware/SSPlayerForGodot)
- [プラットフォームの選び方](../overview/choose-your-platform.md) - 他の Player との比較

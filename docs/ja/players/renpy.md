# 🎭 SpriteStudio Player for Ren'Py

**Ren'Py** 製ビジュアルノベルに SpriteStudio キャラクターを組み込みます。`libssruntime` を基盤とし、各リリースには再生可能な Web デモが同梱されます。

!!! tip "コードで始まる - スクリプト 1 行"
    変換したパックはそのまま画像なので、`show` で画面に出し、ATL や `Transform` で通常の画像と同じように動かせます。

**1. 何を入れるか** -
[GitHub Releases](https://github.com/cri-middleware/SSPlayerForRenPy/releases) から
`SSPlayerForRenPy.zip` を取得します。展開してできる `spritestudio/` フォルダを、プロジェクトの `game/` フォルダにコピーします。

**2. `.sspj` -> `.ssab`** - SpriteStudio のプロジェクトを、`game/` と同じ階層の `SpriteStudio_Source/` に置きます。Ren'Py ランチャーからゲームを起動すると Auto Importer が変換し、**Shift+R** を 1 回押したあとは、保存するたびに変更されたものだけが再変換されます。手動の書き出し作業はありません。

**3. どう画面に出すか** - `show ringo wait1` と書きます。パック `Ringo.ssab` が画像 `ringo` になり、アニメーションがその属性になります。

フォルダを含めた手順は、README の[クイックスタート](https://github.com/cri-middleware/SSPlayerForRenPy/blob/HEAD/README.ja.md#-1-クイックスタート)にあります。

## ➡️ 次に読む

- [ドキュメント](https://cri-middleware.github.io/SSPlayerForRenPy/ja/)
- [リポジトリ](https://github.com/cri-middleware/SSPlayerForRenPy)
- [ブラウザで試す](../overview/try-it.md) - 同梱アニメーションが Ren'Py Web で動く様子

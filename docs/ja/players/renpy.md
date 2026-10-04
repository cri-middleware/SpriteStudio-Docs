# 🎭 SpriteStudio Player for Ren'Py

**Ren'Py** 製ビジュアルノベルに SpriteStudio キャラクターを組み込みます。`libssruntime` を基盤とし、各リリースには再生可能な Web デモが同梱されます。

!!! tip "コードで始まる - スクリプト数行"
    `SSPlayer` は Ren'Py の標準的な Displayable なので、ATL や `Transform` と、通常の画像とまったく同じように組み合わせられます。

**1. 何を入れるか** -
[GitHub Releases](https://github.com/cri-middleware/SSPlayerForRenPy/releases) から
`SSPlayerForRenPy.zip` を取得します。展開してできる `spritestudio/` フォルダを、プロジェクトの `game/` フォルダにコピーします。

**2. `.sspj` -> `.ssab`** - SpriteStudio のソースを `SpriteStudio_Source/` に置きます。
Auto Importer が起動時に変換し、**Shift+R** でリロードすると変更されたものだけが再変換されるため、手動の書き出し作業はありません。

**3. どう画面に出すか** - screen に配置します。

```renpy
screen demo():
    add SSPlayer("overall/Basic.ssab") xalign 0.5 yalign 0.5
```

## ➡️ 次に読む

- [ドキュメント](https://cri-middleware.github.io/SSPlayerForRenPy/ja/)
- [リポジトリ](https://github.com/cri-middleware/SSPlayerForRenPy)
- [ブラウザで試す](../overview/try-it.md) - 同梱アニメーションが Ren'Py Web で動く様子

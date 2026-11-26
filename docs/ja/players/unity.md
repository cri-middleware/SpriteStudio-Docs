---
description: "Unity で SpriteStudio のアニメーションを再生する。.sspj をインポーターに置いてコンポーネントを配置するだけで、コードは要らない。SpriteStudio は、手持ちのイラストにボーン・メッシュ・エフェクトを付けて動かす 2D アニメーションツールです。"
---

# 🎮 SpriteStudio Player for Unity

**Unity Engine** 上で SpriteStudio アニメーションを再生します。再生は共通 Rust コアの
`libssruntime` を通じて行われ、Unity の Job System と組み合わせて高いパフォーマンスを発揮します。

!!! tip "エディタで始まる - 最初のフレームまでコードは不要"
    パッケージを入れ、`.sspj` をエディタにドラッグし、コンポーネントを置いてアセットを割り当てるだけです。スクリプト制御や Timeline も使えますが、ここまでには必要ありません。

**1. 何を入れるか** - `jp.co.cri-mw.spritestudio.ssplayer-unity` を、Package Manager から npm（`jp.co.cri-mw` の scoped registry）経由か、最新の Release の [`jp.co.cri-mw.spritestudio.ssplayer-unity.tgz`](https://github.com/cri-middleware/SSPlayerForUnity/releases/latest/download/jp.co.cri-mw.spritestudio.ssplayer-unity.tgz) で追加します。URP・BRP の両方に対応します。

**2. `.sspj` -> `.ssab`** - **Window > SpriteStudio > Importer** を開き、`.sspj` をドラッグ&ドロップします。`libssconverter` がパッケージに同梱されているため別途ツールを入れる必要はありません。SpriteStudio で編集したら、アセットのインスペクタの **Reconvert** でその場で更新されます。どちらの変換も Windows と macOS のエディタで動きます。Linux のエディタでは [`ssconverter-cli`](../overview/convert-with-a-standalone-tool.md) を使います。

**3. どう画面に出すか** - 生成された `SpriteStudioAnimeAsset` を Project ウィンドウから Hierarchy へドラッグし、**SpriteStudioPlayer**（ワールド空間）か **SpriteStudioGraphic (Canvas UI)** を選んで Play を押します。パックの最初のアニメーションから再生されます。

フォルダを含めた手順は、README の[クイックスタート](https://github.com/cri-middleware/SSPlayerForUnity/blob/HEAD/README.ja.md#-クイックスタート)にあります。

## ➡️ 次に読む

- [ドキュメント](https://cri-middleware.github.io/SSPlayerForUnity/ja/)
- [リポジトリ](https://github.com/cri-middleware/SSPlayerForUnity)
- [Player ごとの違い](../overview/player-differences.md) - uGUI Canvas 経路で何を諦めることになるか

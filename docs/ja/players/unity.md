# 🎮 SSPlayerForUnity

**Unity Engine** 上で SpriteStudio アニメーションを再生します。再生は共通 Rust コアの
`libssruntime` を通じて行われ、Unity の Job System と組み合わせて高いパフォーマンスを発揮します。

!!! tip "エディタで始まる - 最初のフレームまでコードは不要"
    パッケージを入れ、`.sspj` をエディタにドラッグし、コンポーネントを置いてアセットを割り当てる
    だけです。スクリプト制御や Timeline も使えますが、ここまでには必要ありません。

**1. 何を入れるか** -
[GitHub Releases](https://github.com/cri-middleware/SSPlayerForUnity/releases) のパッケージ
tarball を、Unity の Package Manager の **Add package from tarball** から追加します。
*Add package from URL* は使えません（ネイティブバイナリが tarball にしか含まれないため）。
対応は Unity 6.3 LTS 以降、URP・BRP の両方です。

**2. `.sspj` -> `.ssab`** - **Window > SpriteStudio > Importer** を開き、`.sspj` をドラッグ
&ドロップします。`libssconverter` がパッケージに同梱されているため別途ツールを入れる必要はなく、
SpriteStudio 側で編集し直せば Unity のアセットもそのまま更新されます。

**3. どう画面に出すか** - 生成された `SpriteStudioAnimeAsset` を Project ウィンドウから
Hierarchy へドラッグし、`SpriteStudioPlayer`（ワールド空間）か `SpriteStudioGraphic`
（uGUI Canvas）を選び、**Animation Name** を設定して Play を押します。

## ➡️ 次に読む

- **ドキュメント** - 🚧 *準備中*
- [リポジトリ](https://github.com/cri-middleware/SSPlayerForUnity)
- [プレイヤーごとの違い](../overview/player-differences.md) - uGUI Canvas 経路で何を諦めることになるか

# 🌐 SSPlayerForWeb

ブラウザで SpriteStudio アニメーションを再生する **Web 用 Player のコレクション**です。共通の WebAssembly コア（`@spritestudio/ssplayer-core`、`libssruntime` を基盤）を共有します。
SpriteStudio でスプライトを制作し、`.ssab` に変換したうえで、好みのレンダラーで再生できます。

▶️ 実際の動作は [ブラウザで試す](../overview/try-it.md) で確認できます。

!!! tip "コードで始まる - ただし Rust・WASM のツールチェーンは不要"
    WASM コアは各レンダラーパッケージに同梱されているので、1 つ入れて数行書くだけです。コアをソースからビルドするのは Rust 側を変更する場合だけです。

**1. 何を入れるか** - 環境に合わせてレンダラーパッケージを 1 つ選びます（[下の表](#pick-by-environment)）。どれも WASM コアを同梱しているので、依存は 1 つで済みます。
🚧 npm への公開は初回リリースと同時です。それまでは
[リポジトリの examples](https://github.com/cri-middleware/SSPlayerForWeb) をチェックアウトして実行してください。

**2. `.sspj` -> `.ssab`** - この Player 自身のサイトでホストされる `ssconverter-web` を使ってブラウザで変換するか、[スタンドアロンツール](../overview/convert-with-a-standalone-tool.md)のいずれかを使います。変換用パッケージは再生用とは別に選ぶため、下の表でも行を分けています。

**3. どう画面に出すか** - 選んだレンダラーが提供する要素を配置します。フレームワーク非依存の
`<ss-player>` Web Component か、PixiJS v8 アプリ内の `SpriteStudio` 表示オブジェクトです。

## 🧰 環境に合わせてパッケージを選ぶ { #pick-by-environment }

**再生** - 各レンダラーは WASM コアを同梱しているので、インストールするのは 1 つだけです。

| あなたの環境 | パッケージ |
|---|---|
| 単体 / フレームワーク非依存（`<ss-player>` Web Component） | **`@spritestudio/ssplayer-webgl`** |
| PixiJS v8 アプリ | **`@spritestudio/ssplayer-pixi`** |
| 自作レンダラーを実装する | **`@spritestudio/ssplayer-core`** |

**変換** - `.sspj` をランタイムアセットへ変換します。再生用パッケージとは別に選びます。

| あなたの環境 | 使うもの |
|---|---|
| `.sspj` -> `.ssab` を変換する | **`ssconverter-web`** - SSPlayerForWeb のサイトでホストされるブラウザツール（Node CLI も同梱）。npm パッケージではありません |
| 変換機能を自作アプリ / サービスに組み込む | **`@spritestudio/ssconverter-core`** |

**ゲームエンジン統合** - 描画は `@spritestudio/ssplayer-webgl` を基盤にしています。上記のパッケージとは違い、こちらはそもそも npm 公開の予定がなく、リポジトリの
[GitHub Releases](https://github.com/cri-middleware/SSPlayerForWeb/releases) で配布されます。

| あなたの環境 | パッケージ | 状態 |
|---|---|---|
| RPG ツクール MZ（PixiJS v5） | **`@spritestudio/ssplayer-rmmz`** | 🧪 実験的（alpha） |
| TyranoScript - シナリオに `[ss_*]` タグを自分で書く | **`@spritestudio/ssplayer-tyranoscript`** | beta |
| TyranoBuilder - コンポーネントパレットから配置、シナリオコード不要 | **`@spritestudio/ssplayer-tyranobuilder`** | beta |

`ssplayer-tyranobuilder` はレンダラーではなく**オーサリング時のツール**です。TyranoScript
ランタイムを同梱し、さらに `.sspj` をエディタ内で変換するため、TyranoBuilder のプロジェクトでは上の変換用パッケージを選ぶ必要がありません。

## ➡️ 次に読む

- **ドキュメント** - 🚧 *準備中*
- [リポジトリ](https://github.com/cri-middleware/SSPlayerForWeb)
- [ブラウザで試す](../overview/try-it.md) - 各種デモとホスト版コンバーター

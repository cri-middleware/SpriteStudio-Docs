# 🌐 SpriteStudio Player for Web

ブラウザで SpriteStudio アニメーションを再生する **Web 用 Player のコレクション**です。共通の WebAssembly コア（`@spritestudio/ssplayer-core`、`libssruntime` を基盤）を共有します。SpriteStudio でスプライトを制作し、`.ssab` に変換したうえで、好みのレンダラーで再生できます。

▶️ 実際の動作は [ブラウザで試す](../overview/try-it.md) で確認できます。

!!! tip "npm のパッケージはコードで始まる - RPG ツクール MZ・TyranoScript・ティラノビルダーではコード不要"
    npm のパッケージは WASM コアを同梱しているので、1 つ入れて数行書くだけです。1 つのリポジトリが両方の形を出しているため、このページは両方を扱います。3 つのゲームエンジン向けプラグインは、それぞれのエディタで設定し、コードは書きません。

**1. 何を入れるか** - 環境に合わせて npm のレンダラーパッケージを 1 つ選びます（[下の表](#pick-by-environment)）。どれも WASM コアを同梱しているので、依存は 1 つで済みます。RPG ツクール MZ・TyranoScript・ティラノビルダーでは、代わりに GitHub Releases のプラグインを入れます。

**2. `.sspj` -> `.ssab`** - RPG ツクール MZ とティラノビルダーのプラグインは自分で変換します。MZ はテストプレイの開始時、ティラノビルダーはプロジェクトを開いたときです。それ以外では、この Player 自身のサイトでホストされる [`ssconverter-web`](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) を使ってブラウザで変換するか、[スタンドアロンツール](../overview/convert-with-a-standalone-tool.md)のいずれかを使います。変換は再生とは別に選ぶため、下に専用の表があります。

**3. どう画面に出すか** - 選んだレンダラーが提供する要素を配置します。フレームワーク非依存の `<ss-player>` Web Component か、PixiJS アプリ内の `SSPlayer`（PixiJS の `Container`）です。RPG ツクール MZ ではプラグインコマンドの **SS表示**、TyranoScript では `[ss_new]` タグ、ティラノビルダーでは **SpriteStudio 表示** コンポーネントです。

フォルダを含めた手順は各パッケージの README にあり、README の[パッケージの表](https://github.com/cri-middleware/SSPlayerForWeb/blob/HEAD/README.ja.md#-どのパッケージを使うか)からたどれます。

## 🧰 環境に合わせてパッケージを選ぶ { #pick-by-environment }

**再生** - 各レンダラーは WASM コアを同梱しているので、インストールするのは 1 つだけです。

| あなたの環境 | パッケージ |
|---|---|
| 単体 / フレームワーク非依存（`<ss-player>` Web Component） | **`@spritestudio/ssplayer-webgl`** |
| PixiJS アプリ | **`@spritestudio/ssplayer-pixi`** |
| PixiJS アプリで、アニメーションで描く [`@pixi/ui`](https://github.com/pixijs/ui) のボタン | **`@spritestudio/ssplayer-pixi-ui`**（`ssplayer-pixi` も一緒に入ります） |
| 自作レンダラーを実装する | **`@spritestudio/ssplayer-core`** |

**変換** - `.sspj` をランタイムアセットへ変換します。再生用パッケージとは別に選びます。

| あなたの環境 | 使うもの |
|---|---|
| `.sspj` -> `.ssab` を変換する | **`ssconverter-web`** - SpriteStudio Player for Web のサイトでホストされるブラウザツール。npm パッケージではありません |
| 変換機能を自作アプリ / サービスに組み込む | **`@spritestudio/ssconverter-core`** |

**ゲームエンジン統合** - npm のパッケージではなくプラグインです。どれも、そのプラグインの GitHub Release の **Assets** にあるファイルです。

| あなたの環境 | ダウンロード | 状態 |
|---|---|---|
| RPG ツクール MZ | [`@spritestudio/ssplayer-rmmz` の Release](https://github.com/cri-middleware/SSPlayerForWeb/releases?q=ssplayer-rmmz&expanded=true) の **`ssplayer-rmmz-plugin-<version>.zip`** | beta |
| TyranoScript - シナリオに `[ss_*]` タグを自分で書く | [`@spritestudio/ssplayer-tyranoscript` の Release](https://github.com/cri-middleware/SSPlayerForWeb/releases?q=ssplayer-tyranoscript&expanded=true) の **`ssplayer-tyranoscript-plugin-<version>.zip`** | beta |
| ティラノビルダー - コンポーネントパレットから配置、シナリオコード不要 | [`@spritestudio/ssplayer-tyranobuilder` の Release](https://github.com/cri-middleware/SSPlayerForWeb/releases?q=ssplayer-tyranobuilder&expanded=true) の **`ssplayer.tbp`** | beta |

MZ とティラノビルダーのプラグインは `.sspj` を自分で変換する（手順 2）ので、MZ やティラノビルダーのプロジェクトでは、上の変換の表から選ぶ必要はありません。ティラノビルダーのプロジェクトに必要なのは `ssplayer.tbp` だけです。TyranoScript 用プラグインの中身も入っています。

## ➡️ 次に読む

- [ドキュメント](https://cri-middleware.github.io/SSPlayerForWeb/ja/)
- [リポジトリ](https://github.com/cri-middleware/SSPlayerForWeb)
- [ブラウザで試す](../overview/try-it.md) - 各種デモとホスト版コンバーター

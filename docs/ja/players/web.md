# 🌐 SSPlayerForWeb

ブラウザで SpriteStudio 7 アニメーションを再生する **Web 用 Player のコレクション**です。
共通の WebAssembly コア（`@spritestudio/ssplayer-core`、`libssruntime` を基盤）を共有します。
SpriteStudio でスプライトを制作し、`.ssab` に変換したうえで、好みのレンダラーで再生できます。

- **ドキュメント:** _準備中_
- **リポジトリ:** <https://github.com/cri-middleware/SSPlayerForWeb>

▶️ 実際の動作は [ブラウザで試す](../overview/try-it.md) で確認できます。

## 🧰 環境に合わせてパッケージを選ぶ

**再生** - 各レンダラーは WASM コアを同梱しているので、インストールするのは 1 つだけです。

| あなたの環境 | パッケージ |
|---|---|
| 単体 / フレームワーク非依存（`<ss-player>` Web Component） | **`@spritestudio/ssplayer-webgl`** |
| PixiJS v8 アプリ | **`@spritestudio/ssplayer-pixi`** |
| 自作レンダラーを実装する | **`@spritestudio/ssplayer-core`** |

**変換** - `.sspj` をランタイムアセットへ変換します。再生用パッケージとは別に選びます。

| あなたの環境 | パッケージ |
|---|---|
| `.sspj` -> `.ssab` を変換する | **`ssconverter-web`**（Web ツール + Node CLI） |
| 変換機能を自作アプリ / サービスに組み込む | **`@spritestudio/ssconverter-core`** |

**ゲームエンジン統合** - `@spritestudio/ssplayer-webgl` の上に載る薄いアダプターです。
いずれも 🧪 実験的（alpha、npm 未公開）です。

| あなたの環境 | パッケージ |
|---|---|
| RPG ツクール MZ（PixiJS v5） | **`@spritestudio/ssplayer-rmmz`** |
| TyranoScript / TyranoBuilder | **`@spritestudio/ssplayer-tyrano`** |

Player の比較は [プラットフォームの選び方](../overview/choose-your-platform.md) を、
全 Player 共通の変換／再生パイプラインは [SDK コンセプト](../sdk/concepts.md) を参照してください。

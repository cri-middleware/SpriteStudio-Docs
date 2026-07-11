# 🌐 SSPlayerForWeb

ブラウザで SpriteStudio 7 アニメーションを再生する **Web 用 Player のコレクション**です。
共通の WebAssembly コア（`ssplayer-core`、`libssruntime` を基盤）を共有します。SpriteStudio で
スプライトを制作し、`.ssab` に変換したうえで、好みのレンダラーで再生できます。

- **ドキュメント:** <https://cri-middleware.github.io/SSPlayerForWeb/>
- **リポジトリ:** <https://github.com/cri-middleware/SSPlayerForWeb>

## 🧰 環境に合わせてパッケージを選ぶ

各レンダラーは WASM コアを同梱しているので、インストールするのは 1 つだけです。

| あなたの環境 | パッケージ |
|---|---|
| 単体 / フレームワーク非依存（`<ss-player>` Web Component） | **`ssplayer-webgl`** |
| PixiJS v8 アプリ | **`ssplayer-pixi`** |
| 自作レンダラーを実装する | **`ssplayer-core`** |
| `.sspj` -> `.ssab` を変換する | **`ssconverter-web`**（Web ツール + Node CLI） |
| 変換機能を自作アプリ / サービスに組み込む | **`ssconverter-core`** |

**ゲームエンジン統合** - `ssplayer-webgl` の上に載る薄いアダプターです。いずれも 🧪 実験的
（alpha、npm 未公開）です。

| あなたの環境 | パッケージ |
|---|---|
| RPG ツクール MZ（PixiJS v5） | **`ssplayer-rmmz`** |
| TyranoScript / TyranoBuilder | **`ssplayer-tyrano`** |

Player の比較は [プラットフォームの選び方](../overview/choose-your-platform.md) を、
全 Player 共通の変換／再生パイプラインは [SDK コンセプト](../sdk/concepts.md) を参照してください。

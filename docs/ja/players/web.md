# SSPlayerForWeb

ブラウザで SpriteStudio 7 アニメーションを再生する **Web 用 Player のコレクション**です。
共通の WebAssembly コア（`ssplayer-core`、`libssruntime` を基盤）を共有します。SpriteStudio で
スプライトを制作し、`.ssab` に変換したうえで、好みのレンダラーで再生できます。

- **ドキュメント:** <https://cri-middleware.github.io/SSPlayerForWeb/>
- **リポジトリ:** <https://github.com/cri-middleware/SSPlayerForWeb>

## コレクションに含まれる Player

| パッケージ | 内容 |
|---|---|
| **`ssplayer-pixi`** | PixiJS レンダラー。推奨の連携方法です。 |
| **`ssplayer-webgl`** | スタンドアロンの WebGL Player。`<ss-player>` Web Component として提供。 |
| **`ssplayer-tyrano`** | TyranoScript 連携。 |
| **`ssplayer-rmmz`** | RPG ツクール MZ 連携 — 🚧 予定。まだ未実装です。 |
| **`ssconverter-web`** | `.sspj` → `.ssab` をクライアントサイドのみで変換するブラウザフロントエンド。 |

プレイヤーの比較は [プラットフォームの選び方](../overview/choose-your-platform.md) を、
全プレイヤー共通の変換／再生パイプラインは [SDK コンセプト](../sdk/concepts.md) を参照してください。

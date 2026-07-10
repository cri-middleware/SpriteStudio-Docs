# SDK コンセプト

!!! note "スタブ — SpriteStudio-SDK の内容で加筆してください"
    このページは、プラットフォームに依存しない共通コンセプトのプレースホルダーです。
    正式版はここに記述し、各プレイヤーのドキュメントからは複製せずにここへリンクしてください。

**SpriteStudio-SDK** は、すべてのプレイヤーが共有する Rust コアです。2 つのライブラリを提供します。

- **`libssconverter`** — SpriteStudio プロジェクト（`.sspj`）をコンパクトなランタイム形式へ変換します。
- **`libssruntime`** — ランタイム形式を読み込み、再生を駆動します（アニメーション状態、
  トランスフォーム、メッシュ／デフォーム、パーティクル、ブレンド、マスク）。

## パイプライン

1. OPTPiX SpriteStudio 7 で **制作** → `.sspj`。
2. `libssconverter` で **変換**（[コンバーター GUI](../players/converter.md) または
   `ssconverter-cli` 経由）→ ランタイムアセット。
3. `libssruntime` で **再生**。各プラットフォームのプレイヤーがエンジンへ橋渡しします。

## ここに記述したいトピック

- ランタイムデータモデル（セル、パーツ、アニメーション、キーフレーム）。
- 対応機能とプラットフォームごとの注意点。
- ランタイム形式とプレイヤーリリースのバージョン／互換性。

ディスク上の詳細は [フォーマット仕様](./format-spec.md) を、ソースは
[SpriteStudio-SDK リポジトリ](https://github.com/cri-middleware/SpriteStudio-SDK) を参照してください。

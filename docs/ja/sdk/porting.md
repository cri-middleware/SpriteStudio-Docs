# 🔌 Player の移植

公式 Player がまだ無いエンジンやプラットフォームで SpriteStudio アニメーションを動かしたい場合、**SpriteStudio-SDK には本格的な Player 移植ガイドが同梱**されています。`libssruntime`
の上に自作 Player を実装する手順を一通り解説しています。

!!! tip "ガイドの場所"
    正式なガイドは SDK リポジトリで管理されています:
    🚧 [**SpriteStudio Player 移植ガイド**](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/libs/ssruntime/docs/README.ja.md)
    （`libs/ssruntime/docs/README.ja.md`。各ページに `.ja.md` の日本語版があります）。本ページはそこへの案内であり、最新の正式な情報は SDK 側が基準です。

## 🧠 中心となる考え方: Brain と Body

`libssruntime` が **Brain**（頭脳）- アニメーション計算（状態・トランスフォーム・メッシュ／デフォーム・バッチ計画）をすべて担い、エンジンに依存しません。Player 側が **Body**（身体）-
エンジン固有の描画・リソース読み込み・入力を提供します。移植作業の大半は、自エンジンの Body を共通の Brain に接続することです。

## 📋 ガイドの内容

| セクション | 内容 |
|---|---|
| **10. はじめに** | Brain と Player の分担の概要、**制限事項**（技術的な制約 - 最初に読む）、用語集。 |
| **20. 設計** | 事前確認、Player の設計方針（ssab のメモリ・クラス構成・座標系）、すべての Player で揃える **Player API 規約**、`no_std` 環境への統合。 |
| **30. 基本の再生** | ロードと初期化、再生制御、イベント、描画ループ（DrawBatch による描画）。 |
| **40. パーツ** | パーツカラー、メッシュ、9 スライス・シェイプ・テキスト、マスク、インスタンスパーツ、エフェクトパーツ。 |
| **50. 機能** | アニメーションミキシング、パーツオーバーライド、外部リソースとテクスチャ、シーケンス、オーディオ、エディタ統合、配置（fit と align）。 |
| **60. トラブルシューティング** | 症状から原因を探す表と、リンクのエラー。 |

!!! note "都度検証する"
    ガイドでは各段階で `tests/overall/overall.sspj` を実行することを推奨しています。SpriteStudio
    エディタと同じ見た目になれば、その段階は完了です。公式 Player はいずれもこの方式で作られているので、どれも良い参考例になります。現行のラインナップは
    [プラットフォームの選び方](../overview/choose-your-platform.md) を参照してください。

## 🚦 はじめる前に

- 変換 -> 実行時のパイプラインは [SDK コンセプト](./concepts.md) を参照。ガイドが前提とする用語は [用語集](./glossary.md) に揃えてあります。
- ガイドの **制限事項** ページを最初に読む - Player の設計判断に直結します。
- ソースコードと Issue 報告: 🚧 [SpriteStudio-SDK](https://github.com/cri-middleware/SpriteStudio-SDK)。

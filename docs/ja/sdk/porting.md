# 🔌 Player の移植

公式 Player がまだ無いエンジンやプラットフォームで SpriteStudio 7 アニメーションを動かしたい
場合、**SpriteStudio-SDK には本格的な Player 移植ガイドが同梱**されています。`libssruntime`
の上に自作 Player を実装する手順を一通り解説しています。

!!! tip "ガイドの場所"
    正式なガイドは SDK リポジトリで管理されています:
    [**SpriteStudio 7 Player Porting Guide**](https://github.com/cri-middleware/SpriteStudio-SDK/tree/main/libs/ssruntime/docs)
    （`libs/ssruntime/docs/`）。本ページはそこへの案内で、一次情報は SDK 側です。

## 🧠 中心となる考え方: Brain と Body

`libssruntime` が **Brain**（頭脳）- アニメーション計算（状態・トランスフォーム・メッシュ／
デフォーム・バッチ計画）をすべて担い、エンジンに依存しません。 Player 側が **Body**（身体）-
エンジン固有の描画・リソース読み込み・入力を提供します。移植作業の大半は、自エンジンの Body を
共通の Brain に接続することです。

## 📋 ガイドの内容

| セクション | 内容 |
|---|---|
| **10. Introduction** | 基本コンセプトと用語集、および **Limitations**（サポート範囲・仕様上の制約 - 最初に読む）。 |
| **20. Design** | 事前準備・前提条件、Brain/Body アーキテクチャ、段階的な **実装ロードマップ**。 |
| **30. Core** | 最小再生: 読み込みと初期化、再生制御とイベント、描画ループとバッチング。 |
| **40. Components** | パーツ種別ごとの詳細: インスタンス、エフェクト、メッシュ&デフォーム、マスク、パーツカラー、アニメブレンド、外部リソース、シーケンス、オーディオ、特殊パーツ。 |
| **50. Reference** | `no_std` 連携、トラブルシューティング。 |
| **60. Tooling** | `ssconverter` をエンジンのエディタへ統合する方法。 |

!!! note "都度検証する"
    ガイドでは各段階で `tests/overall/overall.sspj` を実行することを推奨しています。SpriteStudio
    エディタと同じ見た目になれば、その段階は完了です。既存の Player
    （[Unity](../players/unity.md) / [Web](../players/web.md) / [Godot](../players/godot.md) /
    [Ren'Py](../players/renpy.md)）はいずれもこの方式で作られており、良い参考例になります。

## 🚦 はじめる前に

- 変換 -> 実行時のパイプラインは [SDK コンセプト](./concepts.md) を参照。
- ガイドの **Limitations** ページを最初に読む - Player の設計判断に直結します。
- ソース・課題: [SpriteStudio-SDK](https://github.com/cri-middleware/SpriteStudio-SDK)。

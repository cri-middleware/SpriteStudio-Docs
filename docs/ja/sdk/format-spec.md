# 📦 フォーマット仕様

SDK は 2 つのバイナリ形式（いずれも **FlatBuffers** ベース）と、ランタイムの FFI
インターフェースを使います。本ページは要約で、**フィールド単位の正式仕様は SDK 側**にあります。

- [**SSAB / SSQB スキーマ**](https://github.com/cri-middleware/SpriteStudio-SDK/blob/main/libs/ssab/SCHEMA.ja.md) - アセットバイナリ。
- [**FrameData スキーマ**](https://github.com/cri-middleware/SpriteStudio-SDK/blob/main/libs/ssruntime/SCHEMA.ja.md) - ランタイムのデータ交換インターフェース。

## 🗄️ SSAB / SSQB - アセットバイナリ

`.ssab`（**S**prite**S**tudio **A**nime **B**inary）と `.ssqb`（Sequence Binary）は、
XML ベースの `ss*e`（`ssae` / `ssce` / `ssee` / `ssse` / `fnt`）から `libssconverter` が
生成する、再生可能な変換済みアセットです。

| | `ss*e`（XML） | `.ssab` / `.ssqb`（バイナリ） |
|---|---|---|
| 形式 | XML / BMFont テキスト | FlatBuffers |
| 文字列検索 | 名前比較 | ハッシュ（`uint32`） |
| アクセス | 構造体へデシリアライズ | ゼロコピー読み取り |
| `no_std` | 非対応 | 対応 |

**変換単位は「`.ssae`（アニメーションパック）1つにつき `.ssab` 1つ」**。各 `.ssab` は自己完結し、
そのパックが実際に参照する `ss*e` リソース（セルマップ・エフェクト・サウンド・フォント）だけを
埋め込みます。`.sspj` プロジェクト自体は `.ssab` には含まれず、変換時のリソース解決にのみ使われます。

### 主要な設計判断

- **ハッシュルックアップ** - 名前を持つ全エンティティが `name_hash: uint32` を持ち、実行時の
  文字列比較なしで O(1) 検索。
- **列指向のアニメーションデータ** - `ss*e` のパーツ別タグ付き属性リストではなく、パーツごとに
  属性別の型付き配列（`position_x_array`・`rotation_z_array` ...）を保持し、1属性のフレーム横断
  反復を効率化。
- **イベントの分離** - イベント属性（ユーザーデータ・シグナル・オーディオ・インスタンス・
  エフェクト）はパーツ別ではなく**フレーム別**（`EventsPerFrame`）に格納し、フレーム単位の
  ディスパッチを最適化。
- **ユニオン型のパーツ種別** - FlatBuffers ユニオンが `ss*e` のタグ文字列ディスパッチを置き換え。
- **ゼロコピー／`no_std`** - 既定のランタイムモードは非確保で読み取り。`converter` フィーチャで
  書き込み用の Object API を有効化。
- **エディタ専用フィールドの除去** - UI 状態・ボーン編集・IK・メッシュウェイト編集などは除外。
  メッシュウェイトはパーツ index 参照の頂点別インフルエンスへ事前解決。

`.ssqb`（シーケンス）は `.ssqe` とほぼ 1:1 で、アニメーションパックを名前／ハッシュで参照する
シーケンスのリストです。

## 🔗 FrameData - ランタイムインターフェース

`.ssab` が（オフライン生成の）**タイムライン全体**を持つのに対し、**`FrameData` は実行時に
1フレーム分だけ動的生成**されます。`libssruntime` がアニメーションのキーフレーム配列を現在
フレームで評価し、パーツごとの `PartState` を出力します。これが **ランタイムコアと描画側を
FFI でつなぐ主要なデータ交換インターフェース**です。

```text
.ssab AnimationData（疎なキーフレーム）  +  現在フレーム N
        |  libssruntime: 補間 + 座標変換
        v
FrameData（密・1フレーム）  --FFI-->  各エンジンの描画
   +- parts: [PartState]  (position_x, rotation_z, alpha, mesh ...)
```

各 `PartState` フィールドは、対応する `.ssab` の `PartAnimationData` 配列から直接マップされます
（例: `position_x` <- `position_x_array` を補間し、対象の座標系へ変換）。フィールド単位の
対応表は [FrameData スキーマ](https://github.com/cri-middleware/SpriteStudio-SDK/blob/main/libs/ssruntime/SCHEMA.ja.md) にあります。

## 🔧 バインディングの再生成

スキーマは SDK 内の FlatBuffers `.fbs` として定義されています
（[`ssab.fbs`](https://github.com/cri-middleware/SpriteStudio-SDK/blob/main/libs/ssab/fbs/ssab.fbs) /
[`ssqb.fbs`](https://github.com/cri-middleware/SpriteStudio-SDK/blob/main/libs/ssab/fbs/ssqb.fbs)、および
[`framedata.fbs`](https://github.com/cri-middleware/SpriteStudio-SDK/blob/main/libs/ssruntime/fbs/framedata.fbs)）。フィーチャフラグ（`default` / `no_std` / `converter`）と
コード生成については [`libssab`](https://github.com/cri-middleware/SpriteStudio-SDK/tree/main/libs/ssab) を参照。

!!! info "スキーマのバージョニング"
    `.ssab` はバイナリ `version` フィールドを持ち、`ssconverter-web` などのツールは
    [スキーマ版ごと](../overview/conversion.md)に公開されます。変換ツールのスキーマは
    Player のランタイム版に合わせてください。

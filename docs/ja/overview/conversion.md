# 🔄 アセットの変換

再生の前に、SpriteStudio プロジェクト（`.sspj` +画像）を一度だけコンパクトなランタイム形式
（`.ssab` / `.ssqb`）へ変換します。以下のどの経路でも、実行しているのは
[SpriteStudio-SDK](../sdk/concepts.md) の**同じ `libssconverter`** であり、**出力も同一**です。
エンジンやワークフローに合った方法を選んでください。

## 🔀 変換の 2 つの方法

### 1. エディタ内蔵（Unity・Godot）

開発エディタを持つエンジンは `libssconverter` を内蔵しているため、その場で変換されます。
**外部ツールは不要**です。

- **Unity** - 内蔵の Importer がドラッグ&ドロップで変換。
- **Godot** - SS Import Dock がドラッグ&ドロップで変換。
- **Ren'Py** - 起動時に自動インポート（`SpriteStudio_Source/` にソースを配置）。

### 2. スタンドアロンツール

エディタ統合を持たないエンジン、CI/CD パイプライン、Web コレクション向けには、スタンドアロンの
フロントエンドで変換します。

| ツール | 向いている用途 | リンク |
|---|---|---|
| **SsConverterGUI** | デスクトップ、CLI 不要 | [概要](../players/converter.md) | [GitHub](https://github.com/cri-middleware/SsConverterGUI) |
| **`ssconverter-cli`** | バッチ／CI・CD 自動化 | [SpriteStudio-SDK](https://github.com/cri-middleware/SpriteStudio-SDK/tree/main/cli) |
| **`ssconverter-web`** | ブラウザ上・完全クライアントサイド | [最新版](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) | [パッケージ](https://github.com/cri-middleware/SSPlayerForWeb/tree/main/packages/ssconverter-web) |

!!! tip "ssconverter-web - `.ssab` スキーマ版ごとに公開"
    [ssconverter-web](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) は
    `.sspj` -> `.ssab` の変換をすべてブラウザ内で行います。サーバーへは何もアップロードされません。

    公開は **`.ssab` スキーマのバージョンごと**で、URL にスキーマが含まれます。

    - 最新版（自動リダイレクト）: <https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/>
    - 特定スキーマ版（例 `v1`）: <https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/v1/>

    Player のランタイム版に合ったスキーマを選んでください。迷ったら最新版リンクを開き、
    アプリ内のバージョン切替から選択できます。

## 📦 生成されるもの

どちらの経路でも `.ssab`（アニメーション）／`.ssqb`（シーケンス）と参照テクスチャが出力され、
`libssruntime` がそれを再生します。パイプラインは [SDK コンセプト](../sdk/concepts.md)、
ディスク上の詳細は [フォーマット仕様](../sdk/format-spec.md) を参照してください。

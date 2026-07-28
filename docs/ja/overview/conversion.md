# 🔄 アセットの変換

再生の前に、SpriteStudio プロジェクト（`.sspj` +画像）を一度だけコンパクトなランタイム形式
（`.ssab` / `.ssqb`）へ変換します。以下のどの経路でも、実行しているのは
[SpriteStudio-SDK](../sdk/concepts.md) の**同じ `libssconverter`** であり、**出力も同一**です。
エンジンやワークフローに合った方法を選んでください。

## 🔀 変換の 2 つの方法

### 1. インポート時に自動変換 - 外部ツール不要（Unity・Godot・Ren'Py・TyranoBuilder）

これらのエンジン向けの公式 Player パッケージには、変換ツールとして `libssconverter` が
**バンドル**されています。エディタなどの開発環境側で自動的に実行されるため、その場で変換
できます。**追加インストールは不要**です。

- **Unity** - [SSPlayerForUnity](../players/unity.md) 付属の Importer がドラッグ&ドロップで変換します。
- **Godot** - [SSPlayerForGodot](../players/godot.md) の SS Import Dock がドラッグ&ドロップで変換します。
- **Ren'Py** - [SSPlayerForRenPy](../players/renpy.md) が起動時に自動インポートします（`SpriteStudio_Source/` にソースを配置）。
- **TyranoBuilder** - [SSPlayerForWeb](../players/web.md) の `ssplayer-tyranobuilder` プラグインが、保存のたびに
  エディタ内で変換します（`SpriteStudio_Source/` にソースを配置）。変換結果はコンポーネントパレットの
  ドロップダウンに現れます。

各 Player のワークフローは、それぞれのドキュメント（スクリーンキャスト付き）で解説しています。
[プラットフォームの選び方](./choose-your-platform.md) を参照してください。

### 2. スタンドアロンツール - 自分で変換する

別のエンジン、CI/CD パイプライン、または [SSPlayerForWeb](../players/web.md) のレンダラー
（Web コレクション）を使う場合は、変換を代行してくれる Player がないため、3 つのスタンドアロンフロントエンド
（デスクトップ GUI・CLI・ブラウザ）のいずれかで変換します。どれを選び、どう使うかは
**[スタンドアロンツールで変換する](./convert-with-a-standalone-tool.md)** で解説します。

## 📦 生成されるもの

どちらの経路でも `.ssab`（アニメーション）／`.ssqb`（シーケンス）と参照テクスチャが出力され、
`libssruntime` がそれを再生します。パイプラインは [SDK コンセプト](../sdk/concepts.md)、
ディスク上の詳細は [フォーマット仕様](../sdk/format-spec.md) を参照してください。

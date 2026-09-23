# 🔄 アセットの変換

再生の前に、SpriteStudio プロジェクト（`.sspj` +画像）を一度だけコンパクトなランタイム形式（`.ssab` / `.ssqb`）へ変換します。以下のどの経路でも、実行しているのは
[SpriteStudio-SDK](../sdk/concepts.md) の**同じ `libssconverter`** であり、**出力も同一**です。エンジンやワークフローに合った方法を選んでください。

入力は **SpriteStudio 7.5 以上**で作成したプロジェクトです。`.ssab` / `.ssqb` の形式がその版に対して定義されているためで、変換が古い版のプロジェクトを新しい版へ更新することはありません。

!!! tip "手元に SpriteStudio プロジェクトがない場合"
    CRI Middleware が無償の
    [サンプルデータ](https://www.webtech.co.jp/help/ja/spritestudio7/download/sample/) を公開しています。キャラクター・エフェクト・UI・シェーダーなどの `.sspj` プロジェクト一式がそろっており、以下のどの経路にもそのまま渡せます。利用条件は各ダウンロードに同梱の readme を参照してください。

## 🔀 変換の 2 つの方法

### 1. インポート時に自動変換 - 外部ツール不要（Unity・Godot・Flutter・Ren'Py・TyranoBuilder）

これらのエンジン向けの公式 Player パッケージには、変換ツールとして `libssconverter` が**バンドル**されています。エディタなどの開発環境側で自動的に実行されるため、その場で変換できます。**追加インストールは不要**です。

- **Unity** - [SSPlayerForUnity](../players/unity.md) 付属の Importer がドラッグ&ドロップで変換します。
- **Godot** - [SSPlayerForGodot](../players/godot.md) の SS Import Dock がドラッグ&ドロップで変換します。
- **Flutter** - [SSPlayerForFlutter](../players/flutter.md) のオートインポート（`sswatch`）が保存のたびに再変換し、実行中のアプリへ反映します（`SpriteStudio_Source/` にソースを配置）。単発の変換は `ssconvert` CLI で行えます。
- **Ren'Py** - [SSPlayerForRenPy](../players/renpy.md) が起動時に自動インポートします（`SpriteStudio_Source/` にソースを配置）。
- **TyranoBuilder** - [SSPlayerForWeb](../players/web.md) の `ssplayer-tyranobuilder` プラグインが、プロジェクトを開いたときにエディタ内で変換します（`SpriteStudio_Source/` にソースを配置）。変換結果はコンポーネントのドロップダウンに現れます。

各 Player のワークフローは、それぞれのドキュメントで解説しています。
[プラットフォームの選び方](./choose-your-platform.md) を参照してください。

### 2. スタンドアロンツール - 自分で変換する

別のエンジン、CI/CD パイプライン、またはインポーターを持たない Player -
[SSPlayerForWeb](../players/web.md) のレンダラー（Web コレクション）、
[SSPlayerForReactNative](../players/react-native.md)、[SSPlayerForWgpu](../players/wgpu.md) -
を使う場合は、変換を代行してくれる Player がないため、3 つのスタンドアロンフロントエンド（デスクトップ GUI・CLI・ブラウザ）のいずれかで変換します。どれを選び、どう使うかは
**[スタンドアロンツールで変換する](./convert-with-a-standalone-tool.md)** で解説します。

## 📦 生成されるもの

どちらの経路でも `.ssab`（アニメーション）／`.ssqb`（シーケンス）と参照テクスチャが出力され、
`libssruntime` がそれを再生します。パイプラインは [SDK コンセプト](../sdk/concepts.md)、ディスク上の詳細は [フォーマット仕様](../sdk/format-spec.md) を参照してください。

変換は一方向です。`.ssab` は再生用の形式で、`.sspj` へ戻す経路はありません。編集は
SpriteStudio のプロジェクト側で行い、変換し直してください。

### プロジェクトの構成と、変換後の対応

SpriteStudio プロジェクトは複数のファイルで構成されます。`.sspj` を渡されて実装を担当する場合は、まずこの対応を押さえてください。**どの経路で変換しても対応は同じ**です。

| SpriteStudio 側 | 役割 | 変換すると |
|---|---|---|
| `.sspj` | プロジェクト本体。参照する `.ssae` / `.ssce` / `.ssqe` の一覧を持つ | **出力されません**。変換時のリソース解決にだけ使われます |
| `.ssae`（アニメーションパック） | パーツ構成とキーフレーム | `.ssab` 1 本になります |
| `.ssce`（セルマップ） | 使用する画像と、その画像から切り出すセル（位置・サイズ・原点） | **単独のファイルにはならず、`.ssab` に取り込まれます** |
| `.ssqe`（シーケンス） | アニメーションのプレイリスト | `.ssqb` 1 本になります（再生は未実装 - [共通の制限事項](../sdk/limitations.md)） |
| 画像（`.png` ほか） | 絵柄そのもの | 出力先へコピーされ、`.ssab` から参照されます |

用語の詳細は [用語集](../sdk/glossary.md)、変換単位の設計判断は
[フォーマット仕様](../sdk/format-spec.md) を参照してください。

!!! warning "画像だけを差し替えられる条件"
    セルの切り出し位置・サイズは `.ssce` から **`.ssab` へ焼き込まれます**。絵を描き替えただけなら画像ファイルの差し替えだけで反映されますが、セルを追加・移動・リサイズしたり画像全体のサイズを変えたりした場合は、**`.ssab` も作り直して一緒に配置**してください。画像だけを新しくすると、古い切り出し位置のまま描画されて絵がずれます。

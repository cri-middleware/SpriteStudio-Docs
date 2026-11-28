# 🔄 アセットの変換

再生の前に、SpriteStudio プロジェクト（`.sspj` +画像）を一度だけコンパクトなランタイム形式（`.ssab` / `.ssqb`）へ変換します。以下のどの経路でも、実行しているのは
[SpriteStudio-SDK](../sdk/concepts.md) の**同じ `libssconverter`** であり、**出力も同一**です。エンジンやワークフローに合った方法を選んでください。

入力は **SpriteStudio 7.6 以上**で作成したプロジェクトです。`.ssab` / `.ssqb` の形式がその版に対して定義されているためで、変換が古い版のプロジェクトを新しい版へ更新することはありません。

> [!TIP] 手元に SpriteStudio プロジェクトがない場合
> CRI Middleware が無償の
> [サンプルデータ](https://www.webtech.co.jp/help/ja/spritestudio7/download/sample/) を公開しています。キャラクター・エフェクト・UI・シェーダーなどの `.sspj` プロジェクト一式がそろっており、以下のどの経路にもそのまま渡せます。利用条件は各ダウンロードに同梱の readme を参照してください。

## 🔀 変換の 2 つの方法

変換は、Player が行うか、スタンドアロンツールで自分で行うかのどちらかです。Player が変換する場合は、Player のパッケージが `libssconverter` を持っているので、ほかに入れるものはありません（Flutter はコンバーターを dev 依存として追加します）。

| 使うもの | 変換するもの | いつ |
|---|---|---|
| **Unity** | [SpriteStudio Player for Unity](../players/unity.md) 付属の Importer | Windows と macOS のエディタへドラッグ&ドロップしたとき。Linux のエディタでは [`ssconverter-cli`](./convert-with-a-standalone-tool.md) を使います |
| **RPG ツクール MZ** | [SpriteStudio Player for Web](../players/web.md) の `ssplayer-rmmz` プラグイン | テストプレイの開始時、タイトルが出る前 |
| **ティラノビルダー** | [SpriteStudio Player for Web](../players/web.md) の `ssplayer-tyranobuilder` プラグイン | プロジェクトを開いたとき、エディタ内で。変換結果はコンポーネントのドロップダウンに現れます |
| **Godot** | [SpriteStudio Player for Godot](../players/godot.md) の SS Importer ドック | ドラッグ&ドロップしたとき |
| **Flutter** | [SpriteStudio Player for Flutter](../players/flutter.md) の `ssconvert` CLI（dev 依存の `ssconverter_dart`） | 手動または CI で実行したとき。1 回に `.sspj` を 1 つ変換します。ライブリロード（dev 依存の `ssgen_flutter`）では、`sswatch` が保存のたびに再変換し、デバッグ実行中のアプリへ反映します |
| **Ren'Py** | [SpriteStudio Player for Ren'Py](../players/renpy.md) | 起動時（自動インポート） |
| [SpriteStudio Player for Web](../players/web.md) のレンダラーと TyranoScript プラグイン、[SpriteStudio Player for wgpu](../players/wgpu.md)、[SpriteStudio Player for React Native](../players/react-native.md) | [スタンドアロンツール](./convert-with-a-standalone-tool.md) | 自分で実行したとき |

RPG ツクール MZ・ティラノビルダー・Flutter・Ren'Py では、ソースを `SpriteStudio_Source/` に置きます。

表に無いエンジンや CI/CD パイプラインでも、スタンドアロンツールで変換します。スタンドアロンツールはデスクトップ GUI・CLI・ブラウザの 3 つで、どれを選び、どう使うかは **[スタンドアロンツールで変換する](./convert-with-a-standalone-tool.md)** で解説します。

各 Player のワークフローは、それぞれのドキュメントで解説しています。[プラットフォームの選び方](./choose-your-platform.md) を参照してください。

## 📦 生成されるもの

どちらの経路でも `.ssab`（アニメーション）／`.ssqb`（シーケンス）と参照テクスチャが出力され、`libssruntime` がそれを再生します。パイプラインは [SDK コンセプト](../sdk/concepts.md)、ディスク上の詳細は [フォーマット仕様](../sdk/format-spec.md) を参照してください。

変換は一方向です。`.ssab` は再生用の形式で、`.sspj` へ戻す経路はありません。編集は
SpriteStudio のプロジェクト側で行い、変換し直してください。

### プロジェクトの構成と、変換後の対応 { #プロジェクトの構成と変換後の対応 }

SpriteStudio プロジェクトは複数のファイルで構成されます。`.sspj` を渡されて実装を担当する場合は、まずこの対応を押さえてください。**どの経路で変換しても対応は同じ**です。

| SpriteStudio 側 | 役割 | 変換すると |
|---|---|---|
| `.sspj` | プロジェクト本体。参照する `.ssae` / `.ssce` / `.ssqe` の一覧を持つ | **出力されません**。変換時のリソース解決にだけ使われます |
| `.ssae`（アニメーションパック） | パーツ構成とキーフレーム | `.ssab` 1 本になります |
| `.ssce`（セルマップ） | 使用する画像と、その画像から切り出すセル（位置・サイズ・原点） | **単独のファイルにはならず、`.ssab` に取り込まれます** |
| `.ssqe`（シーケンス） | アニメーションのプレイリスト | `.ssqb` 1 本になります |
| `.ssee`（エフェクト）・`.ssse`（サウンド）・`.fnt`（ビットマップフォント） | アニメーションが使うエフェクト・サウンド設定・フォント | `.ssce` と同じく **`.ssab` に取り込まれます**。サウンド設定が指す音声ファイルは、画像と同じく出力先へコピーされます（[embedded](#reference-and-embedded) では `.ssab` に入ります） |
| 画像（`.png` ほか） | 絵柄そのもの | 出力先へコピーされ、`.ssab` から参照されます（[embedded](#reference-and-embedded) では `.ssab` に入ります） |

用語の詳細は [用語集](../sdk/glossary.md)、変換単位の設計判断は
[フォーマット仕様](../sdk/format-spec.md) を参照してください。

> [!WARNING] 画像だけを差し替えられる条件
> セルの切り出し位置・サイズは `.ssce` から **`.ssab` へ焼き込まれます**。絵を描き替えただけなら画像ファイルの差し替えだけで反映されますが、セルを追加・移動・リサイズしたり画像全体のサイズを変えたりした場合は、**`.ssab` も作り直して一緒に配置**してください。画像だけを新しくすると、古い切り出し位置のまま描画されて絵がずれます。

### reference と embedded { #reference-and-embedded }

`.ssab` には、画像・音声の置き場所が違う 2 種類があります。

| 種類 | 画像・音声の置き場所 | 読める Player | 向いている場面 |
|---|---|---|---|
| **reference** | `.ssab` の外。変換時に出力先へコピーされます | すべて | エンジンのアセット管理にそのまま載せる場合。画像を差し替えたり、複数の `.ssab` で共有したりできます |
| **embedded** | `.ssab` の中 | Web・Flutter・React Native・wgpu | Web 広告や小さなアプリなど、1 ファイルで配りたい場合 |

Player による変換は既定で reference を出力します。embedded は embedded モードで作ります（CLI と Flutter の `ssconvert` の `--embedded`、GUI とブラウザ版の **Embedded Assets**）。Unity・Godot・Ren'Py は embedded を読めないので、reference で渡してください。embedded の制約は [共通の制限事項](../sdk/limitations.md) にあります。

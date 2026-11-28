# 🧰 スタンドアロンツールで変換する

変換を代行する Player を使わないとき（どれが代行するかは [アセットの変換](./conversion.md) の表にあります）や、表に無いエンジン、ビルド・CI/CD での自動化では、ここにあるスタンドアロンツールで自分で変換します。

## 🧭 どれを使うべき？

3 つのツールが出力する `.ssab` / `.ssqb` は同一です（[理由](./conversion.md)）。出力では差がつかないので、自分のワークフローに合うものを選んでください。どれも embedded の `.ssab` を出力できます（ブラウザ版と GUI は **Embedded Assets**、CLI は `--embedded`）。読める Player は限られるので、先に [reference と embedded](./conversion.md#reference-and-embedded) を確認してください。

| 状況 | 使うツール | 理由 |
|---|---|---|
| 何もインストールできない、単発でさっと | **`ssconverter-web`** | ブラウザ内で完結、導入ゼロ |
| デスクトップで、たまに変換、GUI がよい | **SSConverter GUI**（macOS / Windows） | ドラッグ&ドロップ、ターミナル不要 |
| ビルドや CI/CD の自動化、大量に変換 | **`ssconverter-cli`** | スクリプト化・バッチモード |

> [!TIP] 迷ったらブラウザから
> まず 1 つ `.ssab` を作ってアセットが問題なく変換できるか確かめるなら、インストール不要の ssconverter-web が最速です。変換が繰り返しの作業になったら GUI や CLI へ移りましょう。

## 🌐 ssconverter-web - ブラウザで

`.sspj` -> `.ssab` の変換をすべてブラウザ内で行います。サーバーへは何もアップロードされません。

> [!NOTE] フォルダのドロップ
> フォルダのドロップは **File System Access API** を使用するため、Chromium 系ブラウザ（**Chrome**・**Edge**・**Opera** など）でのみ動作します。Firefox・Safari では **Browse...** でフォルダを選択してください。

1. [`https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/`](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) でコンバーターを開きます。
2. `.sspj` が入ったフォルダをドロップするか、**Browse...** で選択します（画像などの参照ファイルも一緒に読み込まれます）。フォルダに入れる `.sspj` は 1 つだけにしてください。
3. **⚡ Convert & Download** を押します。ZIP には `.sspj` の名前のフォルダが 1 つ入っていて、その中に `.ssab` とテクスチャがあります。**Embedded Assets** をオンにすると、フォルダは `<名前>_emb` になり、テクスチャは `.ssab` の中に入ります。

> [!INFO] `.ssab` スキーマ版ごとに公開
> ssconverter-web は **`.ssab` スキーマのバージョンごと**に公開され、URL にスキーマが含まれます。
>
> - 最新版（自動リダイレクト）: [`https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/`](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/)
> - 特定スキーマ版（例 `v1`）: [`https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/v1/`](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/v1/)
>
> Player のランタイム版に合ったスキーマを選んでください（[理由](../sdk/limitations.md#schema-version)）。迷ったら最新版を使ってください。

## 🖥️ SSConverter GUI - デスクトップアプリ

Tauri 製のデスクトップアプリです。コマンドラインは不要です。配布しているビルドは **macOS と
Windows** で、Linux では下の `ssconverter-cli` を使ってください（出力は同じです）。

1. [GitHub Releases](https://github.com/cri-middleware/SSConverterGUI/releases) から OS に合ったアーカイブをダウンロードして展開します（インストーラーはありません）。Windows では初回起動時に SmartScreen の確認が出ます。対処は[インストール](https://cri-middleware.github.io/SSConverterGUI/ja/install/)を参照してください。
2. アプリを起動し、`.sspj`（または複数の `.sspj` を含むフォルダ）をウィンドウにドロップします（**File...** / **Folder...** からも選べます）。
3. 必要なら出力フォルダを変更し（既定は `.sspj` の隣のフォルダ）、**Convert** を押します。

詳細は [SSConverter GUI の概要](../players/converter.md)、[ドキュメント](https://cri-middleware.github.io/SSConverterGUI/ja/)、[リポジトリ](https://github.com/cri-middleware/SSConverterGUI) を参照してください。

## ⌨️ ssconverter-cli - コマンドライン・CI

Windows / macOS / Linux 向けの単体バイナリです。[SDK Releases](https://github.com/cri-middleware/SpriteStudio-SDK/releases)
からダウンロードできます（ビルド環境不要）。各リリースにはプラットフォームごとの zip が固定の URL `https://github.com/cri-middleware/SpriteStudio-SDK/releases/latest/download/ssconverter-cli-<platform>.zip` で入っているので、スクリプトから最新版を取得できます。プラットフォームの一覧は下記の README にあります。以下のように使います。

```bash
# 単一プロジェクトを変換し、.sspj と同じフォルダに project/ を出力する
ssconverter-cli project.sspj

# 出力ディレクトリを指定する
ssconverter-cli project.sspj -o ./out

# テクスチャを含む参照アセットを .ssab に埋め込み、project_emb/ に出力する（単一ファイルで配布しやすい）
ssconverter-cli project.sspj --embedded

# バッチ: ディレクトリ配下の .sspj を再帰的に探索し、並列で変換する
ssconverter-cli ./assets/projects ./more_assets
```

バッチモードでは各出力がソースと同じフォルダに書き出されます（`-o` は無視されます）。実行結果には、書き出した `.ssab` とそれぞれの中のアニメーション名が出ます。全オプションは
[ssconverter-cli README](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/cli/README.ja.md) を参照してください。

## ➡️ 次に

どれを使っても出力は同じ `.ssab` / `.ssqb` です。出力フォルダは使う Player に渡します。置き場所は各 Player のページにあり、[プラットフォームの選び方](./choose-your-platform.md) から各 Player へ進めます。再生の仕組みは [SDK コンセプト](../sdk/concepts.md)、ディスク上の詳細は [フォーマット仕様](../sdk/format-spec.md) を参照してください。

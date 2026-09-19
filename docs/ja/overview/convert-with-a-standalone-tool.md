# 🧰 スタンドアロンツールで変換する

Unity・Godot・Ren'Py・TyranoBuilder は変換ツールとして `libssconverter` を **バンドル**しており、別ツールを介さずインポート時に
`.sspj` から `.ssab` へ自動で変換します（[アセットの変換](./conversion.md) を参照）。これら以外を対象に
するときは、変換を代行してくれる Player がないため、スタンドアロンツールで自分で変換します。
たとえば次のような場合です。

- ブラウザ（Web）で再生する場合（[SSPlayerForWeb](../players/web.md) のレンダラー）
- 独自の Player を組み込む、または新しいエンジンに移植する場合（[Player の移植](../sdk/porting.md)）
- ビルドや CI/CD で変換を自動化する場合

## 🧭 どれを使うべき？

3 つのツールが出力する `.ssab` / `.ssqb` は同一です（[理由](./conversion.md)）。
出力では差がつかないので、自分のワークフローに合うものを選んでください。

| 状況 | 使うツール | 理由 |
|---|---|---|
| 何もインストールできない、単発でさっと | **`ssconverter-web`** | ブラウザ内で完結、導入ゼロ |
| デスクトップで、たまに変換、GUI がよい | **SSConverterGUI**（macOS / Windows） | ドラッグ&ドロップ、ターミナル不要 |
| ビルドや CI/CD の自動化、大量に変換 | **`ssconverter-cli`** | スクリプト化・バッチモード・`--embedded` |

!!! tip "迷ったらブラウザから"
    ssconverter-web は Web
    アプリなのでインストール不要で、変換は WebAssembly（wasm）によってブラウザ内で実行されます。
    ファイルがサーバーへ送られることはありません。まず 1 つ `.ssab` を作ってアセットが問題なく
    変換できるか確認するのに最速です。変換が繰り返しのワークフローになったら GUI や CLI へ
    移行しましょう。

## 🌐 ssconverter-web - ブラウザで

`.sspj` -> `.ssab` の変換をすべてブラウザ内で行います。サーバーへは何もアップロードされません。

!!! warning "Chromium 系ブラウザで利用してください"
    ssconverter-web は **File System Access API** を使用するため、Chromium 系ブラウザ
    （**Chrome**・**Edge**・**Opera** など）でのみ動作します。Firefox・Safari では利用できません。

1. [`https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/`](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) でコンバーターを開きます —
   🚧 _準備中_。アドレスは確定していますが、SSPlayerForWeb のサイト公開と同時に利用可能になります。
2. `.sspj` が入ったフォルダをドロップします（画像などの参照ファイルも一緒に読み込まれます）。
3. 変換結果（`.ssab` と参照テクスチャ）を ZIP でダウンロードします。

!!! info "`.ssab` スキーマ版ごとに公開"
    ssconverter-web は **`.ssab` スキーマのバージョンごと**に公開され、URL にスキーマが含まれます。

    - 最新版（自動リダイレクト）: [`https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/`](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) — 🚧 _準備中_
    - 特定スキーマ版（例 `v1`）: [`https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/v1/`](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/v1/) — 🚧 _準備中_

    Player のランタイム版に合ったスキーマを選んでください。迷ったら最新版（公開後）を使い、
    アプリ内のバージョン切替から選択してください。

## 🖥️ SSConverterGUI - デスクトップアプリ

Tauri 製のデスクトップアプリです。コマンドラインは不要です。配布しているビルドは **macOS と
Windows** で、Linux では下の `ssconverter-cli` を使ってください（出力は同じです）。

1. [GitHub Releases](https://github.com/cri-middleware/SSConverterGUI/releases) からビルドをダウンロードします。
2. アプリを起動し、`.sspj` をウィンドウにドロップします（またはファイル選択から開きます）。
3. 出力フォルダを選んで変換します。

詳細やスクリーンショットは [SSConverterGUI の概要](../players/converter.md)、
ドキュメント（🚧 準備中）、
[リポジトリ](https://github.com/cri-middleware/SSConverterGUI) を参照してください。

## ⌨️ ssconverter-cli - コマンドライン・CI

Windows / macOS / Linux 向けの単体バイナリです。[SDK Releases](https://github.com/cri-middleware/SpriteStudio-SDK/releases)
からダウンロードでき（ビルド環境不要）、以下のように使います。

```bash
# 単一プロジェクトを変換し、.sspj と同じフォルダに project/ を出力する
ssconverter-cli project.sspj

# 出力ディレクトリを指定する
ssconverter-cli project.sspj -o ./out

# テクスチャを含む参照アセットを .ssab に埋め込む（単一ファイルで配布しやすい）
ssconverter-cli project.sspj --embedded

# バッチ: ディレクトリ配下の .sspj を再帰的に探索し、並列で変換する
ssconverter-cli ./assets/projects ./more_assets
```

バッチモードでは各出力がソースと同じフォルダに書き出されます（`-o` は無視されます）。全オプションは
[ssconverter-cli README](https://github.com/cri-middleware/SpriteStudio-SDK/tree/HEAD/cli) を参照してください。

## ➡️ 次に

どれを使っても出力は同じ `.ssab` / `.ssqb` です。再生の仕組みは [SDK コンセプト](../sdk/concepts.md)、
ディスク上の詳細は [フォーマット仕様](../sdk/format-spec.md) を参照してください。

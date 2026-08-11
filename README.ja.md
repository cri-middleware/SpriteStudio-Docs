[**English**](./README.md) | [**日本語**](./README.ja.md)

# SpriteStudio-Docs

SpriteStudio SDK と公式 Player 群のドキュメント**ポータル**です。

このリポジトリは軽量なハブです。各 Player のドキュメントを**再ホストはしません** - Player の
ドキュメントはそれぞれのリポジトリのサイトで管理されています。ここが提供するのは統一された
入口と、どの Player にも属さない横断的な情報です。

- 製品カードを並べたランディングページ
- [エコシステム概要](docs/ja/overview/ecosystem.md) と
  [プラットフォームの選び方](docs/ja/overview/choose-your-platform.md)
- [アセットの変換](docs/ja/overview/conversion.md) と
  [スタンドアロンツールでの変換](docs/ja/overview/convert-with-a-standalone-tool.md)
- Player 間の[機能サポート状況](docs/ja/overview/feature-support.md)と、共通ランタイムの
  [制限事項](docs/ja/sdk/limitations.md)
- 共通の [SDK コンセプト](docs/ja/sdk/concepts.md)、[用語集](docs/ja/sdk/glossary.md)、
  [フォーマット仕様](docs/ja/sdk/format-spec.md)、[移植ガイドへの案内](docs/ja/sdk/porting.md)
- [サポート窓口の振り分け](docs/ja/support.md)と共通のライセンス情報

公開先: <https://cri-middleware.github.io/SpriteStudio-Docs/>

## 構成

```
docs/
  en/ , ja/          # ロケールごとに1フォルダー、ロケールごとに1設定ファイル
    assets/          # favicon（ロケールごとにコピーを持ちます）
    index.md         # ランディングページ（製品カード）
    overview/        # ecosystem, choose-your-platform, feature-support,
                     #   try-it, conversion, convert-with-a-standalone-tool
    sdk/             # concepts, glossary, format-spec, limitations, porting
                     #   （横断的な正典）
    players/         # 各 Player のドキュメントへリンクする薄い入口ページ
    support.md
    license.md
  requirements.txt
scripts/
  prepare.{sh,ps1}            # venv の作成とツールチェーンの導入
  build.{sh,ps1}              # 両ロケールを正しい順序で strict ビルド
mkdocs.base.yml               # 両ロケール共通の設定
mkdocs.yml                    # 英語   -> site/
mkdocs.ja.yml                 # 日本語 -> site/ja/
.github/workflows/pages.yml   # ビルド（strict）＋ GitHub Pages へのデプロイ
```

すべてのページは `en/` と `ja/` の**両方**に存在し、各ロケールはそれぞれの設定ファイルから
ビルドされます。`mkdocs.yml` と `mkdocs.ja.yml` は `mkdocs.base.yml` から共通設定を継承し、
差分だけを持ちます — ドキュメントディレクトリ、出力先、サイト URL、言語、そしてその言語の
ラベルを持つナビゲーションです。

サイトの生成には [Zensical](https://zensical.org)（MkDocs + Material for MkDocs の後継。
開発チームは同じ）を使用しています。設定ファイルは MkDocs の設定としても有効なままなので、
エンジンを比較したい場合は `mkdocs-material` でも同じサイトをビルドできます。

## ローカル開発

`mkdocs.base.yml` で `strict: true` を設定しているため、下記の build コマンドは内部リンク切れ
で失敗します（フラグは不要ですが、注意喚起のため各所で `--strict` を明示しています）。
**プルリクエストではドキュメントは一切ビルドされません**（`pages.yml` の起動条件は
`workflow_dispatch` のみ）。ローカル実行が唯一の検証手段です。

ビルドは英語を先に実行してください。日本語サイトは `site/ja` に出力されますが、英語ビルドは
開始時に `site/` を消去するため、あとから英語だけをビルドすると日本語サイトは「古いまま残る」
のではなく消えてしまいます。セットアップとこの順序は、2 つのスクリプトが受け持ちます。

```bash
scripts/prepare-docs.sh     # .venv を作成し docs/requirements.txt を導入
scripts/build-docs.sh       # 英語 → 日本語の順に、いずれも --strict でビルド
```

```powershell
scripts\prepare-docs.ps1    # PowerShell 版。オプションも出力も同じです
scripts\build-docs.ps1
```

いずれも Player 各リポジトリのスクリプトと同様に `key=value` 形式のオプションと `--help` を
受け付けます。

| | |
|---|---|
| `prepare-docs.sh python=<exe>` | venv の作成に使うインタープリター（既定は `python3`。`.ps1` は `py`） |
| `prepare-docs.sh venv=<dir>` | venv の作成先（既定は `.venv`） |
| `prepare-docs.sh force=yes` | 既存の venv を削除して作り直す（壊れた場合用） |
| `build-docs.sh locale=<all\|en\|ja>` | ビルドするロケール（既定は `all`＝上記の順序） |
| `build-docs.sh venv=<dir>` | `zensical` を実行する venv。無ければ `PATH` 上のものを使用 |

注意が必要なのは `build-docs.sh locale=en` を単独で実行した場合です。`site/ja` が消えるため、
スクリプトはその旨を警告します。

### スクリプトを使わない場合

スクリプトが実行しているのは次のコマンドだけです。

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r docs/requirements.txt

.venv/bin/zensical build --strict               # 唯一の検証。PR では何も検証されません
.venv/bin/zensical build -f mkdocs.ja.yml --strict
```

```powershell
py -m venv .venv
.\.venv\Scripts\python -m pip install -r docs/requirements.txt

.\.venv\Scripts\zensical build --strict         # 唯一の検証。PR では何も検証されません
.\.venv\Scripts\zensical build -f mkdocs.ja.yml --strict
```

### 執筆中のプレビュー

`serve` にスクリプトはありません。リンクを検証せず、一度に1ロケールしか配信しないためです。

```bash
.venv/bin/zensical serve                        # 英語を http://127.0.0.1:8000 でプレビュー
.venv/bin/zensical serve -f mkdocs.ja.yml       # 日本語をプレビュー（先に別のものを停止）
```

```powershell
.\.venv\Scripts\zensical serve                  # 英語を http://127.0.0.1:8000 でプレビュー
.\.venv\Scripts\zensical serve -f mkdocs.ja.yml # 日本語をプレビュー（先に別のものを停止）
```

`zensical serve --strict` は受け付けられますが現状何もしません。push する前に
`scripts/build-docs.sh` を実行してください。

### 言語切り替えのプレビュー

`serve` は一度に1ロケールしか配信しないため、もう一方の言語が存在せずセレクターは 404 に
なります。両ロケールをビルドして、その出力を配信してください。

```bash
scripts/build-docs.sh

python3 -m http.server 8000 -d site
```

セレクターのリンクは相対パスかつページ単位なので、たとえば `/sdk/concepts/` から切り替えると
日本語のトップページではなく `/ja/sdk/concepts/` に移動します。どのパス配下に置いても
動作します。

## 貢献について

誤りの修正、説明の改善、翻訳の修正を歓迎します。手順とドキュメントの規約は
[CONTRIBUTING.md](./CONTRIBUTING.md) を参照してください。参加にあたっては
[行動規範](./CODE_OF_CONDUCT.md) が適用されます。質問や不具合の報告先は
[SUPPORT.md](./SUPPORT.md) をご覧ください。

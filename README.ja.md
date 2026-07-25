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
- 共通の [SDK コンセプト](docs/ja/sdk/concepts.md)、[フォーマット仕様](docs/ja/sdk/format-spec.md)、
  [移植ガイドへの案内](docs/ja/sdk/porting.md)
- [サポート窓口の振り分け](docs/ja/support.md)と共通のライセンス情報

公開先: <https://cri-middleware.github.io/SpriteStudio-Docs/>

## 構成

```
docs/
  en/ , ja/          # フォルダー方式の i18n（mkdocs-static-i18n）
    index.md         # ランディングページ（製品カード）
    overview/        # ecosystem, choose-your-platform, feature-support,
                     #   try-it, conversion, convert-with-a-standalone-tool
    sdk/             # concepts, format-spec, limitations, porting（横断的な正典）
    players/         # 各 Player のドキュメントへリンクする薄い入口ページ
    support.md
    license.md
  requirements.txt
mkdocs.yml
.github/workflows/pages.yml   # ビルド（strict）＋ GitHub Pages へのデプロイ
```

すべてのページは `en/` と `ja/` の**両方**に存在します。ナビゲーションは `mkdocs.yml` に
一度だけ定義し（日本語のナビ名は同ファイルの `nav_translations` から取得）ます。ツールチェーン
（mkdocs-material + i18n）は SSPlayerForUnity / SSPlayerForRenPy と揃えています。

## ローカル開発

### macOS / Linux（bash）

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r docs/requirements.txt
.venv/bin/mkdocs serve          # http://127.0.0.1:8000 でプレビュー
.venv/bin/mkdocs build --strict # CI と同じ検証
```

### Windows（PowerShell）

```powershell
py -m venv .venv
.\.venv\Scripts\python -m pip install -r docs/requirements.txt
.\.venv\Scripts\mkdocs serve          # http://127.0.0.1:8000 でプレビュー
.\.venv\Scripts\mkdocs build --strict # CI と同じ検証
```

## 関連リポジトリ

| リポジトリ | 役割 |
|---|---|
| [SpriteStudio-SDK](https://github.com/cri-middleware/SpriteStudio-SDK) | 共通の Rust コア（`libssruntime` / `libssconverter`） |
| [SSPlayerForUnity](https://github.com/cri-middleware/SSPlayerForUnity) | Unity 向け Player |
| [SSPlayerForWeb](https://github.com/cri-middleware/SSPlayerForWeb) | Web 向け Player コレクション（PixiJS / WebGL / RPG ツクール MZ / TyranoScript / ssconverter-web） |
| [SSPlayerForGodot](https://github.com/cri-middleware/SSPlayerForGodot) | Godot 向け Player |
| [SSPlayerForFlutter](https://github.com/cri-middleware/SSPlayerForFlutter) | Flutter 向け Player |
| [SSPlayerForRenPy](https://github.com/cri-middleware/SSPlayerForRenPy) | Ren'Py 向け Player |
| [SSConverterGUI](https://github.com/cri-middleware/SSConverterGUI) | デスクトップ版コンバーター GUI |

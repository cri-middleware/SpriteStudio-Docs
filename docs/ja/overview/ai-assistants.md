# 🤖 AI アシスタントと使う

公式の各サイトは、ドキュメントを Markdown でも公開しています。ページを 1 枚ずつ貼り付けなくても、AI アシスタントにそのまま渡せます。このページでは、Markdown の在り処と、アシスタントに場所を知らせる方法をまとめます。

!!! info "🚧 準備中"
    以下のアドレスは、各 Player のサイトが公開されると同時に有効になります。それまでは 404 になるため、リンクにせず文字のまま載せています。

## 🔗 各サイトが提供するもの

どのサイトも、ルートに 2 つのファイルと、全ページの Markdown コピーを置いています。

- `llms.txt` は、サイトのページの目次です。AI アシスタントが最初に読んで、必要なページを選ぶためのものです。
- `llms-full.txt` は、全ページを 1 ファイルにまとめたものです。大きくなることがあるので、通常は `llms.txt` を渡して、必要なページをアシスタントに取らせてください。
- 各ページには、HTML の隣に Markdown のコピーもあります。ページのフォルダー内の `index.md`（Web と React Native のサイトは `<page>.md`）です。ページ題の横のボタンで、そのページの Markdown をクリップボードにコピーできます。

| サイト | `llms.txt` |
|---|---|
| [Unity](../players/unity.md) | `https://cri-middleware.github.io/SSPlayerForUnity/llms.txt` |
| [Web（Player コレクション）](../players/web.md) | `https://cri-middleware.github.io/SSPlayerForWeb/llms.txt` |
| [Godot](../players/godot.md) | `https://cri-middleware.github.io/SSPlayerForGodot/llms.txt` |
| [Flutter](../players/flutter.md) | `https://cri-middleware.github.io/SSPlayerForFlutter/llms.txt` |
| [Ren'Py](../players/renpy.md) | `https://cri-middleware.github.io/SSPlayerForRenPy/llms.txt` |
| [wgpu（Rust・C / C++）](../players/wgpu.md) | `https://cri-middleware.github.io/SSPlayerForWgpu/llms.txt` |
| [React Native](../players/react-native.md) | `https://cri-middleware.github.io/SSPlayerForReactNative/llms.txt` |
| [コンバーター GUI](../players/converter.md) | `https://cri-middleware.github.io/SSConverterGUI/llms.txt` |
| [SDK - Player 移植ガイド](../sdk/porting.md) | `https://cri-middleware.github.io/SpriteStudio-SDK/llms.txt` |
| このポータル | `https://cri-middleware.github.io/SpriteStudio-Docs/llms.txt` |

### 🌐 言語

Web と React Native 以外のサイトでは、リポジトリ名のあとに `ja/` を付けると日本語版のファイルになります（例: `https://cri-middleware.github.io/SSPlayerForUnity/ja/llms.txt`）。Web と React Native のサイトは英語版の 1 組だけです。日本語の各ページの Markdown コピーは、同じパスの `ja/` 配下に `.md` を付けたものです。

## 📦 パッケージの中のドキュメント

Unity パッケージには、インストールした版のドキュメントが、英語・日本語の Markdown で入っています。場所は `Library/PackageCache/jp.co.cri-mw.spritestudio.ssplayer-unity@<hash>/Documentation~/` で、`en/index.md`（日本語は `ja/index.md`）から読めます。ネットワークなしで読め、インストールした版と必ず一致します。`Library/` は通常 gitignore されているため、`.gitignore` を尊重する検索では見つかりません。ripgrep なら `--no-ignore` が要ります。

## 📝 AGENTS.md に貼る数行

アシスタントがドキュメントの場所を知るには、プロジェクトのどこかにそれが書かれている必要があります。次の数行を、プロジェクトの `AGENTS.md`（または `CLAUDE.md`）に貼り、上の表から使う Player のアドレスに差し替えてください。

```markdown
## SpriteStudio Player for Unity

- この Player を使ったコードを書く前にドキュメントを読み、機能を約束する前に「制限事項と対応範囲」のページを確認する。
- インストールした版のドキュメントはパッケージの中にある: `Library/PackageCache/jp.co.cri-mw.spritestudio.ssplayer-unity@*/Documentation~/`（日本語は `ja/index.md` から）。`Library/` は gitignore されているので、`rg --no-ignore` で検索する。
- 最新のドキュメント（Markdown）: https://cri-middleware.github.io/SSPlayerForUnity/ja/llms.txt
```

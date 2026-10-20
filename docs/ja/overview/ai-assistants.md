# 🤖 AI アシスタントと使う

公式の各サイトは、ドキュメントを Markdown でも公開しています。ページを 1 枚ずつ貼り付けなくても、AI アシスタントにそのまま渡せます。このページでは、Markdown の在り処と、アシスタントに場所を知らせる方法をまとめます。

## 🔗 各サイトが提供するもの

どのサイトも、ルートに 2 つのファイルと、全ページの Markdown コピーを置いています。

- `llms.txt` は、サイトのページの目次です。AI アシスタントが最初に読んで、必要なページを選ぶためのものです。
- `llms-full.txt` は、全ページを 1 ファイルにまとめたものです。大きくなることがあるので、通常は `llms.txt` を渡して、必要なページをアシスタントに取らせてください。
- 各ページには、HTML の隣に Markdown のコピーもあります。ページのフォルダー内の `index.md`（Web と React Native のサイトは `<page>.md`）です。ページ題の横のボタンで、そのページの Markdown をクリップボードにコピーできます。

| サイト | `llms.txt` |
|---|---|
| [Unity](../players/unity.md) | [`https://cri-middleware.github.io/SSPlayerForUnity/llms.txt`](https://cri-middleware.github.io/SSPlayerForUnity/llms.txt) |
| [Web（Player コレクション）](../players/web.md) | [`https://cri-middleware.github.io/SSPlayerForWeb/llms.txt`](https://cri-middleware.github.io/SSPlayerForWeb/llms.txt) |
| [Godot](../players/godot.md) | [`https://cri-middleware.github.io/SSPlayerForGodot/llms.txt`](https://cri-middleware.github.io/SSPlayerForGodot/llms.txt) |
| [Flutter](../players/flutter.md) | [`https://cri-middleware.github.io/SSPlayerForFlutter/llms.txt`](https://cri-middleware.github.io/SSPlayerForFlutter/llms.txt) |
| [Ren'Py](../players/renpy.md) | [`https://cri-middleware.github.io/SSPlayerForRenPy/llms.txt`](https://cri-middleware.github.io/SSPlayerForRenPy/llms.txt) |
| [wgpu（Rust・C / C++）](../players/wgpu.md) | [`https://cri-middleware.github.io/SSPlayerForWgpu/llms.txt`](https://cri-middleware.github.io/SSPlayerForWgpu/llms.txt) |
| [React Native](../players/react-native.md) | [`https://cri-middleware.github.io/SSPlayerForReactNative/llms.txt`](https://cri-middleware.github.io/SSPlayerForReactNative/llms.txt) |
| [コンバーター GUI](../players/converter.md) | [`https://cri-middleware.github.io/SSConverterGUI/llms.txt`](https://cri-middleware.github.io/SSConverterGUI/llms.txt) |
| [SDK - Player 移植ガイド](../sdk/porting.md) | [`https://cri-middleware.github.io/SpriteStudio-SDK/llms.txt`](https://cri-middleware.github.io/SpriteStudio-SDK/llms.txt) |
| このポータル | [`https://cri-middleware.github.io/SpriteStudio-Docs/llms.txt`](https://cri-middleware.github.io/SpriteStudio-Docs/llms.txt) |

### 🌐 言語

Web と React Native 以外のサイトでは、リポジトリ名のあとに `ja/` を付けると日本語版のファイルになります（例: `https://cri-middleware.github.io/SSPlayerForUnity/ja/llms.txt`）。Web と React Native のサイトは英語版の 1 組だけです。日本語の各ページの Markdown コピーは、同じパスの `ja/` 配下に `.md` を付けたものです。

## 📦 パッケージの中のドキュメント

どの Player のパッケージにも、インストールした版のドキュメントが Markdown で入っています。英語で、Unity だけは日本語もあります。ネットワークなしで読め、インストールした版と必ず一致します。

| Player | 場所 | Agent Skill |
|---|---|---|
| Unity | `Library/PackageCache/jp.co.cri-mw.spritestudio.ssplayer-unity@<hash>/Documentation~/`。`en/index.md`（日本語は `ja/index.md`）から | — |
| Web | `node_modules/@spritestudio/<package>/docs/`。`README.md` から | `skills/<package>/` |
| Godot | `addons/spritestudio/`。`README.md` から | — |
| Flutter | `ssplayer_flutter` と `ssplayer_flame` それぞれの `doc/`。pub のキャッシュ（`~/.pub-cache/hosted/pub.dev/<package>-<version>/`）にあり、`doc/index.md` から | `skills/ssplayer-flutter-docs/`、`skills/ssplayer-flame-docs/` |
| Ren'Py | `game/spritestudio/`。`README.md` から | — |
| wgpu | npm: `node_modules/@spritestudio/ssplayer-wgpu/docs/`。`README.md` から。C / C++: zip の `README.md` と `docs/`。Rust: クレートの `docs/`。`docs/index.md` から | npm: `skills/ssplayer-wgpu/` |
| React Native | `node_modules/react-native-spritestudio/docs/`。`README.md` から | `skills/react-native-spritestudio/` |

`Library/` と `node_modules/` は通常 gitignore されているため、`.gitignore` を尊重する検索では見つかりません。ripgrep なら `--no-ignore` が要ります。

### 🧩 Agent Skill として

npm と Flutter のパッケージは、同じページを [Agent Skill](https://agentskills.io) としても持っています。`SKILL.md` に、そのページが何のためのものかをアシスタント向けに書いたフォルダーです。プロジェクトの skill ディレクトリ（`.claude/skills/`、`.agents/skills/` など）に置かれると、アシスタントは場所を教わらなくてもドキュメントを見つけます。置くのはパッケージマネージャーです。

- **pnpm 12.11 以降**: `pnpm approve <package>` を 1 回実行します。以後のインストールのたびに、直接依存の skill が、ワークスペースのルートにある skill ディレクトリか、`pnpm-workspace.yaml` の `skills.dirs` が指すディレクトリにリンクされます。承認済みの skill があるのにそのディレクトリが無いとインストールが失敗するので、CI の checkout にも要ります。
- **npm・yarn**: `npx skills experimental_sync` で同じようにリンクされます。
- **Flutter**: `dart run skills@ get` でコピーされます。アップグレードのあとにもう一度実行してください。

## 📝 AGENTS.md に貼る数行

アシスタントがドキュメントの場所を知るには、プロジェクトのどこかにそれが書かれている必要があります。インストールした Agent Skill（上記）はそれ自体がその役目を果たすので、この数行は Agent Skill の無い Player か、skill を入れないプロジェクトのためのものです。次の数行を、プロジェクトの `AGENTS.md`（または `CLAUDE.md`）に貼り、上の表から使う Player のアドレスに差し替えてください。

```markdown
## SpriteStudio Player for Unity

- この Player を使ったコードを書く前にドキュメントを読み、機能を約束する前に「制約と適用範囲」のページを確認する。
- インストールした版のドキュメントはパッケージの中にある: `Library/PackageCache/jp.co.cri-mw.spritestudio.ssplayer-unity@*/Documentation~/`（日本語は `ja/index.md` から）。`Library/` は gitignore されているので、`rg --no-ignore` で検索する。
- 最新のドキュメント（Markdown）: https://cri-middleware.github.io/SSPlayerForUnity/ja/llms.txt
```

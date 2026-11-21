# 🤖 AI アシスタントと使う

公式の各サイトは、ドキュメントを Markdown でも公開しています。ページを 1 枚ずつ貼り付けなくても、AI アシスタントにそのまま渡せます。このページでは、アシスタントに SpriteStudio を教えるプラグイン、Markdown の在り処、アシスタントに場所を知らせる方法、アシスタントがプロジェクトを変換する方法をまとめます。

## 🔌 アシスタントに SpriteStudio を教えるプラグイン

SpriteStudio のプラグインは、どんなプロジェクトに SpriteStudio が合うか、どの Player を使うかをコーディングアシスタントに教え、必要なページへ案内します。Player のパッケージを入れる前から効きます。パッケージを入れた後は、下で説明するパッケージの中のドキュメントが、インストールした版と一致します。

Claude Code では次のとおりです。

```
/plugin install spritestudio --marketplace cri-middleware/SpriteStudio-Docs
```

2.1.275 より前の Claude Code では、`/plugin marketplace add cri-middleware/SpriteStudio-Docs` のあとに `/plugin install spritestudio@spritestudio` を実行します。プラグインはこのサイトのリポジトリに追従します。変更を受け取るには、`/plugin` で `spritestudio` マーケットプレイスの自動更新をオンにするか、`claude plugin update spritestudio@spritestudio` を実行してください。

## 🔗 各サイトが提供するもの

どのサイトも、ルートに 2 つのファイルと、全ページの Markdown コピーを置いています。

- `llms.txt` は、サイトのページの目次です。AI アシスタントが最初に読んで、必要なページを選ぶためのものです。
- `llms-full.txt` は、全ページを 1 ファイルにまとめたものです。大きくなることがあるので、通常は `llms.txt` を渡して、必要なページはアシスタントに取得させてください。
- 各ページには、HTML の隣に Markdown のコピーもあります。ページのフォルダー内の `index.md`（Web と React Native のサイトは `<page>.md`）です。ページタイトルの横のボタンで、そのページの Markdown をクリップボードにコピーできます。

| サイト | `llms.txt` |
|---|---|
| [Unity](../players/unity.md) | [`https://cri-middleware.github.io/SSPlayerForUnity/llms.txt`](https://cri-middleware.github.io/SSPlayerForUnity/llms.txt) |
| [Web（Player コレクション）](../players/web.md) | [`https://cri-middleware.github.io/SSPlayerForWeb/llms.txt`](https://cri-middleware.github.io/SSPlayerForWeb/llms.txt) |
| [Godot](../players/godot.md) | [`https://cri-middleware.github.io/SSPlayerForGodot/llms.txt`](https://cri-middleware.github.io/SSPlayerForGodot/llms.txt) |
| [Flutter](../players/flutter.md) | [`https://cri-middleware.github.io/SSPlayerForFlutter/llms.txt`](https://cri-middleware.github.io/SSPlayerForFlutter/llms.txt) |
| [Ren'Py](../players/renpy.md) | [`https://cri-middleware.github.io/SSPlayerForRenPy/llms.txt`](https://cri-middleware.github.io/SSPlayerForRenPy/llms.txt) |
| [wgpu（Rust・C / C++）](../players/wgpu.md) | [`https://cri-middleware.github.io/SSPlayerForWgpu/llms.txt`](https://cri-middleware.github.io/SSPlayerForWgpu/llms.txt) |
| [React Native](../players/react-native.md) | [`https://cri-middleware.github.io/SSPlayerForReactNative/llms.txt`](https://cri-middleware.github.io/SSPlayerForReactNative/llms.txt) |
| [SSConverter GUI](../players/converter.md) | [`https://cri-middleware.github.io/SSConverterGUI/llms.txt`](https://cri-middleware.github.io/SSConverterGUI/llms.txt) |
| [SDK - Player 移植ガイド](../sdk/porting.md) | [`https://cri-middleware.github.io/SpriteStudio-SDK/llms.txt`](https://cri-middleware.github.io/SpriteStudio-SDK/llms.txt) |
| このポータル | [`https://cri-middleware.github.io/SpriteStudio-Docs/llms.txt`](https://cri-middleware.github.io/SpriteStudio-Docs/llms.txt) |

### 🌐 言語

Web と React Native 以外のサイトでは、リポジトリ名のあとに `ja/` を付けると日本語版のファイルになります（例: `https://cri-middleware.github.io/SSPlayerForUnity/ja/llms.txt`）。Web と React Native のサイトの `llms.txt` / `llms-full.txt` は英語版だけです。日本語の各ページの Markdown コピーは、同じパスの `ja/` 配下に `.md` を付けたものです。

## 📦 パッケージの中のドキュメント

どの Player のパッケージにも、インストールした版のドキュメントが Markdown で入っています。英語で、Unity だけは日本語もあります。ネットワークなしで読め、インストールした版と必ず一致します。

| Player | 場所 | Agent Skill |
|---|---|---|
| Unity | `Library/PackageCache/jp.co.cri-mw.spritestudio.ssplayer-unity@<hash>/Documentation~/`。`en/index.md`（日本語は `ja/index.md`）から | — |
| Web（npm パッケージ） | `node_modules/@spritestudio/<package>/docs/`。`README.md` から | `skills/<package>/` |
| Godot | `addons/spritestudio/`。`README.md` から | — |
| Flutter | `ssplayer_flutter` と `ssplayer_flame` それぞれの `doc/`。pub のキャッシュ（`~/.pub-cache/hosted/pub.dev/<package>-<version>/`）にあり、`doc/index.md` から | `skills/ssplayer-flutter-docs/`、`skills/ssplayer-flame-docs/` |
| Ren'Py | `game/spritestudio/`。`README.md` から | — |
| wgpu | npm: `node_modules/@spritestudio/ssplayer-wgpu/docs/`。`README.md` から。C / C++: zip の `README.md` と `docs/`。Rust: クレートの `docs/`。`docs/index.md` から | npm: `skills/ssplayer-wgpu/` |
| React Native | `node_modules/react-native-spritestudio/docs/`。`README.md` から | `skills/react-native-spritestudio/` |

`Library/` と `node_modules/` は通常 gitignore されているため、`.gitignore` を尊重する検索では見つかりません。ripgrep なら `--no-ignore` が要ります。

### 🧩 Agent Skill として

npm と Flutter のパッケージは、同じページを [Agent Skill](https://agentskills.io) としても持っています。`SKILL.md` に、そのページが何のためのものかをアシスタント向けに書いたフォルダーです。プロジェクトの skill ディレクトリ（`.claude/skills/`、`.agents/skills/` など）に置かれると、アシスタントは場所を教わらなくてもドキュメントを見つけます。置くのはパッケージマネージャーです。

- **pnpm 12.11 以降**: `pnpm approve <package>` を 1 回実行します。以後のインストールのたびに、直接依存の skill が、ワークスペースのルートにある skill ディレクトリか、`pnpm-workspace.yaml` の `skills.dirs` が指すディレクトリ（無ければ作られます）にリンクされます。pnpm が見分けるコーディングエージェント（Claude Code など）の中で実行すると、ディレクトリが無ければそのエージェントのものが作られます。それ以外の場所（端末や CI）では、承認済みの skill があるのにどちらも無いとインストールが失敗するので、ディレクトリか `skills.dirs` の設定をコミットしてください。
- **npm、または `nodeLinker: node-modules` の yarn**: `npx skills experimental_sync` で同じようにリンクされます。どのエージェント向けにリンクするかを尋ねられます（`-a claude-code -y` を付けると尋ねられません）。yarn の既定の Plug'n'Play では、読み取る `node_modules` がありません。
- **Flutter**: `dart run skills@ get --all` で、プロジェクトにあるコーディングエージェントの skill ディレクトリ（`.claude/` など）にコピーされます。まだ無いときは `--agent claude`（ほかに `codex`・`copilot`・`cursor` など）で指定してください。`--all` を付けないと一覧を出すだけです。アップグレードのあとにもう一度実行してください。

## ⌨️ プロジェクトの変換

アシスタントはコマンドを実行できてもウィンドウは扱えないので、変換には `ssconverter-cli` を使います。SDK の各リリースにはプラットフォームごとの zip が固定の URL `https://github.com/cri-middleware/SpriteStudio-SDK/releases/latest/download/ssconverter-cli-<platform>.zip` で入っていて、プラットフォームの一覧は [CLI の README](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/cli/README.ja.md) にあります。実行結果には書き出した `.ssab` ごとに中のアニメーション名が出るので、Player に渡す名前はそこで分かります。

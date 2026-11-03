# 🤖 Using with AI Assistants

Every official site publishes its documentation as Markdown too, so you can hand it to an AI assistant instead of pasting pages one by one. This page says where the Markdown is, how to point an assistant at it, and how an assistant converts a project.

## 🔗 What each site serves

Every site serves two files at its root, and a Markdown copy of every page:

- `llms.txt` is an index of the site's pages, written for an AI assistant to read first and pick pages from.
- `llms-full.txt` is every page in one file. It can be large, so prefer `llms.txt` and let the assistant fetch the pages it needs.
- Each page also has a Markdown copy next to its HTML: `index.md` inside the page's folder, or `<page>.md` on the Web and React Native sites. A button beside the page title copies that page's Markdown to the clipboard.

| Site | `llms.txt` |
|---|---|
| [Unity](../players/unity.md) | [`https://cri-middleware.github.io/SSPlayerForUnity/llms.txt`](https://cri-middleware.github.io/SSPlayerForUnity/llms.txt) |
| [Web (Player Collection)](../players/web.md) | [`https://cri-middleware.github.io/SSPlayerForWeb/llms.txt`](https://cri-middleware.github.io/SSPlayerForWeb/llms.txt) |
| [Godot](../players/godot.md) | [`https://cri-middleware.github.io/SSPlayerForGodot/llms.txt`](https://cri-middleware.github.io/SSPlayerForGodot/llms.txt) |
| [Flutter](../players/flutter.md) | [`https://cri-middleware.github.io/SSPlayerForFlutter/llms.txt`](https://cri-middleware.github.io/SSPlayerForFlutter/llms.txt) |
| [Ren'Py](../players/renpy.md) | [`https://cri-middleware.github.io/SSPlayerForRenPy/llms.txt`](https://cri-middleware.github.io/SSPlayerForRenPy/llms.txt) |
| [wgpu (Rust, C / C++)](../players/wgpu.md) | [`https://cri-middleware.github.io/SSPlayerForWgpu/llms.txt`](https://cri-middleware.github.io/SSPlayerForWgpu/llms.txt) |
| [React Native](../players/react-native.md) | [`https://cri-middleware.github.io/SSPlayerForReactNative/llms.txt`](https://cri-middleware.github.io/SSPlayerForReactNative/llms.txt) |
| [SSConverter GUI](../players/converter.md) | [`https://cri-middleware.github.io/SSConverterGUI/llms.txt`](https://cri-middleware.github.io/SSConverterGUI/llms.txt) |
| [SDK - the Player Porting Guide](../sdk/porting.md) | [`https://cri-middleware.github.io/SpriteStudio-SDK/llms.txt`](https://cri-middleware.github.io/SpriteStudio-SDK/llms.txt) |
| This portal | [`https://cri-middleware.github.io/SpriteStudio-Docs/llms.txt`](https://cri-middleware.github.io/SpriteStudio-Docs/llms.txt) |

### 🌐 Languages

For the sites other than Web and React Native, add `ja/` after the repository name to get the Japanese files, for example `https://cri-middleware.github.io/SSPlayerForUnity/ja/llms.txt`. The Web and React Native sites write one pair of English files; each of their Japanese pages has a Markdown copy at the same path under `ja/` with `.md` appended.

## 📦 Docs inside the package

Every player's package carries its documentation for the version you installed, as Markdown: in English, and for Unity in Japanese too. It reads without a network and always matches the installed version.

| Player | Where | Agent Skill |
|---|---|---|
| Unity | `Library/PackageCache/jp.co.cri-mw.spritestudio.ssplayer-unity@<hash>/Documentation~/`, starting at `en/index.md` (Japanese: `ja/index.md`) | — |
| Web | `node_modules/@spritestudio/<package>/docs/`, starting at `README.md` | `skills/<package>/` |
| Godot | `addons/spritestudio/`, starting at `README.md` | — |
| Flutter | `doc/` in `ssplayer_flutter` and in `ssplayer_flame`, in the pub cache (`~/.pub-cache/hosted/pub.dev/<package>-<version>/`), starting at `doc/index.md` | `skills/ssplayer-flutter-docs/`, `skills/ssplayer-flame-docs/` |
| Ren'Py | `game/spritestudio/`, starting at `README.md` | — |
| wgpu | npm: `node_modules/@spritestudio/ssplayer-wgpu/docs/`, starting at `README.md`. C / C++: the zip's `README.md` and `docs/`. Rust: the crate's `docs/`, starting at `docs/index.md` | npm: `skills/ssplayer-wgpu/` |
| React Native | `node_modules/react-native-spritestudio/docs/`, starting at `README.md` | `skills/react-native-spritestudio/` |

`Library/` and `node_modules/` are normally gitignored, so a search that respects `.gitignore` skips them; ripgrep needs `--no-ignore`.

### 🧩 As an Agent Skill

The npm and Flutter packages also carry those pages as an [Agent Skill](https://agentskills.io): a folder whose `SKILL.md` tells an assistant what the pages are for. Once it is in your project's skill directory (`.claude/skills/`, `.agents/skills/`, and so on), the assistant finds the docs without being told where they are. Your package manager puts it there:

- **pnpm 12.11 or later**: run `pnpm approve <package>` once. Every install after that links the skills of your direct dependencies into the skill directories at the workspace root, or into the ones `skills.dirs` in `pnpm-workspace.yaml` names. An install with an approved skill and no such directory fails, so a CI checkout needs one too.
- **npm or yarn**: `npx skills experimental_sync` links them the same way.
- **Flutter**: `dart run skills@ get` copies them. Run it again after upgrading.

## ⌨️ Converting a project

An assistant can run commands but cannot use a window, so it converts with `ssconverter-cli`. Each SDK release has one zip per platform at a fixed URL, `https://github.com/cri-middleware/SpriteStudio-SDK/releases/latest/download/ssconverter-cli-<platform>.zip`; the platforms are listed in the [CLI README](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/cli/README.md). Its output names every `.ssab` it wrote with the animations inside, which are the names to pass to the player.

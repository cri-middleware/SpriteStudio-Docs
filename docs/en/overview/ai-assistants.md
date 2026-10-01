# 🤖 Using with AI Assistants

Every official site publishes its documentation as Markdown too, so you can hand it to an AI assistant instead of pasting pages one by one. This page says where the Markdown is and how to point an assistant at it.

!!! info "🚧 Coming soon"
    The addresses below go live as each player's site is published. They are written as plain text, not links, because they 404 until then.

## 🔗 What each site serves

Every site serves two files at its root, and a Markdown copy of every page:

- `llms.txt` is an index of the site's pages, written for an AI assistant to read first and pick pages from.
- `llms-full.txt` is every page in one file. It can be large, so prefer `llms.txt` and let the assistant fetch the pages it needs.
- Each page also has a Markdown copy next to its HTML: `index.md` inside the page's folder, or `<page>.md` on the Web and React Native sites. A button beside the page title copies that page's Markdown to the clipboard.

| Site | `llms.txt` |
|---|---|
| [Unity](../players/unity.md) | `https://cri-middleware.github.io/SSPlayerForUnity/llms.txt` |
| [Web (Player Collection)](../players/web.md) | `https://cri-middleware.github.io/SSPlayerForWeb/llms.txt` |
| [Godot](../players/godot.md) | `https://cri-middleware.github.io/SSPlayerForGodot/llms.txt` |
| [Flutter](../players/flutter.md) | `https://cri-middleware.github.io/SSPlayerForFlutter/llms.txt` |
| [Ren'Py](../players/renpy.md) | `https://cri-middleware.github.io/SSPlayerForRenPy/llms.txt` |
| [wgpu (Rust, C / C++)](../players/wgpu.md) | `https://cri-middleware.github.io/SSPlayerForWgpu/llms.txt` |
| [React Native](../players/react-native.md) | `https://cri-middleware.github.io/SSPlayerForReactNative/llms.txt` |
| [Converter GUI](../players/converter.md) | `https://cri-middleware.github.io/SSConverterGUI/llms.txt` |
| [SDK - the Player Porting Guide](../sdk/porting.md) | `https://cri-middleware.github.io/SpriteStudio-SDK/llms.txt` |
| This portal | `https://cri-middleware.github.io/SpriteStudio-Docs/llms.txt` |

### 🌐 Languages

For the sites other than Web and React Native, add `ja/` after the repository name to get the Japanese files, for example `https://cri-middleware.github.io/SSPlayerForUnity/ja/llms.txt`. The Web and React Native sites write one pair of English files; each of their Japanese pages has a Markdown copy at the same path under `ja/` with `.md` appended.

## 📦 Docs inside the package

The Unity package carries its documentation for the version you installed, as Markdown in English and Japanese: in `Library/PackageCache/jp.co.cri-mw.spritestudio.ssplayer-unity@<hash>/Documentation~/`, starting at `en/index.md`. It reads without a network and always matches the installed version. `Library/` is normally gitignored, so a search that respects `.gitignore` skips it; ripgrep needs `--no-ignore`.

## 📝 A snippet for your AGENTS.md

An assistant only knows where the docs are if something in your project says so. Paste this into your project's `AGENTS.md` (or `CLAUDE.md`), and swap in your player's address from the table above:

```markdown
## SpriteStudio Player for Unity

- Read the player's docs before writing code against it, and check its Limitations & Scope page before promising a feature.
- The docs for the installed version are inside the package: `Library/PackageCache/jp.co.cri-mw.spritestudio.ssplayer-unity@*/Documentation~/`, starting at `en/index.md`. `Library/` is gitignored, so search it with `rg --no-ignore`.
- The latest docs, as Markdown: https://cri-middleware.github.io/SSPlayerForUnity/llms.txt
```

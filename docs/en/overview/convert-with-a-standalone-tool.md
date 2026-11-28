# 🧰 Converting with a Standalone Tool

When your player doesn't convert for you (the table in [Converting Assets](./conversion.md) says
which ones do), on an engine that table doesn't list, or in a build or CI/CD pipeline, you convert
with one of the standalone tools below.

## 🧭 Which one should I use?

All three emit the same `.ssab` / `.ssqb` ([why](./conversion.md)) - pick by workflow, not by
output. Each can emit an embedded `.ssab` too (**Embedded Assets** in the browser tool and the
GUI, `--embedded` on the CLI); not every player reads one, so check
[Reference and embedded](./conversion.md#reference-and-embedded) first.

| Your situation | Use | Why |
|---|---|---|
| Can't install anything, or just a quick one-off | **`ssconverter-web`** | Runs fully in the browser, nothing to install |
| On the desktop, occasional conversions, prefer a UI | **SSConverter GUI** (macOS / Windows) | Drag & drop, no terminal needed |
| Automating a build, CI/CD, or many projects at once | **`ssconverter-cli`** | Scriptable, batch mode |

> [!TIP] Not sure? Start in the browser.
> The quickest way to get one `.ssab` and confirm your assets convert cleanly is ssconverter-web,
> with nothing to install. Move to the GUI or CLI once conversion becomes a repeatable part of
> your workflow.

## 🌐 ssconverter-web - in the browser

Converts `.sspj` -> `.ssab` entirely in your browser; nothing is uploaded to a server.

> [!NOTE] Dropping a folder
> Dropping a folder relies on the **File System Access API**, so it works only in Chromium-based
> browsers (**Chrome**, **Edge**, **Opera**). In Firefox and Safari, pick the folder with
> **Browse...** instead.

1. Open the converter at [`https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/`](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/).
2. Drop in the folder that contains your `.sspj`, or pick it with **Browse...** (its images and other referenced files are read along with it). The folder must hold exactly one `.sspj`.
3. Press **⚡ Convert & Download**. The ZIP holds one folder named after the `.sspj`, with the `.ssab` and its textures inside; with **Embedded Assets** on, the folder is `<name>_emb` and the textures are inside the `.ssab`.

> [!INFO] Versioned by `.ssab` schema
> ssconverter-web is published **per `.ssab` schema version**, so the URL carries the schema:
>
> - Latest (auto-redirects): [`https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/`](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/)
> - A specific schema, e.g. `v1`: [`https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/v1/`](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/v1/)
>
> Match the schema to your player's runtime version ([why](../sdk/limitations.md#schema-version)) - when in doubt, use the latest
> (auto-redirecting) build.

## 🖥️ SSConverter GUI - desktop app

A Tauri desktop app. No command line. Builds are published for **macOS and Windows** - on Linux,
take `ssconverter-cli` below instead; the output is the same.

1. Download the archive for your OS from [GitHub Releases](https://github.com/cri-middleware/SSConverterGUI/releases) and
   unpack it - there is no installer. On Windows, SmartScreen asks on first launch; the
   [Installation guide](https://cri-middleware.github.io/SSConverterGUI/install/) says what to do.
2. Launch it and drop a `.sspj` - or a folder of them - onto the window (or pick one with
   **File...** / **Folder...**).
3. Optionally change the output folder (by default, a folder next to the `.sspj`), then click
   **Convert**.

Details: [SSConverter GUI overview](../players/converter.md) ·
[Documentation](https://cri-middleware.github.io/SSConverterGUI/) ·
[Repository](https://github.com/cri-middleware/SSConverterGUI).

## ⌨️ ssconverter-cli - command line & CI

A single self-contained binary for Windows / macOS / Linux. Download it from the
[SDK Releases](https://github.com/cri-middleware/SpriteStudio-SDK/releases) (no build
environment required). Each release has one zip per platform at a fixed URL,
`https://github.com/cri-middleware/SpriteStudio-SDK/releases/latest/download/ssconverter-cli-<platform>.zip`,
so a script can fetch the latest; the platforms are listed in the README linked below. Then:

```bash
# Single project -> writes a project/ folder alongside the .sspj
ssconverter-cli project.sspj

# Choose the output directory
ssconverter-cli project.sspj -o ./out

# Embed referenced assets (textures, etc.) into the .ssab, written to project_emb/ (one self-contained file, easy to ship)
ssconverter-cli project.sspj --embedded

# Batch: recursively find every .sspj under these directories and convert them in parallel
ssconverter-cli ./assets/projects ./more_assets
```

In batch mode each output is written next to its source (`-o` is ignored). Each run lists the
`.ssab` it wrote and the animations inside each. Full option list:
[ssconverter-cli README](https://github.com/cri-middleware/SpriteStudio-SDK/tree/HEAD/cli).

## ➡️ Next

Whatever you used, the output is the same `.ssab` / `.ssqb`. Hand the output folder to your
player - its page says where it goes, and [Choose Your Platform](./choose-your-platform.md) links
each one. For how the runtime plays it back, see [SDK Concepts](../sdk/concepts.md); for the
on-disk details, the [Format Specification](../sdk/format-spec.md).

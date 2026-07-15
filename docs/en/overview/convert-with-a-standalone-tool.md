# 🧰 Converting with a Standalone Tool

Unity, Godot, and Ren'Py **embed** `libssconverter`, so they convert automatically on import -
`.sspj` becomes `.ssab` seamlessly, with no separate tool (see
[Converting Assets](./conversion.md)). Targeting anything other than those three means no player
converts for you, so you run a standalone tool yourself - for example when you:

- play back in the browser ([SSPlayerForWeb](../players/web.md)),
- integrate your own player, or bring SpriteStudio to a new engine ([Porting a Player](../sdk/porting.md)), or
- automate conversion in a build or CI/CD pipeline.

## 🧭 Which one should I use?

All three run the same `libssconverter`, so the `.ssab` / `.ssqb` they produce is identical -
pick by workflow, not by output.

| Your situation | Use | Why |
|---|---|---|
| Can't install anything, or just a quick one-off | **`ssconverter-web`** | Runs fully in the browser, nothing to install |
| On the desktop, occasional conversions, prefer a UI | **SSConverterGUI** | Drag & drop, no terminal needed |
| Automating a build, CI/CD, or many projects at once | **`ssconverter-cli`** | Scriptable, batch mode, `--embedded` |

!!! tip "Not sure? Start in the browser."
    [ssconverter-web](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) is a web
    app - nothing to install - and runs the conversion in your browser via WebAssembly (wasm),
    so your files never leave your machine. It's the fastest way to get one `.ssab` and confirm
    your assets convert cleanly. Move to the GUI or CLI once conversion becomes a repeatable
    part of your workflow.

## 🌐 ssconverter-web - in the browser

Converts `.sspj` -> `.ssab` entirely in your browser; nothing is uploaded to a server.

!!! warning "Use a Chromium-based browser"
    ssconverter-web relies on the **File System Access API**, so it works only in Chromium-based
    browsers (**Chrome**, **Edge**, **Opera**). Firefox and Safari are not supported.

1. Open the converter: <https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/>
2. Drop in the folder that contains your `.sspj` (its images and other referenced files are read along with it).
3. Download the result as a ZIP (the `.ssab` and its referenced textures).

!!! info "Versioned by `.ssab` schema"
    ssconverter-web is published **per `.ssab` schema version**, so the URL carries the schema:

    - Latest (auto-redirects): <https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/>
    - A specific schema, e.g. `v1`: <https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/v1/>

    Match the schema to your player's runtime version - when in doubt, use the latest link and
    pick the version from the in-app switcher.

## 🖥️ SSConverterGUI - desktop app

A cross-platform Tauri desktop app. No command line.

1. Download a build from [GitHub Releases](https://github.com/cri-middleware/SSConverterGUI/releases).
2. Launch it and drag your `.sspj` onto the window (or open it from the file picker).
3. Choose an output folder and convert.

Details & screenshots: [SSConverterGUI overview](../players/converter.md) ·
[Repository](https://github.com/cri-middleware/SSConverterGUI).

## ⌨️ ssconverter-cli - command line & CI

A single self-contained binary for Windows / macOS / Linux. Download it from the
[SDK Releases](https://github.com/cri-middleware/SpriteStudio-SDK/releases) (no build
environment required), then:

```bash
# Single project -> writes a project/ folder alongside the .sspj
ssconverter-cli project.sspj

# Choose the output directory
ssconverter-cli project.sspj -o ./out

# Embed referenced assets (textures, etc.) into the .ssab (one self-contained file, easy to ship)
ssconverter-cli project.sspj --embedded

# Batch: recursively find every .sspj under these directories and convert them in parallel
ssconverter-cli ./assets/projects ./more_assets
```

In batch mode each output is written next to its source (`-o` is ignored). Full option list:
[ssconverter-cli README](https://github.com/cri-middleware/SpriteStudio-SDK/tree/main/cli).

## ➡️ Next

Whatever you used, the output is the same `.ssab` / `.ssqb`. See [SDK Concepts](../sdk/concepts.md)
for how the runtime plays it back, or the [Format Specification](../sdk/format-spec.md) for the
on-disk details.

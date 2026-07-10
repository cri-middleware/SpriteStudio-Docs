# 🔄 Converting Assets

Before playback, a SpriteStudio project (`.sspj` + images) is converted once into the compact
runtime format (`.ssab` / `.ssqb`). Every path below runs the **same `libssconverter`** from
[SpriteStudio-SDK](../sdk/concepts.md) and produces the **same output** - pick whichever fits
your engine and workflow.

## 🔀 Two ways to convert

### 1. Automatic - no external tool (Unity, Godot, Ren'Py)

These players embed `libssconverter` and run it for you, so conversion happens
in-place - **no external tool required**:

- **Unity** - the built-in Importer converts on drag & drop.
- **Godot** - the SS Import Dock converts on drag & drop.
- **Ren'Py** - auto-imports on startup (drop sources into `SpriteStudio_Source/`).

### 2. Standalone tools

For engines without an editor integration, for CI/CD pipelines, or for the Web collection,
convert with one of the standalone front-ends:

| Tool | Best for | Links |
|---|---|---|
| **SsConverterGUI** | Desktop, no CLI needed | [Overview](../players/converter.md) · [GitHub](https://github.com/cri-middleware/SsConverterGUI) |
| **`ssconverter-cli`** | Batch / CI-CD automation | [SpriteStudio-SDK](https://github.com/cri-middleware/SpriteStudio-SDK/tree/main/cli) |
| **`ssconverter-web`** | In the browser, fully client-side | [Latest](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) · [Package](https://github.com/cri-middleware/SSPlayerForWeb/tree/main/packages/ssconverter-web) |

!!! tip "ssconverter-web - versioned by `.ssab` schema"
    [ssconverter-web](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) converts
    `.sspj` -> `.ssab` entirely in the browser - nothing is uploaded to a server.

    It is published **per `.ssab` schema version**, so the URL includes the schema:

    - Latest (auto-redirects): <https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/>
    - A specific schema, e.g. `v1`: <https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/v1/>

    Match the schema to your player's runtime version. When in doubt, use the latest link and
    pick the version from the in-app switcher.

## 📦 What you get

Both paths emit `.ssab` (animation) / `.ssqb` (sequence) plus the referenced textures, which
`libssruntime` then plays back. See [SDK Concepts](../sdk/concepts.md) for the pipeline and the
[Format Specification](../sdk/format-spec.md) for on-disk details.

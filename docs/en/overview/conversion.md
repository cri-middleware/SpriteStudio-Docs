# 🔄 Converting Assets

Before playback, a SpriteStudio project (`.sspj` + images) is converted once into the compact
runtime format (`.ssab` / `.ssqb`). Every path below runs the **same `libssconverter`** from
[SpriteStudio-SDK](../sdk/concepts.md) and produces the **same output** - pick whichever fits
your engine and workflow.

## 🔀 Two ways to convert

### 1. Converted automatically on import - no external tool (Unity, Godot, Ren'Py)

The official player packages for these engines **bundle** `libssconverter` as a conversion tool.
It runs automatically on the editor / development side, so conversion happens
in-place - **nothing else to install**:

- **Unity** - [SSPlayerForUnity](../players/unity.md)'s bundled Importer converts on drag & drop.
- **Godot** - [SSPlayerForGodot](../players/godot.md)'s SS Import Dock converts on drag & drop.
- **Ren'Py** - [SSPlayerForRenPy](../players/renpy.md) auto-imports on startup (drop sources into `SpriteStudio_Source/`).

Each player's own docs (with screencasts) walk through its workflow - see
[Choose Your Platform](./choose-your-platform.md).

### 2. Standalone tools - convert it yourself

On a different engine, in a CI/CD pipeline, or using [SSPlayerForWeb](../players/web.md) (the Web
collection)? No player converts for you, so you convert with one of three standalone front-ends -
a desktop GUI, a CLI, or a browser tool. Which one to pick and how to run each is covered in
**[Converting with a Standalone Tool](./convert-with-a-standalone-tool.md)**.

## 📦 What you get

Both paths emit `.ssab` (animation) / `.ssqb` (sequence) plus the referenced textures, which
`libssruntime` then plays back. See [SDK Concepts](../sdk/concepts.md) for the pipeline and the
[Format Specification](../sdk/format-spec.md) for on-disk details.

# 🔄 Converting Assets

Before playback, a SpriteStudio project (`.sspj` + images) is converted once into the compact
runtime format (`.ssab` / `.ssqb`). Every path below runs the **same `libssconverter`** from
[SpriteStudio-SDK](../sdk/concepts.md) and produces the **same output** - pick whichever fits
your engine and workflow.

The input is a project authored in **SpriteStudio 7.5 or later**: the `.ssab` / `.ssqb` formats
are defined against that version, and conversion does not upgrade an older project to it.

!!! tip "No SpriteStudio project of your own yet?"
    CRI Middleware publishes free
    [sample data](https://www.webtech.co.jp/help/ja/spritestudio7/download/sample/) - complete
    `.sspj` projects (characters, effects, UI, shaders) you can feed straight into any path
    below. Each download carries its own readme with the terms of use. (Help Center page, in
    Japanese.)

## 🔀 Two ways to convert

### 1. Converted automatically on import - no external tool (Unity, Godot, Flutter, Ren'Py, TyranoBuilder)

The official player packages for these engines **bundle** `libssconverter` as a conversion tool.
It runs automatically on the editor / development side, so conversion happens
in-place - **nothing else to install**:

- **Unity** - [SSPlayerForUnity](../players/unity.md)'s bundled Importer converts on drag & drop.
- **Godot** - [SSPlayerForGodot](../players/godot.md)'s SS Import Dock converts on drag & drop.
- **Flutter** - [SSPlayerForFlutter](../players/flutter.md)'s auto importer (`sswatch`) re-converts on save and pushes the
  result into the running app (drop sources into `SpriteStudio_Source/`); its `ssconvert` CLI converts once.
- **Ren'Py** - [SSPlayerForRenPy](../players/renpy.md) auto-imports on startup (drop sources into `SpriteStudio_Source/`).
- **TyranoBuilder** - [SSPlayerForWeb](../players/web.md)'s `ssplayer-tyranobuilder` plugin converts inside the
  editor when the project is opened (drop sources into `SpriteStudio_Source/`); the result then appears in the
  component's dropdowns.

Each player's own docs (with screencasts) walk through its workflow - see
[Choose Your Platform](./choose-your-platform.md).

### 2. Standalone tools - convert it yourself

On a different engine, in a CI/CD pipeline, or using one of the players that hosts no importer -
[SSPlayerForWeb](../players/web.md)'s renderers (the Web collection),
[SSPlayerForReactNative](../players/react-native.md), or [SSPlayerForWgpu](../players/wgpu.md)?
No player converts for you there, so you convert with one of three standalone front-ends -
a desktop GUI, a CLI, or a browser tool. Which one to pick and how to run each is covered in
**[Converting with a Standalone Tool](./convert-with-a-standalone-tool.md)**.

## 📦 What you get

Both paths emit `.ssab` (animation) / `.ssqb` (sequence) plus the referenced textures, which
`libssruntime` then plays back. See [SDK Concepts](../sdk/concepts.md) for the pipeline and the
[Format Specification](../sdk/format-spec.md) for on-disk details.

Conversion runs one way only: `.ssab` is a playback format, and there is no route back to
`.sspj`. Keep editing the SpriteStudio project and convert again.

### How a project's files map to the output

A SpriteStudio project is made up of several files. If you have been handed a `.sspj` and asked to
implement against it, this mapping is the first thing to know - and it is **the same whichever
conversion path you take**.

| SpriteStudio file | Role | On conversion |
|---|---|---|
| `.sspj` | The project itself; holds the list of `.ssae` / `.ssce` / `.ssqe` it references | **Not emitted.** It is used only to resolve resources during conversion |
| `.ssae` (animation pack) | Part structure and keyframes | Becomes one `.ssab` |
| `.ssce` (cell map) | The image used, and the cells cut out of it (position, size, pivot) | **Never becomes a file of its own - it is folded into the `.ssab`** |
| `.ssqe` (sequence) | A playlist of animations | Becomes one `.ssqb` (playback is not implemented - [Shared Limitations](../sdk/limitations.md)) |
| Images (`.png` and so on) | The artwork itself | Copied to the output location and referenced by the `.ssab` |

See the [Glossary](../sdk/glossary.md) for the terms and the
[Format Specification](../sdk/format-spec.md) for the design decisions behind the conversion unit.

!!! warning "When you can swap the image alone"
    Cell positions and sizes are **baked from the `.ssce` into the `.ssab`**. Repainting the artwork
    is reflected by replacing the image file alone, but if you add, move or resize cells - or change
    the overall image size - **rebuild the `.ssab` and ship it alongside**. Shipping only the new
    image renders it against the old cut-out rectangles, so the artwork shifts.

# 🕹️ SpriteStudio Player for Godot

Renders SpriteStudio animations natively in the **Godot Engine**, backed by `libssruntime`.

!!! tip "Editor-first - no code to reach the first frame"
    Copy the add-on in, drag your `.sspj` onto the editor, add a node and assign the asset.
    GDScript control is available; nothing above needs it.

**1. What you install** - the `addons` folder from
the [latest Release](https://github.com/cri-middleware/SSPlayerForGodot/releases/latest), copied into your
Godot project root. The player comes in two forms:

- **GDExtension** - the drop-in binary add-on the Release carries; no engine rebuild required.
- **Custom module** - built from source into a custom Godot build for tighter integration.

**2. `.sspj` -> `.ssab`** - drag the `.sspj` from your file manager onto the add-on's **SS Importer**
dock, which converts it inside the project, so there is no separate tool to install.

**3. Getting it on screen** - drop the converted `.ssab` into the 2D viewport; that places a
`SpriteStudioPlayer2D` node playing it.

The steps, with the folders they use, are in the README's [Quick Start](https://github.com/cri-middleware/SSPlayerForGodot#-quick-start-with-gdextension).

## ➡️ Read next

- [Documentation](https://cri-middleware.github.io/SSPlayerForGodot/)
- [Repository](https://github.com/cri-middleware/SSPlayerForGodot)
- [Choose Your Platform](../overview/choose-your-platform.md) - compare with the other players

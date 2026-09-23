# 🕹️ SSPlayerForGodot

Renders SpriteStudio animations natively in the **Godot Engine**, backed by `libssruntime`.

!!! tip "Editor-first - no code to reach the first frame"
    Copy the add-on in, drag your `.sspj` onto the editor, add a node and assign the asset.
    GDScript control is available; nothing above needs it.

**1. What you install** - the `addons` folder from
🚧 [GitHub Releases](https://github.com/cri-middleware/SSPlayerForGodot/releases), copied into your
Godot project root. Godot 4.7-series. It ships in two forms:

- **GDExtension** - drop-in binary add-on; no engine rebuild required.
- **Custom module** - compiled into a custom Godot build for tighter integration.

**2. `.sspj` -> `.ssab`** - drag & drop the `.sspj` onto the Godot editor. The add-on's SS Import
Dock converts it in place, so there is no separate tool to install.

**3. Getting it on screen** - add a `SpriteStudioPlayer2D` node and assign the `.ssab` to its
**Ssab** property.

## ➡️ Read next

- **Documentation** - 🚧 *coming soon*
- [Repository](https://github.com/cri-middleware/SSPlayerForGodot)
- [Choose Your Platform](../overview/choose-your-platform.md) - compare with the other players

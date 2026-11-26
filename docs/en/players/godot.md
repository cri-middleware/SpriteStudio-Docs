---
description: "Play SpriteStudio animations in Godot 4: drop a .sspj on the editor and place a node, with no code. SpriteStudio adds bones, mesh and effects to 2D illustrations."
---

# 🕹️ SpriteStudio Player for Godot

Renders SpriteStudio animations natively in the **Godot Engine**, backed by `libssruntime`.

!!! tip "Editor-first - no code to reach the first frame"
    Copy the add-on in, drag your `.sspj` onto the editor, add a node and assign the asset.
    GDScript control is available; nothing above needs it.

**1. What you install** - `ssplayer-godot-extension-<Godot version>.zip` from the
[latest Release](https://github.com/cri-middleware/SSPlayerForGodot/releases/latest)'s Assets; its `addons`
folder goes into your Godot project root, with no engine rebuild (a custom module built into Godot
itself is the other form, from source).

**2. `.sspj` -> `.ssab`** - drag the `.sspj` from your file manager onto the add-on's **SS Importer**
dock, which converts it inside the project, so there is no separate tool to install.

**3. Getting it on screen** - drop the converted `.ssab` into the 2D viewport; that places a
`SpriteStudioPlayer2D` node with its first animation selected. **Play from start** in the
**SpriteStudio** bottom panel plays it in the editor, and so does running the scene.

The steps, with the folders they use, are in the README's [Quick Start](https://github.com/cri-middleware/SSPlayerForGodot#-quick-start-with-gdextension).

## ➡️ Read next

- [Documentation](https://cri-middleware.github.io/SSPlayerForGodot/)
- [Repository](https://github.com/cri-middleware/SSPlayerForGodot)
- [Choose Your Platform](../overview/choose-your-platform.md) - compare with the other players

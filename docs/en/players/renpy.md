# 🎭 SSPlayerForRenPy

Bring SpriteStudio characters into **Ren'Py** visual novels, backed by `libssruntime`.
A playable Web demo ships with each release.

!!! tip "Code-first - a few lines of script"
    `SSPlayer` is a standard Ren'Py Displayable, so it composes with ATL and `Transform` exactly
    like any other image.

**1. What you install** - `SSPlayerForRenPy.zip` from
🚧 [GitHub Releases](https://github.com/cri-middleware/SSPlayerForRenPy/releases). Extract it and
copy the resulting `spritestudio/` folder into your project's `game/` folder.

**2. `.sspj` -> `.ssab`** - drop your SpriteStudio sources into `SpriteStudio_Source/`. The Auto
Importer converts them on startup, and reloading with **Shift+R** re-converts only what changed,
so there is no manual export step.

**3. Getting it on screen** - add the player to a screen:

```renpy
screen demo():
    add SSPlayer("overall/Basic.ssab") xalign 0.5 yalign 0.5
```

## ➡️ Read next

- **Documentation** - 🚧 *coming soon*
- 🚧 [Repository](https://github.com/cri-middleware/SSPlayerForRenPy)
- [Try It in Your Browser](../overview/try-it.md) - the bundled animations running in Ren'Py Web

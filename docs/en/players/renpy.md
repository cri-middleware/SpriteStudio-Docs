# 🎭 SpriteStudio Player for Ren'Py

Bring SpriteStudio characters into **Ren'Py** visual novels, backed by `libssruntime`.

▶️ See it first, no install: the bundled animations run in Ren'Py Web -
[Try it in your browser](../overview/try-it.md).

!!! tip "Code-first - one line of script"
    A converted pack is already an image, so `show` puts it on screen, and ATL and `Transform`
    move it like any other image.

**1. What you install** - [`SSPlayerForRenPy.zip`](https://github.com/cri-middleware/SSPlayerForRenPy/releases/latest/download/SSPlayerForRenPy.zip),
from the latest Release. Extract it and
copy the resulting `spritestudio/` folder into your project's `game/` folder.

**2. `.sspj` -> `.ssab`** - copy your SpriteStudio project's whole folder into `SpriteStudio_Source/`, beside
`game/`. The Auto Importer converts it when the game launches from the Ren'Py launcher, and after
one **Shift+R** each save re-converts what changed, so there is no manual export step.

**3. Getting it on screen** - `show ringo wait1`: the pack `Ringo.ssab` is the image `ringo`, and
each of its animations an attribute.

The steps, with the folders they use, are in the README's [Quick Start](https://github.com/cri-middleware/SSPlayerForRenPy#-quick-start).

## ➡️ Read next

- [Documentation](https://cri-middleware.github.io/SSPlayerForRenPy/)
- [Repository](https://github.com/cri-middleware/SSPlayerForRenPy)
- [Try It in Your Browser](../overview/try-it.md) - the bundled animations running in Ren'Py Web

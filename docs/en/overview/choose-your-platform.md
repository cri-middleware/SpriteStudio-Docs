# 🧭 Choose Your Platform

Pick the one that matches your target runtime. Names link to its overview page here; the right
column links to its full details.

| I want to ship on... | Use | Details |
|---|---|---|
| A Unity game | **[SSPlayerForUnity](../players/unity.md)** | [Docs](https://cri-middleware.github.io/SSPlayerForUnity/) |
| The **browser** - PixiJS, WebGL | **[SSPlayerForWeb](../players/web.md)** (player collection) | [Docs](https://cri-middleware.github.io/SSPlayerForWeb/) |
| **RPG Maker MZ**, **TyranoScript** - 🧪 experimental (alpha) | **[SSPlayerForWeb](../players/web.md)** (`ssplayer-webgl` adapters) | [Docs](https://cri-middleware.github.io/SSPlayerForWeb/usage/rmmz) |
| A Godot game | **[SSPlayerForGodot](../players/godot.md)** | [Docs](https://cri-middleware.github.io/SSPlayerForGodot/) |
| A **Flutter** app - 🧪 early development | **[SSPlayerForFlutter](../players/flutter.md)** | [GitHub](https://github.com/cri-middleware/SSPlayerForFlutter) |
| A Ren'Py visual novel | **[SSPlayerForRenPy](../players/renpy.md)** | [Docs](https://cri-middleware.github.io/SSPlayerForRenPy/) |
| Building your own player / integration | **SpriteStudio-SDK** | [Porting a Player](../sdk/porting.md) |

Only converting `.sspj`? Pick a standalone tool rather than a player.

| I want to convert on... | Use | Details |
|---|---|---|
| The browser | **[SSPlayerForWeb](../players/web.md)** (`ssconverter-web`) | [Try it](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) |
| The desktop - GUI | **[SSConverterGUI](../players/converter.md)** | [Docs](https://cri-middleware.github.io/SSConverterGUI/) |
| The desktop - CLI | **SpriteStudio-SDK** (`ssconverter-cli`) | [How to run it](./convert-with-a-standalone-tool.md) |

## ✅ Common to every platform

- The **conversion step** (`.sspj` -> the runtime assets `.ssab` / `.ssqb` + textures) is the
  same everywhere - see
  [SDK Concepts](../sdk/concepts.md) for the pipeline, and [Converting Assets](./conversion.md)
  for every way to convert (automatic on import, GUI, CLI, or browser).
- Feature coverage (bones, mesh/deform, particles, extended blend, masks) is driven by the
  shared core, so it is consistent across platforms.
- Licensing is shared - see [License](../license.md).

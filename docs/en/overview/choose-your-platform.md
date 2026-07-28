# 🧭 Choose Your Platform

Pick the one that matches your target runtime. Names link to its overview page here; the right
column links to its full details.

| I want to ship on... | Use | Details |
|---|---|---|
| A Unity game | **[SSPlayerForUnity](../players/unity.md)** | Docs (coming soon) |
| The **browser** - PixiJS, WebGL | **[SSPlayerForWeb](../players/web.md)** (player collection) | Docs (coming soon) |
| **RPG Maker MZ** - 🧪 experimental (alpha) | **[SSPlayerForWeb](../players/web.md)** (`ssplayer-rmmz`) | Docs (coming soon) |
| A **TyranoScript / TyranoBuilder** visual novel - beta | **[SSPlayerForWeb](../players/web.md)** (`ssplayer-tyranoscript` / `ssplayer-tyranobuilder`) | Docs (coming soon) |
| A Godot game | **[SSPlayerForGodot](../players/godot.md)** | Docs (coming soon) |
| A **Flutter** app | **[SSPlayerForFlutter](../players/flutter.md)** | Docs (coming soon) |
| A Ren'Py visual novel | **[SSPlayerForRenPy](../players/renpy.md)** | Docs (coming soon) |
| Building your own player / integration | **SpriteStudio-SDK** | [Porting a Player](../sdk/porting.md) |

Only converting `.sspj`? Pick a standalone tool rather than a player.

| I want to convert on... | Use | Details |
|---|---|---|
| The browser | **[SSPlayerForWeb](../players/web.md)** (`ssconverter-web`) | Try it (coming soon) |
| The desktop - GUI | **[SSConverterGUI](../players/converter.md)** | Docs (coming soon) |
| The desktop - CLI | **SpriteStudio-SDK** (`ssconverter-cli`) | [How to run it](./convert-with-a-standalone-tool.md) |

## ✅ Common to every platform

- The **conversion step** (`.sspj` -> the runtime assets `.ssab` / `.ssqb` + textures) is the
  same everywhere - see
  [SDK Concepts](../sdk/concepts.md) for the pipeline, and [Converting Assets](./conversion.md)
  for every way to convert (automatic on import, GUI, CLI, or browser).
- Feature coverage (bones, mesh/deform, particles, extended blend, masks) is driven by the
  shared core, so the feature *set* is the same everywhere. What still differs per engine is
  listed in [Feature Support](./feature-support.md); the constraints that apply everywhere are
  in [Shared Limitations](../sdk/limitations.md).
- Licensing is shared - see [License](../license.md).

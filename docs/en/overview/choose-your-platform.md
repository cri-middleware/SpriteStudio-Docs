# 🧭 Choose Your Platform

Pick the player that matches your target runtime. Each links to its own full documentation.

| I want to ship on... | Use | Docs / Repo |
|---|---|---|
| A Unity game | **SSPlayerForUnity** | [Docs](https://cri-middleware.github.io/SSPlayerForUnity/) |
| The **browser** - PixiJS, WebGL, **RPG Maker MZ**, or **TyranoScript** | **SSPlayerForWeb** (player collection) | [Docs](https://cri-middleware.github.io/SSPlayerForWeb/) |
| A Godot game | **SSPlayerForGodot** | [Docs](https://cri-middleware.github.io/SSPlayerForGodot/) |
| A **Flutter** app - 🧪 early development | **SSPlayerForFlutter** | [GitHub](https://github.com/cri-middleware/SSPlayerForFlutter) |
| A Ren'Py visual novel | **SSPlayerForRenPy** | [Docs](https://cri-middleware.github.io/SSPlayerForRenPy/) |
| Just converting `.sspj` in the browser | **SSPlayerForWeb** (`ssconverter-web`) | [Try it](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) |
| Just converting `.sspj` on the desktop - GUI | **SSConverterGUI** | [GitHub](https://github.com/cri-middleware/SsConverterGUI) |
| Just converting `.sspj` on the desktop - CLI | **SpriteStudio-SDK** (`ssconverter-cli`) | [GitHub](https://github.com/cri-middleware/SpriteStudio-SDK) |
| Building your own player / integration | **SpriteStudio-SDK** | [Porting a Player](../sdk/porting.md) |

## ✅ Common to every platform

- The **conversion step** (`.sspj` -> the runtime assets `.ssab` / `.ssqb` + textures) is the
  same everywhere - see
  [SDK Concepts](../sdk/concepts.md) for the pipeline, and [Converting Assets](./conversion.md)
  for every way to convert (automatic on import, GUI, CLI, or browser).
- Feature coverage (bones, mesh/deform, particles, extended blend, masks) is driven by the
  shared core, so it is consistent across platforms.
- Licensing is shared - see [License](../license.md).

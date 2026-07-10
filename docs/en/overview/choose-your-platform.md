# Choose Your Platform

Pick the player that matches your target runtime. Each links to its own full documentation.

| I want to ship on… | Use | Docs |
|---|---|---|
| A Unity game | **SSPlayerForUnity** | [Docs](https://cri-middleware.github.io/SSPlayerForUnity/) |
| The **browser** — PixiJS, standalone WebGL, or **TyranoScript** | **SSPlayerForWeb** (player collection) | [Docs](https://cri-middleware.github.io/SSPlayerForWeb/) |
| A Godot game | **SSPlayerForGodot** | [Docs](https://cri-middleware.github.io/SSPlayerForGodot/) |
| A Ren'Py visual novel | **SSPlayerForRenPy** | [Docs](https://cri-middleware.github.io/SSPlayerForRenPy/) |
| Just converting `.sspj` on the desktop | **SsConverterGUI** | [GitHub](https://github.com/cri-middleware/SsConverterGUI) |
| Building your own integration | **SpriteStudio-SDK** | [Concepts](../sdk/concepts.md) |

## Common to every platform

- The **conversion step** (`.sspj` → runtime assets) is the same everywhere — see
  [SDK Concepts](../sdk/concepts.md). You can convert with the [Converter GUI](../players/converter.md)
  or the `ssconverter-cli` bundled with each player.
- Feature coverage (bones, mesh/deform, particles, extended blend, masks) is driven by the
  shared core, so it is consistent across platforms.
- Licensing is shared — see [License](../license.md).

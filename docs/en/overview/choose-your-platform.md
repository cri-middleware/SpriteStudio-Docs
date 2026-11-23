# 🧭 Choose Your Platform

Pick the one that matches your target runtime. Names link to its overview page here; the right
column links to its full details.

| I want to ship on... | Use | Details |
|---|---|---|
| A **Unity** game | **[SpriteStudio Player for Unity](../players/unity.md)** | [Docs](https://cri-middleware.github.io/SSPlayerForUnity/) |
| The **browser** - PixiJS, WebGL | **[SpriteStudio Player for Web](../players/web.md)** (player collection) | [Docs](https://cri-middleware.github.io/SSPlayerForWeb/) |
| **RPG Maker MZ** | **[SpriteStudio Player for Web](../players/web.md)** (`ssplayer-rmmz`) | [Docs](https://cri-middleware.github.io/SSPlayerForWeb/usage/rmmz) |
| A **TyranoScript / TyranoBuilder** visual novel | **[SpriteStudio Player for Web](../players/web.md)** (`ssplayer-tyranoscript` / `ssplayer-tyranobuilder`) | Docs: [TyranoScript](https://cri-middleware.github.io/SSPlayerForWeb/usage/tyrano) / [TyranoBuilder](https://cri-middleware.github.io/SSPlayerForWeb/usage/tyranobuilder) |
| A **Godot** game | **[SpriteStudio Player for Godot](../players/godot.md)** | [Docs](https://cri-middleware.github.io/SSPlayerForGodot/) |
| A **Flutter** app | **[SpriteStudio Player for Flutter](../players/flutter.md)** | [Docs](https://cri-middleware.github.io/SSPlayerForFlutter/) |
| A **Flame** game | **[SpriteStudio Player for Flutter](../players/flutter.md)** (`ssplayer_flame`) | [Docs](https://cri-middleware.github.io/SSPlayerForFlutter/guide/flame/) |
| A **Ren'Py** visual novel | **[SpriteStudio Player for Ren'Py](../players/renpy.md)** | [Docs](https://cri-middleware.github.io/SSPlayerForRenPy/) |
| The **browser** - WebGPU | **[SpriteStudio Player for wgpu](../players/wgpu.md)** (`@spritestudio/ssplayer-wgpu`) | [Docs](https://cri-middleware.github.io/SSPlayerForWgpu/start/web/) |
| A **Bevy** game | **[SpriteStudio Player for wgpu](../players/wgpu.md)** (`ssplayer-bevy`) | [Docs](https://cri-middleware.github.io/SSPlayerForWgpu/start/bevy/) |
| A **Rust** or **C / C++** app with no engine, rendering its own frames | **[SpriteStudio Player for wgpu](../players/wgpu.md)** | [Docs](https://cri-middleware.github.io/SSPlayerForWgpu/) |
| A **React Native** app | **[SpriteStudio Player for React Native](../players/react-native.md)** | [Docs](https://cri-middleware.github.io/SSPlayerForReactNative/) |
| An engine not listed here - building your own player or integration | **SpriteStudio-SDK** | [Porting a Player](../sdk/porting.md) |

Only converting `.sspj`? Pick a standalone tool rather than a player.

| I want to convert on... | Use | Details |
|---|---|---|
| The browser | **[SpriteStudio Player for Web](../players/web.md)** (`ssconverter-web`) | [Try it](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) |
| The desktop - GUI (macOS / Windows) | **[SSConverter GUI](../players/converter.md)** | [Docs](https://cri-middleware.github.io/SSConverterGUI/) |
| The desktop - CLI | **SpriteStudio-SDK** (`ssconverter-cli`) | [How to run it](./convert-with-a-standalone-tool.md) |

## ✅ Common to every platform

- The **conversion step** (`.sspj` -> the runtime assets `.ssab` / `.ssqb` + textures) is the
  same everywhere - see
  [SDK Concepts](../sdk/concepts.md) for the pipeline, and [Converting Assets](./conversion.md)
  for every way to convert (in the player, GUI, CLI, or browser).
- Feature coverage (bones, mesh/deform, particles, extended blend, masks) is driven by the
  shared core, so the feature *set* is the same everywhere. What still differs per engine is
  listed in [Player Differences](./player-differences.md); the constraints that apply everywhere are
  in [Shared Limitations](../sdk/limitations.md).
- Licensing is shared - see [License](../license.md).

# 🌐 SSPlayerForWeb

A **collection of Web players** for SpriteStudio 7 animations in the browser, sharing one
WebAssembly core (`ssplayer-core`, built on `libssruntime`). Author your sprite art in
SpriteStudio, convert to `.ssab`, then play it back through the renderer of your choice.

- **Documentation:** <https://cri-middleware.github.io/SSPlayerForWeb/>
- **Repository:** <https://github.com/cri-middleware/SSPlayerForWeb>

## 🧰 Which package? Pick by environment

Each renderer bundles the WASM core, so you install just one.

| Your environment | Package |
|---|---|
| Standalone / no framework (`<ss-player>` Web Component) | **`ssplayer-webgl`** |
| PixiJS v8 app | **`ssplayer-pixi`** |
| Building your own renderer | **`ssplayer-core`** |
| Converting `.sspj` -> `.ssab` | **`ssconverter-web`** (Web tool + Node CLI) |
| Embedding conversion in your own app / service | **`ssconverter-core`** |

**Game-engine integrations** - thin adapters on top of `ssplayer-webgl`, both 🧪 experimental
(alpha, not yet on npm):

| Your environment | Package |
|---|---|
| RPG Maker MZ (PixiJS v5) | **`ssplayer-rmmz`** |
| TyranoScript / TyranoBuilder | **`ssplayer-tyrano`** |

See [Choose Your Platform](../overview/choose-your-platform.md) to compare players, or
[SDK Concepts](../sdk/concepts.md) for the conversion/playback pipeline shared across all of them.

# 🌐 SSPlayerForWeb

A **collection of Web players** for SpriteStudio 7 animations in the browser, sharing one
WebAssembly core (`@spritestudio/ssplayer-core`, built on `libssruntime`). Author your sprite
art in SpriteStudio, convert to `.ssab`, then play it back through the renderer of your choice.

- **Documentation:** _coming soon_
- **Repository:** <https://github.com/cri-middleware/SSPlayerForWeb>

▶️ See the players running live: [Try it in your browser](../overview/try-it.md).

## 🧰 Which package? Pick by environment

**Playback** - each renderer bundles the WASM core, so you install just one.

| Your environment | Package |
|---|---|
| Standalone / no framework (`<ss-player>` Web Component) | **`@spritestudio/ssplayer-webgl`** |
| PixiJS v8 app | **`@spritestudio/ssplayer-pixi`** |
| Building your own renderer | **`@spritestudio/ssplayer-core`** |

**Conversion** - turns `.sspj` into runtime assets; picked separately from the playback package.

| Your environment | Package |
|---|---|
| Converting `.sspj` -> `.ssab` | **`ssconverter-web`** (Web tool + Node CLI) |
| Embedding conversion in your own app / service | **`@spritestudio/ssconverter-core`** |

**Game-engine integrations** - thin adapters on top of `@spritestudio/ssplayer-webgl`, both
🧪 experimental (alpha, not yet on npm):

| Your environment | Package |
|---|---|
| RPG Maker MZ (PixiJS v5) | **`@spritestudio/ssplayer-rmmz`** |
| TyranoScript / TyranoBuilder | **`@spritestudio/ssplayer-tyrano`** |

See [Choose Your Platform](../overview/choose-your-platform.md) to compare players, or
[SDK Concepts](../sdk/concepts.md) for the conversion/playback pipeline shared across all of them.

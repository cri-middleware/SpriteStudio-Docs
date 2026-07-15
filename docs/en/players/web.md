# 🌐 SSPlayerForWeb

A **collection of Web players** for SpriteStudio 7 animations in the browser, sharing one
WebAssembly core (`@spritestudio/ssplayer-core`, built on `libssruntime`). Author your sprite
art in SpriteStudio, convert to `.ssab`, then play it back through the renderer of your choice.

- **Documentation:** <https://cri-middleware.github.io/SSPlayerForWeb/>
- **Repository:** <https://github.com/cri-middleware/SSPlayerForWeb>

▶️ See the players running live: [Try it in your browser](../overview/try-it.md).

## 🧰 Which package? Pick by environment

**Playback** - each renderer bundles the WASM core, so you install just one.

| Your environment | Package |
|---|---|
| Standalone / no framework (`<ss-player>` Web Component) | **[`@spritestudio/ssplayer-webgl`](https://cri-middleware.github.io/SSPlayerForWeb/usage/webgl)** |
| PixiJS v8 app | **[`@spritestudio/ssplayer-pixi`](https://cri-middleware.github.io/SSPlayerForWeb/usage/pixi)** |
| Building your own renderer | **[`@spritestudio/ssplayer-core`](https://cri-middleware.github.io/SSPlayerForWeb/setup/install)** |

**Conversion** - turns `.sspj` into runtime assets; picked separately from the playback package.

| Your environment | Package |
|---|---|
| Converting `.sspj` -> `.ssab` | **[`ssconverter-web`](https://cri-middleware.github.io/SSPlayerForWeb/usage/assets)** (Web tool + Node CLI) |
| Embedding conversion in your own app / service | **[`@spritestudio/ssconverter-core`](https://cri-middleware.github.io/SSPlayerForWeb/usage/assets)** |

**Game-engine integrations** - thin adapters on top of `@spritestudio/ssplayer-webgl`, both
🧪 experimental (alpha, not yet on npm):

| Your environment | Package |
|---|---|
| RPG Maker MZ (PixiJS v5) | **[`@spritestudio/ssplayer-rmmz`](https://cri-middleware.github.io/SSPlayerForWeb/usage/rmmz)** |
| TyranoScript / TyranoBuilder | **[`@spritestudio/ssplayer-tyrano`](https://cri-middleware.github.io/SSPlayerForWeb/usage/tyrano)** |

See [Choose Your Platform](../overview/choose-your-platform.md) to compare players, or
[SDK Concepts](../sdk/concepts.md) for the conversion/playback pipeline shared across all of them.

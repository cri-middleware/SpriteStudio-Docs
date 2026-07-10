# SSPlayerForWeb

A **collection of Web players** for SpriteStudio 7 animations in the browser, sharing one
WebAssembly core (`ssplayer-core`, built on `libssruntime`). Author your sprite art in
SpriteStudio, convert to `.ssab`, then play it back through the renderer of your choice.

- **Documentation:** <https://cri-middleware.github.io/SSPlayerForWeb/>
- **Repository:** <https://github.com/cri-middleware/SSPlayerForWeb>

## Players in the collection

| Package | What it is |
|---|---|
| **`ssplayer-pixi`** | PixiJS renderer — the recommended integration. |
| **`ssplayer-webgl`** | Standalone WebGL player exposed as the `<ss-player>` Web Component. |
| **`ssplayer-tyrano`** | TyranoScript integration. |
| **`ssplayer-rmmz`** | RPG Maker MZ integration — 🚧 planned, not yet implemented. |
| **`ssconverter-web`** | Browser front-end that converts `.sspj` → `.ssab` entirely client-side. |

See [Choose Your Platform](../overview/choose-your-platform.md) to compare players, or
[SDK Concepts](../sdk/concepts.md) for the conversion/playback pipeline shared across all of them.

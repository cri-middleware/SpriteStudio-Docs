# 🌐 SSPlayerForWeb

A **collection of Web players** for SpriteStudio 7 animations in the browser, sharing one
WebAssembly core (`@spritestudio/ssplayer-core`, built on `libssruntime`). Author your sprite
art in SpriteStudio, convert to `.ssab`, then play it back through the renderer of your choice.

- **Documentation:** _coming soon_
- **Repository:** <https://github.com/cri-middleware/SSPlayerForWeb>

▶️ See the players running live: [Try it in your browser](../overview/try-it.md).

## 🧰 Which package? Pick by environment

**Playback** - each renderer bundles the WASM core, so you install just one. All three are on npm.

| Your environment | Package |
|---|---|
| Standalone / no framework (`<ss-player>` Web Component) | **`@spritestudio/ssplayer-webgl`** |
| PixiJS v8 app | **`@spritestudio/ssplayer-pixi`** |
| Building your own renderer | **`@spritestudio/ssplayer-core`** |

**Conversion** - turns `.sspj` into runtime assets; picked separately from the playback package.

| Your environment | Use |
|---|---|
| Converting `.sspj` -> `.ssab` | **`ssconverter-web`** - a browser tool hosted on the SSPlayerForWeb site, with a Node CLI alongside it; not an npm package |
| Embedding conversion in your own app / service | **`@spritestudio/ssconverter-core`** - on npm |

**Game-engine integrations** - rendering built on `@spritestudio/ssplayer-webgl`. None of these
is published to npm; each is distributed through the repository's
[GitHub Releases](https://github.com/cri-middleware/SSPlayerForWeb/releases).

| Your environment | Package | Status |
|---|---|---|
| RPG Maker MZ (PixiJS v5) | **`@spritestudio/ssplayer-rmmz`** | 🧪 experimental (alpha) |
| TyranoScript - writing `[ss_*]` tags in a scenario yourself | **`@spritestudio/ssplayer-tyranoscript`** | beta |
| TyranoBuilder - placing animations from the component palette, no scenario code | **`@spritestudio/ssplayer-tyranobuilder`** | beta |

`ssplayer-tyranobuilder` is **author-time tooling** rather than a renderer: it ships the
TyranoScript runtime *and* converts `.sspj` inside the editor, so a TyranoBuilder project needs
neither of the conversion packages above.

See [Choose Your Platform](../overview/choose-your-platform.md) to compare players, or
[SDK Concepts](../sdk/concepts.md) for the conversion/playback pipeline shared across all of them.

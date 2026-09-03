# 🌐 SSPlayerForWeb

A **collection of Web players** for SpriteStudio animations in the browser, sharing one
WebAssembly core (`@spritestudio/ssplayer-core`, built on `libssruntime`). Author your sprite
art in SpriteStudio, convert to `.ssab`, then play it back through the renderer of your choice.

▶️ See the players running live: [Try it in your browser](../overview/try-it.md).

!!! tip "Code-first - and no Rust or WASM toolchain"
    The WASM core ships inside each renderer package, so you install one package and write a few
    lines. Building the core from source is only for changing the Rust.

**1. What you install** - one renderer package, picked by your environment: see
[the table below](#pick-by-environment). Each bundles the WASM core, so it is a
single dependency. 🚧 They are published to npm with the first release; until then, run the
[repository's examples](https://github.com/cri-middleware/SSPlayerForWeb) from a checkout.

**2. `.sspj` -> `.ssab`** - convert in the browser with `ssconverter-web`, hosted on this
player's own site, or with any of the [standalone tools](../overview/convert-with-a-standalone-tool.md).
Conversion is picked separately from playback, so it has its own row in the tables below.

**3. Getting it on screen** - place the element your renderer provides: the framework-free
`<ss-player>` Web Component, or a `SpriteStudio` display object inside a PixiJS v8 app.

## 🧰 Which package? Pick by environment { #pick-by-environment }

**Playback** - each renderer bundles the WASM core, so you install just one.

| Your environment | Package |
|---|---|
| Standalone / no framework (`<ss-player>` Web Component) | **`@spritestudio/ssplayer-webgl`** |
| PixiJS v8 app | **`@spritestudio/ssplayer-pixi`** |
| Building your own renderer | **`@spritestudio/ssplayer-core`** |

**Conversion** - turns `.sspj` into runtime assets; picked separately from the playback package.

| Your environment | Use |
|---|---|
| Converting `.sspj` -> `.ssab` | **`ssconverter-web`** - a browser tool hosted on the SSPlayerForWeb site, with a Node CLI alongside it; not an npm package |
| Embedding conversion in your own app / service | **`@spritestudio/ssconverter-core`** |

**Game-engine integrations** - rendering built on `@spritestudio/ssplayer-webgl`. Unlike the
packages above, these are not headed for npm at all; each is distributed through the repository's
[GitHub Releases](https://github.com/cri-middleware/SSPlayerForWeb/releases).

| Your environment | Package | Status |
|---|---|---|
| RPG Maker MZ (PixiJS v5) | **`@spritestudio/ssplayer-rmmz`** | 🧪 experimental (alpha) |
| TyranoScript - writing `[ss_*]` tags in a scenario yourself | **`@spritestudio/ssplayer-tyranoscript`** | beta |
| TyranoBuilder - placing animations from the component palette, no scenario code | **`@spritestudio/ssplayer-tyranobuilder`** | beta |

`ssplayer-tyranobuilder` is **author-time tooling** rather than a renderer: it ships the
TyranoScript runtime *and* converts `.sspj` inside the editor, so a TyranoBuilder project needs
neither of the conversion packages above.

## ➡️ Read next

- **Documentation** - 🚧 *coming soon*
- [Repository](https://github.com/cri-middleware/SSPlayerForWeb)
- [Try It in Your Browser](../overview/try-it.md) - the live demos and the hosted converter

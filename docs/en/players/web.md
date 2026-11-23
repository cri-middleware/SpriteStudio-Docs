# 🌐 SpriteStudio Player for Web

A **collection of Web players** for SpriteStudio animations in the browser, sharing one
WebAssembly core (`@spritestudio/ssplayer-core`, built on `libssruntime`). Author your sprite
art in SpriteStudio, convert to `.ssab`, then play it back through the renderer of your choice.

▶️ See the players running live: [Try it in your browser](../overview/try-it.md).

!!! tip "Code-first for the npm packages - no code in RPG Maker MZ, TyranoScript or TyranoBuilder"
    The npm packages bundle the WASM core, so you install one and write a few lines. The three
    game-engine plugins are set up in their editors, with no code.

**1. What you install** - one renderer package from npm, picked by your environment: see
[the table below](#pick-by-environment). Each bundles the WASM core, so it is a
single dependency. RPG Maker MZ, TyranoScript and TyranoBuilder take a plugin from GitHub
Releases instead.

**2. `.sspj` -> `.ssab`** - the RPG Maker MZ and TyranoBuilder plugins convert on their own: MZ
when a test play starts, TyranoBuilder as the project opens. Anywhere else, convert in the browser
with [`ssconverter-web`](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/), hosted on
this player's own site, or with any of the [standalone tools](../overview/convert-with-a-standalone-tool.md).
Conversion is picked separately from playback, so it has its own table below.

**3. Getting it on screen** - place the element your renderer provides: the framework-free
`<ss-player>` Web Component, or an `SSPlayer` - a PixiJS `Container` - inside a PixiJS app. In
RPG Maker MZ it is the **Show SS** plugin command, in TyranoScript an `[ss_new]` tag, and in
TyranoBuilder the **SpriteStudio: show** component.

The steps, with the folders they use, are in each package's README, linked from the README's
[package table](https://github.com/cri-middleware/SSPlayerForWeb#-which-package-should-i-use).

## 🧰 Which package? Pick by environment { #pick-by-environment }

**Playback** - each renderer bundles the WASM core, so you install just one.

| Your environment | Package |
|---|---|
| Standalone / no framework (`<ss-player>` Web Component) | **`@spritestudio/ssplayer-webgl`** |
| PixiJS app | **`@spritestudio/ssplayer-pixi`** |
| PixiJS app with [`@pixi/ui`](https://github.com/pixijs/ui) buttons drawn by animations | **`@spritestudio/ssplayer-pixi-ui`** (brings `ssplayer-pixi` with it) |
| Building your own renderer | **`@spritestudio/ssplayer-core`** |

**Conversion** - turns `.sspj` into runtime assets; picked separately from the playback package.

| Your environment | Use |
|---|---|
| Converting `.sspj` -> `.ssab` | **`ssconverter-web`** - a browser tool hosted on the SpriteStudio Player for Web site; not an npm package |
| Embedding conversion in your own app / service | **`@spritestudio/ssconverter-core`** |

**Game-engine integrations** - plugins rather than npm packages: each is a file under **Assets**
on that plugin's GitHub Release.

| Your environment | Download |
|---|---|
| RPG Maker MZ | **`ssplayer-rmmz-plugin-<version>.zip`** from the [`@spritestudio/ssplayer-rmmz` Release](https://github.com/cri-middleware/SSPlayerForWeb/releases?q=ssplayer-rmmz&expanded=true) |
| TyranoScript - writing `[ss_*]` tags in a scenario yourself | **`ssplayer-tyranoscript-plugin-<version>.zip`** from the [`@spritestudio/ssplayer-tyranoscript` Release](https://github.com/cri-middleware/SSPlayerForWeb/releases?q=ssplayer-tyranoscript&expanded=true) |
| TyranoBuilder - placing animations from the component palette, no scenario code | **`ssplayer.tbp`** from the [`@spritestudio/ssplayer-tyranobuilder` Release](https://github.com/cri-middleware/SSPlayerForWeb/releases?q=ssplayer-tyranobuilder&expanded=true) |

The MZ and TyranoBuilder plugins convert `.sspj` themselves (step 2), so an MZ or TyranoBuilder
project needs neither of the conversion rows above. `ssplayer.tbp` is the only download a TyranoBuilder
project needs: it already holds the TyranoScript plugin.

## ➡️ Read next

- [Documentation](https://cri-middleware.github.io/SSPlayerForWeb/)
- [Repository](https://github.com/cri-middleware/SSPlayerForWeb)
- [Try It in Your Browser](../overview/try-it.md) - the live demos and the hosted converter

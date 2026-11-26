---
description: "Play SpriteStudio animations and convert a project in your browser, with nothing to install. SpriteStudio adds bones, mesh and effects to 2D illustrations."
---

# ▶️ Try It in Your Browser

See SpriteStudio conversion and playback running live - **no install, nothing to set up**.
Everything here runs entirely in your browser. Each item is hosted on its player's own
site; this page just gathers the links.

## 🔄 Convert in your browser

| Tool | What it does |
|---|---|
| [ssconverter-web](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/) | Converts your `.sspj` into `.ssab` right in the browser: the whole pipeline runs locally on WebAssembly, so nothing is ever uploaded to a server. |

For the step-by-step walkthrough (and the desktop / CLI alternatives), see [Converting with a Standalone Tool](./convert-with-a-standalone-tool.md).

## 🎮 Live player demos

### [SpriteStudio Player for Web](../players/web.md)

| Demo | Package | What it shows |
|---|---|---|
| [PixiJS demo](https://cri-middleware.github.io/SSPlayerForWeb/examples/pixi/) | `@spritestudio/ssplayer-pixi` | A `.ssab` animation in a PixiJS app - **drag & drop a directory of `.ssab` + `.png` files** to preview your own. |
| [WebGL demo](https://cri-middleware.github.io/SSPlayerForWeb/examples/webgl/) | `@spritestudio/ssplayer-webgl` | The framework-free WebGL renderer - **drop a directory of `.ssab` + `.png`** to preview your own. |
| [Part override demo](https://cri-middleware.github.io/SSPlayerForWeb/examples/override/) | `@spritestudio/ssplayer-pixi` | Per-part color, visibility and cell changes on the Ringo sample while it plays - see [Changing a Character at Runtime](./runtime-changes.md). |
| [PixiJS UI demo](https://cri-middleware.github.io/SSPlayerForWeb/examples/pixi/ui.html) | `@spritestudio/ssplayer-pixi-ui` | Two `@pixi/ui` buttons drawn by the Ringo sample - see [UI Integration](./ui-integration.md). |
| [Motion blending demo](https://cri-middleware.github.io/SSPlayerForWeb/examples/pixi/blend.html) | `@spritestudio/ssplayer-pixi` | Crossfades, an additive overlay and a second track on one character - see [Motion Blending](./motion-blending.md). |
| [RPG Maker MZ demo](https://cri-middleware.github.io/SSPlayerForWeb/examples/rmmz/) | `@spritestudio/ssplayer-rmmz` | A sample MZ project with SpriteStudio animations in correct Z-order. |
| [TyranoScript demo](https://cri-middleware.github.io/SSPlayerForWeb/examples/tyranoscript/) | `@spritestudio/ssplayer-tyranoscript` | SpriteStudio animations in a TyranoScript visual novel, driven by `[ss_*]` tags. |

### [SpriteStudio Player for Flutter](../players/flutter.md)

| Demo | Package | What it shows |
|---|---|---|
| [Flutter demo](https://cri-middleware.github.io/SSPlayerForFlutter/demo/flutter/) | `ssplayer_flutter` | The `SpriteStudioView` widget in a Flutter web build. |
| [Flame demo](https://cri-middleware.github.io/SSPlayerForFlutter/demo/flame/) | `ssplayer_flame` | The same playback as a `SpriteStudioComponent`, driven by a Flame game loop. |

These demos run on that player's Web target.

### [SpriteStudio Player for Ren'Py](../players/renpy.md)

| Demo | What it shows |
|---|---|
| [Ren'Py demo](https://cri-middleware.github.io/SSPlayerForRenPy/demo/) | Bundled SpriteStudio animations running in Ren'Py Web. |

### [SpriteStudio Player for wgpu](../players/wgpu.md)

| Demo | Package | What it shows |
|---|---|---|
| [WebGPU demo](https://cri-middleware.github.io/SSPlayerForWgpu/demo/) | `@spritestudio/ssplayer-wgpu` | The JavaScript API and the `<ss-player-webgpu>` custom element - **drop a directory of `.ssab` + `.png`** to preview your own. |

It needs a browser that supports WebGPU.

## 📂 Preview your own animation

The PixiJS, WebGL and WebGPU demos take a dropped folder
of `.ssab` + `.png` (the PixiJS and WebGL demos also take a single embedded `.ssab`), so convert your `.sspj` first - with the browser converter above, or any of the
[standalone tools](./convert-with-a-standalone-tool.md).
[Converting Assets](./conversion.md) walks the whole path. If you don't have a project of your
own yet, the free [sample data](https://www.webtech.co.jp/help/ja/spritestudio7/download/sample/) works
as-is (Help Center page, in Japanese).

## ➡️ Next

[Choose Your Platform](./choose-your-platform.md) matches your engine to its player, with the install
and first-frame steps.

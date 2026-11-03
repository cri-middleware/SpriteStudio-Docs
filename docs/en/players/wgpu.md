# 🦀 SpriteStudio Player for wgpu

A player for SpriteStudio animations, written in **Rust** and rendering through
[wgpu](https://wgpu.rs/): wgpu puts WebGPU, Vulkan, DX12 and Metal behind one API, so the same
player runs on any of them. The host does not have to be Rust - C, C++ and the browser are
served from the same library.

▶️ See it first, no install: the WebGPU demo runs in a browser -
[Try it in your browser](../overview/try-it.md).

!!! tip "Code-first - and one library behind four faces"
    Which face you install decides the language you write - and whether the player can draw into
    a render pass of your own, which is a Rust-side feature. The C and JavaScript faces wrap the
    Rust API under different names, and the Bevy adapter builds on it.

**1. What you install** - pick the face that matches your host.

| Your host | What you add |
|---|---|
| A **Rust** app | `ssplayer-wgpu` as a git dependency - Cargo also checks out the SpriteStudio-SDK submodule it builds against, and no other tooling is needed. |
| A **Bevy** app | `ssplayer-bevy` instead - it pulls the player in and adds the `SsPlayer` / `SsTransform` / `SsPlayback` components. |
| A **C or C++** app | A cdylib / staticlib plus a generated header: prebuilt for Windows and macOS as `ssplayer-wgpu-<platform>-<arch>.zip` on [GitHub Releases](https://github.com/cri-middleware/SSPlayerForWgpu/releases?q=ssplayer-wgpu&expanded=true), or - on Linux, or for the Windows DLL - built from a checkout with `scripts/build.sh` into `bin/`. |
| The **browser** (WebGPU) | The npm package `@spritestudio/ssplayer-wgpu` - the wasm plus a TypeScript layer, with the `<ss-player-webgpu>` custom element in its own entry point. |

**2. `.sspj` -> `.ssab`** - nothing here hosts an importer and nothing converts at runtime, so
this is a host-side step with the browser's [`ssconverter-web`](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/),
the desktop [SSConverter GUI](./converter.md) or the SDK's `ssconverter-cli` - see
[Converting Assets](../overview/conversion.md).

**3. Getting it on screen** - one `SSRenderer` per device, one `SSScene` per render target, and
any number of `SSPlayer`s drawn into it in one pass, inside a render pass the host opened.

The C and JavaScript faces carry the same calls under their own names, with one structural
difference: they build and own their device rather than drawing into a pass of yours (below). In
a Bevy app the adapter does this for you: you spawn the three components and characters go into
Bevy's own 2D pass.

The steps for each face are in the README's [Installation](https://github.com/cri-middleware/SSPlayerForWgpu#-installation).

## 🔩 Which faces borrow your device

The decision that shapes this player is the **borrow model**: the Rust API does not own the wgpu
`Device` / `Queue` / `Surface`. The host owns them and lends them per frame - which is why the
scene above draws inside a render pass the host opened. So the player rides along inside any wgpu
application, your own renderer or an engine that already has a device of its own, without
locking you into one.

**The C and browser faces do not borrow.** wgpu's types have no stable C representation, so there
is nothing to hand across that boundary: the C face builds and owns a device on the window handle
you give it, and the browser face creates its own device and a surface per canvas. Both draw
frames of their own rather than into a pass of yours, so compositing a character into your pass
is a Rust-side feature - directly or through an engine adapter. From C a scene draws only to the
window or layer it was created on, so the route is a window or layer of the player's own (a child
window, or a `CAMetalLayer` placed in your layer tree), not your pass or a texture.

The borrow model is also what keeps the **Bevy** adapter small: the adapter draws on the device
Bevy already owns, so characters go into Bevy's own 2D pass rather than through a second
renderer. It follows Bevy's release line rather than the player's, tracking one line at a time -
because Bevy and the player have to resolve to a single `wgpu`, a mismatch is a compile error
rather than a runtime surprise. The repository names which line, along with the camera settings
a Bevy app needs.

## ➡️ Read next

- [Documentation](https://cri-middleware.github.io/SSPlayerForWgpu/)
- [Repository](https://github.com/cri-middleware/SSPlayerForWgpu)
- [Converting with a Standalone Tool](../overview/convert-with-a-standalone-tool.md) - picking a tool and putting it in a build pipeline

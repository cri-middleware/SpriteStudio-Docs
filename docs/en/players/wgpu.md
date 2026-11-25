# 🦀 SpriteStudio Player for wgpu

A player for SpriteStudio animations, written in **Rust** and rendering through
[wgpu](https://wgpu.rs/): wgpu puts WebGPU, Vulkan, DX12 and Metal behind one API, so the same
player runs on any of them. The host does not have to be Rust - C, C++ and the browser are
served from the same library.

▶️ See it first, no install: the WebGPU demo runs in a browser -
[Try it in your browser](../overview/try-it.md).

!!! tip "Code-first - and one library behind four faces"
    Which face you install decides the language you write. The C and JavaScript faces wrap the
    Rust API under different names, and the Bevy adapter builds on it.

**1. What you install** - pick the face that matches your host.

| Your host | What you add |
|---|---|
| A **Rust** app | `cargo add ssplayer-wgpu` - or, for changes not released yet, a git dependency on the repository; Cargo also checks out the SpriteStudio-SDK submodule it builds against. |
| A **Bevy** app | `cargo add ssplayer-bevy` instead (or the same as a git dependency) - it pulls the player in and adds the `SsPlayer` / `SsTransform` / `SsPlayback` components. |
| A **C or C++** app | A cdylib / staticlib plus a generated header: prebuilt for Windows and macOS as `ssplayer-wgpu-<platform>-<arch>.zip` on [GitHub Releases](https://github.com/cri-middleware/SSPlayerForWgpu/releases?expanded=true), or - on Linux, or for the Windows DLL - built from a checkout with `scripts/build.sh` into `bin/`. |
| The **browser** (WebGPU) | The npm package `@spritestudio/ssplayer-wgpu` - the wasm plus a TypeScript layer, with the `<ss-player-webgpu>` custom element in its own entry point. |

**2. `.sspj` -> `.ssab`** - nothing here hosts an importer and nothing converts at runtime, so
this is a host-side step with the browser's [`ssconverter-web`](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/),
the desktop [SSConverter GUI](./converter.md) or the SDK's `ssconverter-cli` - see
[Converting Assets](../overview/conversion.md).

**3. Getting it on screen** - one `SSRenderer` per device, one `SSScene` per render target, and
any number of `SSPlayer`s drawn into it in one pass, inside a render pass the host opened.

In a Bevy app the adapter does this for you: you spawn the three components and characters go
into Bevy's own 2D pass.

The steps for each face are in the README's [Installation](https://github.com/cri-middleware/SSPlayerForWgpu#-installation).

## 🔩 Drawing into your own render pass

The C and browser faces create their own device and draw frames of their own, so drawing a
character into a render pass of yours is Rust-only - directly, or through the Bevy adapter, which
tracks one Bevy release line at a time. [The borrow model](https://cri-middleware.github.io/SSPlayerForWgpu/wgpu/borrow-model/)
has the reasoning.

## ➡️ Read next

- [Documentation](https://cri-middleware.github.io/SSPlayerForWgpu/)
- [Repository](https://github.com/cri-middleware/SSPlayerForWgpu)
- [Converting with a Standalone Tool](../overview/convert-with-a-standalone-tool.md) - picking a tool and putting it in a build pipeline

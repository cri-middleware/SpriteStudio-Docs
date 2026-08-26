# 🦀 SSPlayerForWgpu

A player for SpriteStudio 7 animations, written in **Rust** and rendering through
[wgpu](https://wgpu.rs/): wgpu puts WebGPU, Vulkan, DX12 and Metal behind one API, so the same
player runs on any of them. The host does not have to be Rust - C, C++ and the browser are
served from the same library.

- **Documentation:** _coming soon_
- **Repository:** <https://github.com/cri-middleware/SSPlayerForWgpu>

The decision that shapes it is the **borrow model**: the player does not own the wgpu
`Device` / `Queue` / `Surface`. The host owns them and lends them per frame, so the player can
ride along inside any wgpu application - your own renderer, or a game engine that already has a
device of its own - without locking you into one.

One library carries three faces over that same core:

- **Rust** - `SSRenderer` / `SSScene` / `SSPlayer`, the API the other two wrap.
- **C and C++** - a cdylib / staticlib plus a generated header, with Metal, DX12 and Vulkan
  viewers as samples.
- **WebGPU in the browser** - an npm package carrying the wasm, with a `<ss-player-webgpu>`
  custom element over it.

**Bevy** is served by a fourth route, a separate crate over the Rust face
(`ssplayer-wgpu-bevy`). The borrow model is what makes it small: the adapter draws on the device
Bevy already owns, so characters go into Bevy's own 2D pass rather than through a second renderer.
It follows Bevy's release line rather than the player's, tracking one line at a time - the
repository names which, along with the camera settings a Bevy app needs.

Nothing here hosts an importer, so converting `.sspj` to `.ssab` is a host-side step with one of
the standalone tools - see [Converting Assets](../overview/conversion.md).

See [Choose Your Platform](../overview/choose-your-platform.md) to compare players, or
[SDK Concepts](../sdk/concepts.md) for the conversion/playback pipeline shared across all of them.

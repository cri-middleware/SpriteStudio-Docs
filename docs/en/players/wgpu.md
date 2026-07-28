# 🦀 SSPlayerForWgpu

A **Rust** player for SpriteStudio 7 animations, rendering through
[wgpu](https://wgpu.rs/) - so one code path covers WebGPU, Vulkan, DX12, Metal, and GL.

!!! info "In development"
    This player has not shipped yet. This page exists so the portal has an entry for it; the
    details will be filled in as it lands.

- **Documentation:** _coming soon_
- **Repository:** <https://github.com/cri-middleware/SSPlayerForWgpu>

The decision that shapes it is the **borrow model**: the player does not own the wgpu
`Device` / `Queue` / `Surface`. The host owns them and lends them per frame, so the player can
ride along inside any wgpu application - your own renderer or another engine - without locking
you into one.

See [Choose Your Platform](../overview/choose-your-platform.md) to compare players, or
[SDK Concepts](../sdk/concepts.md) for the conversion/playback pipeline shared across all of them.

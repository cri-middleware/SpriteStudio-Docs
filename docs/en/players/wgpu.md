# 🦀 SSPlayerForWgpu

A player for SpriteStudio animations, written in **Rust** and rendering through
[wgpu](https://wgpu.rs/): wgpu puts WebGPU, Vulkan, DX12 and Metal behind one API, so the same
player runs on any of them. The host does not have to be Rust - C, C++ and the browser are
served from the same library.

!!! tip "Code-first - and one library behind three faces"
    Which face you install decides the language you write, not what the player can do. The Rust
    API is the one the other two wrap, under different names.

**1. What you install** - pick the face that matches your host. While
[SpriteStudio-SDK](https://github.com/cri-middleware/SpriteStudio-SDK) is private, every route
below needs access to it: the player links `ssruntime` and `ssab` as Rust crates rather than
through a released C-API, so the SDK comes in as a git submodule.

| Your host | What you add |
|---|---|
| A **Rust** app | `ssplayer-wgpu` as a git dependency - Cargo checks out the submodule for you, and no other tooling is needed. 🚧 Not on crates.io until the SDK crates publish first. |
| A **Bevy** app | `ssplayer-wgpu-bevy` instead - it pulls the player in and adds the `SsPlayer` / `SsTransform` / `SsPlayback` components. |
| A **C or C++** app | A cdylib / staticlib plus a generated header, built from the repository with `scripts/build.sh` into `bin/`. 🚧 No prebuilt downloads yet. |
| The **browser** (WebGPU) | The npm package `@spritestudio/ssplayer-wgpu` - the wasm plus a TypeScript layer, with the `<ss-player-webgpu>` custom element in its own entry point. 🚧 Not on npm yet. |

**2. `.sspj` -> `.ssab`** - nothing here hosts an importer and nothing converts at runtime, so
this is a host-side step with the desktop [SSConverterGUI](./converter.md) or the SDK's
`ssconverter-cli` - see [Converting Assets](../overview/conversion.md). Nothing of your own is
needed to try the player first: the bundled samples run on the SDK's own test animations.

**3. Getting it on screen** - one `SSRenderer` per device, one `SSScene` per render target, and
any number of `SSPlayer`s drawn into it in one pass:

```rust
let mut renderer = SSRenderer::new(&device);
let mut scene = SSScene::new(&device, &SceneConfig { color_format, stencil_format });

let mut player = SSPlayer::new();
player.load("assets/overall/Basic.ssab")?;   // pack, atlases and sibling packs, in one call
player.set_animation("Basic")?;
player.play();

scene.update(&mut renderer, &device, &queue, delta_secs, &mut [&mut player]);
scene.draw(&renderer, &mut rpass);           // into a pass the host opened
```

The C and JavaScript faces are the same shape under different names. In a Bevy app the adapter
does this for you: you spawn the three components and characters go into Bevy's own 2D pass.

## 🔩 Why the host keeps its device

The decision that shapes this player is the **borrow model**: it does not own the wgpu
`Device` / `Queue` / `Surface`. The host owns them and lends them per frame - which is what
`scene.draw` into a pass *you* opened means above. So the player rides along inside any wgpu
application, your own renderer or an engine that already has a device of its own, without
locking you into one.

It is also what keeps the **Bevy** adapter small: the adapter draws on the device Bevy already
owns, so characters go into Bevy's own 2D pass rather than through a second renderer. It
follows Bevy's release line rather than the player's, tracking one line at a time - because
Bevy and the player have to resolve to a single `wgpu`, a mismatch is a compile error rather
than a runtime surprise. The repository names which line, along with the camera settings a
Bevy app needs.

## ➡️ Read next

- **Documentation** - 🚧 *coming soon*
- [Repository](https://github.com/cri-middleware/SSPlayerForWgpu) - the crate READMEs are the reference until then
- [Converting Assets](../overview/conversion.md) - picking a tool and putting it in a build pipeline

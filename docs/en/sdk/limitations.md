# ⚠️ Shared Limitations

Everything on this page comes from the **shared core** (`libssruntime` / `libssab`), so it
applies to **every official player** regardless of engine. Each player's own docs list only what
is specific to it - for those differences see [Feature Support](../overview/feature-support.md).

!!! tip "Source of truth"
    The canonical, implementation-level list lives in the SDK's Player Porting Guide
    ([`libs/ssruntime/docs`](https://github.com/cri-middleware/SpriteStudio-SDK/tree/main/libs/ssruntime/docs),
    *Introduction → Limitations*). This page is the user-facing summary.

## 🎬 Playback & timeline

### `independent = true` parts do not reverse or seek correctly

An Instance or Effect part authored with `independent = true` runs on its **own real-time clock**,
detached from the parent timeline. The parent's **reverse playback** and **seeking** therefore
break it - a real-time clock cannot run backwards, and there is no single correct "elapsed time"
for an arbitrary past frame. Forward playback, including forward frame skips, is correct.

**What to do:** prefer authoring without `independent = true` for animations you may play in
reverse or seek. If you must use it, tell your users that those children are only correct during
forward playback.

### Seeking does not fire the events it skips over

Jumping the playhead directly (setting the frame) emits only the **destination frame's**
`UserData` / `Signal` / `Audio` events - every event on the frames passed over is skipped.

**What to do:** if you need every intermediate event, advance the animation step by step
(repeated `update()`) instead of jumping.

### Audio never plays in reverse

Sound events fire only while the animation advances **forward** in time. When the effective
direction is backward - reverse direction, the return leg of ping-pong, or a negative speed -
audio events are skipped. Reverse audio is not something the common audio backends provide.

### Animation blending is single-`.ssab` only

Weighted blending / crossfade between animations has two hard constraints:

- **Same `.ssab`.** Blending across resources is not supported.
- **Same cell per part.** Every blended animation must assign the *same* cell to the *same*
  part; the cell metadata is taken from the primary source, so a mismatch produces size / pivot
  errors that visibly break the pose. Animations inside one `.ssae` normally satisfy this.

Two secondary behaviors are worth knowing: for parts that carry `parts_color`, the visible alpha
comes from the **primary** source rather than the blended value; and by default only the primary
source fires events (each source has an event threshold).

### Sequence (`.ssqe` / `.ssqb`) playback is not implemented yet

Conversion already produces `.ssqb`, but runtime playback of sequences is still on the
[SDK roadmap](https://github.com/cri-middleware/SpriteStudio-SDK/blob/main/ROADMAP.md) - it lands
with the runtime state machine.

## 🧩 What the runtime does *not* draw for you

`libssruntime` computes animation **state**; two features are deliberately left to the player,
because they need the host engine:

| Feature | The runtime provides | The player must implement |
|---|---|---|
| **Text parts** | Glyph layout (bitmap position, size, texture reference) | Drawing the glyphs |
| **Audio** | The play event (file name, exact timing) | Actual sound playback via the engine's audio system |

So whether text parts render, and whether sounds are audible, is a **per-player** property -
check [Feature Support](../overview/feature-support.md).

## 🌐 Browsers require WebAssembly SIMD

The WASM build of the runtime uses **WebAssembly SIMD** instructions and **will not run on
browsers without SIMD support**. This applies to every browser-facing target: the Web players,
Godot's Web export, Flutter Web, and Ren'Py Web.

**What to do:** treat WebAssembly SIMD as a browser requirement for your distribution.

## 🔐 `.ssab` input is not validated

For maximum performance and minimum binary size (embedded / WASM targets), the runtime performs
**no structural validation** of the `.ssab` it loads. A corrupted or maliciously crafted asset
can cause out-of-bounds access, undefined behavior, or a crash.

**What to do:** load only assets you trust. If your product loads `.ssab` dynamically - over the
network, or from user input - validate it beforehand on your side, or restrict loading to assets
you ship.

## 📦 Embedded-mode `.ssab`

`.ssab` can be generated in *embedded* mode, which packs the referenced assets into the binary
itself. Two constraints follow:

- **Asset paths are the key.** Embedding is keyed by the asset file paths recorded in the `.sspj`
  / `ss*e` files, so duplicated paths within a project **collide**. Keep asset paths unique.
- **Only the assets that pack actually uses are embedded.** The body of another `.ssab`
  referenced as an *external instance* is not included - ship those referenced `.ssab` files
  alongside.

## ➡️ Next

- [Feature Support](../overview/feature-support.md) - what differs between players.
- [SDK Concepts](./concepts.md) - the convert -> playback pipeline these constraints come from.
- [Support](../support.md) - where to report something that is *not* on this page.

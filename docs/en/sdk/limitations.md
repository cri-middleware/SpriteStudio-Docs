# ⚠️ Shared Limitations

Everything on this page comes from the **shared core** (`libssruntime` / `libssab`), so it
applies to **every official player** regardless of engine. Each player's own docs list only what
is specific to it - for those differences see [Player Differences](../overview/player-differences.md).

!!! tip "Source of truth"
    The canonical, implementation-level list lives in the SDK's Player Porting Guide
    (🚧 [`20_limitations.md`](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/libs/ssruntime/docs/10_introduction/20_limitations.md) -
    the guide's own table of contents is 🚧 [`README.md`](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/libs/ssruntime/docs/README.md)).
    This page is the user-facing summary.

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
direction is backward - a reverse direction, or the return leg of ping-pong - audio events are
skipped. Reverse audio is not something the common audio backends provide.

A negative playback speed is **not** one of those cases: speed is a multiplier, and a negative
one stops the playhead rather than turning it around. Reverse is the playback direction's job.
A speed of `0` stops it too.

### Animation mixing is single-`.ssab` only

Animations are stacked on **tracks** - track 0 first, each further track mixed in on top of it.
Stacking has two hard constraints:

- **Same `.ssab`.** Mixing across resources is not supported.
- **Same cell per part.** Every stacked animation must assign the *same* cell to the *same*
  part; the cell metadata is taken from **track 0**, so a mismatch produces size / pivot
  errors that visibly break the pose. Animations inside one `.ssae` normally satisfy this.

Three secondary behaviors are worth knowing: for parts that carry `parts_color`, the visible
alpha comes from **track 0** rather than the mixed value; by default only a track's
fully-weighted animation fires events (each source has an event threshold, and track 0's
animation always fires); and sources of different lengths run on independent clocks, so keeping
them in step is the player's job.

### Sequence (`.ssqe` / `.ssqb`) playback is not implemented yet

Conversion already produces `.ssqb`, but runtime playback of sequences is still on the
🚧 [SDK roadmap](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/ROADMAP.md) - it lands
with the runtime state machine.

## 🧩 What the player must supply

`libssruntime` computes animation **state**; two features are deliberately left to the player,
because they need the host engine:

| Feature | The runtime provides | The player must implement |
|---|---|---|
| **Text parts** | The authored text, plus the glyph atlas for a bitmap-font project. Text also keeps its slot in the draw plan, so it composites by priority alongside every other part | Glyph layout, rasterization for outline fonts, and the draw call - through the host engine's text stack |
| **Audio** | The play event (file name, exact timing) | Actual sound playback via the engine's audio system |

A text part authored as a **mask** is the exception: it is left out of the draw plan entirely,
because the runtime has no glyphs with which to write coverage.

### Text and 9-slice parts are not drawn by any player yet

Two part types reach the player intact but have no implementation in **any** official player at
present. This is not a difference between engines - it is uniform:

- **Text parts** - the runtime supplies the authored string, the bitmap glyph atlas, and the
  part's slot in the draw plan. No player draws the glyphs yet.
- **9-slice parts** - the runtime builds the entire grid into dedicated buffers (`Nines` batches),
  ready to upload. No player reads those buffers yet, so the part renders as nothing rather than
  as a stretched cell.

Both keep their place in the draw order, so an animation that uses them plays with those parts
missing rather than failing.

**What to do:** replace them with ordinary parts at authoring time for anything you ship today.

## 🖌️ Rendering constraints

### 9-slice parts ignore UV animation and rotated cells

The **UV animation attributes** and **cells rotated inside their cellmap** do not apply to
9-slice parts. The grid is built from the cell rectangle alone, matching what the authoring tool
does.

### Destination-sampling blend modes assume opaque pixels underneath

`Mul`, `Sub`, `Screen`, `Exclusion`, and `Invert` read the pixels they are drawn over, so they
match the editor only where those pixels are **opaque** - the case SpriteStudio itself assumes.

**What to do:** give a blend-heavy animation an opaque background layer if exact parity with the
editor matters.

Which blend modes a given engine can reproduce *at all* is a separate, per-player question - see
[Player Differences](../overview/player-differences.md).

## 📦 Shipping & loading

### A `.ssab` whose schema version differs from the runtime does not load

`.ssab` and `.ssqb` carry their schema version in the binary, and the runtime **fails the load**
of a file whose version is not the one it reads, naming both the version it expected and the one
it got. Nothing is read partially, and an asset built against an older schema does not quietly
keep working.

**What to do:** rebuild your assets with the SDK version your player runs. It is the same reason
the hosted converter is published
[per schema version](../overview/convert-with-a-standalone-tool.md).

### `.ssab` input is not validated

For maximum performance and minimum binary size (embedded / WASM targets), the runtime performs
**no structural validation** of the `.ssab` it loads. A corrupted or maliciously crafted asset
can cause out-of-bounds access, undefined behavior, or a crash.

**What to do:** load only assets you trust. If your product loads `.ssab` dynamically - over the
network, or from user input - validate it beforehand on your side, or restrict loading to assets
you ship.

### Embedded-mode `.ssab` has two constraints

`.ssab` can be generated in *embedded* mode, which packs the referenced assets into the binary
itself. Two constraints follow:

- **Asset paths are the key.** Embedding is keyed by the asset file paths recorded in the `.sspj`
  / `ss*e` files, so duplicated paths within a project **collide**. Keep asset paths unique.
- **Only the assets that pack actually uses are embedded.** The body of another `.ssab`
  referenced as an *external instance* is not included - ship those referenced `.ssab` files
  alongside.

### Browsers require WebAssembly SIMD

The WASM build of the runtime uses **WebAssembly SIMD** instructions and **will not run on
browsers without SIMD support**. This applies to every player's browser-facing target except the
RPG Maker MZ plugin, which ships a runtime build without SIMD.

**What to do:** treat WebAssembly SIMD as a browser requirement for your distribution.

## ➡️ Next

- [Glossary](./glossary.md) - the vocabulary used on this page.
- [Player Differences](../overview/player-differences.md) - what differs between players.
- [SDK Concepts](./concepts.md) - the convert -> playback pipeline these constraints come from.
- [Support](../support.md) - where to report something that is *not* on this page.

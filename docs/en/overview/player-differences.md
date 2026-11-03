# 🧩 Player Differences

Every official player evaluates animations with the **same core**, so the *feature set* is shared
rather than reimplemented per engine - it is listed under
[SDK Concepts](../sdk/concepts.md). What can still differ is:

1. **What the engine's rendering layer can reproduce** - blend modes in particular map onto
   whatever fixed-function blend states the host engine exposes.
2. **What each player's host allows** - its platforms, its own rendering and UI model, and how the
   player ships for it.

This page covers only those differences **between players**. The constraints that apply
*everywhere* - seek and reverse behavior, blending rules, browser requirements, and the features
the core computes but leaves the player to draw or play - are in
[Shared Limitations](../sdk/limitations.md).

## 🔍 Documented per-player differences

| Player | In short | Details |
|---|---|---|
| **[Unity](../players/unity.md)** | The uGUI (Canvas) path carries limits the world path does not | [Limitations & Scope](https://cri-middleware.github.io/SSPlayerForUnity/limitations/) |
| **[Web](../players/web.md)** | `ssplayer-webgl` masks only with a stencil buffer; the framework integrations are beta | [Limitations & Scope](https://cri-middleware.github.io/SSPlayerForWeb/limitations) |
| **[Godot](../players/godot.md)** | Four of the twelve blend modes are honored; the Web export has extra requirements | [Limitations & Scope](https://cri-middleware.github.io/SSPlayerForGodot/limitations/) |
| **[Flutter](../players/flutter.md)** | Two render backends, and the Canvas one costs batching on two blends | [Limitations & Scope](https://cri-middleware.github.io/SSPlayerForFlutter/limitations/) |
| **[Ren'Py](../players/renpy.md)** | A whole-part tint on Mesh parts is approximate, and a save keeps only track 0 | [Limitations & Scope](https://cri-middleware.github.io/SSPlayerForRenPy/limitations/) |
| **[wgpu](../players/wgpu.md)** | The C face draws only to its own window, the web face needs WebGPU, and the Bevy adapter draws one view | [Limitations & Scope](https://cri-middleware.github.io/SSPlayerForWgpu/limitations/) |
| **[React Native](../players/react-native.md)** | Masks do not clip Effect parts, and nothing draws on the web | [Limitations & Scope](https://cri-middleware.github.io/SSPlayerForReactNative/limitations) |

!!! note "How to read this page"
    Each section below summarizes what that player's own **Limitations & Scope** page states -
    every player publishes one, linked in the table above. The summary keeps what differs between
    players; the full list, and every exact case, is on that page.

    Anything true of *every* player - including the fact that **text and 9-slice parts are drawn
    by none of them yet** - is on [Shared Limitations](../sdk/limitations.md) instead, since it is
    not a difference.

### Unity

The **uGUI (Canvas) path** trades capability for CanvasRenderer's "1 renderer = 1 mesh + 1
material": it assumes a **single atlas** (parts from other atlases cannot sample correctly) and
supports **`Mix` / `Add` only**, collapsing every other blend to `Mix`. It also gives up part
tracking, per-part shaders and Timeline control. The world path has none of these limits; it draws
`Mul2` as `Mul` and `Screen2` as `Screen`.

### Web

**`ssplayer-webgl` masks through the stencil buffer**, so on a context without one no mask can be
written: parts drawn outside a mask draw unclipped, and parts set to draw only inside a mask are
not drawn. The framework integrations - **RPG Maker MZ, TyranoScript and TyranoBuilder** - are
**beta**; on RPG Maker MZ a picture's tint and blend mode do not affect the animation.

In the browser converter `ssconverter-web`, dropping a folder needs the File System Access API,
so dropping is **Chromium-only**; other browsers pick the folder with **Browse...**.

### Godot

Only **four of the twelve blend modes** are honored - `Mix`, `Mul`, `Add` and `Sub`. `Mulalpha`
and `Mul2` draw as `Mul`, and the other six fall back to `Mix`: the plugin draws straight to a
Godot canvas item, so a part is limited to the modes a `CanvasItemMaterial` maps onto. Masks
**do not clip Effect parts**.

Ships as GDExtension **or** custom module; the **Web export** has extra requirements (a
`dlink_enabled` engine template for GDExtension - the custom module needs none) and is
single-threaded (`nothread`), which is why it needs no COOP/COEP headers.

### Flutter

Two render backends: Canvas, always available and the only one on the Web, and `flutter_gpu`,
used only when the run switches it on (`--enable-flutter-gpu`). On Canvas, `Sub` and `Invert` are
reconstructed from four and three passes (they cannot batch); on **both** backends `Mulalpha` /
`Mul2` render as `Mul` and `Screen2` as `Screen`. Masks **do not clip Effect parts** on either backend. The Web target is a
**developer preview**.

Widget **part following** carries the transform but not the draw order - a followed widget paints
above the whole animation rather than between its parts - and its anchor has to cover the view's
own box.

### Ren'Py

`Mulalpha` / `Mul2` draw as `Mul`, and `Screen2` as `Screen`. **Part tracking** carries the
transform but not the draw order - a pinned child paints in front of the whole sprite rather than
between its parts.

A whole-part tint on Mesh parts is approximated (alpha only), and the particles an Effect part
emits are not clipped by masks, even where the editor clips them. Part overrides reach only the
parts of the pack the player itself plays, not those inside an Instance part. A save does not keep
the track stack: a loaded save comes back on track 0's animation alone. Its own docs enumerate each
case.

### wgpu

`Mulalpha` / `Mul2` draw as `Mul`, and `Screen2` as `Screen`. The **C face builds and owns its
device** and draws only to the window it was given - not into a render pass of yours, nor into a
texture. Drawing into a pass you own is for Rust and the Bevy adapter: your application and the
player must resolve to one `wgpu`, and the pass must have **MSAA off**. The **web face needs
WebGPU**, with no WebGL fallback.

The **Bevy adapter** is a separate crate, following Bevy's release line rather than the player's
and tracking one line at a time. It draws **one view** - a second one is skipped with a warning
(the camera also wants `CompositingSpace::Srgb` for faithful color).

### React Native

Masks clip Normal, Mesh and Shape parts; **Effect parts draw unmasked**.

Platform reach is narrower too: **nothing draws on the web** - the web entry is a stub, so an app
that also builds for the web still bundles - and Windows has no route.

## 🎨 Why blend modes are the usual difference

SpriteStudio realizes each blend as a GPU blend state, so reproduction depends on what the host
engine exposes. Where a mode has no equivalent, players fall back rather than fail - which is why
most entries above cluster around the same few modes:

- **`Div2` / `Overlay2`** read the colour already behind the part, which no GPU blend state can do,
  and no published formula defines them, so every player draws them as `Mix`. Being the same
  everywhere, it is left out of the sections above.
- **`Sub` / `Invert`** need a reverse-subtract or destination-replace state. An engine without one can
  still reconstruct them exactly from multiple passes, at the cost of batching - so the difference
  may show up as performance rather than as a visual gap.

## ➡️ Next

- [Choose Your Platform](./choose-your-platform.md) - pick a player by target runtime.
- [Shared Limitations](../sdk/limitations.md) - the constraints that apply everywhere.
- [Support](../support.md) - if a difference here looks like a bug, this is where to report it.

# 🧩 Player Differences

Every official player evaluates animations with the **same core**, so the *feature set* is shared
rather than reimplemented per engine - it is listed under
[SDK Concepts](../sdk/concepts.md). What can still differ is:

1. **What the engine's rendering layer can reproduce** - blend modes in particular map onto
   whatever fixed-function blend states the host engine exposes.
2. **What each player has implemented so far** - the players are at different stages.

This page covers only those differences **between players**. The constraints that apply
*everywhere* - seek and reverse behavior, blending rules, browser requirements, and the features
the core computes but leaves the player to draw or play - are in
[Shared Limitations](../sdk/limitations.md).

## 🔍 Documented per-player differences

| Player | In short |
|---|---|
| **[Unity](../players/unity.md)** | The uGUI (Canvas) path carries limits the world path does not |
| **[Web](../players/web.md)** | `ssplayer-webgl` masks only with a stencil buffer; the framework integrations are beta |
| **[Godot](../players/godot.md)** | Four of the twelve blend modes are honored; the Web export has extra requirements |
| **[Flutter](../players/flutter.md)** | Two render backends, and the Canvas one costs batching on two blends |
| **[Ren'Py](../players/renpy.md)** | `Div2` / `Overlay2` fall back to `Mix`, and a few features are approximate |
| **[wgpu](../players/wgpu.md)** | Masking has two backends, and the Bevy adapter draws one view |
| **[React Native](../players/react-native.md)** | Masks do not clip Effect parts, and nothing draws on the web |

!!! note "How to read this page"
    Each section below summarizes what that player's own **Limitations & Scope** page states -
    every player publishes one, and the exact cases are listed there. So a gap absent here is
    absent from that player's own account too - which is still not the same as a guarantee of
    support.

    Anything true of *every* player - including the fact that **text and 9-slice parts are drawn
    by none of them yet** - is on [Shared Limitations](../sdk/limitations.md) instead, since it is
    not a difference.

### Unity

The **uGUI (Canvas) path** trades capability for CanvasRenderer's "1 renderer = 1 mesh + 1
material": it assumes a **single atlas** (parts from other atlases cannot sample correctly) and
supports **`Mix` / `Add` only**, collapsing every other blend to `Mix`. The world path has neither
limit.

Edit mode shows only a static preview of the start frame.

### Web

**`ssplayer-webgl` masks through the stencil buffer**, so on a context without one no mask can be
written: parts drawn outside a mask draw unclipped, and parts set to draw only inside a mask are
not drawn. The framework integrations - **RPG Maker MZ, TyranoScript and TyranoBuilder** - are
**beta**; on RPG Maker MZ a picture's tint and blend mode do not affect the animation.

The browser converter `ssconverter-web` needs the File System Access API, so it is
**Chromium-only**.

### Godot

Only **four of the twelve blend modes** are honored - `Mix`, `Mul`, `Add` and `Sub`. `Mulalpha`
and `Mul2` draw as `Mul`, and the other six fall back to `Mix`: the plugin draws straight to a
Godot canvas item, so a part is limited to the modes a `CanvasItemMaterial` maps onto. Masks
**do not clip Effect parts**.

Ships as GDExtension **or** custom module; the **Web export** has extra requirements (a
`dlink_enabled` engine template for GDExtension - the custom module needs none) and is
single-threaded (`nothread`), which is why it needs no COOP/COEP headers.

### Flutter

Two render backends (`flutter_gpu` / Canvas; Web is always Canvas). On Canvas, `Sub` and `Invert`
are reconstructed from four and three passes (they cannot batch); `Div2` / `Overlay2` render as `Mix` on
**both** backends. Masks **do not clip Effect parts** on either backend. The Web target is a
**developer preview**.

Widget **part following** carries the transform but not the draw order - a followed widget paints
above the whole animation rather than between its parts - and its anchor has to cover the view's
own box.

### Ren'Py

`Div2` / `Overlay2` fall back to `Mix`. **Part tracking** carries the transform but not the draw
order - a pinned child paints in front of the whole sprite rather than between its parts.

A few features are approximate rather than exact - masking, whole-part tint on Mesh parts, and
anything nested inside an Instance part - and the particles an Effect part emits are not clipped by masks, even where the editor clips them. Its own docs enumerate each case.

### wgpu

`Div2` / `Overlay2` fall back to `Mix`. Masking has **two backends, and what the host's pass lends
picks between them**: the **stencil** one, or the **coverage-bitmap** one for a pass that lends no
stencil, at the cost of one extra render pass per masking player, and one more for every 24 mask
writers past the first 24. Both backends stop at 96 writers per player. Either way, the pass the
player draws into must have **MSAA off**.

The **Bevy adapter** is a separate crate, following Bevy's release line rather than the player's
and tracking one line at a time. It takes the coverage backend, since Bevy's 2d depth texture
carries no stencil, and draws **one view** - a second one is skipped with a warning (the camera
also wants `CompositingSpace::Srgb` for faithful color). Packs load through Bevy's `AssetServer`,
so hot reload, packed assets and shared atlases work as they do for any Bevy asset.

### React Native

Masks clip Normal, Mesh and Shape parts; **Effect parts draw unmasked**.

Platform reach is narrower too: **nothing draws on the web** - the web entry is a stub, so an app
that ships both halves still bundles - and Windows has no route.

## 🎨 Why blend modes are the usual difference

SpriteStudio realizes each blend as a GPU blend state, so reproduction depends on what the host
engine exposes. Where a mode has no equivalent, players fall back rather than fail - which is why
most entries above cluster around the same few modes:

- **`Div2` / `Overlay2`** read the colour already behind the part, which no GPU blend state can do,
  so falling back to `Mix` is deliberate behavior rather than an unfinished implementation.
- **`Sub` / `Invert`** need a reverse-subtract or destination-replace state. An engine without one can
  still reconstruct them exactly from multiple passes, at the cost of batching - so the difference
  may show up as performance rather than as a visual gap.

A blend can also look wrong without the player being at fault: the modes that sample the
destination assume opaque pixels underneath. That rule is core-wide - see
[Shared Limitations](../sdk/limitations.md).

## ➡️ Next

- [Choose Your Platform](./choose-your-platform.md) - pick a player by target runtime.
- [Shared Limitations](../sdk/limitations.md) - the constraints that apply everywhere.
- [Support](../support.md) - if a difference here looks like a bug, this is where to report it.

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

| Player | Known differences |
|---|---|
| **[Unity](../players/unity.md)** | The **uGUI (Canvas) path** trades capability for CanvasRenderer's "1 renderer = 1 mesh + 1 material": it assumes a **single atlas** (parts from other atlases cannot sample correctly) and supports **MIX / ADD only**, collapsing every other blend to `Mix`. The world path has neither limit. `.ssqb` assets **import** and can be referenced - playing a sequence back is a [shared](../sdk/limitations.md) gap, not a Unity one. Edit mode shows only a static preview of the start frame. |
| **[Web](../players/web.md)** | The renderer packages (`ssplayer-webgl`, `ssplayer-pixi`) carry no feature gaps of their own. The framework integrations are at different stages: **RPG Maker MZ is experimental (alpha)** - a picture's tint does not affect the animation - while the **TyranoScript and TyranoBuilder plugins are beta**. TyranoBuilder has no component yet for per-part color / visibility or for linking an animation to a speaker; those are written with `[ss_*]` tags instead. The browser converter `ssconverter-web` needs the File System Access API, so it is **Chromium-only**. |
| **[Godot](../players/godot.md)** | No feature gaps beyond the shared ones. Ships as GDExtension **or** custom module; the **Web export** has extra requirements (a `dlink_enabled` engine template for GDExtension - the custom module needs none) and is single-threaded (`nothread`), which is why it needs no COOP/COEP headers. |
| **[Flutter](../players/flutter.md)** | Two render backends (`flutter_gpu` / Canvas; Web is always Canvas). On Canvas, `Sub` and `Invert` are reconstructed from three passes (they cannot batch); `Div2` / `Overlay2` render as `Mix` on **both** backends. Widget **part following** carries the transform but not the draw order - a followed widget paints above the whole animation rather than between its parts - and assumes the view draws unscaled. |
| **[Ren'Py](../players/renpy.md)** | Division / Overlay fall back to `Mix`. **Part tracking** carries the transform but not the draw order - a pinned child paints in front of the whole sprite rather than between its parts. A few features are approximate rather than exact - masking, whole-part tint on Mesh parts, and anything nested inside an Instance part. Its own docs enumerate each case. |
| **[React Native](../players/react-native.md)** | **Masked Effect draws unmasked** - the mask replay places its coverage sample by inverting one affine quad's UV, and an effect is a cloud of quads with no single shape to cut. Masked **Mesh** is supported: a mesh needs its texcoord channel for its atlas, so it is drawn into an isolated layer that the same triangles then cut with `kDstIn`, carrying the coverage UV per vertex. A child's **own mask writers write nothing** for any frame in which a mask from outside reaches into it. Platform reach is narrower too: tvOS / visionOS wait on Tier 3 Rust targets, and Windows has no route. |
| **[wgpu](../players/wgpu.md)** | `Div2` / `Overlay2` fall back to `Mix`. Masking has **two backends, and what the host's pass lends picks between them**: the **stencil** one approximates overlapping masks that mix INCR and INVERT, bounds nesting by the 8 bits available, and drops writers past the 24th; the **coverage-bitmap** one serves a pass that lends no stencil, with the same semantics at the cost of one extra render pass per masking player. Group alpha composites **each part in turn**, so two overlapping parts at `0.5` leave their overlap at `0.75` rather than at `0.5`. The 13 integration shaders are covered for **Normal parts only** - `map0` / `map1` secondary textures, and a shader part combined with a mask, are not. The **Bevy adapter** is a separate crate, following Bevy's release line rather than the player's and tracking one line at a time. It takes the coverage backend, since Bevy's 2d depth texture carries no stencil, and states three limits of its own: a **second view is skipped** with a warning, **MSAA must be off** (and the camera wants `CompositingSpace::Srgb` for faithful colour), and loading is **synchronous**, going to the filesystem rather than Bevy's `AssetServer` - so no hot reload, packed assets or shared atlases. |

!!! note "How to read this table"
    Each entry is a summary of what that player's own **Limitations & Scope** page states; follow
    the link for the exact cases. Every player publishes one. So a gap absent here is absent from
    that player's own account too - which is still not the same as a guarantee of support.

    Anything true of *every* player - including the fact that **text and 9-slice parts are drawn
    by none of them yet** - is on [Shared Limitations](../sdk/limitations.md) instead, since it is
    not a difference.

## 🎨 Why blend modes are the usual difference

SpriteStudio realizes each blend as a GPU blend state, so reproduction depends on what the host
engine exposes. Where a mode has no equivalent, players fall back rather than fail - which is why
the entries above cluster around the same few modes:

- **Division / Overlay** have no GPU blend mapping in the reference players either, so falling
  back to `Mix` is deliberate behavior rather than an unfinished implementation.
- **Sub / Invert** need a reverse-subtract or destination-replace state. An engine without one can
  still reconstruct them exactly from multiple passes, at the cost of batching - so the difference
  may show up as performance rather than as a visual gap.

A blend can also look wrong without the player being at fault: the modes that sample the
destination assume opaque pixels underneath. That rule is core-wide - see
[Shared Limitations](../sdk/limitations.md).

## ➡️ Next

- [Choose Your Platform](./choose-your-platform.md) - pick a player by target runtime.
- [Shared Limitations](../sdk/limitations.md) - the constraints that apply everywhere.
- [Support](../support.md) - if a difference here looks like a bug, this is where to report it.

# 🧩 Feature Support

Every official player evaluates animations with the **same core**, so the *feature set* is shared
rather than reimplemented per engine - it is listed under
[SDK Concepts](../sdk/concepts.md). What can still differ is:

1. **What the engine's rendering layer can reproduce** - blend modes in particular map onto
   whatever fixed-function blend states the host engine exposes.
2. **What each player has implemented so far** - the players are at different stages.
3. **How the API is shaped** - a handful of deliberate choices that follow the host platform
   rather than the family. These are not gaps, and they have their own section below.

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
| **[React Native](../players/react-native.md)** | **Masked Mesh and masked Effect draw unmasked** - the mask replay places its coverage sample by inverting one affine quad's UV, which a mesh's texcoord channel and an effect's cloud of quads cannot supply. A child's **own mask writers write nothing** for any frame in which a mask from outside reaches into it. Platform reach is narrower too: tvOS / visionOS wait on Tier 3 Rust targets, and Windows has no route. |
| **[wgpu](../players/wgpu.md)** | `Div2` / `Overlay2` fall back to `Mix`. Masking is **stencil-only**: overlapping masks that mix INCR and INVERT are approximated, nesting is bounded by the 8 bits available, and writers past the 24th are dropped. Group alpha composites **each part in turn**, so two overlapping parts at `0.5` leave their overlap at `0.75` rather than at `0.5`. The 13 integration shaders are covered for **Normal parts only** - `map0` / `map1` secondary textures, and a shader part combined with a mask, are not. |

!!! note "How to read this table"
    Each entry is a summary of what that player's own **Limitations & Scope** page states; follow
    the link for the exact cases. Every player publishes one except **wgpu**, whose
    [ROADMAP](https://github.com/cri-middleware/SSPlayerForWgpu/blob/HEAD/ROADMAP.md) covers the
    same ground until it has a documentation site. So a gap absent here is absent from that
    player's own account too - which is still not the same as a guarantee of support.

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

## ⚙️ Differences by design - not gaps

The table above is about what a player cannot yet reproduce. This section is the opposite: places
where the players deliberately differ, because following the host platform serves you better than
following each other.

### What does *not* differ

Worth stating first, because it is the larger half. **Playback semantics are identical across every
player**, and are the SDK's contract rather than each player's invention:

- **Four transport verbs**, and they are not interchangeable. `play` is a *head-out* - it rewinds
  to the start of the section and re-arms the loop count - so it cannot lift a `pause`; `resume`
  does that, and does nothing on a stopped animation. `stop` does not rewind.
- **`isPlaying` stays true while paused.** A pause is a hold, not a stop; `isPausing` tells the two
  apart.
- **`looped` is a pulse, `finished` is an edge.** `finished` never fires under an infinite loop
  count, and never fires for a commanded `stop`.
- **Selecting the animation already selected does nothing.** It is a switch; with nothing to switch
  to, the playhead stays, the loop budget is not re-armed and the overrides survive. Restarting is
  `play`'s job.
- **What survives an animation switch**: the speed, the frame-rate override, frame skip, and the
  playback direction / style. What does not: the playback section, whose frame numbers mean nothing
  against a different clip.

### Where the clock comes from, and in what unit

Time is the one thing a player cannot take from the SDK, because every host measures it its own
way. So the tick is spelled in each platform's own idiom:

| Player | Who advances it | Unit |
|---|---|---|
| **Unity** | `SpriteStudioUpdateManager`, batched | (no public tick) |
| **Godot** | the node, on `_process` / `_physics_process` - or `ANIMATION_PROCESS_MANUAL` plus `advance()` | seconds |
| **Web** | the `SSSurface` ticker (`ssplayer-webgl`); `Ticker.shared` (`ssplayer-pixi`) | milliseconds |
| **Flutter** | a `Ticker` when given a `vsync`, otherwise the host calls `advance()` | `Duration` |
| **React Native** | the view's frame loop, or `startClock()` headless | milliseconds |
| **Ren'Py** | the displayable's `render()` | milliseconds |
| **wgpu** | **the host** - it owns the clock and lends the player a delta | seconds |

### Autoplay depends on how the player comes into being

There is no family-wide default here, because the question only exists for some of them:

| How you get a player | Autoplay | Why |
|---|---|---|
| **placed** in a scene (Unity, Godot) | **on** by default | nothing calls `play()` for a node you dropped in, so a still frame would read as broken |
| **declared** as markup (`<ss-player>`, `<ss-player-webgpu>`) | **opt-in** attribute | the attribute *is* that call, and an HTML boolean attribute cannot idiomatically default to on - the same shape as `<video autoplay>` |
| **declared** as a component (`<SpriteStudioView playing>`) | prop, **on** by default | a React prop is state, not a one-shot flag |
| **shown** as a displayable (Ren'Py) | always | `show` means "this is on screen and animating" |
| **constructed** in code (Web's JS API, Flutter, wgpu) | no such concept | you already have the call |

### Sub-frame interpolation follows the host, not the family

Whether what is drawn may sit *between* two authored frames. The playhead is fractional either way;
this only decides whether the drawn frame is floored.

| Default | Players |
|---|---|
| **off** | Unity, Godot - game engines, where pinning to authored frames is the usual expectation |
| **on** | Web, Flutter, Ren'Py, React Native, wgpu - applications and renderers, where a display refreshing faster than the animation was authored at is the point |

Every player exposes a setter, so this is a default rather than a limit.

### Events reach you the way the host expects

The same events - user data, signals, audio, plus loop and finish - delivered in each platform's
own shape:

| Player | Shape |
|---|---|
| **Godot** | signals (`user_data`, `signal_emitted`, `audio`, `animation_finished`, …) |
| **Unity** | C# `event` **and** `UnityEvent`, so both code and the inspector can subscribe |
| **Web** | `onX(listener)` returning an unsubscribe |
| **Flutter**, **React Native** | callback fields on the player |
| **Ren'Py** | observed on the frame result, plus a bounded `poll_events()` queue |
| **wgpu** | polled - `events()` after each update, matching the borrow model |

### Loading a pack

| Player | Shape |
|---|---|
| **Unity**, **Godot** | an engine asset reference, resolved by the editor's importer - synchronous |
| **Web**, **React Native** | asynchronous, from a URL or a source descriptor |
| **Flutter** | asynchronous, from bytes (`loadAsset` reads them for you) |
| **Ren'Py** | a path given to the displayable, loaded lazily on first render |
| **wgpu** | synchronous from a path, or asynchronous through an `AssetLoader` the host supplies |

Selecting an animation is **synchronous everywhere**, deliberately: everything that could stall -
textures, instance packs, sounds - belongs to the pack and is done by the load.

## ➡️ Next

- [Choose Your Platform](./choose-your-platform.md) - pick a player by target runtime.
- [Shared Limitations](../sdk/limitations.md) - the constraints that apply everywhere.
- [Support](../support.md) - if a difference here looks like a bug, this is where to report it.

# 🧩 Feature Support

Every official player evaluates animations with the **same core**, so the *feature set* is shared
rather than reimplemented per engine. What can still differ is:

1. **What the engine's rendering layer can reproduce** - blend modes in particular map onto
   whatever fixed-function blend states the host engine exposes.
2. **What each player has implemented so far** - the players are at different stages.

Read this page together with [Shared Limitations](../sdk/limitations.md), which covers the
constraints that apply *everywhere* (seek/reverse behavior, blending rules, browser requirements).

## ✅ Provided by the shared core

These come from `libssruntime` and are therefore available to every player:

- Bone hierarchies and transforms, with full keyframe interpolation (Bezier / Hermite / Linear / ...)
- Mesh & deform
- Effect parts (particles)
- Instance parts
- Masks
- Parts color (per-part color blending)
- Frame-accurate events - user data, signal, audio
- Sub-frame interpolation (smooth playback above the base frame rate)
- Whole-animation blending / crossfade (within one `.ssab` - see
  [Shared Limitations](../sdk/limitations.md))
- The **Override Layer API** - override a part's color, cell reference, or visibility at runtime

Two of these are *state only*: **text parts** and **audio** need the player to draw the glyphs and
to actually play the sound (see [Shared Limitations](../sdk/limitations.md)).

## 🔍 Documented per-player differences

| Player | Known differences |
|---|---|
| **[Unity](../players/unity.md)** | No player-specific limitations are documented. Covers bones, mesh & deform, particles, extended blending, and masks; adds uGUI (Canvas) rendering and Timeline integration. |
| **[Web](../players/web.md)** | The renderer packages (`ssplayer-webgl`, `ssplayer-pixi`) carry no documented feature gaps. The **RPG Maker MZ and TyranoScript adapters are experimental (alpha)**. |
| **[Godot](../players/godot.md)** | No feature gaps documented. Ships as GDExtension **or** custom module; the **Web export** has extra requirements (a `dlink_enabled` engine template for GDExtension - the custom module needs none). |
| **[Flutter](../players/flutter.md)** | Two render backends (`flutter_gpu` / Canvas; Web is always Canvas). On Canvas, `Sub` and `Invert` are reconstructed from three passes (they cannot batch), and `Div2` / `Overlay2` render as `Mix`. |
| **[Ren'Py](../players/renpy.md)** | The longest list: **Text / NineSlice parts are not rendered**; **animation blending is not implemented**; Division / Overlay fall back to `Mix`; masks do not clip Effect particles; a whole-part tint on Mesh parts is approximated (alpha only); part overrides do not reach parts *inside* an Instance part. |

!!! note "How to read this table"
    It lists only what each player's own documentation states. An empty entry means *nothing is
    documented*, which is not the same as a guarantee - each player's docs remain the source of
    truth, and the Ren'Py list is long partly because it is the most thoroughly written down.

## 🎨 About blend modes

SpriteStudio realizes each blend as a GPU blend state, so reproduction depends on what the host
engine exposes. Where a mode has no equivalent, players fall back rather than fail:

- **Division / Overlay** fall back to `Mix` - documented for both Flutter and Ren'Py. The Flutter
  docs note this is intentional, because these modes have no GPU blend mapping in the reference
  players either.
- **Sub / Invert** need a reverse-subtract or destination-replace state. Flutter's Canvas backend
  reconstructs them exactly from three passes; a backend without that reconstruction may differ.
- Modes that sample the destination (`Mul`, `Sub`, `Screen`, `Exclusion`, `Invert`) match the
  editor where the pixels underneath are **opaque** - the case SpriteStudio itself assumes. Give a
  blend-heavy animation an opaque background layer if exact parity matters.

## ❔ Not documented yet

- **Text and NineSlice parts** - only the Ren'Py docs state their status (not rendered). The other
  players do not document either way; verify with the player you target if your project uses them.
- **Sequence (`.ssqe`) playback** - not implemented in the runtime yet, so no player has it (see
  [Shared Limitations](../sdk/limitations.md)).

## ➡️ Next

- [Choose Your Platform](./choose-your-platform.md) - pick a player by target runtime.
- [Shared Limitations](../sdk/limitations.md) - the constraints that apply everywhere.
- [Support](../support.md) - if a difference here looks like a bug, this is where to report it.

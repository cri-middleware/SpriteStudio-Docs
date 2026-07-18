# 📦 Format Specification

The SDK uses two binary formats, both **FlatBuffers**-based, plus a runtime FFI interface.
This page summarizes them; the **canonical, field-level specs live in the SDK**:

- [**SSAB / SSQB Schema**](https://github.com/cri-middleware/SpriteStudio-SDK/blob/main/libs/ssab/SCHEMA.md) - the asset binary.
- [**FrameData Schema**](https://github.com/cri-middleware/SpriteStudio-SDK/blob/main/libs/ssruntime/SCHEMA.md) - the runtime exchange interface.

## 🗄️ SSAB / SSQB - the asset binary

`.ssab` (**S**prite**S**tudio **A**nime **B**inary) and `.ssqb` (Sequence Binary) are the
converted, play-ready assets produced by `libssconverter` from the XML-based `ss*e` sources
(`ssae` / `ssce` / `ssee` / `ssse` / `fnt` / `ssqe`).

| | `ss*e` (XML) | `.ssab` / `.ssqb` (binary) |
|---|---|---|
| Format | XML / BMFont text | FlatBuffers |
| String lookup | Name comparison | Hash-based (`uint32`) |
| Access | Deserialize to owned structs | Zero-copy read |
| `no_std` | No | Yes |

**Conversion unit - one `.ssab` per `.ssae` (animation pack).** Each `.ssab` is
self-contained: it embeds only the `ss*e` resources (cellmaps, effects, sounds, fonts) that
the pack actually references. The `.sspj` project itself is *not* stored in `.ssab` - it is
used only to resolve resource references during conversion.

### Key design decisions

- **Hash-based lookups** - every named entity carries `name_hash: uint32` for O(1) lookup, no
  string compares at runtime.
- **Columnar animation data** - instead of `ss*e`'s per-part tagged attribute lists, each
  part stores typed arrays per attribute (`position_x_array`, `rotation_z_array`, ...),
  enabling efficient iteration of one attribute across frames.
- **Event separation** - event attributes (user data, signal, audio, instance, effect) are
  stored **per frame** (`EventsPerFrame`) rather than per part, optimizing frame dispatch.
- **Union-based part types** - a FlatBuffers union replaces `ss*e`'s tag-string dispatch.
- **Zero-copy / `no_std`** - the default runtime mode reads without allocation; a `converter`
  feature enables the Object API for writing.
- **Editor-only fields stripped** - UI state, bone-editing, IK, and mesh-weight-editing fields
  are dropped; mesh weights are pre-resolved to per-vertex influences indexed by part.

`.ssqb` (Sequence) mirrors `.ssqe` almost 1:1 - a list of sequences referencing animation
packs by name/hash.

## 🔗 FrameData - the runtime interface

Where `.ssab` holds the *whole timeline* (generated offline), **`FrameData` is generated
dynamically at runtime for a single frame**. `libssruntime` takes an animation's keyframe
arrays, evaluates them at the current frame, and outputs a `PartState` per part - the
primary **data-exchange interface between the runtime core and your renderer over FFI**.

```text
.ssab AnimationData (sparse keyframes)  +  current frame N
        |  libssruntime: interpolate + coordinate-convert
        v
FrameData (dense, one frame)  --FFI-->  your renderer
   +- parts: [PartState]  (position_x, rotation_z, alpha, mesh, ...)
```

Each `PartState` field maps directly from the corresponding `.ssab` `PartAnimationData` array
(e.g. `position_x` <- `position_x_array`, interpolated and converted to your coordinate
system). The full field-by-field mapping is in the
[FrameData Schema](https://github.com/cri-middleware/SpriteStudio-SDK/blob/main/libs/ssruntime/SCHEMA.md).

## 🔧 Regenerating bindings

The schemas are defined as FlatBuffers `.fbs` files in the SDK
([`ssab.fbs`](https://github.com/cri-middleware/SpriteStudio-SDK/blob/main/libs/ssab/fbs/ssab.fbs) /
[`ssqb.fbs`](https://github.com/cri-middleware/SpriteStudio-SDK/blob/main/libs/ssab/fbs/ssqb.fbs), and
[`framedata.fbs`](https://github.com/cri-middleware/SpriteStudio-SDK/blob/main/libs/ssruntime/fbs/framedata.fbs)).
See [`libssab`](https://github.com/cri-middleware/SpriteStudio-SDK/tree/main/libs/ssab)
for feature flags (`default` / `no_std` / `converter`) and codegen.

!!! info "Schema versioning"
    `.ssab` carries a binary `version` field, and tooling such as `ssconverter-web` is
    published [per schema version](../overview/convert-with-a-standalone-tool.md). Match the converter's schema to
    your player's runtime version.

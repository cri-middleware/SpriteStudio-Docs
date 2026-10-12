# 📖 Glossary

The vocabulary shared by this portal, the SDK, and every player's documentation. Terms are
grouped by which side of the pipeline they belong to: what you author in SpriteStudio, and what
the SDK produces and plays back.

## 🎨 Authoring - SpriteStudio side

| Term | What it is |
|---|---|
| **Project** (`.sspj`) | The SpriteStudio project file. It references everything else - animation packs, cellmaps, effects, sounds - and is read at conversion time to resolve those references. It is *not* stored in the converted asset. |
| **Animation pack** (`.ssae`) | A set of **parts** plus the **animations** that drive them. Also the **unit of conversion**: one `.ssae` becomes one `.ssab`. |
| **Animation** | One timeline inside an animation pack (e.g. `walk`, `attack`). Selected by name at playback time. |
| **Part** | One node in the animation's hierarchy - a sprite, a bone, a mask, and so on. Parts form a parent/child tree; transforms and color/opacity inherit down it. |
| **Cell** | A rectangular region of a texture - the image a part draws. |
| **Cellmap** (`.ssce`) | A texture plus the cells defined on it. Parts reference cells through their cellmap. |
| **Effect** (`.ssee`) | A particle effect definition, played by an Effect part. |
| **Sound** (`.ssse`) | Sound settings referenced by audio events on the timeline. |
| **Sequence** (`.ssqe`) | A playlist that chains animations together. Converted to `.ssqb`. |
| **Bitmap font** (`.fnt`) | The BMFont-format font a Text part draws with. |
| **User data / Signal** | Markers placed on a frame that the runtime reports back as **events** - the frame-accurate hook for triggering game logic, sound effects, and so on. |
| **Parts color** | A per-part color blend authored on the timeline, applied on top of the part's texture. |
| **`independent`** | A flag on an Instance or Effect part that detaches its child from the parent timeline, running it on its own real-time clock. It has real consequences for reverse playback and seeking - see [Shared Limitations](./limitations.md). |

### Part types

These are the part types as SpriteStudio names them; in the `.ssab` schema each one is spelled
`PartType*` (`PartTypeNormal`, `PartTypeMesh`, ...). The ones you meet most often:

| Part type | Draws |
|---|---|
| `Null` | Nothing. A grouping / pivot node that gives its children a shared transform. |
| `Normal` | A cell (the ordinary sprite part). |
| `Mesh` | A deformable mesh, driven by bones (mesh & deform). |
| `Instance` | Another animation, mounted inside this one. |
| `Effect` | A particle effect (`.ssee`). |
| `Mask` | A stencil that clips the parts it covers. |
| `Shape` | A generated primitive (rectangle, triangle, star, arrow, ...). |
| `Text` | Bitmap-font text. |
| `Nines` | A nine-sliced (9-slice) image. |
| `Armature` | A bone. Draws nothing itself; it drives the parts bound to it. |

## ⚙️ Runtime - SDK side

| Term | What it is |
|---|---|
| **`.ssab`** (SpriteStudio Anime Binary) | The converted, play-ready asset: one animation pack in a compact FlatBuffers binary. See the [Format Specification](./format-spec.md). |
| **`.ssqb`** | The converted sequence binary, the `.ssqe` counterpart of `.ssab`. |
| **`libsspj`** | The authoring-side parser: reads `.sspj` projects and the `ss*e` files they reference. |
| **`libssab`** | The `.ssab` / `.ssqb` library - creates and parses the animation binaries. |
| **`libssconverter`** | The conversion half of the SDK: `.sspj` -> `.ssab` / `.ssqb`. The same code runs in every conversion front-end - see [Converting Assets](../overview/conversion.md). |
| **`libssruntime`** | The playback half: evaluates the timeline for the current frame and hands the result to your renderer. |
| **Brain / Body** | The architectural split. The **Brain** (`libssruntime`) does all the animation math and is engine-agnostic; the **Body** (a player) draws what the Brain computed. See [SDK Concepts](./concepts.md). |
| **`FrameData`** | The Brain's output for **one frame** - dense, ready to render, generated at runtime. The data-exchange interface between the runtime and your renderer. |
| **`PartState`** | One part's resolved state inside a `FrameData`: position, rotation, alpha, mesh vertices, and the rest. |
| **`DrawBatch`** | The cross-engine drawing plan the runtime emits - what to draw, in what order, with which blend and mask state. Every player consumes the same plan, which is what keeps them visually consistent. |
| **Override Layer API** | The runtime API for overriding a part's **color, cell reference, or visibility** at playback time. The override wins over both keyframes and mixing. |
| **Animation mixing / crossfade** | Stacking several animations on tracks and mixing them by weight, or fading between them. Constrained to one `.ssab` - see [Shared Limitations](./limitations.md). |
| **Sub-frame interpolation** | Evaluating between whole frames, so playback stays smooth above the animation's authored frame rate (and in slow motion). |
| **Name hash** | Every named entity in `.ssab` carries a 32-bit FNV-1a hash of its name, so the runtime looks names up without string comparison. |
| **Embedded mode** | An optional conversion mode that additionally packs the referenced **binary assets** - images, sounds - into the `.ssab`. (The `ss*e` data the pack references is embedded either way; see [Format Specification](./format-spec.md).) How it differs from the default, reference, and which players read it: [Converting Assets](../overview/conversion.md#reference-and-embedded). Comes with caveats - see [Shared Limitations](./limitations.md). |
| **External instance** | An Instance part that mounts an animation living in *another* `.ssab`. That file has to be supplied separately. |
| **`no_std`** | The Rust mode the core is written in: no OS and no standard library, which is what lets it run from embedded targets to browsers. |

## ➡️ Next

- [SDK Concepts](./concepts.md) - how these pieces fit together.
- [Format Specification](./format-spec.md) - the binary these terms describe.
- [Shared Limitations](./limitations.md) - the constraints attached to several of them.

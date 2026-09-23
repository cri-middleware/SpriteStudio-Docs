# 🔌 Porting a Player

Want to run SpriteStudio animations on an engine or platform that doesn't have an
official player yet? **SpriteStudio-SDK ships a full Player Porting Guide** that walks you
through building one on top of `libssruntime`.

!!! tip "Where the guide lives"
    The canonical guide is maintained in the SDK repository:
    🚧 [**SpriteStudio Player Porting Guide**](https://github.com/cri-middleware/SpriteStudio-SDK/tree/HEAD/libs/ssruntime/docs)
    (`libs/ssruntime/docs/`). This page is a map into it - the SDK is the source of truth.

## 🧠 Core idea: Brain vs. Body

`libssruntime` is the **Brain** - it does all the animation computation (state, transforms,
mesh/deform, batching plan) and is engine-agnostic. Your player provides the **Body** - the
engine-specific rendering, resource loading, and input. Porting is mostly about wiring your
engine's Body to the shared Brain.

## 📋 What the guide covers

| Section | Contents |
|---|---|
| **10. Introduction** | Core concepts & glossary, and **Limitations** (support scope / spec constraints - read first). |
| **20. Design** | Preparation & prerequisites, Brain-vs-Body architecture, and a staged **implementation roadmap**. |
| **30. Core** | Minimal playback: loading & initialization, playback control & events, the render loop & batching. |
| **40. Components** | Per part-type detail: instance, effect, mesh & deform, mask, parts color, animation mixing, part overrides, external resources, sequence, audio, special parts. |
| **50. Reference** | `no_std` integration and troubleshooting. |
| **60. Tooling** | Integrating `ssconverter` into your engine's editor. |

!!! note "Verify as you go"
    The guide recommends running `tests/overall/overall.sspj` at each stage - if it matches
    the SpriteStudio editor, that step is done. Every official player is built this way, so any
    of them makes a good reference - see
    [Choose Your Platform](../overview/choose-your-platform.md) for the current lineup.

## 🚦 Before you start

- Read [SDK Concepts](./concepts.md) for the convert -> runtime pipeline, and keep the
  [Glossary](./glossary.md) open for the terms the guide assumes.
- Read the guide's **Limitations** page first - it shapes your player's design decisions.
- Source & issues: 🚧 [SpriteStudio-SDK](https://github.com/cri-middleware/SpriteStudio-SDK).

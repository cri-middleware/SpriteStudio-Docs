# SDK Concepts

!!! note "Stub — fill in from SpriteStudio-SDK"
    This page is a placeholder for the shared, platform-independent concepts. Author the
    canonical version here and link to it from the per-player docs instead of duplicating.

**SpriteStudio-SDK** is the Rust core shared by every player. It provides two libraries:

- **`libssconverter`** — converts a SpriteStudio project (`.sspj`) into a compact runtime
  format.
- **`libssruntime`** — loads the runtime format and drives playback (animation state,
  transforms, mesh/deform, particles, blending, masks).

## Pipeline

1. **Author** in OPTPiX SpriteStudio 7 → `.sspj`.
2. **Convert** with `libssconverter` (via the [Converter GUI](../players/converter.md) or
   `ssconverter-cli`) → runtime assets.
3. **Play back** with `libssruntime`, bound to your engine by the platform player.

## Suggested topics to document here

- Runtime data model (cells, parts, animations, keyframes).
- Supported features and any per-platform caveats.
- Versioning / compatibility between the runtime format and player releases.

See the [Format Specification](./format-spec.md) for on-disk details, and the
[SpriteStudio-SDK repository](https://github.com/cri-middleware/SpriteStudio-SDK) for source.

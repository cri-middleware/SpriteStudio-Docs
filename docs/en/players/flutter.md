# 📱 SSPlayerForFlutter

Play SpriteStudio 7 (`.ssab`) animations in **Flutter** apps. The `SpriteStudioView`
widget drives the shared Rust runtime (`libssruntime`) over `dart:ffi` and draws through
`Canvas.drawVertices`, so animations composite like any other widget across Flutter's
targets. A bundled Dart converter (`ssconverter_dart` / the `ssconvert` CLI) turns
`.sspj` projects into `.ssab`.

!!! warning "Early development"
    🧪 SSPlayerForFlutter is **under active development** (alpha, built on
    `ssruntime_dart 7.0.0-alpha.x`) and **not yet published to pub.dev**. Basic playback
    works today; advanced features (part color, masks, mesh deform, effects, instances)
    are still in progress. APIs and package layout may change.

- **Repository:** <https://github.com/cri-middleware/SSPlayerForFlutter>

See [Choose Your Platform](../overview/choose-your-platform.md) to compare players, or
[SDK Concepts](../sdk/concepts.md) for the conversion/playback pipeline shared across all of them.

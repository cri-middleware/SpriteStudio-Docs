# 📱 SSPlayerForFlutter

Play SpriteStudio 7 (`.ssab`) animations in **Flutter** apps. The `SpriteStudioView`
widget (from the `ssplayer_flutter` package) drives the shared Rust runtime
(`libssruntime`) over `dart:ffi` and draws through `Canvas.drawVertices`, so animations
composite like any other widget across Flutter's targets. It also ships a
[Flame](https://flame-engine.org/) adapter (`ssplayer_flame`), a bundled `ssconvert` CLI
that turns `.sspj` projects into `.ssab`, and live-reload of editor edits into a running app.
Packages aren't on pub.dev yet — install from the GitHub Releases bundle for now.

- **Documentation:** _coming soon_
- **Repository:** <https://github.com/cri-middleware/SSPlayerForFlutter>

See [Choose Your Platform](../overview/choose-your-platform.md) to compare players, or
[SDK Concepts](../sdk/concepts.md) for the conversion/playback pipeline shared across all of them.

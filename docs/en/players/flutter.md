---
description: "Play SpriteStudio animations in Flutter apps and Flame games, with a converter CLI and live reload. SpriteStudio adds bones, mesh and effects to 2D illustrations."
---

# 📱 SpriteStudio Player for Flutter

Play SpriteStudio animations in **Flutter** apps, backed by `libssruntime`. The
`SpriteStudioAnimation` widget composites like any other widget.

▶️ See it first, no install: the widget and Flame demos run in a browser -
[Try it in your browser](../overview/try-it.md).

!!! tip "Code-first - and no Rust toolchain"
    The native core is fetched, not built: the first build downloads a prebuilt runtime, and the
    converter does the same.

**1. What you install** - `ssplayer_flutter` from pub.dev (`flutter pub add ssplayer_flutter`),
which brings `ssruntime_dart` with it, and `ssconverter_dart` as a dev dependency for the
converter (`flutter pub add --dev ssconverter_dart`) - see
[Installation](https://cri-middleware.github.io/SSPlayerForFlutter/guide/install/).

**2. `.sspj` -> `.ssab`** - put your SpriteStudio project under `SpriteStudio_Source/`, convert it
with the `ssconvert` CLI from `ssconverter_dart`, and list the output folder under `assets:` in
`pubspec.yaml`. One `.sspj` yields one `.ssab` per animation pack.

**3. Getting it on screen** - one `SpriteStudioAnimation.asset(…)` widget with the `.ssab`'s asset
path; a `SpriteStudioPlayer` in a `SpriteStudioView` when you drive playback yourself.

The steps, with the folders they use, are in the README's [Quick Start](https://github.com/cri-middleware/SSPlayerForFlutter#-quick-start).

Alongside the player it ships:

- **A [Flame](https://flame-engine.org/) adapter** - `ssplayer_flame` drops an animation into a Flame game.
- **[Live reload](https://cri-middleware.github.io/SSPlayerForFlutter/guide/live-reload/)** - a save
  in SpriteStudio re-converts only the changed project and pushes it into the running debug app.

## ➡️ Read next

- [Documentation](https://cri-middleware.github.io/SSPlayerForFlutter/)
- [Repository](https://github.com/cri-middleware/SSPlayerForFlutter)
- [Try It in Your Browser](../overview/try-it.md) - both demos, plus the other players' live builds

# 📱 SpriteStudio Player for Flutter

Play SpriteStudio animations in **Flutter** apps, backed by `libssruntime`. The
`SpriteStudioView` widget composites like any other widget, across Flutter's targets.

▶️ See it first, no install: the widget and Flame demos run in a browser -
[Try it in your browser](../overview/try-it.md).

!!! tip "Code-first - and no Rust toolchain"
    The native core is fetched, not built: `ssruntime_dart`'s native-assets hook downloads the
    prebuilt `libssruntime` from the pinned SDK release, and the converter downloads
    `libssconverter` the same way.

**1. What you install** - `ssplayer_flutter` from pub.dev (`flutter pub add ssplayer_flutter`),
which brings `ssruntime_dart` with it, and `ssconverter_dart` as a dev dependency for the
converter (`flutter pub add --dev ssconverter_dart`) - see
[Installation](https://cri-middleware.github.io/SSPlayerForFlutter/guide/install/).

**2. `.sspj` -> `.ssab`** - put your SpriteStudio project under `SpriteStudio_Source/`, convert it
with the `ssconvert` CLI from `ssconverter_dart`, and list the output folder under `assets:` in
`pubspec.yaml`. One `.sspj` yields one `.ssab` per animation pack.

**3. Getting it on screen** - one `SpriteStudioAnimation.asset(…)` widget with the `.ssab`'s asset
path; a `SpriteStudioPlayer` in a `SpriteStudioView` when you drive playback yourself.

The steps, with the folders they use, are in the README's [Quick Start](https://github.com/cri-middleware/SSPlayerForFlutter#-1-quick-start).

Alongside the player it ships:

- **A [Flame](https://flame-engine.org/) adapter** - drop an animation into a Flame game.
- **Live reload** - add `ssgen_flutter` as a dev dependency and run its `sswatch` next to
  `flutter run`: a save in SpriteStudio re-converts only the changed project and pushes it into the
  running debug app.

## ➡️ Read next

- [Documentation](https://cri-middleware.github.io/SSPlayerForFlutter/)
- [Repository](https://github.com/cri-middleware/SSPlayerForFlutter)
- [Try It in Your Browser](../overview/try-it.md) - both demos, plus the other players' live builds

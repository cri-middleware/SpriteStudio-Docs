# 📱 SpriteStudio Player for Flutter

Play SpriteStudio animations in **Flutter** apps, backed by `libssruntime`. The
`SpriteStudioView` widget composites like any other widget, across Flutter's targets.

▶️ See it first, no install: the widget and Flame demos run in a browser -
[Try it in your browser](../overview/try-it.md).

!!! tip "Code-first - and no Rust toolchain"
    The native core is fetched, not built: `ssruntime_dart`'s native-assets hook downloads the
    prebuilt `libssruntime` from the pinned SDK release, and the converter downloads
    `libssconverter` the same way.

**1. What you install** - a `ssplayer_flutter` dependency in `pubspec.yaml`, as a git dependency
on its release tag (`ssplayer_flutter-v<version>`), with the `ssruntime_dart` it names taken from
the same tag under `dependency_overrides` - see
[Installation](https://cri-middleware.github.io/SSPlayerForFlutter/guide/install/).

**2. `.sspj` -> `.ssab`** - put your SpriteStudio project under `SpriteStudio_Source/` and run the
bundled CLI. One `.sspj` yields one `.ssab` per animation pack:

```bash
dart run ssconverter_dart:ssconvert -e -o assets/spritestudio/MyChar/ SpriteStudio_Source/MyChar/MyChar.sspj
```

**3. Getting it on screen** - `await player.loadAsset('assets/spritestudio/MyChar/MyChar.ssab')`,
then set an animation and place a `SpriteStudioView(player: player, …)` in your widget tree.

Alongside the player it ships:

- **A [Flame](https://flame-engine.org/) adapter** - drop an animation into a Flame game.
- **Live reload** - run `sswatch` next to `flutter run` and a save in SpriteStudio re-converts
  only the changed project and pushes it into the running app.

## ➡️ Read next

- [Documentation](https://cri-middleware.github.io/SSPlayerForFlutter/)
- [Repository](https://github.com/cri-middleware/SSPlayerForFlutter)
- [Try It in Your Browser](../overview/try-it.md) - both demos, plus the other players' live builds

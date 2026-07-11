# 🕹️ SSPlayerForGodot

Renders SpriteStudio animations natively in the **Godot Engine**, backed by `libssruntime`.
It ships in two forms:

- **GDExtension** - drop-in binary add-on; no engine rebuild required.
- **Custom module** - compiled into a custom Godot build for tighter integration.

It also plays back animation sound (`ssaudio`) events through the engine's audio, with a hook
to route them to a custom audio backend.

- **Documentation:** <https://cri-middleware.github.io/SSPlayerForGodot/>
- **Repository:** <https://github.com/cri-middleware/SSPlayerForGodot>

See [Choose Your Platform](../overview/choose-your-platform.md) to compare players, or
[SDK Concepts](../sdk/concepts.md) for the conversion/playback pipeline shared across all of them.

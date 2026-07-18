# 🎬 SpriteStudio Docs

The documentation portal for the **SpriteStudio SDK** and its official players.

[OPTPiX SpriteStudio 7](https://www.webtech.co.jp/spritestudio/) is a 2D animation tool.
This portal is the single entry point to every official runtime and tool that plays back
SpriteStudio animations - all powered by the shared Rust core, **SpriteStudio-SDK**.

Not sure where to start? See [Choose Your Platform](./overview/choose-your-platform.md),
or read [how the pieces fit together](./overview/ecosystem.md).

▶️ Prefer to see it first? [Try it in your browser](./overview/try-it.md) - live demos and a
hosted converter, no install.

## 🎮 Players & Tools

<div class="grid cards" markdown>

-   :material-unity: __Unity__

    ---

    Play back SpriteStudio 7 animations in the Unity Engine, accelerated by the Job System.

    [:octicons-arrow-right-24: Overview](./players/unity.md) |
    Docs (coming soon) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForUnity)

-   :material-web: __Web (Player Collection)__

    ---

    A collection of browser players - PixiJS, framework-free WebGL, RPG Maker MZ, TyranoScript -
    plus a client-side converter (ssconverter-web).

    [:octicons-arrow-right-24: Overview](./players/web.md) |
    Docs (coming soon) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForWeb)

-   :simple-godotengine: __Godot__

    ---

    Render SpriteStudio animations natively in Godot - available as both a GDExtension and a custom module.

    [:octicons-arrow-right-24: Overview](./players/godot.md) |
    Docs (coming soon) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForGodot)

-   :simple-flutter: __Flutter__

    ---

    Play SpriteStudio 7 animations in Flutter apps via a `SpriteStudioView` widget.
    🧪 **In early development** - not yet released.

    [:octicons-arrow-right-24: Overview](./players/flutter.md) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForFlutter)

-   :material-drama-masks: __Ren'Py__

    ---

    Bring SpriteStudio characters into Ren'Py visual novels.

    [:octicons-arrow-right-24: Overview](./players/renpy.md) |
    Docs (coming soon) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForRenPy)

-   :material-file-swap: __Converter GUI__

    ---

    A desktop app for converting `.sspj` projects into runtime-ready assets.

    [:octicons-arrow-right-24: Overview](./players/converter.md) |
    Docs (coming soon) |
    [GitHub](https://github.com/cri-middleware/SSConverterGUI)

-   :material-cog: __SpriteStudio-SDK__

    ---

    The shared Rust core (`libssruntime` / `libssconverter`) every player builds on.
    Includes a full **Player Porting Guide** for new engines.

    [:octicons-arrow-right-24: Concepts](./sdk/concepts.md) |
    [Porting](./sdk/porting.md) |
    [GitHub](https://github.com/cri-middleware/SpriteStudio-SDK)

</div>

!!! note "About this portal"
    **Using a player?** Start above - [Choose Your Platform](./overview/choose-your-platform.md)
    points you to the right one, and each player links out to its own detailed docs.

    **Using the SDK directly, or building a new player?** See
    [SDK & Development](./sdk/concepts.md).

    Each player keeps its detailed documentation in its own repository; this portal is the
    entry point plus the **cross-cutting** material that belongs to no single player.

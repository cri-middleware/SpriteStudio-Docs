# 🎬 SpriteStudio Docs

The documentation portal for the **SpriteStudio SDK** and its official players.

[SpriteStudio](https://www.webtech.co.jp/spritestudio/) is a 2D animation tool.
This portal is the single entry point to every official runtime and tool that plays back
SpriteStudio animations - all powered by the shared Rust core, **SpriteStudio-SDK**.

Not sure where to start? See [Choose Your Platform](./overview/choose-your-platform.md),
or read [how the pieces fit together](./overview/ecosystem.md).

▶️ Prefer to see it first? [Try it in your browser](./overview/try-it.md) - live demos and a
hosted converter, no install.

🎚️ One character, several animations: crossfade between them and layer one over another, each
authored on its own - see [Motion Blending](./overview/motion-blending.md).

🔘 Building a UI? A SpriteStudio animation can be a button in your UI toolkit, with every
state drawn in SpriteStudio - see [UI Integration](./overview/ui-integration.md).

🎨 No SpriteStudio project of your own? CRI Middleware publishes free
[sample data](https://www.webtech.co.jp/help/ja/spritestudio7/download/sample/) - complete `.sspj` projects
(characters, effects, UI) you can feed straight into
[conversion](./overview/conversion.md). (Help Center page, in Japanese.)

## 🎮 Players & Tools

<div class="grid cards" markdown>

-   :material-unity: __Unity__

    ---

    Play back SpriteStudio animations in the Unity Engine, accelerated by the Job System.

    [:octicons-arrow-right-24: Overview](./players/unity.md) |
    [Docs](https://cri-middleware.github.io/SSPlayerForUnity/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForUnity)

-   :material-web: __Web (Player Collection)__

    ---

    A collection of browser players - PixiJS, framework-free WebGL, RPG Maker MZ, TyranoScript,
    TyranoBuilder - plus a client-side converter (ssconverter-web).

    [:octicons-arrow-right-24: Overview](./players/web.md) |
    [Docs](https://cri-middleware.github.io/SSPlayerForWeb/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForWeb)

-   :simple-godotengine: __Godot__

    ---

    Render SpriteStudio animations natively in Godot - available as both a GDExtension and a custom module.

    [:octicons-arrow-right-24: Overview](./players/godot.md) |
    [Docs](https://cri-middleware.github.io/SSPlayerForGodot/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForGodot)

-   :simple-flutter: __Flutter__

    ---

    Play SpriteStudio animations in Flutter apps via a `SpriteStudioView` widget.

    [:octicons-arrow-right-24: Overview](./players/flutter.md) |
    [Docs](https://cri-middleware.github.io/SSPlayerForFlutter/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForFlutter)

-   :material-drama-masks: __Ren'Py__

    ---

    Bring SpriteStudio characters into Ren'Py visual novels.

    [:octicons-arrow-right-24: Overview](./players/renpy.md) |
    [Docs](https://cri-middleware.github.io/SSPlayerForRenPy/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForRenPy)

-   :simple-rust: __wgpu (Rust, C / C++)__

    ---

    A player that renders through wgpu, which puts WebGPU, Vulkan, DX12 and Metal behind one
    API - so the same player runs on any of them.

    [:octicons-arrow-right-24: Overview](./players/wgpu.md) |
    [Docs](https://cri-middleware.github.io/SSPlayerForWgpu/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForWgpu)

-   :simple-react: __React Native__

    ---

    Play SpriteStudio animations in React Native apps through a `<SpriteStudioView>`
    component, drawn natively via Skia.

    [:octicons-arrow-right-24: Overview](./players/react-native.md) |
    [Docs](https://cri-middleware.github.io/SSPlayerForReactNative/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForReactNative)

-   :material-file-swap: __Converter GUI__

    ---

    A desktop app for converting `.sspj` projects into runtime-ready assets.

    [:octicons-arrow-right-24: Overview](./players/converter.md) |
    [Docs](https://cri-middleware.github.io/SSConverterGUI/) |
    [GitHub](https://github.com/cri-middleware/SSConverterGUI)

-   :material-cog: __SpriteStudio-SDK__

    ---

    The shared Rust core (`libssruntime` / `libssconverter`) every player builds on.
    Includes a full **Player Porting Guide** for new engines.

    [:octicons-arrow-right-24: Concepts](./sdk/concepts.md) |
    [Porting](./sdk/porting.md) |
    [Docs](https://cri-middleware.github.io/SpriteStudio-SDK/) |
    [GitHub](https://github.com/cri-middleware/SpriteStudio-SDK)

</div>

!!! note "About this portal"
    **Using a player?** Start above - [Choose Your Platform](./overview/choose-your-platform.md)
    points you to the right one, and each player links out to its own detailed docs.

    **Using the SDK directly, or building a new player?** See
    [SDK & Development](./sdk/concepts.md).

    **Stuck, or found a bug?** [Support](./support.md) routes you to the right repository or
    channel.

    Each player keeps its detailed documentation in its own repository; this portal is the
    entry point plus the **cross-cutting** material that belongs to no single player.

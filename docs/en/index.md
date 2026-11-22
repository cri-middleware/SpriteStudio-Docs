# 🎬 SpriteStudio Docs

The documentation portal for the **SpriteStudio SDK** and its official players.

[SpriteStudio](https://www.webtech.co.jp/spritestudio/) is a 2D animation tool.
This portal is the single entry point to every official runtime that plays back
SpriteStudio animations, and to the tools that convert for them - all powered by the shared Rust core, **SpriteStudio-SDK**.

Not sure where to start? See [Choose Your Platform](./overview/choose-your-platform.md),
or read [how the pieces fit together](./overview/ecosystem.md).

▶️ Prefer to see it first? [Try it in your browser](./overview/try-it.md) - live demos and a
hosted converter, no install.

✨ Beyond playback: [Motion Blending](./overview/motion-blending.md),
[UI Integration](./overview/ui-integration.md) and
[Changing a Character at Runtime](./overview/runtime-changes.md).

🎨 No SpriteStudio project of your own? CRI Middleware publishes free
[sample data](https://www.webtech.co.jp/help/ja/spritestudio7/download/sample/) - complete `.sspj` projects
(characters, effects, UI) you can feed straight into
[conversion](./overview/conversion.md). (Help Center page, in Japanese.)

## 🎮 Players & Tools

<div class="grid cards" markdown>

-   :material-unity: __Unity__

    ---

    Draws in world space or on a uGUI Canvas, where it can be a button or a toggle. Burst jobs and
    the SIMD-optimised Rust core build the mesh with no GC allocations.

    :octicons-arrow-right-24: [Overview](./players/unity.md) |
    [Docs](https://cri-middleware.github.io/SSPlayerForUnity/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForUnity)

-   :material-web: __Web (Player Collection)__

    ---

    Players for every stack, from a dependency-free `<ss-player>` tag to PixiJS, RPG Maker MZ,
    TyranoScript and TyranoBuilder. Unlike `<video>`, it scales freely and reacts to input.
    Includes ssconverter-web, which converts right in the browser.

    :octicons-arrow-right-24: [Overview](./players/web.md) |
    [Docs](https://cri-middleware.github.io/SSPlayerForWeb/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForWeb)

-   :simple-godotengine: __Godot__

    ---

    `SpriteStudioPlayer2D` is just another node in your scene, and the GDExtension installs
    without rebuilding the engine. The SIMD-optimised Rust core computes the poses, so even crowded
    scenes stay smooth.

    :octicons-arrow-right-24: [Overview](./players/godot.md) |
    [Docs](https://cri-middleware.github.io/SSPlayerForGodot/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForGodot)

-   :simple-flutter: __Flutter__

    ---

    A widget like any other - place, size, transform and clip it - and a Flame component too.
    Flutter's own renderer draws it: no WebView, no video decoding.

    :octicons-arrow-right-24: [Overview](./players/flutter.md) |
    [Docs](https://cri-middleware.github.io/SSPlayerForFlutter/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForFlutter)

-   :material-drama-masks: __Ren'Py__

    ---

    Use it like any other image with one `show` line, with lip flap that follows your dialogue.
    A lightweight alternative to video for openings and moving backgrounds.

    :octicons-arrow-right-24: [Overview](./players/renpy.md) |
    [Docs](https://cri-middleware.github.io/SSPlayerForRenPy/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForRenPy)

-   :simple-rust: __wgpu (Rust, C / C++, WebGPU)__

    ---

    One wgpu renderer from Rust and Bevy to C/C++ and the browser. It borrows the host's GPU, so
    it lives inside any wgpu app, egui and Bevy included.

    :octicons-arrow-right-24: [Overview](./players/wgpu.md) |
    [Docs](https://cri-middleware.github.io/SSPlayerForWgpu/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForWgpu)

-   :simple-react: __React Native__

    ---

    An ordinary view, drawn by native code through Skia: no vertices through JavaScript and no
    React re-render each frame.

    :octicons-arrow-right-24: [Overview](./players/react-native.md) |
    [Docs](https://cri-middleware.github.io/SSPlayerForReactNative/) |
    [GitHub](https://github.com/cri-middleware/SSPlayerForReactNative)

-   :material-file-swap: __SSConverter GUI__

    ---

    A desktop app for converting `.sspj` projects into runtime-ready assets.

    :octicons-arrow-right-24: [Overview](./players/converter.md) |
    [Docs](https://cri-middleware.github.io/SSConverterGUI/) |
    [GitHub](https://github.com/cri-middleware/SSConverterGUI)

-   :material-cog: __SpriteStudio-SDK__

    ---

    The shared Rust core (`libssruntime` / `libssconverter`) every player builds on.
    Includes a full **Player Porting Guide** for new engines.

    :octicons-arrow-right-24: [Concepts](./sdk/concepts.md) |
    [Porting](./sdk/porting.md) |
    [Docs](https://cri-middleware.github.io/SpriteStudio-SDK/) |
    [GitHub](https://github.com/cri-middleware/SpriteStudio-SDK)

</div>

!!! note "About this portal"
    **Using the SDK directly, or building a new player?** See
    [SDK & Development](./sdk/concepts.md).

    **Stuck, or found a bug?** [Support](./support.md) routes you to the right repository or
    channel.

    Each player keeps its detailed documentation in its own repository; this portal is the
    entry point plus the **cross-cutting** material that belongs to no single player.

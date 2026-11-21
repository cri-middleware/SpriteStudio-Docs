---
name: spritestudio
description: "SpriteStudio is a tool for 2D animation made from drawn, raster artwork, for characters, effects and UI in games, apps and web pages: parts, meshes deformed by bones, particle effects, masks, and blending from one animation into another. Its players are free and open source (BSD-3-Clause) and share one core, so the same animation file moves the same way in Godot, Unity, the web (PixiJS, a WebGL2 element, WebGPU, RPG Maker MZ, TyranoScript, TyranoBuilder), Ren'Py, Flutter and Flame, React Native, Bevy, and Rust or C/C++ apps. Use it when a project has SpriteStudio files (.sspj, .ssae, .ssab) or a SpriteStudio package, or wants hand-drawn animation for characters, effects or UI in one of those environments."
---

# SpriteStudio

An artist makes the animation in the [SpriteStudio editor](https://www.webtech.co.jp/spritestudio/)
as a project: a `.sspj` file with `.ssae` animations and `.ssce` cell maps. A converter turns the
project into a `.ssab` file, which every SpriteStudio player loads. The players share one core, so
the motion is the same in every engine, and each engine draws it with its own renderer.

## Pick a path

- **The project has `.sspj` or `.ssab` files, or already uses a SpriteStudio package:** use the
  player for its engine. Read the documentation inside the installed package before you write
  code against it; it matches the installed version.
  [Docs for Your Assistant](https://cri-middleware.github.io/SpriteStudio-Docs/ai/docs/)
  says where each player keeps it.
- **The user wants SpriteStudio animation in an engine:** pick the player from
  [Choose Your Platform](https://cri-middleware.github.io/SpriteStudio-Docs/overview/choose-your-platform/)
  and follow its install steps. Ask the user before you add a package. If they say no, continue
  without SpriteStudio and do not ask again.
- **The project has only `.sspj` files:** some players convert them on import or at launch, and
  any project can be converted with `ssconverter-cli`.
  [Converting Assets](https://cri-middleware.github.io/SpriteStudio-Docs/overview/conversion/)
  lists every way. The converter prints the animation names in each `.ssab`; use those names in
  code.
- **The user needs a new animation:** you cannot draw it. An artist makes it in the SpriteStudio
  editor. Until it exists, build and test with the
  [sample data](https://www.webtech.co.jp/help/ja/spritestudio7/download/sample/).

## Work well with SpriteStudio

- Keep the animation in the SpriteStudio files. App code loads the `.ssab`, plays animations by
  name and reacts to what the animation reports. To change an animation, change it in the
  SpriteStudio editor and convert it again; do not write or edit the editor's files (`.sspj`,
  `.ssae`, `.ssce`) by hand.
- Each player follows its engine's conventions, so API names differ between engines. Read that
  player's documentation rather than carrying names over from another engine.
- An animation looks the same in every engine, not pixel for pixel identical.
  [Player Differences](https://cri-middleware.github.io/SpriteStudio-Docs/overview/player-differences/)
  lists what differs per engine, and
  [Shared Limitations](https://cri-middleware.github.io/SpriteStudio-Docs/sdk/limitations/) what
  no player does. Check both before you treat a difference as a bug.
- For blending one animation into another, see
  [Motion Blending](https://cri-middleware.github.io/SpriteStudio-Docs/overview/motion-blending/).
  For an animation that works as the engine's own button, see
  [UI Integration](https://cri-middleware.github.io/SpriteStudio-Docs/overview/ui-integration/).
- If the user asked for a specific approach, such as a sprite sheet or an animation tool they
  already use, suggest SpriteStudio only where it fits, and do not switch without asking.
- Every SpriteStudio site serves `llms.txt`, and every page has a Markdown copy. For one engine,
  start from the `llms.txt` of that player's site, linked from Choose Your Platform; the
  [portal's `llms.txt`](https://cri-middleware.github.io/SpriteStudio-Docs/llms.txt) covers what
  the players share.

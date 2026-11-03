# 🎚️ Motion Blending

One character can play several animations at once and move between them without a cut: a walk
underneath, an aim laid over it, a one-shot reaction crossfaded in. Each piece is an animation the
artist authored on its own in SpriteStudio. The player combines them at runtime, so trying a new
combination needs no re-export, and nothing changes in the `.ssab`.

▶️ Live demos: [PixiJS](https://cri-middleware.github.io/SSPlayerForWeb/examples/pixi/blend.html) and
[WebGL](https://cri-middleware.github.io/SSPlayerForWeb/examples/webgl/blend.html) - crossfades and
overlays on one character, each on a key, with the state of every track beside the picture.

## ✨ What you get

- **Crossfade instead of cut.** Move from idle into an attack over a fraction of a second rather
  than in one frame.
- **Layer one animation over another.** Animations are stacked on tracks: a limp over a walk, a
  blink or a wave over anything. Each track has its own strength, so an overlay can come in at half
  strength, or fade in and out.
- **Blend two animations on one track.** Weight them against each other, as in a walk-to-run blend.
- **Drive a track from a value.** Move a track's playhead yourself instead of playing it, to turn
  a head by a tracked value.
- **Start a cycle in phase.** An animation laid on a track can start at the point track 0's
  animation has reached, so a run laid over a walk half-way through its stride starts half-way
  through its own.
- **One clock for the whole character.** Pausing, resuming and stopping act on every track at once.

The animations you combine come from one `.ssab`, and a few attributes - such as which cell a part
shows - follow the main animation rather than mixing. [Shared Limitations](../sdk/limitations.md)
lists them.

## 🎮 Where to use it

| Player | What you call | Details |
|---|---|---|
| **[Unity](../players/unity.md)** | Methods on `SpriteStudioPlayer` and `SpriteStudioGraphic`, the same on both | [Guide](https://cri-middleware.github.io/SSPlayerForUnity/workflow/motion_blending/) |
| **[Web](../players/web.md)** | Methods on `SSPlayer` in `ssplayer-pixi`, `ssplayer-webgl` and RPG Maker MZ; MZ's **Set SS Track** / **Fade SS Track** / **Clear SS Track** commands; TyranoScript's `[ss_track]` / `[ss_track_fade]` / `[ss_track_clear]` tags and `transition=` on `[ss_play]` | [Guide](https://cri-middleware.github.io/SSPlayerForWeb/customize/motion-blending) |
| **[Godot](../players/godot.md)** | Methods on `SpriteStudioPlayer2D` | [Guide](https://cri-middleware.github.io/SSPlayerForGodot/workflow/motion_blending/) |
| **[Flutter](../players/flutter.md)** | Methods on `SpriteStudioPlayer` | [Guide](https://cri-middleware.github.io/SSPlayerForFlutter/guide/motion-blending/) |
| **[Ren'Py](../players/renpy.md)** | `ss_crossfade`, `ss_set_track_animation` and the other `ss_*` track calls | [Guide](https://cri-middleware.github.io/SSPlayerForRenPy/usage/#mixing-animations) |
| **[wgpu](../players/wgpu.md)** | `SSPlayer` in Rust, `ss_player_*` in C, `SsPlayerWeb` in JavaScript, `SsTrackCommand` in Bevy | [Guide](https://cri-middleware.github.io/SSPlayerForWgpu/guide/motion-blending/) |
| **[React Native](../players/react-native.md)** | The `transitionMs` prop crossfades with no code; the player's track calls do the rest | [Guide](https://cri-middleware.github.io/SSPlayerForReactNative/usage/motion-blending) |

Building a player of your own? The model behind every row - tracks, strength and weight, and why
track 0 is special - is the
[Animation Mixing](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/libs/ssruntime/docs/50_features/10_animation_mixing.md)
chapter of the SDK's Player Porting Guide - see [Porting a Player](../sdk/porting.md).

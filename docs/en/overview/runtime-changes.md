# 🧥 Changing a Character at Runtime

A SpriteStudio animation is not a fixed clip. While it plays, your game or app can hang things off its
parts, swap the artwork it draws with, and recolour, re-cell or hide single parts - for equipment,
costumes, colour variants, damage flashes and health bars - with no new export from SpriteStudio.

▶️ Live demo: the [Override Layer API demo](https://cri-middleware.github.io/SSPlayerForWeb/examples/override/)
applies per-part colour, visibility and cell overrides one at a time while the Ringo sample keeps
playing, with the call behind each step on screen.

## 🎯 Follow a part

Attach something of your own to a part - a weapon in a hand, an effect at a muzzle, a health bar over
a head - and it moves, turns and scales with that part every frame. What follows is yours: a node,
widget or view your engine draws, so it can be anything the engine can show.

A mesh (skinned) part cannot be followed directly; [Shared Limitations](../sdk/limitations.md) says
why, and what to follow instead.

## 🧥 Swap a texture

Replace the image a cell map draws from while the animation plays: a costume, a colour variant, a
piece of equipment, an avatar assembled from parts. Unlike the texture change an artist keys on the
timeline, your code decides when. The cells keep their positions and sizes, so the new image needs
the original's size and layout - the same rule as
[swapping the image alone](./conversion.md#how-a-projects-files-map-to-the-output) after conversion.

## 🎨 Override a part

Set one part's colour, the cell it shows, or whether it is visible, on top of what the animation keys:
tint a character red on damage, hide an accessory, put a different face cell in place. The animation
keeps playing underneath, and clearing the override hands the part back to it.

## 🎮 Where to use it

| Player | Follow a part | Swap a texture | Override a part |
|---|---|---|---|
| **[Unity](../players/unity.md)** | [Guide](https://cri-middleware.github.io/SSPlayerForUnity/workflow/usage_scripting/#part-tracking-following-a-specified-part) | [Guide](https://cri-middleware.github.io/SSPlayerForUnity/workflow/usage_scripting/#dynamic-texture-replacement-cellmap-overrides--avatar-customization) | [Guide](https://cri-middleware.github.io/SSPlayerForUnity/workflow/usage_scripting/#part-overrides-part-color--cell--visibility) |
| **[Web](../players/web.md)** | [Guide](https://cri-middleware.github.io/SSPlayerForWeb/customize/part-following) | [Guide](https://cri-middleware.github.io/SSPlayerForWeb/customize/texture-replacement) | [Guide](https://cri-middleware.github.io/SSPlayerForWeb/customize/part-overrides) |
| **[Godot](../players/godot.md)** | [Guide](https://cri-middleware.github.io/SSPlayerForGodot/workflow/usage_scripting/#part-tracking-following-a-specified-part) | [Guide](https://cri-middleware.github.io/SSPlayerForGodot/workflow/usage_scripting/#dynamic-texture-replacement-avatar-customization) | [Guide](https://cri-middleware.github.io/SSPlayerForGodot/workflow/usage_scripting/#part-overrides-color--cell--visibility) |
| **[Flutter](../players/flutter.md)** | [Guide](https://cri-middleware.github.io/SSPlayerForFlutter/guide/part-following/) | [Guide](https://cri-middleware.github.io/SSPlayerForFlutter/guide/textures/) | [Guide](https://cri-middleware.github.io/SSPlayerForFlutter/guide/part-overrides/) |
| **[Ren'Py](../players/renpy.md)** | [Guide](https://cri-middleware.github.io/SSPlayerForRenPy/usage/#5-part-tracking-following-a-specified-part) | [Guide](https://cri-middleware.github.io/SSPlayerForRenPy/usage/#7-runtime-texture-replacement-costume--expression-changes) | [Guide](https://cri-middleware.github.io/SSPlayerForRenPy/usage/#6-part-overrides-part-color--cell--visibility) |
| **[wgpu](../players/wgpu.md)** | [Guide](https://cri-middleware.github.io/SSPlayerForWgpu/guide/part-overrides/#following-a-part) | [Guide](https://cri-middleware.github.io/SSPlayerForWgpu/guide/texture-replacement/) | [Guide](https://cri-middleware.github.io/SSPlayerForWgpu/guide/part-overrides/) |
| **[React Native](../players/react-native.md)** | [Guide](https://cri-middleware.github.io/SSPlayerForReactNative/usage/parts#following-a-part) | [Guide](https://cri-middleware.github.io/SSPlayerForReactNative/usage/textures#replacing-a-texture) | [Guide](https://cri-middleware.github.io/SSPlayerForReactNative/usage/parts) |

Building a player of your own? The SDK's Player Porting Guide covers these in
[Part Overrides](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/libs/ssruntime/docs/50_features/20_part_overrides.md),
[External Resources & Textures](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/libs/ssruntime/docs/50_features/30_external_resources.md)
and the API conventions for
[reading a part](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/libs/ssruntime/docs/20_design/30_api_conventions.md#9-reading-a-part) -
see [Porting a Player](../sdk/porting.md).

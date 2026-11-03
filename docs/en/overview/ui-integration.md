# 🔘 UI Integration

A SpriteStudio animation can be a button in your app's own UI toolkit: a uGUI `Button` in Unity, a
`BaseButton` in Godot, the `InkWell` or `ElevatedButton` you already use in Flutter. Because it is
that toolkit's button, clicks, keyboard focus, the disabled state and screen readers work as they do
for every other button, while the animation shows which state the button is in.

▶️ [Live demo](https://cri-middleware.github.io/SSPlayerForWeb/examples/pixi/ui.html) - two buttons
drawn by the Ringo sample in a PixiJS app, one taking the pointer only on the parts it names.

## ✨ What you get

- **It is your toolkit's button.** Its events, focus and keyboard navigation, and its disabled state
  stay the toolkit's own, so the button fits the rest of your UI with nothing to re-implement.
- **Every state is drawn in SpriteStudio.** Put a label named after each state - `normal`, `hover`,
  `pressed`, `disabled` and so on - in one animation, and the button plays that section, looping,
  while it is in that state. How each state looks is decided in the editor, not in code. A state
  without a label falls back, in the end to the whole animation, so even a plain looping animation
  makes a working button, and animations you already have can be assigned to states instead.
- **Clicks on the artwork only.** For an irregular shape, name the parts that take the pointer, and
  the rest of the button's box stops taking it.
- **Reduced motion.** With reduced motion on, each state holds still on the first frame of its
  section, and a `reduced_motion` label can give the idle state a calm loop instead.
- **Screen readers.** The button takes the name a screen reader announces; the animation itself stays
  decoration.
- **One animation, every player in the table.** The players below follow the same convention - the
  same state labels, the same fallbacks - so an animation authored as a button works as one on any
  of them. A toggle's on position adds `selected_` labels (`selected_normal`, `selected_hover`,
  ...); Unity, Godot and Ren'Py read them, and the other players play the plain labels.

## 🎮 Where to use it

| Player | The button it becomes | Details |
|---|---|---|
| **[Unity](../players/unity.md)** | A uGUI `Button` or `Toggle`: **SpriteStudio Button** / **SpriteStudio Toggle** (assembly `SpriteStudio.UI`) | [Guide](https://cri-middleware.github.io/SSPlayerForUnity/workflow/ui_buttons/) |
| **[Web](../players/web.md)** - PixiJS | A `@pixi/ui` `ButtonContainer`: `SSButton` (`@spritestudio/ssplayer-pixi-ui`) | [Guide](https://cri-middleware.github.io/SSPlayerForWeb/usage/pixi-ui) |
| **[Godot](../players/godot.md)** | A `BaseButton`: `SpriteStudioButton` | [Guide](https://cri-middleware.github.io/SSPlayerForGodot/workflow/ui_buttons/) |
| **[Flutter](../players/flutter.md)** | Any button that takes a `statesController` (`InkWell`, `ElevatedButton`, ...), drawn by `SpriteStudioStateView` (`package:ssplayer_flutter/ui.dart`) | [Guide](https://cri-middleware.github.io/SSPlayerForFlutter/guide/buttons/) |
| **[Ren'Py](../players/renpy.md)** | A Ren'Py button, like `imagebutton`: `SSButton` | [Guide](https://cri-middleware.github.io/SSPlayerForRenPy/buttons/) |
| **[React Native](../players/react-native.md)** | A `<Pressable>` over the view: `<SpriteStudioButton>` (`react-native-spritestudio-ui`) | [Guide](https://cri-middleware.github.io/SSPlayerForReactNative/usage/ui) |

Building a player of your own? The convention every player follows is the
[UI integration](https://github.com/cri-middleware/SpriteStudio-SDK/blob/HEAD/libs/ssruntime/docs/50_features/80_ui_integration.md)
chapter of the SDK's Player Porting Guide - see [Porting a Player](../sdk/porting.md).

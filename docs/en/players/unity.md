# 🎮 SpriteStudio Player for Unity

Play back SpriteStudio animations in the **Unity Engine**. Playback runs through
`libssruntime` (the shared Rust core) combined with Unity's Job System for high performance.

!!! tip "Editor-first - no code to reach the first frame"
    Install the package, drag your `.sspj` onto the editor, place a component and assign the
    asset. Scripting and Timeline are there when you want them; nothing above needs them.

**1. What you install** - `jp.co.cri-mw.spritestudio.ssplayer-unity`, through Package Manager from
npm (a scoped registry for `jp.co.cri-mw`) or as the tarball from
[GitHub Releases](https://github.com/cri-middleware/SSPlayerForUnity/releases). It runs on both URP and
BRP.

**2. `.sspj` -> `.ssab`** - open **Window > SpriteStudio > Importer** and drag the `.sspj` in.
`libssconverter` is bundled with the package, so there is no separate tool to install, and
re-editing in SpriteStudio updates the Unity asset in place.

**3. Getting it on screen** - drag the generated `SpriteStudioAnimeAsset` from the Project
window into the Hierarchy, pick `SpriteStudioPlayer` (world space) or `SpriteStudioGraphic`
(uGUI Canvas), and press Play: it starts on the pack's first animation.

The steps, with the folders they use, are in the README's [Quick Start](https://github.com/cri-middleware/SSPlayerForUnity#-quick-start).

## ➡️ Read next

- [Documentation](https://cri-middleware.github.io/SSPlayerForUnity/)
- [Repository](https://github.com/cri-middleware/SSPlayerForUnity)
- [Player Differences](../overview/player-differences.md) - what the uGUI Canvas path trades away

# ⚛️ SSPlayerForReactNative

Play SpriteStudio 7 animations in **React Native** apps, on the New Architecture, through a
`<SpriteStudioView>` component.

!!! info "In development"
    This player has not shipped yet. This page exists so the portal has an entry for it; the
    details will be filled in as it lands.

- **Documentation:** _coming soon_
- **Repository:** <https://github.com/cri-middleware/SSPlayerForReactNative>

Once `<SpriteStudioView>` is in your tree, the native side takes over: both the geometry and the
draw happen natively through [React Native Skia](https://shopify.github.io/react-native-skia/),
so what JavaScript does each frame is one call per animation on screen.

React Native has no editor to host an importer in, so converting `.sspj` to `.ssab` is a
host-side step with the SDK's `ssconverter-cli` - see [Converting Assets](../overview/conversion.md).

See [Choose Your Platform](../overview/choose-your-platform.md) to compare players, or
[SDK Concepts](../sdk/concepts.md) for the conversion/playback pipeline shared across all of them.

# ⚛️ SSPlayerForReactNative

Play SpriteStudio 7 animations in **React Native** apps, on the New Architecture, through a
`<SpriteStudioView>` component.

!!! info "In development"
    This player has not shipped yet. This page exists so the portal has an entry for it; the
    details will be filled in as it lands.

- **Documentation:** _coming soon_
- **Repository:** <https://github.com/cri-middleware/SSPlayerForReactNative>

The decision that shapes it is **where a frame is drawn**: the native layer both bakes the
geometry and issues the draw through
[React Native Skia](https://shopify.github.io/react-native-skia/), so JavaScript's per-frame job
is one call per player rather than a crossing per vertex.

React Native has no editor to host an importer in, so converting `.sspj` to `.ssab` is a
host-side step with the SDK's `ssconverter-cli` - see [Converting Assets](../overview/conversion.md).

See [Choose Your Platform](../overview/choose-your-platform.md) to compare players, or
[SDK Concepts](../sdk/concepts.md) for the conversion/playback pipeline shared across all of them.

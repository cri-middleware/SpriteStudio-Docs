# ⚛️ SpriteStudio Player for React Native

Play SpriteStudio animations in **React Native** apps, on the New Architecture, through a
`<SpriteStudioView>` component.

!!! tip "Code-first - and a development build, not Expo Go"
    The package compiles into your app's own binary, so **Expo Go cannot run it**. In a managed
    app that means `npx expo prebuild` then `npx expo run:ios` / `run:android`; a bare app
    rebuilds its existing native projects. Autolinking picks the package up either way.

**1. What you install** - `react-native-spritestudio` and its native peers, added with `npx expo install` - see
[Installation](https://cri-middleware.github.io/SSPlayerForReactNative/setup/install).

**2. `.sspj` -> `.ssab`** - React Native has no editor to host an importer in, so this is a
host-side step with `ssconverter-web`, [SSConverter GUI](./converter.md) or the SDK's
`ssconverter-cli` - see [Converting Assets](../overview/conversion.md). **A pack is a directory, not
a file**, and Metro bundles only what a `require()` names, so the pack folder ships as a native app
asset through the package's Expo config plugin.

**3. Getting it on screen** - a `<SpriteStudioView>` whose `source` names the pack by its path
inside that asset folder.

Once it is in your tree the native side takes over: both the geometry and the draw happen natively
through [React Native Skia](https://shopify.github.io/react-native-skia/), so what JavaScript does
each frame is one call per animation on screen. Alongside the view it ships **`<SpriteStudioScene>`**,
which draws a whole cast through one canvas and one clock.

The steps, with the folders they use, are in the README's [Quick Start](https://github.com/cri-middleware/SSPlayerForReactNative#-quick-start).

## ➡️ Read next

- [Documentation](https://cri-middleware.github.io/SSPlayerForReactNative/)
- [Repository](https://github.com/cri-middleware/SSPlayerForReactNative)
- [Converting Assets](../overview/conversion.md) - picking a tool and putting it in a build pipeline

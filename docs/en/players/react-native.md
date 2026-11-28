---
description: "Play SpriteStudio animations in React Native apps, drawn natively through React Native Skia. SpriteStudio adds bones, mesh and effects to 2D illustrations."
---

# ⚛️ SpriteStudio Player for React Native

Play SpriteStudio animations in **React Native** apps, on the New Architecture, through a
`<SpriteStudioView>` component.

> [!TIP] Code-first - and a development build, not Expo Go
> The package compiles into your app's own binary, so **Expo Go cannot run it**: make a
> development build with `npx expo prebuild`, then `npx expo run:ios` / `run:android`.

**1. What you install** - `react-native-spritestudio` and its native peers, added with `npx expo install` - see
[Installation](https://cri-middleware.github.io/SSPlayerForReactNative/setup/install).

**2. `.sspj` -> `.ssab`** - React Native has no editor to host an importer in, so this is a
host-side step with the browser's [`ssconverter-web`](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/), [SSConverter GUI](./converter.md) or the SDK's
`ssconverter-cli` - see [Converting Assets](../overview/conversion.md). The pack folder ships as a
native app asset through the package's Expo config plugin.

**3. Getting it on screen** - a `<SpriteStudioView>` whose `source` names the pack by its path
inside that asset folder.

The geometry and the draw run natively through
[React Native Skia](https://shopify.github.io/react-native-skia/), so what JavaScript does each
frame is the same few calls per animation on screen, however complex it is. Alongside the view it ships **`<SpriteStudioScene>`**,
which draws a whole cast through one canvas and one clock.

The steps, with the folders they use, are in the README's [Quick Start](https://github.com/cri-middleware/SSPlayerForReactNative#-quick-start).

## ➡️ Read next

- [Documentation](https://cri-middleware.github.io/SSPlayerForReactNative/)
- [Repository](https://github.com/cri-middleware/SSPlayerForReactNative)
- [Converting with a Standalone Tool](../overview/convert-with-a-standalone-tool.md) - picking a tool and putting it in a build pipeline

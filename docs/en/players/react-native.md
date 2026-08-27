# ⚛️ SSPlayerForReactNative

Play SpriteStudio animations in **React Native** apps, on the New Architecture, through a
`<SpriteStudioView>` component.

!!! tip "Code-first - and a development build, not Expo Go"
    The package compiles into your app's own binary, so **Expo Go cannot run it**. In a managed
    app that means `npx expo prebuild` then `npx expo run:ios` / `run:android`; a bare app
    rebuilds its existing native projects. Autolinking picks the package up either way.

**1. What you install** - the package plus its native peers:

```bash
npx expo install react-native-spritestudio @shopify/react-native-skia react-native-nitro-modules react-native-reanimated react-native-worklets
```

🚧 It is not on npm until the first release; until then, run it from a checkout.

**2. `.sspj` -> `.ssab`** - React Native has no editor to host an importer in, so this is a
host-side step with the SDK's `ssconverter-cli` or [SSConverterGUI](./converter.md) - see
[Converting Assets](../overview/conversion.md). **A pack is a directory, not a file**: a `.ssab`
names its textures and its external packs by paths relative to itself, and Metro bundles only what
a `require()` names. So pack directories ship as native app assets - point the Expo config plugin
at yours:

```json
{ "expo": { "plugins": [["react-native-spritestudio", { "assets": ["./assets/ss"] }]] } }
```

**3. Getting it on screen** - address a pack by its path inside that asset root:

```tsx
<SpriteStudioView source="ss/overall/Basic.ssab" animation="anime_1" fit="contain" style={{ flex: 1 }} />
```

Once it is in your tree the native side takes over: both the geometry and the draw happen natively
through [React Native Skia](https://shopify.github.io/react-native-skia/), so what JavaScript does
each frame is one call per animation on screen. Alongside the view it ships **`<SpriteStudioScene>`**,
which draws a whole cast through one canvas and one clock.

## ➡️ Read next

- **Documentation** - *coming soon*
- [Repository](https://github.com/cri-middleware/SSPlayerForReactNative)
- [Converting Assets](../overview/conversion.md) - picking a tool and putting it in a build pipeline

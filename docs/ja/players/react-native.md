# ⚛️ SpriteStudio Player for React Native

**React Native** アプリ（New Architecture）で SpriteStudio アニメーションを再生します。
`<SpriteStudioView>` コンポーネントとして配置できます。

!!! tip "コードで始まる - かつ Expo Go ではなく development build が必要"
    このパッケージはアプリ自身のバイナリに組み込まれるため、**Expo Go では動きません**。
    managed なアプリなら `npx expo prebuild` のあと `npx expo run:ios` / `run:android`、
    bare なアプリなら既存のネイティブプロジェクトを再ビルドします。どちらも autolinking がパッケージを拾います。

**1. 何を入れるか** - パッケージとネイティブ側の peer 依存です。

```bash
npx expo install react-native-spritestudio @shopify/react-native-skia react-native-nitro-modules react-native-reanimated react-native-worklets
```

🚧 初回リリースまでは npm に公開されていません。それまではチェックアウトから実行します。

**2. `.sspj` -> `.ssab`** - React Native にはインポーターを組み込むエディターがないため、
SDK の `ssconverter-cli` か [SSConverter GUI](./converter.md) を使うホスト側の作業になります（[アセットの変換](../overview/conversion.md) を参照）。**パックはファイルではなくディレクトリです**。`.ssab` はテクスチャや外部パックを自身からの相対パスで参照し、Metro は `require()` が名指ししたものしかバンドルしません。そのためパックのディレクトリはネイティブアセットとして同梱します。Expo config plugin に自分のパスを指定してください。

```json
{ "expo": { "plugins": [["react-native-spritestudio", { "assets": ["./assets/ss"] }]] } }
```

**3. どう画面に出すか** - アセットルート内のパスでパックを指定します。

```tsx
<SpriteStudioView source="ss/overall/Basic.ssab" animation="anime_1" fit="contain" style={{ flex: 1 }} />
```

ツリーに置いたあとはネイティブ側が担当します。ジオメトリの生成も描画も
[React Native Skia](https://shopify.github.io/react-native-skia/) を介してネイティブ層で完結するため、JavaScript が毎フレーム行うのは、表示中の 1 アニメーションにつき 1 回の呼び出しだけです。ビューと併せて **`<SpriteStudioScene>`** を同梱しており、複数体を 1 つのキャンバスと 1 つのクロックでまとめて描画できます。

## ➡️ 次に読む

- **ドキュメント** - 🚧 *準備中*
- 🚧 [リポジトリ](https://github.com/cri-middleware/SSPlayerForReactNative)
- [アセットの変換](../overview/conversion.md) - ツールの選び方とビルドパイプラインへの組み込み

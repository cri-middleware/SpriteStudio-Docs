# ⚛️ SpriteStudio Player for React Native

**React Native** アプリ（New Architecture）で SpriteStudio アニメーションを再生します。`<SpriteStudioView>` コンポーネントとして配置できます。

!!! tip "コードで始まる - Expo Go ではなく development build が必要"
    このパッケージはアプリ自身のバイナリに組み込まれるため、**Expo Go では動きません**。`npx expo prebuild` のあと `npx expo run:ios` / `run:android` で development build を作ります。

**1. 何を入れるか** - `react-native-spritestudio` とネイティブ側の peer 依存を `npx expo install` で入れます（[インストール](https://cri-middleware.github.io/SSPlayerForReactNative/ja/setup/install) を参照）。

**2. `.sspj` -> `.ssab`** - React Native にはインポーターを組み込むエディターがないため、ブラウザで動く [`ssconverter-web`](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/)、[SSConverter GUI](./converter.md)、SDK の `ssconverter-cli` のいずれかを使うホスト側の作業になります（[アセットの変換](../overview/conversion.md) を参照）。パックのフォルダは、パッケージの Expo config plugin でネイティブアセットとして同梱します。

**3. どう画面に出すか** - `source` にそのアセットフォルダ内のパスを指定した `<SpriteStudioView>` を置きます。

ジオメトリの生成も描画も [React Native Skia](https://shopify.github.io/react-native-skia/) を介してネイティブ層で行うため、JavaScript が毎フレーム行うのは、表示中のアニメーションごとに、どれほど複雑でも同じ数回の呼び出しだけです。ビューと併せて **`<SpriteStudioScene>`** を同梱しており、複数体を 1 つのキャンバスと 1 つのクロックでまとめて描画できます。

フォルダを含めた手順は、README の[クイックスタート](https://github.com/cri-middleware/SSPlayerForReactNative/blob/HEAD/README.ja.md#-クイックスタート)にあります。

## ➡️ 次に読む

- [ドキュメント](https://cri-middleware.github.io/SSPlayerForReactNative/ja/)
- [リポジトリ](https://github.com/cri-middleware/SSPlayerForReactNative)
- [スタンドアロンツールでの変換](../overview/convert-with-a-standalone-tool.md) - ツールの選び方とビルドパイプラインへの組み込み

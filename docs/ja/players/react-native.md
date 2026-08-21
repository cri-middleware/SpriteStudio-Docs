# ⚛️ SSPlayerForReactNative

**React Native** アプリ（New Architecture）で SpriteStudio 7 アニメーションを再生します。
`<SpriteStudioView>` コンポーネントとして配置できます。

!!! info "開発中"
    この Player はまだリリースされていません。このページはポータル上の入口を用意するための
    もので、詳細は実装の進行にあわせて追記します。

- **ドキュメント:** _準備中_
- **リポジトリ:** <https://github.com/cri-middleware/SSPlayerForReactNative>

`<SpriteStudioView>` を置いたあとは、ネイティブ側が担当します。ジオメトリの生成も描画も
[React Native Skia](https://shopify.github.io/react-native-skia/) を介してネイティブ層で
完結するため、JavaScript が毎フレーム行うのは、表示中の 1 アニメーションにつき 1 回の
呼び出しだけです。

React Native にはインポーターを組み込むエディターがないため、`.sspj` から `.ssab` への変換は
SDK の `ssconverter-cli` を使うホスト側の作業になります。詳しくは
[アセットの変換](../overview/conversion.md) を参照してください。

Player の比較は [プラットフォームの選び方](../overview/choose-your-platform.md) を、
全 Player 共通の変換／再生パイプラインは [SDK コンセプト](../sdk/concepts.md) を参照してください。

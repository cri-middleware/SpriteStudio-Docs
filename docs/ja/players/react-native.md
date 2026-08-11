# ⚛️ SSPlayerForReactNative

**React Native** アプリ（New Architecture）で SpriteStudio 7 アニメーションを再生します。
`<SpriteStudioView>` コンポーネントとして配置できます。

!!! info "開発中"
    この Player はまだリリースされていません。このページはポータル上の入口を用意するための
    もので、詳細は実装の進行にあわせて追記します。

- **ドキュメント:** _準備中_
- **リポジトリ:** <https://github.com/cri-middleware/SSPlayerForReactNative>

設計上の要は **フレームをどこで描画するか** です。ジオメトリの生成も描画も
[React Native Skia](https://shopify.github.io/react-native-skia/) を介してネイティブ側で
完結するため、JavaScript 側のフレームごとの処理は、頂点ごとの往復ではなく Player 1 つにつき
1 回の呼び出しで済みます。

React Native にはインポーターを組み込むエディターがないため、`.sspj` から `.ssab` への変換は
SDK の `ssconverter-cli` を使うホスト側の作業になります。詳しくは
[アセットの変換](../overview/conversion.md) を参照してください。

Player の比較は [プラットフォームの選び方](../overview/choose-your-platform.md) を、
全 Player 共通の変換／再生パイプラインは [SDK コンセプト](../sdk/concepts.md) を参照してください。

# 📱 SSPlayerForFlutter

**Flutter** アプリで SpriteStudio 7 アニメーションを再生します。`libssruntime` を基盤とし、
`SpriteStudioView` ウィジェットが Flutter の各ターゲットで通常のウィジェットと同様に合成されます。

- **ドキュメント:** _準備中_
- **Web デモ:** [ウィジェット版](https://cri-middleware.github.io/SSPlayerForFlutter/demo/flutter/) ・ [Flame 版](https://cri-middleware.github.io/SSPlayerForFlutter/demo/flame/) - インストール不要でブラウザから試せます
- **リポジトリ:** <https://github.com/cri-middleware/SSPlayerForFlutter>

Player 本体に加えて、次のものが提供されます。

- **[Flame](https://flame-engine.org/) アダプター** - Flame 製ゲームにアニメーションを組み込めます。
- **同梱の `ssconvert` CLI** - `.sspj` プロジェクトを `.ssab` に変換します。
- **ライブリロード** - 編集内容が実行中のアプリに反映されます。

Player の比較は [プラットフォームの選び方](../overview/choose-your-platform.md) を、
全 Player 共通の変換／再生パイプラインは [SDK コンセプト](../sdk/concepts.md) を参照してください。

# 🦀 SSPlayerForWgpu

SpriteStudio 7 アニメーションを再生する、**Rust** 製で [wgpu](https://wgpu.rs/) 描画の
Player です。wgpu が WebGPU・Vulkan・DX12・Metal の違いを吸収するため、同じ Player が
どのバックエンドでも動きます。ホスト側は Rust とは限らず、C / C++ とブラウザにも同じ
ライブラリから提供します。

- **ドキュメント:** _準備中_
- **リポジトリ:** <https://github.com/cri-middleware/SSPlayerForWgpu>

設計上の要は **借用モデル** です。Player は wgpu の `Device` / `Queue` / `Surface` を所有せず、
ホスト側が所有してフレームごとに貸し出します。そのため、特定のエンジンに縛られることなく、
自作レンダラーでも、すでに自前のデバイスを持つゲームエンジンでも、wgpu を使う
アプリケーションであれば同居できます。

同じコアの上に、1 つのライブラリが 3 つの顔を持ちます。

- **Rust** - `SSRenderer` / `SSScene` / `SSPlayer`。他の 2 つはこの API のラッパーです。
- **C / C++** - cdylib・staticlib と生成ヘッダー。Metal・DX12・Vulkan のビューアーをサンプルとして
  同梱しています。
- **ブラウザの WebGPU** - wasm をまとめた npm パッケージと、その上の `<ss-player-webgpu>`
  カスタム要素。

いずれの経路にもインポーターはないため、`.sspj` から `.ssab` への変換はスタンドアロンツールを
使うホスト側の作業になります。詳しくは [アセットの変換](../overview/conversion.md) を参照して
ください。

Player の比較は [プラットフォームの選び方](../overview/choose-your-platform.md) を、
全 Player 共通の変換／再生パイプラインは [SDK コンセプト](../sdk/concepts.md) を参照してください。

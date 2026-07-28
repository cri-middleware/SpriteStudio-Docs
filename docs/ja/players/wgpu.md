# 🦀 SSPlayerForWgpu

SpriteStudio 7 アニメーションを再生する **Rust** 向け Player です。[wgpu](https://wgpu.rs/) で
描画するため、WebGPU・Vulkan・DX12・Metal・GL を単一のコードパスでカバーします。

!!! info "開発中"
    この Player はまだリリースされていません。このページはポータル上の入口を用意するための
    もので、詳細は実装の進行にあわせて追記します。

- **ドキュメント:** _準備中_
- **リポジトリ:** <https://github.com/cri-middleware/SSPlayerForWgpu>

設計上の要は **借用モデル** です。Player は wgpu の `Device` / `Queue` / `Surface` を所有せず、
ホスト側が所有してフレームごとに貸し出します。そのため、特定のエンジンに縛られることなく、
自作レンダラーでも他のエンジンでも、任意の wgpu アプリケーションに同居できます。

Player の比較は [プラットフォームの選び方](../overview/choose-your-platform.md) を、
全 Player 共通の変換／再生パイプラインは [SDK コンセプト](../sdk/concepts.md) を参照してください。

# 🦀 SSPlayerForWgpu

**Rust** で書かれ、[wgpu](https://wgpu.rs/) を通じて描画する SpriteStudio 7 用の Player です。
wgpu は WebGPU・Vulkan・DX12・Metal を 1 つの API の下にまとめるため、同じ Player がそのどれでも
動きます。ホスト側は Rust である必要はなく、C・C++・ブラウザも同じライブラリから利用できます。

!!! tip "コードで始まる - 1 つのライブラリに 3 つのフェイス"
    どのフェイスを入れるかで決まるのは書く言語であって、Player にできることではありません。
    Rust の API が本体で、他の 2 つはそれを別名で包んだものです。

**1. 何を入れるか** - ホストに合うフェイスを選びます。
[SpriteStudio-SDK](https://github.com/cri-middleware/SpriteStudio-SDK) が private の間は、下の
どの経路にも SDK へのアクセスが必要です。この Player は `ssruntime` と `ssab` を、公開された
C-API 経由ではなく Rust クレートとしてリンクするため、SDK は git submodule として入ります。

| ホスト | 追加するもの |
|---|---|
| **Rust** アプリ | `ssplayer-wgpu` を git 依存として追加します。submodule は Cargo が取得するので、他のツールは不要です。🚧 SDK クレートの公開が先なので、crates.io にはまだありません。 |
| **Bevy** アプリ | 代わりに `ssplayer-wgpu-bevy` を追加します。Player 本体を引き込み、`SsPlayer` / `SsTransform` / `SsPlayback` の 3 コンポーネントを追加します。 |
| **C / C++** アプリ | cdylib / staticlib と生成されたヘッダー。リポジトリで `scripts/build.sh` を実行すると `bin/` にまとまります。🚧 ビルド済みの配布はまだありません。 |
| **ブラウザ**（WebGPU） | npm パッケージ `@spritestudio/ssplayer-wgpu`。wasm と TypeScript 層、`<ss-player-webgpu>` カスタム要素は独立したエントリポイントです。🚧 npm 未公開です。 |

**2. `.sspj` -> `.ssab`** - この Player はインポーターを持たず、実行時に変換も行いません。
デスクトップ版 [SSConverterGUI](./converter.md) か SDK の `ssconverter-cli` を使うホスト側の
作業になります（[アセットの変換](../overview/conversion.md) を参照）。試すだけなら自分の素材は
不要です。同梱サンプルは SDK 自身のテストアニメーションで動きます。

**3. どう画面に出すか** - デバイスごとに `SSRenderer` を 1 つ、描画ターゲットごとに `SSScene`
を 1 つ、そこに任意の数の `SSPlayer` を 1 パスで描画します。

```rust
let mut renderer = SSRenderer::new(&device);
let mut scene = SSScene::new(&device, &SceneConfig { color_format, stencil_format });

let mut player = SSPlayer::new();
player.load("assets/overall/Basic.ssab")?;   // パック・アトラス・関連パックを 1 回で読み込む
player.set_animation("Basic")?;
player.play();

scene.update(&mut renderer, &device, &queue, delta_secs, &mut [&mut player]);
scene.draw(&renderer, &mut rpass);           // ホストが開いたパスへ描画する
```

C と JavaScript のフェイスも、名前が違うだけで同じ形です。Bevy アプリではアダプターがこれを
代行するので、3 つのコンポーネントを spawn すればキャラクターが Bevy 自身の 2D パスに入ります。

## 🔩 デバイスをホストが持ち続ける理由

この Player の設計を決めているのは **borrow モデル**です。Player は wgpu の
`Device` / `Queue` / `Surface` を所有せず、ホストが所有してフレームごとに貸します。上の
`scene.draw` が「*あなたが*開いたパスへ描画する」形になっているのはそのためです。おかげで
この Player は、自作レンダラーでも、既にデバイスを持っているエンジンでも、任意の wgpu
アプリケーションの中に相乗りでき、特定のホストに縛られません。

**Bevy** アダプターが小さく収まっているのも同じ理由です。アダプターは Bevy が既に所有している
デバイスの上に描くため、キャラクターは 2 つ目のレンダラーを通らず Bevy 自身の 2D パスに入ります。
バージョンは Player 側ではなく Bevy のリリースラインに追従し、一度に 1 ラインだけを対象とします。
Bevy と Player が単一の `wgpu` に解決される必要があり、食い違えば実行時ではなくコンパイルエラーに
なるためです。どのラインを対象にしているかと、Bevy アプリ側に必要なカメラ設定は、リポジトリに
記載があります。

## ➡️ 次に読む

- **ドキュメント** - *準備中*
- [リポジトリ](https://github.com/cri-middleware/SSPlayerForWgpu) - 公開までは各クレートの README が参照先です
- [アセットの変換](../overview/conversion.md) - ツールの選び方とビルドパイプラインへの組み込み

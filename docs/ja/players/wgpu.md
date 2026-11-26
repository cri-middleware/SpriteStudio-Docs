---
description: "Rust の wgpu で SpriteStudio のアニメーションを再生する。同じライブラリを C / C++・ブラウザ・Bevy からも使える。SpriteStudio は、手持ちのイラストにボーン・メッシュ・エフェクトを付けて動かす 2D アニメーションツールです。"
---

# 🦀 SpriteStudio Player for wgpu

**Rust** で書かれ、[wgpu](https://wgpu.rs/) を通じて描画する SpriteStudio 用の Player です。wgpu は WebGPU・Vulkan・DX12・Metal を 1 つの API の下にまとめるため、同じ Player がそのどれでも動きます。ホスト側は Rust である必要はなく、C・C++・ブラウザも同じライブラリから利用できます。

▶️ インストール不要で試せます: WebGPU のデモがブラウザで動きます -
[ブラウザで試す](../overview/try-it.md)。

!!! tip "コードで始まる - 1 つのライブラリに 4 つの Face"
    どの Face を入れるかで、書く言語が決まります。C と JavaScript の Face は Rust の API を別名で包んだもので、Bevy アダプターはその上に構築されています。

**1. 何を入れるか** - ホストに合う Face を選びます。

| ホスト | 追加するもの |
|---|---|
| **Rust** アプリ | `cargo add ssplayer-wgpu`。未リリースの変更を使うならリポジトリを git 依存にします（ビルドに使う SpriteStudio-SDK の submodule も Cargo が取得します）。 |
| **Bevy** アプリ | 代わりに `cargo add ssplayer-bevy`（git 依存でも可）。Player 本体を引き込み、`SsPlayer` / `SsTransform` / `SsPlayback` の 3 コンポーネントを追加します。 |
| **C / C++** アプリ | cdylib / staticlib と生成されたヘッダー。Windows と macOS 向けのビルド済みのものが [GitHub Releases](https://github.com/cri-middleware/SSPlayerForWgpu/releases?expanded=true) に `ssplayer-wgpu-<platform>-<arch>.zip` としてあります。Linux の場合や Windows の DLL が必要な場合は、チェックアウトで `scripts/build.sh` を実行して `bin/` にビルドします。 |
| **ブラウザ**（WebGPU） | npm パッケージ `@spritestudio/ssplayer-wgpu`。wasm とその上の TypeScript 層で、`<ss-player-webgpu>` カスタム要素は独立したエントリポイントにあります。 |

**2. `.sspj` -> `.ssab`** - この Player はインポーターを持たず、実行時に変換も行いません。ブラウザで動く [`ssconverter-web`](https://cri-middleware.github.io/SSPlayerForWeb/ssconverter/)、デスクトップ版 [SSConverter GUI](./converter.md)、SDK の `ssconverter-cli` のいずれかを使うホスト側の作業になります（[アセットの変換](../overview/conversion.md) を参照）。

**3. どう画面に出すか** - デバイスごとに `SSRenderer` を 1 つ、描画ターゲットごとに `SSScene`
を 1 つ、そこに任意の数の `SSPlayer` を、ホストが開いたレンダーパスの中で 1 パスで描画します。

Bevy アプリではアダプターがこれを代行するので、3 つのコンポーネントを spawn すればキャラクターが Bevy 自身の 2D パスに入ります。

Face ごとの手順は、README の[インストール](https://github.com/cri-middleware/SSPlayerForWgpu/blob/HEAD/README.ja.md#-インストール)にあります。

## 🔩 自分のレンダーパスへ描き込む

C とブラウザの Face は自前のデバイスを作って自分のフレームを描くので、キャラクターを自分のレンダーパスへ描き込めるのは Rust だけです（直接、または Bevy のリリースラインに 1 つずつ追従する Bevy アダプター経由）。理由は [borrow モデル](https://cri-middleware.github.io/SSPlayerForWgpu/ja/wgpu/borrow-model/) にあります。

## ➡️ 次に読む

- [ドキュメント](https://cri-middleware.github.io/SSPlayerForWgpu/ja/)
- [リポジトリ](https://github.com/cri-middleware/SSPlayerForWgpu)
- [スタンドアロンツールでの変換](../overview/convert-with-a-standalone-tool.md) - ツールの選び方とビルドパイプラインへの組み込み

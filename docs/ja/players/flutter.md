---
description: "Flutter アプリと Flame のゲームで SpriteStudio のアニメーションを再生する。変換 CLI とライブリロード付き。SpriteStudio は、手持ちのイラストにボーン・メッシュ・エフェクトを付けて動かす 2D アニメーションツールです。"
---

# 📱 SpriteStudio Player for Flutter

**Flutter** アプリで SpriteStudio アニメーションを再生します。`libssruntime` を基盤とし、`SpriteStudioAnimation` ウィジェットが通常のウィジェットと同様に合成されます。

▶️ インストール不要で試せます: ウィジェット版と Flame 版のデモがブラウザで動きます -
[ブラウザで試す](../overview/try-it.md)。

> [!TIP] コードで始まる - Rust ツールチェーンは不要
> ネイティブコアはビルドではなく取得されます。最初のビルドでビルド済みのランタイムをダウンロードし、コンバーターも同じように取得します。

**1. 何を入れるか** - pub.dev の `ssplayer_flutter` です（`flutter pub add ssplayer_flutter`）。`ssruntime_dart` は一緒に入ります。変換用に、`ssconverter_dart` を dev 依存として追加します（`flutter pub add --dev ssconverter_dart`。[インストール](https://cri-middleware.github.io/SSPlayerForFlutter/ja/guide/install/) を参照）。

**2. `.sspj` -> `.ssab`** - SpriteStudio プロジェクトを `SpriteStudio_Source/` 以下に置き、`ssconverter_dart` の `ssconvert` CLI で変換して、出力したフォルダを `pubspec.yaml` の `assets:` に登録します。1 つの `.sspj` からアニメーションパックごとに 1 つの `.ssab` ができます。

**3. どう画面に出すか** - `.ssab` のアセットのパスを渡した `SpriteStudioAnimation.asset(…)` ウィジェットを 1 つ置きます。再生を自分で制御するときは、`SpriteStudioPlayer` を `SpriteStudioView` に渡します。

フォルダを含めた手順は、README の[クイックスタート](https://github.com/cri-middleware/SSPlayerForFlutter/blob/HEAD/README.ja.md#-クイックスタート)にあります。

Player 本体に加えて、次のものが提供されます。

- **[Flame](https://flame-engine.org/) アダプター** - `ssplayer_flame` で、Flame 製ゲームにアニメーションを組み込めます。
- **[ライブリロード](https://cri-middleware.github.io/SSPlayerForFlutter/ja/guide/live-reload/)** - SpriteStudio で保存した時点で、変更されたプロジェクトだけが再変換され、デバッグ実行中のアプリに反映されます。

## ➡️ 次に読む

- [ドキュメント](https://cri-middleware.github.io/SSPlayerForFlutter/ja/)
- [リポジトリ](https://github.com/cri-middleware/SSPlayerForFlutter)
- [ブラウザで試す](../overview/try-it.md) - 上記 2 つのデモと、他 Player の実動ビルド

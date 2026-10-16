# 📱 SpriteStudio Player for Flutter

**Flutter** アプリで SpriteStudio アニメーションを再生します。`libssruntime` を基盤とし、`SpriteStudioView` ウィジェットが Flutter の各ターゲットで通常のウィジェットと同様に合成されます。

▶️ インストール不要で試せます: ウィジェット版と Flame 版のデモがブラウザで動きます -
[ブラウザで試す](../overview/try-it.md)。

!!! tip "コードで始まる - ただし Rust ツールチェーンは不要"
    ネイティブコアはビルドではなく取得されます。`ssruntime_dart` の native assets フックが、固定された SDK リリースからビルド済みの `libssruntime` をダウンロードし、コンバーターも同じ仕組みで `libssconverter` を取得します。

**1. 何を入れるか** - pub.dev の `ssplayer_flutter` です（`flutter pub add ssplayer_flutter`）。`ssruntime_dart` は一緒に入ります。変換用に、`ssconverter_dart` を dev 依存として追加します（`flutter pub add --dev ssconverter_dart`。[インストール](https://cri-middleware.github.io/SSPlayerForFlutter/ja/guide/install/) を参照）。

**2. `.sspj` -> `.ssab`** - SpriteStudio プロジェクトを `SpriteStudio_Source/` 以下に置き、`ssconverter_dart` の `ssconvert` CLI で変換します。1 つの `.sspj` からアニメーションパックごとに 1 つの `.ssab` ができます。

```bash
dart run ssconverter_dart:ssconvert -e -o assets/spritestudio/MyChar/ SpriteStudio_Source/MyChar/MyChar.sspj
```

**3. どう画面に出すか** - `await player.loadAsset('assets/spritestudio/MyChar/MyChar.ssab')`
でロードし、アニメーションを設定して `SpriteStudioView(player: player, …)` をウィジェットツリーに置きます。

Player 本体に加えて、次のものが提供されます。

- **[Flame](https://flame-engine.org/) アダプター** - Flame 製ゲームにアニメーションを組み込めます。
- **ライブリロード** - `flutter run` と並べて `sswatch` を実行すると、SpriteStudio で保存した時点で変更されたプロジェクトだけが再変換され、実行中のアプリに反映されます。

## ➡️ 次に読む

- [ドキュメント](https://cri-middleware.github.io/SSPlayerForFlutter/ja/)
- [リポジトリ](https://github.com/cri-middleware/SSPlayerForFlutter)
- [ブラウザで試す](../overview/try-it.md) - 上記 2 つのデモと、他 Player の実動ビルド

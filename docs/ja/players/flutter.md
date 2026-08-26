# 📱 SSPlayerForFlutter

**Flutter** アプリで SpriteStudio 7 アニメーションを再生します。`libssruntime` を基盤とし、
`SpriteStudioView` ウィジェットが Flutter の各ターゲットで通常のウィジェットと同様に合成されます。

▶️ インストール不要で試せます: [ウィジェット版デモ](https://cri-middleware.github.io/SSPlayerForFlutter/demo/flutter/)、
[Flame 版デモ](https://cri-middleware.github.io/SSPlayerForFlutter/demo/flame/) はどちらもブラウザで動きます。

!!! tip "コードで始まる - ただし Rust ツールチェーンは不要"
    ネイティブコアはビルドではなく取得されます。`ssruntime_dart` の native assets フックが、
    固定された SDK リリースからビルド済みの `libssruntime` をダウンロードし、コンバーターも
    同じ仕組みで `libssconverter` を取得します。

**1. 何を入れるか** - `pubspec.yaml` に `ssplayer_flutter` の依存を追加します。🚧 パッケージが
pub.dev に公開されるまでは、
[GitHub Releases](https://github.com/cri-middleware/SSPlayerForFlutter/releases) のバンドルを
ダウンロードしてプロジェクト内に展開し、
`vendor/SSPlayerForFlutter/packages/ssplayer_flutter` への path 依存を指定します
（`packages/` の構造が保たれているため、推移依存の `ssruntime_dart` も解決されます）。

**2. `.sspj` -> `.ssab`** - SpriteStudio プロジェクトを `SpriteStudio_Source/` 以下に置き、
同梱の CLI で変換します。1 つの `.sspj` からアニメーションパックごとに 1 つの `.ssab` ができます。

```bash
dart run ssconverter_dart:ssconvert -e -o assets/spritestudio/MyChar/ SpriteStudio_Source/MyChar/MyChar.sspj
```

**3. どう画面に出すか** - `await player.loadAsset('assets/spritestudio/MyChar/MyChar.ssab')`
でロードし、アニメーションを設定して `SpriteStudioView(player: player, …)` をウィジェット
ツリーに置きます。

Player 本体に加えて、次のものが提供されます。

- **[Flame](https://flame-engine.org/) アダプター** - Flame 製ゲームにアニメーションを組み込めます。
- **ライブリロード** - `flutter run` と並べて `sswatch` を実行すると、SpriteStudio 7 で保存した
  時点で変更されたプロジェクトだけが再変換され、実行中のアプリに反映されます。

## ➡️ 次に読む

- **ドキュメント** - *準備中*
- [リポジトリ](https://github.com/cri-middleware/SSPlayerForFlutter)
- [ブラウザで試す](../overview/try-it.md) - 上記 2 つのデモと、他 Player の実動ビルド

# 🤝 サポート

SDK と各公式 Player はそれぞれ別のリポジトリです。そのため最初に迷うのは、たいてい**どこに聞けばよいか** です。このページはその振り分けを行います（各リポジトリにも、同じ窓口を記載した `SUPPORT.md` があります）。

## 🛠️ 不具合報告・機能要望 - GitHub Issues

該当するコードを持つリポジトリへ投稿してください。投稿前に既存の Issue を検索してください。

| リポジトリ | Issues | 対象 |
|---|---|---|
| [SpriteStudio-SDK](https://github.com/cri-middleware/SpriteStudio-SDK) | [Issues](https://github.com/cri-middleware/SpriteStudio-SDK/issues) | 変換結果、再生計算、`.ssab` / `.ssqb` フォーマット、`ssconverter-cli` |
| [SSPlayerForUnity](https://github.com/cri-middleware/SSPlayerForUnity) | [Issues](https://github.com/cri-middleware/SSPlayerForUnity/issues) | Unity へのインポート、コンポーネント、描画 |
| [SSPlayerForWeb](https://github.com/cri-middleware/SSPlayerForWeb) | [Issues](https://github.com/cri-middleware/SSPlayerForWeb/issues) | ブラウザ向け Player 群、RPG ツクール MZ・TyranoScript・ティラノビルダー用プラグイン、`ssconverter-web` |
| [SSPlayerForGodot](https://github.com/cri-middleware/SSPlayerForGodot) | [Issues](https://github.com/cri-middleware/SSPlayerForGodot/issues) | GDExtension / カスタムモジュール、SS Importer ドック |
| [SSPlayerForFlutter](https://github.com/cri-middleware/SSPlayerForFlutter) | [Issues](https://github.com/cri-middleware/SSPlayerForFlutter/issues) | `SpriteStudioAnimation` と `SpriteStudioView`、Flame アダプター、`ssconvert` |
| [SSPlayerForRenPy](https://github.com/cri-middleware/SSPlayerForRenPy) | [Issues](https://github.com/cri-middleware/SSPlayerForRenPy/issues) | Ren'Py の Displayable、自動インポート |
| [SSPlayerForWgpu](https://github.com/cri-middleware/SSPlayerForWgpu) | [Issues](https://github.com/cri-middleware/SSPlayerForWgpu/issues) | Rust クレートと C / C++・ブラウザの各 Face、Bevy アダプター |
| [SSPlayerForReactNative](https://github.com/cri-middleware/SSPlayerForReactNative) | [Issues](https://github.com/cri-middleware/SSPlayerForReactNative/issues) | `<SpriteStudioView>` / `<SpriteStudioScene>`、ネイティブモジュール、Skia 描画 |
| [SSConverterGUI](https://github.com/cri-middleware/SSConverterGUI) | [Issues](https://github.com/cri-middleware/SSConverterGUI/issues) | デスクトップアプリ本体（UI・ファイル選択・パッケージング） |

### 🧭 どこに出せばよいか分からないときは

問題が出る場所で選びます。

| 起きていること | 投稿先 |
|---|---|
| 変換結果が壊れている／変換中にクラッシュする | **SpriteStudio-SDK** |
| 試したどの Player でも **同じ壊れ方** をする | **SpriteStudio-SDK** |
| 特定のエンジンでのみ壊れる | その **Player** のリポジトリ（先に [Player ごとの違い](./overview/player-differences.md) を確認） |

既知の制約は [共通の制限事項](./sdk/limitations.md) にあります。

## ❓ 使い方の質問 - コミュニティフォーラム

使い方の質問、実装の相談、他の開発者との情報交換は、Issues ではなく公式フォーラムをご利用ください。

👉 [**SpriteStudio コミュニティ**](https://spritestudio.jp/community/)

## 🔒 個別のお問い合わせ・大容量の再現データ

非公開でのご相談、機微な内容の報告、大きな再現データ（`.sspj` プロジェクト等）の送付、契約に基づくサポートは、公式のヘルプセンターをご利用ください。フォーム内にファイルアップロード機能があり、8 MB までの zip ファイルを添付できます。

👉 [**ヘルプセンター（お問い合わせフォーム）**](https://www.webtech.co.jp/help/ja/spritestudio7/inquiries/ssplayer_tool/)

> [!NOTE] SpriteStudio 本体について
> **エディター**（オーサリング、SpriteStudio アプリケーション、ツール自体のライセンス）に関するお問い合わせは、Player のリポジトリではなく、同じヘルプセンターから
> [CRI Middleware](https://www.webtech.co.jp/spritestudio/) へお願いします。お問い合わせの前に、[**SpriteStudio ヘルプセンター**](https://www.webtech.co.jp/help/ja/spritestudio7/) に初心者ガイド・ユーザーガイド・チュートリアル動画・逆引きリファレンスがそろっています。

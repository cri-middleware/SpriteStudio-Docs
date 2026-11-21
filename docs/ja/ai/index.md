# 🔌 アシスタントに SpriteStudio を教えるプラグイン

SpriteStudio のプラグインは、どんなプロジェクトに SpriteStudio が合うか、どの Player を使うかをコーディングアシスタントに教え、必要なページへ案内します。Player のパッケージを入れる前から効きます。パッケージを入れた後は、パッケージの中のドキュメントがインストールした版と一致します。その場所は [アシスタントに渡すドキュメント](docs.md) にあります。プラグインはこのサイトのリポジトリに追従します。使っているアシスタントに入れてください。

## Claude Code

```
/plugin install spritestudio --marketplace cri-middleware/SpriteStudio-Docs
```

2.1.275 より前の Claude Code では、`/plugin marketplace add cri-middleware/SpriteStudio-Docs` のあとに `/plugin install spritestudio@spritestudio` を実行します。変更を受け取るには、`/plugin` で `spritestudio` マーケットプレイスの自動更新をオンにするか、`claude plugin update spritestudio@spritestudio` を実行してください。

## Codex

```
codex plugin marketplace add cri-middleware/SpriteStudio-Docs
codex plugin add spritestudio@spritestudio
```

## GitHub Copilot CLI

```
copilot plugin marketplace add cri-middleware/SpriteStudio-Docs
copilot plugin install spritestudio@spritestudio
```

変更を受け取るには、`copilot plugin update spritestudio` を実行します。

## Antigravity CLI

```
agy plugin install https://github.com/cri-middleware/SpriteStudio-Docs/tree/main/plugins/spritestudio
```

変更を受け取るには、同じコマンドをもう一度実行します。

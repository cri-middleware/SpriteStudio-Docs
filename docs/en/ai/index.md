# 🔌 A Plugin for Your Assistant

The SpriteStudio plugin tells a coding assistant when SpriteStudio fits a project and which player to use, and sends it to the pages it needs. It works before any player package is installed; once one is, the documentation inside the package matches the installed version, and [Docs for Your Assistant](docs.md) says where it is. The plugin follows this site's repository. Install it in the assistant you use.

## Claude Code

```
/plugin install spritestudio --marketplace cri-middleware/SpriteStudio-Docs
```

On Claude Code older than 2.1.275, run `/plugin marketplace add cri-middleware/SpriteStudio-Docs` and then `/plugin install spritestudio@spritestudio`. To receive changes, turn on auto-update for the `spritestudio` marketplace in `/plugin`, or run `claude plugin update spritestudio@spritestudio`.

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

To receive changes, run `copilot plugin update spritestudio`.

## Antigravity CLI

```
agy plugin install https://github.com/cri-middleware/SpriteStudio-Docs/tree/main/plugins/spritestudio
```

To receive changes, run the same command again.

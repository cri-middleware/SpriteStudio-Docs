# 🤝 Support

The SDK and every official player are separate repositories, so the first question is usually
**where to ask**. This page routes you; most repositories also ship their own `SUPPORT.md`
listing the same channels.

## 🛠️ Bugs & feature requests - GitHub Issues

File these in the repository that owns the code. Search existing issues first.

| Repository | Issues | Use it for |
|---|---|---|
| 🚧 [SpriteStudio-SDK](https://github.com/cri-middleware/SpriteStudio-SDK) | 🚧 [Issues](https://github.com/cri-middleware/SpriteStudio-SDK/issues) | Conversion output, playback math, the `.ssab` / `.ssqb` format, `ssconverter-cli` |
| 🚧 [SSPlayerForUnity](https://github.com/cri-middleware/SSPlayerForUnity) | 🚧 [Issues](https://github.com/cri-middleware/SSPlayerForUnity/issues) | Unity import, components, rendering |
| 🚧 [SSPlayerForWeb](https://github.com/cri-middleware/SSPlayerForWeb) | 🚧 [Issues](https://github.com/cri-middleware/SSPlayerForWeb/issues) | The browser players and `ssconverter-web` |
| [SSPlayerForGodot](https://github.com/cri-middleware/SSPlayerForGodot) | [Issues](https://github.com/cri-middleware/SSPlayerForGodot/issues) | The GDExtension / custom module, SS Import Dock |
| 🚧 [SSPlayerForFlutter](https://github.com/cri-middleware/SSPlayerForFlutter) | 🚧 [Issues](https://github.com/cri-middleware/SSPlayerForFlutter/issues) | `SpriteStudioView`, the Flame adapter, `ssconvert` |
| 🚧 [SSPlayerForRenPy](https://github.com/cri-middleware/SSPlayerForRenPy) | 🚧 [Issues](https://github.com/cri-middleware/SSPlayerForRenPy/issues) | The Ren'Py displayable, auto-import |
| 🚧 [SSPlayerForWgpu](https://github.com/cri-middleware/SSPlayerForWgpu) | 🚧 [Issues](https://github.com/cri-middleware/SSPlayerForWgpu/issues) | The Rust crate and its C / C++ and browser faces, the Bevy adapter |
| 🚧 [SSPlayerForReactNative](https://github.com/cri-middleware/SSPlayerForReactNative) | 🚧 [Issues](https://github.com/cri-middleware/SSPlayerForReactNative/issues) | `<SpriteStudioView>` / `<SpriteStudioScene>`, the native module, Skia rendering |
| 🚧 [SSConverterGUI](https://github.com/cri-middleware/SSConverterGUI) | 🚧 [Issues](https://github.com/cri-middleware/SSConverterGUI/issues) | The desktop app itself (UI, packaging, updates) |

### 🧭 Not sure which one?

Because every player shares one core, the deciding question is **whether the symptom is in the
shared core or in the engine-specific layer**:

| Symptom | Where it belongs |
|---|---|
| Conversion produces a wrong or corrupt asset, or crashes - and it reproduces in the GUI, the CLI, **and** the browser tool | **SpriteStudio-SDK** (the conversion engine is shared) |
| The Converter GUI misbehaves but `ssconverter-cli` converts the same `.sspj` fine | **SSConverterGUI** (a front-end issue) |
| An animation plays wrong the **same way on every player** you tried | **SpriteStudio-SDK** (the playback core is shared) |
| An animation plays wrong on **one engine only** | that **player's** repository |
| A part type or blend mode is missing on one engine | check [Player Differences](./overview/player-differences.md) first - it may be a known difference |

Before filing, it also helps to check [Shared Limitations](./sdk/limitations.md): several
frequently-reported behaviors (seeking not firing events, reverse playback of
`independent = true` parts, no audio in reverse) are documented constraints of the shared
runtime, not bugs.

## ❓ How-to questions - community forum

For usage questions, implementation advice, and tips from other developers, use the official
forum rather than Issues:

👉 [**SpriteStudio Community**](https://spritestudio.jp/community/)

## 🔒 Private inquiries & large repro data

For private consultation, sensitive reports, or support with contractual guarantees, use the
official inquiry form:

👉 [**CRI Middleware inquiry form (English)**](https://www.webtech.co.jp/contact/en.html)

The English form has no file upload. To send large reproduction data (e.g. a `.sspj` project),
use the [Japanese Help Center form](https://www.webtech.co.jp/help/ja/spritestudio7/inquiries/ssplayer_tool/), which
takes a zip of up to 8 MB.

!!! note "About SpriteStudio itself"
    Questions about the **editor** (authoring, the SpriteStudio application, licensing of the
    tool) go to [CRI Middleware](https://www.webtech.co.jp/spritestudio/) through the same form -
    not to the player repositories. Before asking, the
    [**SpriteStudio Help Center**](https://www.webtech.co.jp/help/en/spritestudio7/) already
    covers using the editor: beginners' guide, user guide, tutorial videos, and a
    reverse-lookup reference.

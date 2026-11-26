---
description: "SSConverter GUI, a desktop app that converts SpriteStudio projects (.sspj) for the official players. SpriteStudio adds bones, mesh and effects to 2D illustrations."
---

# 🖥️ SSConverter GUI

A **desktop app** (Tauri) that wraps `libssconverter`, so you can convert `.sspj` projects into
runtime-ready assets without touching the CLI. The builds on offer are **macOS and Windows**; on
Linux use the SDK's `ssconverter-cli`, which is the same `libssconverter` without a window.

- **Download:** [GitHub Releases](https://github.com/cri-middleware/SSConverterGUI/releases)
- **How to use it:** [Converting with a Standalone Tool](../overview/convert-with-a-standalone-tool.md)
- **Documentation:** <https://cri-middleware.github.io/SSConverterGUI/>
- **Repository:** <https://github.com/cri-middleware/SSConverterGUI>

It converts rather than plays, so this page has no install, convert and play steps of its own:
copy the output folder to where your player loads assets from - each player's Quick Start shows where,
and [Choose Your Platform](../overview/choose-your-platform.md) leads to it.
For the conversion pipeline these assets feed into, see [SDK Concepts](../sdk/concepts.md).

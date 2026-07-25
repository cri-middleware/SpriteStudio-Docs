[**English**](./README.md) | [**日本語**](./README.ja.md)

# SpriteStudio-Docs

Documentation **portal** for the SpriteStudio SDK and its official players.

This repository is a lightweight hub. It does **not** re-host each player's docs - every
player keeps its own site in its own repository. This portal provides the unified entry
point and hosts the cross-cutting material that belongs to no single player:

- the landing page with product cards,
- the [ecosystem overview](docs/en/overview/ecosystem.md) and
  [platform chooser](docs/en/overview/choose-your-platform.md),
- the [asset-conversion overview](docs/en/overview/conversion.md) and the
  [standalone conversion tools](docs/en/overview/convert-with-a-standalone-tool.md),
- [feature support](docs/en/overview/feature-support.md) across players and the shared
  [runtime limitations](docs/en/sdk/limitations.md),
- shared [SDK concepts](docs/en/sdk/concepts.md), the
  [format specification](docs/en/sdk/format-spec.md), and the
  [porting guide map](docs/en/sdk/porting.md),
- [support routing](docs/en/support.md) and shared licensing.

Published at: <https://cri-middleware.github.io/SpriteStudio-Docs/>

## Structure

```
docs/
  en/ , ja/          # folder-based i18n (mkdocs-static-i18n)
    index.md         # landing page (product cards)
    overview/        # ecosystem, choose-your-platform, feature-support,
                     #   try-it, conversion, convert-with-a-standalone-tool
    sdk/             # concepts, format-spec, limitations, porting (canonical, cross-player)
    players/         # thin entry pages that link out to each player's own docs
    support.md
    license.md
  requirements.txt
mkdocs.yml
.github/workflows/pages.yml   # build (strict) + deploy via GitHub Pages
```

Every page exists in **both** `en/` and `ja/`; the navigation is defined once in `mkdocs.yml`
(Japanese nav labels come from its `nav_translations` map). The toolchain (mkdocs-material +
i18n) is kept aligned with SSPlayerForUnity / SSPlayerForRenPy.

## Local development

### macOS / Linux (bash)

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r docs/requirements.txt
.venv/bin/mkdocs serve          # preview at http://127.0.0.1:8000
.venv/bin/mkdocs build --strict # what CI runs
```

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\python -m pip install -r docs/requirements.txt
.\.venv\Scripts\mkdocs serve          # preview at http://127.0.0.1:8000
.\.venv\Scripts\mkdocs build --strict # what CI runs
```

## Related repositories

| Repository | Role |
|---|---|
| [SpriteStudio-SDK](https://github.com/cri-middleware/SpriteStudio-SDK) | Shared Rust core (`libssruntime` / `libssconverter`) |
| [SSPlayerForUnity](https://github.com/cri-middleware/SSPlayerForUnity) | Unity player |
| [SSPlayerForWeb](https://github.com/cri-middleware/SSPlayerForWeb) | Web player collection (PixiJS / WebGL / RPG Maker MZ / TyranoScript / ssconverter-web) |
| [SSPlayerForGodot](https://github.com/cri-middleware/SSPlayerForGodot) | Godot player |
| [SSPlayerForFlutter](https://github.com/cri-middleware/SSPlayerForFlutter) | Flutter player |
| [SSPlayerForRenPy](https://github.com/cri-middleware/SSPlayerForRenPy) | Ren'Py player |
| [SSConverterGUI](https://github.com/cri-middleware/SSConverterGUI) | Desktop converter GUI |

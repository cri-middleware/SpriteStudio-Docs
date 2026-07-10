# SpriteStudio-Docs

Documentation **portal** for the SpriteStudio SDK and its official players.

This repository is a lightweight hub. It does **not** re-host each player's docs — every
player keeps its own site in its own repository. This portal provides the unified entry
point and hosts the cross-cutting material that belongs to no single player:

- the landing page with product cards,
- the [ecosystem overview](docs/en/overview/ecosystem.md),
- shared [SDK concepts](docs/en/sdk/concepts.md) and the [format specification](docs/en/sdk/format-spec.md),
- shared licensing.

Published at: <https://cri-middleware.github.io/SpriteStudio-Docs/>

## Structure

```
docs/
  en/ , ja/          # folder-based i18n (mkdocs-static-i18n)
    index.md         # landing page (product cards)
    overview/        # ecosystem, choose-your-platform
    sdk/             # concepts, format-spec (canonical, cross-player)
    players/         # thin entry pages that link out to each player's own docs
    license.md
  requirements.txt
mkdocs.yml
.github/workflows/docs.yml   # build (strict) + gh-deploy to gh-pages
```

The toolchain (mkdocs-material + i18n) is kept aligned with SSPlayerForUnity / SSPlayerForRenPy.

## Local development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r docs/requirements.txt
mkdocs serve          # preview at http://127.0.0.1:8000
mkdocs build --strict # what CI runs
```

## Related repositories

| Repository | Role |
|---|---|
| [SpriteStudio-SDK](https://github.com/cri-middleware/SpriteStudio-SDK) | Shared Rust core (`libssruntime` / `libssconverter`) |
| [SSPlayerForUnity](https://github.com/cri-middleware/SSPlayerForUnity) | Unity player |
| [SSPlayerForWeb](https://github.com/cri-middleware/SSPlayerForWeb) | Web player collection (PixiJS / WebGL / TyranoScript / ssconverter-web) |
| [SSPlayerForGodot](https://github.com/cri-middleware/SSPlayerForGodot) | Godot player |
| [SSPlayerForRenPy](https://github.com/cri-middleware/SSPlayerForRenPy) | Ren'Py player |
| [SsConverterGUI](https://github.com/cri-middleware/SsConverterGUI) | Desktop converter GUI |

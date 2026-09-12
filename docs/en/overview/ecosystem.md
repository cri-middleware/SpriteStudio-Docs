# 🌐 Ecosystem

Every official player shares one Rust core, **SpriteStudio-SDK**. A SpriteStudio project
(`.sspj`) is converted once into a compact runtime format, then played back through
`libssruntime` regardless of the target engine.

That same SDK - both conversion and playback - is embedded in every official player, so
**one shared SDK powers many players (one-to-many)**. (Each player's own docs zoom into its
specific convert/import workflow.)

```mermaid
graph LR
    SS[" .sspj / Images<br/>(SpriteStudio) "]

    subgraph SDK ["SpriteStudio-SDK - shared core, embedded in every player"]
        CONV(" libssconverter<br/>convert ")
        RT(" libssruntime<br/>play back ")
    end

    PLAYER[[" Any official player<br/>(see Players &amp; Tools) "]]
    SCREEN{{" Screen / Canvas "}}

    SS --> CONV
    CONV -. ".ssab / .ssqb" .-> RT
    RT -- "1-to-N players" --> PLAYER --> SCREEN

    classDef sdk fill:#818cf82e,stroke:#818cf8;
    class CONV,RT sdk;
```

<small>The highlighted **SpriteStudio-SDK** core (`libssconverter` + `libssruntime`) is what
every player builds on; the dashed hand-off is the generated **`.ssab / .ssqb`** asset. One
core drives *every* player - see [Choose Your Platform](./choose-your-platform.md) for the
current lineup.</small>

Conversion can happen **automatically on import** (Unity, Godot, Ren'Py, TyranoBuilder) or via a **standalone
tool** (SSConverterGUI, `ssconverter-cli`, `ssconverter-web`) - see
[Converting Assets](./conversion.md), which owns the routes and what each one emits.

## 🧩 The pieces

| Component | Role |
|---|---|
| **SpriteStudio-SDK** | The shared Rust core. `libssconverter` converts `.sspj` into runtime assets; `libssruntime` plays them back. Consumed by every player as a git submodule - including `libssconverter`, so Unity, Godot, Ren'Py, and TyranoBuilder convert in-place. |
| **SSPlayerForUnity / ForGodot** | Bundle `libssconverter` as a conversion tool and run it on the engine-editor side, so import & playback need no external tool. |
| **SSPlayerForRenPy** | Bundles `libssconverter` as a conversion tool and auto-imports on startup, so no external tool is needed. |
| **SSPlayerForWeb / ForFlutter** | `libssruntime` bindings + rendering; conversion via the bundled standalone tools. SSPlayerForWeb's TyranoBuilder plugin is the exception - it converts inside the editor, so that route needs no separate tool. |
| **SSPlayerForReactNative / ForWgpu** | `libssruntime` bindings + rendering, with no converter of their own: neither has an editor to host an importer in, so conversion is a host-side step with one of the standalone tools below. |
| **SSConverterGUI / `ssconverter-cli` / `ssconverter-web`** | Standalone front-ends over `libssconverter` for converting without a player (desktop GUI, CLI/CI, browser). |

Because conversion and playback live in the SDK, all players stay consistent in feature
support and behavior - a fix in the core benefits every platform at once.

See [SDK Concepts](../sdk/concepts.md) for what the runtime format contains, and the
[Format Specification](../sdk/format-spec.md) for the on-disk details.

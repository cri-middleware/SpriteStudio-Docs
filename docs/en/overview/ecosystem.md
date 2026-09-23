# 🌐 Ecosystem

Every official player shares one Rust core, **SpriteStudio-SDK**. A SpriteStudio project
(`.sspj`) is converted once into a compact runtime format, then played back through
`libssruntime` regardless of the target engine.

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
every player builds on; the dashed hand-off is the generated **`.ssab / .ssqb`** asset. For
the current lineup of players, see [Choose Your Platform](./choose-your-platform.md).</small>

Conversion can happen **automatically on import** or via a **standalone tool** - which engines
do which, and what each route emits, is in [Converting Assets](./conversion.md).

## 🧩 The pieces

| Component | Role |
|---|---|
| **SpriteStudio-SDK** | The shared Rust core. `libssconverter` converts `.sspj` into runtime assets; `libssruntime` plays them back. Every player consumes it as a git submodule, `libssconverter` included - which is what lets some of them convert in-place. |
| **The players** | `libssruntime` bindings plus the rendering for one engine. Some also convert for you during development ([Converting Assets](./conversion.md) says which); the rest leave conversion to the tools below. |
| **SSConverterGUI / `ssconverter-cli` / `ssconverter-web`** | Standalone front-ends over `libssconverter` for converting without a player (desktop GUI, CLI/CI, browser). |

Because conversion and playback live in the SDK, all players stay consistent in feature
support and behavior - a fix in the core benefits every platform at once.

See [SDK Concepts](../sdk/concepts.md) for what the runtime format contains, and the
[Format Specification](../sdk/format-spec.md) for the on-disk details.

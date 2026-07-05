+++
title = "16. Diagnosesystem"
weight = 16
+++

# 16. Diagnosesystem


Zen C bietet ein kategorisiertes Diagnosesystem, das eine granulare Kontrolle über Compiler-Warnungen ermöglicht. Dies hilft dabei, hohe Standards für die Codequalität einzuhalten und gleichzeitig die Reibung bei der Interaktion mit externem C-Code zu verringern.

#### Diagnose-Kategorien

Warnungen sind in logische Kategorien gruppiert. Jede Kategorie kann global über Compiler-Flags aktiviert oder deaktiviert werden.

| Kategorie | Beschreibung | Standard |
| :--- | :--- | :--- |
| **`INTEROP`** | Warnungen im Zusammenhang mit C-Header-Imports und undefinierten externen Funktionen. | **OFF** |
| **`PEDANTIC`** | Besonders strenge Prüfungen auf potenzielle Probleme oder Codequalität. | **OFF** |
| **`UNUSED`** | Warnungen für definierte, aber ungenutzte Variablen, Parameter oder Funktionen. | **ON** |
| **`SAFETY`** | Kritische Sicherheitswarnungen wie Nullpointer-Zugriff oder Division durch Null. | **ON** |
| **`LOGIC`** | Logikbezogene Warnungen wie nicht erreichbarer Code oder konstante Vergleiche. | **ON** |
| **`CONVERSION`** | Warnungen bei impliziten oder einschränkenden Typumwandlungen. | **ON** |
| **`STYLE`** | Warnungen zum Codierstil wie beispeilsweise Variable Shadowing. | **ON** |

#### Compiler-Flags

Du kannst die Diagnosen mit den Flags `-W` (aktivieren) und `-Wno-` (deaktivieren) steuern, gefolgt vom Kategorienamen oder einer spezifischen Diagnose-ID.

##### Kategorie-Flags

- `-Winterop`: Aktiviert alle interoperabilitätsbezogenen Warnungen.
- `-Wno-unused`: Schaltet Warnungen bei ungenutzten Variablen/Parametern gezielt stumm.
- `-Wsafety`: Stellt sicher, dass alle Sicherheitsprüfungen aktiv sind.
- `-Wall`: Aktiviert alle wichtigen Diagnosekategorien.
- `-Wextra`: Aktiviert noch strengere Diagnosen (entspricht `-Wpedantic`).

##### Anwendungsbeispiel

```bash
# Mit aktivierten C-Interop-Warnungen kompilieren
zc app.zc -Winterop

# Mit allen Warnungen außer für ungenutzten Code kompilieren
zc app.zc -Wall -Wno-unused
```

#### C-Interop Friction

Standardmäßig unterdrückt Zen C "Undefined function"-Warnungen für Funktionen, die wahrscheinlich zu C-Standardbibliotheken gehören (`INTEROP`-Kategorie ist **OFF**).

Wenn du möchtest, dass der Compiler jede undefinierte Funktion streng markiert (z. B. um Tippfehler abzufangen), aktiviere die Interop-Kategorie:

```bash
zc main.zc -Winterop
```

Wenn aktiviert, liefert der Compiler hilfreiche Vorschläge für gängige C-Funktionen:
```
warning: Undefined function 'abs'
  --> main.zc:5:13
   |
5  |     let x = abs(-5);
   |             ^ here
   |
   = note: If this is a C function, it might need to be whitelisted in 'zenc.json'
```

#### Whitelisting

Wenn du häufig eine bestimmte C-Bibliothek verwendest und `-Winterop` aktiviert lassen möchtest, ohne von bestimmten Funktionen genervt zu werden, kannst du diese zur `c_function_whitelist` in der Konfigurationsdatei `zenc.json` hinzufügen.

## Further Reading

- **Language Server**: Siehe die [LSP-Dokumentation](../LSP.md) für die Editor-Integration.
- **MISRA Compliance**: Siehe [MISRA Rules](17-misra-rules) für die vollständige Regelreferenz.
- **Contributing**: Siehe [Contributing Guide](../README.md#contributing) für die Beitragsrichtlinien.

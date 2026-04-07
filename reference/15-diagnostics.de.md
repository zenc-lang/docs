+++
title = "15. Diagnosesystem"
weight = 15
+++

# 15. Diagnosesystem

Zen C verfügt über ein kategorisiertes Diagnosesystem, das eine feingranulare Kontrolle über Compiler-Warnungen ermöglicht. Dies erlaubt es Ihnen, hohe Codequalitätsstandards einzuhalten und gleichzeitig Reibungsverluste bei der Interaktion mit externem C-Code zu reduzieren.

## Diagnose-Kategorien

Warnungen sind in logische Kategorien gruppiert. Jede Kategorie kann global über Compiler-Flags aktiviert oder deaktiviert werden.

| Kategorie | Beschreibung | Standard |
| :--- | :--- | :--- |
| **`INTEROP`** | Warnungen im Zusammenhang mit C-Header-Imports und undefinierten externen Funktionen. | **AUS** |
| **`PEDANTIC`** | Besonders strenge Prüfungen auf potenzielle Probleme oder Codequalität. | **AUS** |
| **`UNUSED`** | Warnungen für definierte, aber nicht verwendete Variablen, Parameter oder Funktionen. | **AN** |
| **`SAFETY`** | Kritische Sicherheitswarnungen wie Nullpointer-Zugriff oder Division durch Null. | **AN** |
| **`LOGIC`** | Logikbezogene Warnungen wie nicht erreichbarer Code oder konstante Vergleiche. | **AN** |
| **`CONVERSION`** | Warnungen für implizite oder einschränkende Typumwandlungen. | **AN** |
| **`STYLE`** | Warnungen zum Codierungsstil wie Variablenbeschattung (Shadowing). | **AN** |

## Compiler-Flags

Sie können Diagnosen mit den Flags `-W` (aktivieren) und `-Wno-` (deaktivieren), gefolgt vom Kategorienamen oder einer spezifischen Diagnose-ID, steuern.

### Kategorie-Flags

- `-Winterop`: Aktiviert alle interop-bezogenen Warnungen.
- `-Wno-unused`: Unterdrückt gezielt Warnungen zu nicht verwendeten Variablen/Parametern.
- `-Wsafety`: Stellt sicher, dass alle Sicherheitsprüfungen aktiv sind.
- `-Wall`: Aktiviert alle wichtigen Diagnose-Kategorien.
- `-Wextra`: Aktiviert noch strengere Diagnosen (entspricht `-Wpedantic`).

### Anwendungsbeispiel

```bash
# Kompilieren mit aktivierten C-Interop-Warnungen
zc app.zc -Winterop

# Kompilieren mit allen aktivierten Warnungen außer Unused-Warnungen
zc app.zc -Wall -Wno-unused
```

## C-Interop-Reibung

Standardmäßig unterdrückt Zen C Warnungen zu "undefinierten Funktionen" für Funktionen, die wahrscheinlich in C-Standardbibliotheken zu finden sind (die Kategorie `INTEROP` ist **AUS**).

Wenn Sie möchten, dass der Compiler jede undefinierte Funktion streng meldet (z. B. um Tippfehler zu finden), aktivieren Sie die Interop-Kategorie:

```bash
zc main.zc -Winterop
```

Wenn aktiviert, liefert der Compiler hilfreiche Hinweise für gängige C-Funktionen:
```text
warning: Undefined function 'abs'
  --> main.zc:5:13
   |
5  |     let x = abs(-5);
   |             ^ here
   |
   = note: If this is a C function, it might need to be whitelisted in 'zenc.json'
```

## Whitelisting

Wenn Sie eine bestimmte C-Bibliothek häufig verwenden und `-Winterop` aktiviert lassen möchten, ohne von bestimmten Funktionen gestört zu werden, können Sie diese zur `c_function_whitelist` in Ihrer `zenc.json`-Konfigurationsdatei hinzufügen.

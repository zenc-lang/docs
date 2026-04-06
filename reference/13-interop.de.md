+++
title = "17. C-Interoperabilität"
weight = 13
+++

# 17. C-Interoperabilität


Zen C bietet zwei Wege, um mit C-Code zu interagieren: **Trusted Imports** (praktisch) und **Explicit FFI** (sicher/präzise).

#### Methode 1: Trusted Imports (praktisch)

C-Headerdatei können direkt mit dem Schlüsselwort `import` und der Dateiendung `.h` importieren werden. Dadurch wird die Headerdatei als Modul behandelt und es wird davon ausgegangen, dass alle darüber aufgerufenen Symbole vorhanden sind.

```zc
//> link: -lm
import "math.h" as c_math;

fn main() {
	// Der Compiler vertraut auf die Korrektheit; gibt 'cos(...)' direkt aus
    let x = c_math::cos(3.14159);
}
```

> **Vorteile**: Keine Boilerplate. Alle Inhalte im Header sind sofort zugänglich.
> **Nachteil**: Zen C prüft die Typen nicht, Fehler werden vom C-Compiler erkannt.

#### Methode 2: Explicit FFI (sicher)

Für strenge Typprüfung oder wenn Header nicht eingebunden werden sollen. Nutze `extern fn`.

```zc
include <stdio.h> // Generiert #include <stdio.h>

// Strenge Signatur definieren
extern fn printf(fmt: char*, ...) -> c_int;

fn main() {
    printf("Hallo FFI: %d\n", 42); // Typprüfung durch Zen C
}
```

> **Vorteile**: Typprüfung durch Zen C.  
> **Nachteil**: Manuelle Deklaration der Funktionen erforderlich.

#### `import` vs `include`

- **`import "file.h"`**: Registriert Header als Modul; erlaubt impliziten Zugriff auf Symbole (`file::function()`).  
- **`include <file.h>`**: Fügt nur `#include` in generiertes C ein; Symbole müssen mit `extern fn` manuell deklariert werden.

---

## Standardbibliothek

Zen C enthält eine Standardbibliothek (`std`), die grundlegende Funktionalität abdeckt.

[Zur Dokumentation der Standardbibliothek](docs/std/README.md)

### Wichtige Module

<details>
<summary>Klicke, um alle Standardbibliotheks-Module zu sehen</summary>

| Modul | Beschreibung | Docs |
| :--- | :--- | :--- |
| **`std/bigfloat.zc`** | Gleitkomma-Arithmetik mit beliebiger Genauigkeit. | [Docs](docs/std/bigfloat.md) |
| **`std/bigint.zc`** | Ganzzahlen mit beliebiger Genauigkeit `BigInt`. | [Docs](docs/std/bigint.md) |
| **`std/bits.zc`** | Niedrigstufige Bitoperationen (`rotl`, `rotr`). | [Docs](docs/std/bits.md) |
| **`std/complex.zc`** | Komplexe Zahlen `Complex`. | [Docs](docs/std/complex.md) |
| **`std/vec.zc`** | Dynamisches, wachsendes Array `Vec<T>`. | [Docs](docs/std/vec.md) |
| **`std/string.zc`** | Heap-allokierter `String` mit UTF-8 Unterstützung. | [Docs](docs/std/string.md) |
| **`std/queue.zc`** | FIFO-Warteschlange (Ringpuffer). | [Docs](docs/std/queue.md) |
| **`std/map.zc`** | Generische Hash-Map `Map<V>`. | [Docs](docs/std/map.md) |
| **`std/fs.zc`** | Dateisystemoperationen. | [Docs](docs/std/fs.md) |
| **`std/io.zc`** | Standard Ein-/Ausgabe (`print`/`println`). | [Docs](docs/std/io.md) |
| **`std/option.zc`** | Optionale Werte (`Some`/`None`). | [Docs](docs/std/option.md) |
| **`std/result.zc`** | Fehlerbehandlung (`Ok`/`Err`). | [Docs](docs/std/result.md) |
| **`std/path.zc`** | Plattformübergreifende Pfadmanipulation. | [Docs](docs/std/path.md) |
| **`std/env.zc`** | Prozess-Umgebungsvariablen. | [Docs](docs/std/env.md) |
| **`std/net/`** | TCP, UDP, HTTP, DNS, URL. | [Docs](docs/std/net.md) |
| **`std/thread.zc`** | Threads und Synchronisation. | [Docs](docs/std/thread.md) |
| **`std/time.zc`** | Zeitmessung und Sleep-Funktionen. | [Docs](docs/std/time.md) |
| **`std/json.zc`** | JSON Parsing und Serialisierung. | [Docs](docs/std/json.md) |
| **`std/stack.zc`** | LIFO-Stack `Stack<T>`. | [Docs](docs/std/stack.md) |
| **`std/set.zc`** | Generisches Hash-Set `Set<T>`. | [Docs](docs/std/set.md) |
| **`std/process.zc`** | Prozessausführung und Management. | [Docs](docs/std/process.md) |
| **`std/regex.zc`** | Reguläre Ausdrücke (TRE-basiert). | [Docs](docs/std/regex.md) |
| **`std/simd.zc`** | Native SIMD-Vektortypen. | [Docs](docs/std/simd.md) |

</details>

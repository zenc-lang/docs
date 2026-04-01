+++
title = "12. Fortgeschrittenes & Metaprogrammierung"
weight = 12
+++

# 12. Fortgeschrittenes & Metaprogrammierung


### Metaprogrammierung

#### Comptime
Führt Code zur Compile-Zeit aus, um Quellcode zu generieren oder Nachrichten auszugeben.

```zc
comptime {
    // Generiert Code während der Kompilierung (wird auf stdout geschrieben)
    println "let build_date = \"2024-01-01\";";
}

println "Build Date: {build_date}";
```

<details>
<summary><b>Hilfsfunktionen</b></summary>

Spezielle Funktionen innerhalb von `comptime`-Blöcken für Code-Generierung und Diagnostik:
<table>
<tr>
<th>Funktion</th>
<th>Beschreibung</th>
</tr>
<tr>
<td><code>yield(str)</code></td>
<td>Generiert explizit Code (Alternative zu <code>printf</code>)</td>
</tr>
<tr>
<td><code>code(str)</code></td>
<td>Alias für <code>yield()</code>,  klarere Absicht für Code-Generierung</td>
</tr>
<tr>
<td><code>compile_error(msg)</code></td>
<td>Bricht die Kompilierung mit Fehlermeldung ab</td>
</tr>
<tr>
<td><code>compile_warn(msg)</code></td>
<td>Gibt eine Warnung zur Compile-Zeit aus (Kompilierung wird fortgesetzt)</td>
</tr>
</table>

**Beispiel:**
```zc
comptime {
    compile_warn("Generiere optimierten Code...");
    
    let ENABLE_FEATURE = 1;
    if (ENABLE_FEATURE == 0) {
        compile_error("Feature muss aktiviert sein!");
    }
    
    // Verwende code() mit Raw-Strings für saubere Generierung
    code(r"let FEATURE_ENABLED = 1;");
}
```
</details>

<details>
<summary><b>Build-Metadaten</b></summary>

Zugriff auf Compiler-Buildinformationen zur Compile-Zeit:

<table>
<tr>
<th>Konstante</th>
<th>Typ</th>
<th>Beschreibung</th>
</tr>
<tr>
<td><code>__COMPTIME_TARGET__</code></td>
<td>string</td>
<td>Plattform: <code>"linux"</code>, <code>"windows"</code>, oder <code>"macos"</code></td>
</tr>
<tr>
<td><code>__COMPTIME_FILE__</code></td>
<td>string</td>
<td>Aktueller Quellcode-Dateiname, der kompiliert wird</td>
</tr>
</table>

**Beispiel:**
```zc
comptime {
    // Plattform-spezifische Code-Generierung
    println "let PLATFORM = \"{__COMPTIME_TARGET__}\";";
}

println "Running on: {PLATFORM}";
```
</details>

{% alert(type="tip") %}
Verwende in der Kompilierzeit rohe Zeichenketten (`r"..."`), um das Maskieren von geschweiften Klammern zu vermeiden: `code(r"fn test() { return 42; }")`. Verwende andernfalls `{{` und `}}`, um geschweifte Klammern innerhalb regulärer Zeichenketten zu maskieren.
{% end %}


#### Embed
Binde Dateien als bestimmte Typen ein.
```zc
// Standard (Slice_char)
let data = embed "assets/logo.png";

// Typisierte Einbindung
let text = embed "shader.glsl" as string;    // Einbindung als C-String
let rom  = embed "bios.bin" as u8[1024];     // Einbindung als fixiertes Array
let wav  = embed "sound.wav" as u8[];        // Einbindung als Slice_u8
```

#### Plugins
Importiere Compiler-Plugins zur Erweiterung der Syntax.
```zc
import plugin "regex"
let re = regex! { ^[a-z]+$ };
```

#### Generische C-Makros
Leite Preprocessor-Makros direkt an C weiter.

{% alert(type="tip") %}
Für einfache Konstanten benutze lieber `def`. Nutze `#define` nur, wenn C-Präprozessor-Makros oder bedingte Kompilierung nötig sind.
{% end %}

```zc
#define MAX_BUFFER 1024
```

#### Bedingte Kompilierung
Mit `@cfg()` kannst du jede Top-Level-Deklaration bedingt ein- oder ausschließen, basierend auf `-D` Flags.

```zc
// Build mit: zc build app.zc -DUSE_OPENGL

@cfg(USE_OPENGL)
import "opengl_backend.zc";

@cfg(USE_VULKAN)
import "vulkan_backend.zc";

// Oder: inkludieren, wenn irgendein Backend gewählt ist
@cfg(any(USE_OPENGL, USE_VULKAN))
fn init_graphics() { /* ... */ }

// UND mit Negation
@cfg(not(USE_OPENGL))
@cfg(not(USE_VULKAN))
fn fallback_init() { println "Kein Backend ausgewählt"; }
```

| Form | Bedeutung |
|:---|:---|
| `@cfg(NAME)` | Einbinden, wenn `-DNAME` gesetzt ist |
| `@cfg(not(NAME))` | Einbinden, wenn `-DNAME` NICHT gesetzt ist |
| `@cfg(any(A, B, ...))` | Einbinden, wenn IRGENDEINE Bedingung wahr ist (OR) |
| `@cfg(all(A, B, ...))` | Einbinden, wenn ALLE Bedingungen wahr sind (AND) |

Mehrere `@cfg` auf einer Deklaration werden ANDed. `not()` kann in `any()` und `all()` verwendet werden. Funktioniert mit jeder Deklaration auf oberster Ebene: `fn`, `struct`, `import`, `impl`, `raw`, `def`, `test` etc.

### Attribute

Dekoriere Funktionen und Strukturen, um das Verhalten des Compilers zu beeinflussen.

| Attribut | Geltungsbereich | Beschreibung |
|:---|:---|:---|
| `@required` | Fn | Warnung, wenn Rückgabewert ignoriert wird. |
| `@deprecated("msg")` | Fn/Struct | Warnung bei Nutzung mit Nachricht. |
| `@inline` | Fn | Hinweis an den Compiler zum Inlining. |
| `@noinline` | Fn | Verhindert Inlining. |
| `@packed` | Struct | Entfernt Padding zwischen Feldern. |
| `@align(N)` | Struct | Erzwingt Ausrichtung auf N Bytes. |
| `@constructor` | Fn | Wird vor `main` ausgeführt. |
| `@destructor` | Fn | Wird nach Beenden von `main` ausgeführt. |
| `@unused` | Fn/Var | Unterdrückt Warnungen für ungenutzte Variablen. |
| `@weak` | Fn | Schwache Symbolbindung (Weak linkage). |
| `@section("name")` | Fn | Platziert Code in einem bestimmten Abschnitt. |
| `@noreturn` | Fn | Funktion kehrt nicht zurück (z.B. `exit`). |
| `@pure` | Fn | Funktion ohne Seiteneffekte (Optimierungshinweis). |
| `@cold` | Fn | Funktion wird selten ausgeführt (Branch-Prediction-Hinweis). |
| `@hot` | Fn | Funktion wird häufig ausgeführt (Optimierungshinweis). |
| `@export` | Fn/Struct | Exportiert Symbol (Sichtbarkeit standardmäßig). |
| `@global` | Fn | CUDA: Kernel-Einstiegspunkt (`__global__`). |
| `@device` | Fn | CUDA: Device-Funktion (`__device__`). |
| `@host` | Fn | CUDA: Host-Funktion (`__host__`). |
| `@comptime` | Fn | Hilfsfunktion für Compile-Time-Ausführung. |
| `@cfg(NAME)` | Any | Bedingte Kompilierung: nur einbinden, wenn `-DNAME` gesetzt ist. Unterstützt `not()`, `any()`, `all()`. |
| `@derive(...)` | Struct | Implementiert automatisch Traits (`Debug`, `Eq`, `Copy`, `Clone`). |
| `@ctype("type")` | Fn Param | Überschreibt den generierten C-Typ eines Parameters. |
| `@<custom>` | Any | Leitet generische Attribute an C weiter (z.B. `@flatten`, `@alias("name")`). |

#### Eigene Attribute

Zen C unterstützt ein leistungsstarkes System **benutzerdefinierter Attribute**, mit dem du beliebige GCC/Clang-`__attribute__` direkt in Ihrem Code verwenden kannst. Jedes Attribut, das vom Zen-C-Compiler nicht explizit erkannt wird, wird als generisches Attribut behandelt und an den generierten C-Code weitergegeben.

Dies erlaubt Zugriff auf erweiterte Compiler-Funktionen, Optimierungen und Linker-Directives, ohne dass die Sprache selbst diese explizit unterstützen muss.

#### Syntax-Mapping
Zen C Attribute werden direkt auf C Attribute abgebildet:
- `@name` → `__attribute__((name))`  
- `@name(args)` → `__attribute__((name(args)))`  
- `@name("string")` → `__attribute__((name("string")))`  

#### Smart Derives

Zen C bietet "Smart Derives" mit Beachtung von Move-Semantics:

- **`@derive(Eq)`**: Generiert eine Gleichheitsmethode, die Argumente per Referenz nimmt (`fn eq(self, other: T*)`).  
    - Beim Vergleich zweier non-Copy-Strukturen (`a == b`) wird `b` automatisch per Referenz (`&b`) übergeben, um Move zu vermeiden.  
    - Rekursive Feldvergleiche bevorzugen ebenfalls Pointer-Zugriff, um Besitzübergaben zu verhindern.

### Inline-Assembly

Zen C unterstützt Inline-Assembly vollständig, transpiliert direkt zu GCC-Extended `asm`.

#### Grundlegende Nutzung
Schreibe den Assembler-Code innerhalb von `asm`-Blöcken. Zeichenketten werden automatisch verkettet.
```zc
asm {
    "nop"
    "mfence"
}
```

#### Volatile
Verhindert, dass der Compiler Assembly-Code mit Seiteneffekten entfernt.
```zc
asm volatile {
    "rdtsc"
}
```

#### Benannte Constraints
Zen C vereinfacht die komplexe GCC-Syntax durch benannte Bindungen:

```zc
// Syntax: : out(variable) : in(variable) : clobber(reg)
// Platzhalter {variable} für bessere Lesbarkeit

fn summe(x: int) -> int {
    let ergebnis: int;
    asm {
        "mov {x}, {ergebnis}"
        "add $5, {ergebnis}"
        : out(ergebnis)
        : in(x)
        : clobber("cc")
    }
    return ergebnis;
}
```

| Typ | Syntax | GCC-Äquivalent |
|:---|:---|:---|
| **Output** | `: out(variable)` | `"=r"(variable)` |
| **Input** | `: in(variable)` | `"r"(variable)` |
| **Clobber** | `: clobber("rax")` | `"rax"` |
| **Memory** | `: clobber("memory")` | `"memory"` |

> **Hinweis:** Bei Verwendung der Intel-Syntax (über `-masm=intel`) muss der Build korrekt konfiguriert sein (z. B. `//> cflags: -masm=intel`). TCC unterstützt keine Assemblierung mit Intel-Syntax.

### Build-Direktiven

Zen C unterstützt spezielle Kommentare am Anfang der Quellcode-Datei, um den Build-Prozess zu konfigurieren, ohne Makefile oder komplexes Build-System.

| Direktive | Argumente | Beschreibung |
|:---|:---|:---|
| `//> link:` | `-lfoo` oder `pfad/zu/lib.a` | Mit einer Bibliothek oder Objektdatei linken. |
| `//> lib:` | `pfad/zu/libs` | Bibliothekssuchpfad hinzufügen (`-L`). |
| `//> include:` | `pfad/zu/headers` | Include-Suchpfad hinzufügen (`-I`). |
| `//> framework:` | `Cocoa` | macOS-Framework linken. |
| `//> cflags:` | `-Wall -O3` | Beliebige Compiler-Flags für C übergeben. |
| `//> define:` | `MACRO` oder `KEY=VAL` | Preprocessor-Makro definieren (`-D`). |
| `//> pkg-config:` | `gtk+-3.0` | `pkg-config` ausführen und Flags & Libraries anhängen. |
| `//> shell:` | `command` | Shell-Befehl während Build ausführen. |
| `//> get:` | `http://url/file` | Datei herunterladen, wenn sie nicht existiert. |

#### Features

**1. OS-Guarding**  
Präfixe wie `linux:`, `windows:`, `macos:` (oder `darwin:`) lassen Direktiven nur auf bestimmten Plattformen gelten.

```zc
//> linux: link: -lm
//> windows: link: -lws2_32
//> macos: framework: Cocoa
```

**2. Environment-Variablen**  
`${VAR}` kann in Direktiven expandiert werden.

```zc
//> include: ${HOME}/mylib/include
//> lib: ${ZC_ROOT}/std
```

#### Beispiele

```zc
//> include: ./include
//> lib: ./libs
//> link: -lraylib -lm
//> cflags: -Ofast
//> pkg-config: gtk+-3.0

import "raylib.h"

fn main() { ... }
```

### Schlüsselwörter

Zen C reserviert folgende Schlüsselwörter:

#### Deklarationen
`alias`, `def`, `enum`, `fn`, `impl`, `import`, `let`, `module`, `opaque`, `struct`, `trait`, `union`, `use`

#### Kontrollfluss
`async`, `await`, `break`, `catch`, `continue`, `defer`, `do`, `else`, `for`, `goto`, `guard`, `if`, `loop`, `match`, `return`, `try`, `unless`, `while`

#### Spezielle
`asm`, `assert`, `autofree`, `comptime`, `const`, `embed`, `launch`, `ref`, `sizeof`, `static`, `test`, `volatile`

#### Konstanten
`true`, `false`, `null`

#### C-Reserviert
Die folgenden Bezeichner sind reserviert, da sie Schlüsselwörter in C11 sind:
`auto`, `case`, `char`, `default`, `double`, `extern`, `float`, `inline`, `int`, `long`, `register`, `restrict`, `short`, `signed`, `switch`, `typedef`, `unsigned`, `void`, `_Atomic`, `_Bool`, `_Complex`, `_Generic`, `_Imaginary`, `_Noreturn`, `_Static_assert`, `_Thread_local`

#### Operatoren
`and`, `or`

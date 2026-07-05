+++
title = "1. Variablen und Konstanten"
weight = 1
+++

# 1. Variablen und Konstanten {#1-variablen-und-konstanten}


Zen C unterscheidet zwischen Compile-Zeit-Konstanten und Laufzeit-Variablen.

#### Manifeste Konstanten (`def`)

Werte, die nur zur Kompilierzeit existieren (im Code enthalten sind). Verwende diese für Arraygrößen, feste Konfigurationen und magische Zahlen.

``` zc
def MAX_SIZE = 1024;
let buffer: char[MAX_SIZE]; // Gültige Arraygröße
```

#### Variablen (`let`)
Speicherorte im Arbeitsspeicher. Können veränderlich oder schreibgeschützt (`const`) sein.

```zc
let x = 10;             // Veränderlich
x = 20;                 // OK

let y: const int = 10;  // Schreibgeschützt (Typqualifiziert)
// y = 20;              // Error: kann nicht einer Konstante zugewiesen werden
```

{% alert(type="tip") %}
**Typinferenz**: Zen C leitet automatisch Datentypen für initialisierte Variablen ab. Auf unterstützten Compilern wird der Datentyp zu C23 `auto` kompiliert, andernfalls zur GCC-Erweiterung `__auto_type`.
{% end %}

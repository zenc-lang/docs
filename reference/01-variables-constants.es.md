+++
title = "1. Variables y Constantes"
weight = 1
+++

# 1. Variables y Constantes {#1-variables-y-constantes}


Zen C distingue entre constantes en tiempo de compilación y variables en tiempo de ejecución.

#### Constantes Manifiestas (`def`)
Valores que existen solo en tiempo de compilación (se pliegan en el código). Úsalos para tamaños de arrays, configuración fija y números mágicos.

```zc
def MAX_SIZE = 1024;
let buffer: char[MAX_SIZE]; // Tamaño de array válido
```

#### Variables (`let`)
Ubicaciones de almacenamiento en memoria. Pueden ser mutables o de solo lectura (`const`).

```zc
let x = 10;             // Mutable
x = 20;                 // OK

let y: const int = 10;  // Solo lectura (Calificado por tipo)
// y = 20;              // Error: no se puede asignar a una constante
```

{% alert(type="tip") %}
**Inferencia de tipos**: Zen C infiere automáticamente los tipos para variables inicializadas. Se compila a `auto` de C23 en compiladores compatibles, o a la extensión `__auto_type` de GCC en otros casos.
{% end %}

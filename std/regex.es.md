# std/regex

El módulo `std/regex` proporciona soporte para expresiones regulares basado en `regex.h` de POSIX.

## Uso

```zc
import "std/regex.zc"

fn main() {
    if regex_match("^[a-z]+$", "hola") {
        println "¡Coincide!";
    }
    
    let re = Regex::compile("\\d+");
    let count = re.count("123 abc 456");
    re.destroy();
}
```

## Definiciones de Estructura

### `Regex`

Representa una expresión regular compilada.

```zc
struct Regex {
    // Handles internos
}
```

### `Match`

Representa una coincidencia exitosa de regex.

```zc
struct Match {
    text: char*;
    start: int;
    len: int;
}
```

## Métodos

### Construcción de Regex

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **compile** | `Regex::compile(pattern: char*) -> Regex` | Compila un patrón de regex con las banderas predeterminadas. |
| **compile_with_flags** | `Regex::compile_with_flags(pattern: char*, flags: int) -> Regex` | Compila con banderas POSIX personalizadas. |
| **destroy** | `destroy(self)` | Libera la regex compilada. |

### Coincidencia y Búsqueda

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **match** | `match(self, text: char*) -> bool` | Devuelve verdadero si el patrón coincide en cualquier parte de `text`. |
| **find** | `find(self, text: char*) -> Option<Match>` | Devuelve la primera coincidencia incluyendo posición y longitud. |
| **count** | `count(self, text: char*) -> int` | Devuelve el número de coincidencias no superpuestas. |
| **split** | `split(self, text: char*) -> Vec<String>` | Divide el texto por el patrón. |

### Acceso a Coincidencias

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **as_string** | `as_string(self) -> char*` | Devuelve un puntero al inicio de la coincidencia. |
| **end** | `end(self) -> int` | Devuelve el índice después del último carácter de la coincidencia. |

### Funciones de Ayuda Estáticas

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **regex_match** | `regex_match(pattern: char*, text: char*) -> bool` | Comprobación rápida de una coincidencia. |
| **regex_find** | `regex_find(pattern: char*, text: char*) -> Option<Match>` | Encuentra la primera coincidencia. |
| **regex_count** | `regex_count(pattern: char*, text: char*) -> int` | Cuenta todas las coincidencias. |
| **regex_split** | `regex_split(pattern: char*, text: char*) -> Vec<String>` | Divide el texto por un patrón. |

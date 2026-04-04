# std/string

`String` es un tipo de cadena de caracteres (string) ampliable y asignado en el montón. Envuelve un `Vec<char>` y garantiza la terminación nula para la compatibilidad con C.

## Uso

```zc
import "std/string.zc"

fn main() {
    let s = String::from("Hola");

    // Append requiere un puntero a otra String
    let parte = String::from(" Mundo");
    s.append(&parte);
    
    // Iteración (compatible con UTF-8)
    for c in s {
        println "{c}";
    }

    // Usar c_str() para imprimir
    println "{s.c_str()}"; // Imprime "Hola Mundo"
    
    if (s.starts_with("Hola")) {
        // ...
    }
} // s se libera automáticamente aquí
```

## Definición de Estructura

```zc
struct String {
    vec: Vec<char>;
}
```

## Métodos

### Construcción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `String::new(s: char*) -> String` | Crea una nueva String a partir de una primitiva de cadena C. |
| **from** | `String::from(s: char*) -> String` | Alias de `new`. |
| **from_rune** | `String::from_rune(r: rune) -> String` | Crea una nueva String a partir de una sola `rune`. |
| **from_runes** | `String::from_runes(runes: rune*, count: usize) -> String` | Crea una nueva String a partir de una matriz de `runes`. |
| **from_runes_vec** | `String::from_runes_vec(runes: Vec<rune>) -> String` | Crea una nueva String a partir de un vector de objetos `rune`. |

### Modificación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **append** | `append(self, other: String*)` | Añade otra cadena a esta. |
| **append_c** | `append_c(self, s: char*)` | Añade un literal de cadena C. |
| **push_rune** | `push_rune(self, r: rune)` | Añade un único punto de código Unicode (`rune`) a la cadena. |
| **insert_rune** | `insert_rune(self, idx: usize, r: rune)` | Inserta una `rune` en el *índice de caracteres* especificado. |
| **remove_rune_at** | `remove_rune_at(self, idx: usize) -> rune` | Elimina y devuelve la `rune` en el *índice de caracteres* especificado. |
| **reserve** | `reserve(self, cap: usize)` | Asegura que la cadena tenga al menos una capacidad de `cap` caracteres. |
| **clear** | `clear(self)` | Limpia la cadena. |

### Acceso y Consulta

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **c_str** | `c_str(self) -> char*` | Devuelve el puntero de cadena C subyacente. |
| **length** | `length(self) -> usize` | Devuelve la longitud de la cadena (excluyendo el terminador nulo). |
| **is_empty** | `is_empty(self) -> bool` | Devuelve verdadero si la longitud es 0. |
| **to_string** | `to_string(self) -> char*` | Mapea a `c_str()`. Se usa para la interpolación `{var}`. |
| **starts_with** | `starts_with(self, prefix: char*) -> bool` | Comprueba si la cadena comienza con el prefijo dado. |
| **ends_with** | `ends_with(self, suffix: char*) -> bool` | Comprueba si la cadena termina con el sufijo dado. |
| **contains** | `contains(self, target: char) -> bool` | Comprueba si la cadena contiene el carácter dado. |
| **contains_str** | `contains_str(self, target: char*) -> bool` | Comprueba si la cadena contiene la subcadena dada. |
| **find** | `find(self, target: char) -> Option<usize>` | Devuelve el índice de la primera ocurrencia del byte `target`. |
| **find_str** | `find_str(self, target: char*) -> Option<usize>` | Devuelve el índice de la primera ocurrencia de la subcadena `target`. |
| **find_all_str** | `find_all_str(self, target: char*) -> Vec<usize>` | Devuelve un vector que contiene todos los índices donde ocurre `target`. |
| **substring** | `substring(self, start: usize, len: usize) -> String` | Devuelve una nueva String que contiene la subcadena especificada. |

### Soporte UTF-8

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **utf8_len** | `utf8_len(self) -> usize` | Devuelve el número de puntos de código Unicode (caracteres). |
| **utf8_at** | `utf8_at(self, idx: usize) -> String` | Devuelve el carácter en el índice especificado como una nueva String. |
| **utf8_get** | `utf8_get(self, idx: usize) -> rune` | Devuelve el carácter en el índice especificado como una `rune`. |
| **utf8_substr** | `utf8_substr(self, start_idx: usize, num_chars: usize) -> String` | Devuelve una subcadena basada en índices de caracteres. |
| **runes** | `runes(self) -> Vec<rune>` | Devuelve un vector que contiene todos los puntos de código Unicode. |
| **chars** | `chars(self) -> StringCharsIter` | Devuelve un iterador manual que produce `Option<rune>`. |

### Transformaciones

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **to_lowercase** | `to_lowercase(self) -> String` | Devuelve una nueva cadena convertida a minúsculas. |
| **to_uppercase** | `to_uppercase(self) -> String` | Devuelve una nueva cadena convertida a mayúsculas. |
| **split** | `split(self, delim: char) -> Vec<String>` | Divide la cadena en un vector de subcadenas. |
| **trim** | `trim(self) -> String` | Devuelve una nueva cadena con los espacios en blanco iniciales/finales eliminados. |
| **replace** | `replace(self, target: char*, replacement: char*) -> String` | Devuelve una nueva cadena con los reemplazos realizados. |
| **pad_left** | `pad_left(self, target_len: usize, pad_char: char) -> String` | Devuelve una nueva cadena rellenada a la izquierda. |
| **pad_right** | `pad_right(self, target_len: usize, pad_char: char) -> String` | Devuelve una nueva cadena rellenada a la derecha. |

### Comparación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **eq** | `eq(self, other: String*) -> bool` | Comprobación de igualdad estructural. |
| **neq** | `neq(self, other: String*) -> bool` | Comprobación de desigualdad estructural. |
| **compare** | `compare(self, other: String*) -> int` | Comparación léxica. |
| **compare_ignore_case** | `compare_ignore_case(self, other: String*) -> int` | Comparación léxica sin distinguir entre mayúsculas y minúsculas. |
| **eq_ignore_case** | `eq_ignore_case(self, other: String*) -> bool` | Comprobación de igualdad sin distinguir entre mayúsculas y minúsculas. |

## Operadores

| Operador | Método | Descripción |
| :--- | :--- | :--- |
| `+` | **add** | `s1 + &s2`. Concatena cadenas en una nueva `String`. |
| `+=` | **add_assign** | `s1 += &s2`. Añade `s2` a `s1` in situ. |
| `==` | **eq** | `s1 == &s2`. Comprobación de igualdad estructural. |
| `!=` | **neq** | `s1 != &s2`. Comprobación de desigualdad estructural. |
| `<` | **lt** | `s1 < &s2`. Comparación léxica. |
| `>` | **gt** | `s1 > &s2`. Comparación léxica. |
| `<=` | **le** | `s1 <= &s2`. Comparación léxica. |
| `>=` | **ge** | `s1 >= &s2`. Comparación léxica. |
| `{}` | **to_string** | Se utiliza para la interpolación de cadenas en `printf`/`println`. |

## Iteración

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **iterator** | `iterator(self) -> StringCharsIter` | Devuelve un iterador que produce `rune`. Usado por `for c in s`. |

## Gestión de Memoria

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera manualmente la memoria de la cadena. |
| **destroy** | `destroy(self)` | Alias de `free`. |
| **forget** | `forget(self)` | Evita la liberación automática (transfiere la propiedad). |
| **Trait** | `impl Drop for String` | Llama automáticamente a `free()` cuando sale del alcance. |

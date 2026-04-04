# std/utf8

El módulo `std/utf8` proporciona utilidades para trabajar con puntos de código Unicode (tipo `rune`) y codificación UTF-8.

## Uso

```zc
import "std/utf8.zc"

fn main() {
    let r = 'ñ';
    
    if (Utf8::is_alpha(r)) {
        println "{r} es una letra";
    }
}
```

## Métodos

### Consulta e Identificación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **is_digit** | `is_digit(r: rune) -> bool` | Devuelve verdadero si la runa es un dígito decimal (0-9). |
| **is_alpha** | `is_alpha(r: rune) -> bool` | Devuelve verdadero si la runa es un carácter alfabético. |
| **is_whitespace** | `is_whitespace(r: rune) -> bool` | Devuelve verdadero si la runa es un carácter de espacio en blanco. |
| **is_upper** | `is_upper(r: rune) -> bool` | Devuelve verdadero si la runa es una letra mayúscula. |
| **is_lower** | `is_lower(r: rune) -> bool` | Devuelve verdadero si la runa es una letra minúscula. |
| **is_valid** | `is_valid(data: char*, len: usize) -> bool` | Devuelve verdadero si el búfer contiene datos UTF-8 válidos. |

### Transformación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **to_upper** | `to_upper(r: rune) -> rune` | Devuelve la versión en mayúsculas de la runa. |
| **to_lower** | `to_lower(r: rune) -> rune` | Devuelve la versión en minúsculas de la runa. |

### Codificación y Decodificación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **encode** | `encode(r: rune, buf: char*) -> usize` | Codifica una runa en UTF-8. Devuelve los bytes escritos (1-4). |
| **rune_len** | `rune_len(r: rune) -> usize` | Devuelve el número de bytes necesarios para codificar la runa. |
| **decode** | `decode(data: char*, len: usize, consumed: usize*) -> rune` | Decodifica la primera secuencia UTF-8 de los datos. |

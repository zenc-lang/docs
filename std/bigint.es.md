# std/bigint

`BigInt` proporciona aritmética de enteros de precisión arbitraria para Zen-C. Permite cálculos con enteros que exceden la capacidad de los tipos numéricos estándar como `u64`.

## Resumen

- **Precisión Arbitraria**: Los números están limitados solo por la memoria disponible.
- **Basado en Decimales**: Actualmente utiliza una representación simple en base 10 por simplicidad.
- **RAII**: Implementa el rasgo `Drop` para la gestión automática de la memoria del almacenamiento interno de dígitos.
- **Conveniente**: Admite la sobrecarga de operadores para una aritmética intuitiva.

## Uso

```zc
import "std/bigint.zc"

fn main() {
    let a = BigInt::from_int(1_000_000_000_000_000);
    let b = BigInt::from_int(2_000_000_000_000_000);
    
    // Utiliza sobrecarga de operadores
    let sum = a + b; 
    
    let s = sum.to_string();
    println "Suma: {s}";
    free(s);
} // sum, a, y b se liberan automáticamente aquí
```

## Definición de Estructura

```zc
struct BigInt {
    digits: Vec<u8>*;
}
```

## Métodos

### Construcción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `BigInt::new() -> BigInt` | Crea un nuevo `BigInt` inicializado a 0. |
| **from_int** | `BigInt::from_int(val: u64) -> BigInt` | Crea un nuevo `BigInt` a partir de un entero de 64 bits. |

### Modificación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **add_in_place** | `add_in_place(self, other: BigInt)` | Suma `other` a `self` mutando el estado interno. |

### Utilidad

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **clone** | `clone(self) -> BigInt` | Devuelve una copia profunda del `BigInt`. |
| **to_string** | `to_string(self) -> char*` | Devuelve una representación de cadena asignada en el montón. |

## Operadores

| Operador | Método | Descripción |
| :--- | :--- | :--- |
| `+` | **add** | Devuelve un nuevo `BigInt` que contiene la suma de dos valores. |
| `{}` | **to_string** | Habilita automáticamente la interpolación en cadenas formateadas. |

## Gestión de Memoria

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **free_mem** | `free_mem(self)` | Libera manualmente el almacenamiento subyacente de `Vec` y `BigInt`. |
| **Trait** | `impl Drop for BigInt` | Llama automáticamente a `free_mem()` cuando sale del alcance. |

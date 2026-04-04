# std/bigfloat

`BigFloat` proporciona aritmética de coma flotante decimal de precisión arbitraria para Zen-C. Se implementa como un `BigInt` escalado, permitiendo cálculos de alta precisión sin errores de redondeo binario.

## Resumen

- **Precisión Arbitraria**: Admite números decimales de cualquier tamaño, limitados solo por la memoria.
- **Representación Escalada**: Utiliza una magnitud `BigInt` y una escala `int` para representar valores decimales.
- **Control de Precisión**: Alinee fácilmente las escalas para sumas y restas precisas.
- **RAII**: La memoria para la magnitud subyacente se gestiona automáticamente mediante el rasgo `Drop`.

## Uso

```zc
import "std/bigfloat.zc"

fn main() {
    let a = BigFloat::from_int(123);
    a.scale = 2; // Representa 1.23
    
    let b = BigFloat::from_int(4567);
    b.scale = 3; // Representa 4.567
    
    let sum = a.add(b);
    
    let s = sum.to_string();
    println "Suma: {s}"; // Suma: 5.797
    free(s);
} // a, b, y sum se liberan automáticamente aquí
```

## Definición de Estructura

```zc
struct BigFloat {
    magnitude: BigInt;
    scale: int;
}
```

## Métodos

### Construcción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `BigFloat::new() -> BigFloat` | Crea un nuevo `BigFloat` inicializado a 0.0. |
| **from_int** | `BigFloat::from_int(val: u64) -> BigFloat` | Crea un `BigFloat` desde un entero con escala 0. |

### Modificación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **add** | `add(self, other: BigFloat) -> BigFloat` | Suma dos valores `BigFloat`, alineando automáticamente sus escalas. Devuelve un nuevo `BigFloat`. |
| **align_scale** | `align_scale(self, target_scale: int)` | Aumenta la escala del `BigFloat` a `target_scale` desplazando la magnitud. |

### Utilidad

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **clone** | `clone(self) -> BigFloat` | Devuelve una copia profunda del `BigFloat`. |
| **to_string** | `to_string(self) -> char*` | Devuelve una representación de cadena asignada en el montón con el punto decimal. |

## Gestión de Memoria

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **free_mem** | `free_mem(self)` | Libera manualmente la memoria subyacente del `BigInt`. |
| **Trait** | `impl Drop for BigFloat` | Llama automáticamente a `free_mem()` cuando sale del alcance. |

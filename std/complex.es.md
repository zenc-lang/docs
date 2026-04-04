# std/complex

La biblioteca `std/complex` proporciona la estructura `Complex` y operaciones matemáticas esenciales para trabajar con números complejos en Zen-C.

## Resumen

- **Tipo de Valor**: Estructura simple con componentes `real` e `imag`.
- **Soporte de Operadores**: Admite `+`, `-`, `*`, `/`, `==`, y `!=` mediante la sobrecarga de operadores.
- **Propiedades**: Proporciona métodos para calcular la magnitud y la fase.
- **Interpolación**: Puede usarse directamente en f-strings y sentencias de impresión.

## Uso

```zc
import "std/complex.zc"

fn main() {
    let c1 = Complex::new(3.0, 4.0);
    let c2 = Complex::new(1.0, 2.0);
    
    let sum = c1 + c2;
    let prod = c1 * c2;
    
    println "Suma: {sum}";       // Suma: 4.000000 + 6.000000i
    println "Magnitud: {c1.magnitude()}";
}
```

## Definición de Estructura

```zc
struct Complex {
    real: double;
    imag: double;
}
```

## Métodos

### Construcción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `Complex::new(r: double, i: double) -> Complex` | Crea un nuevo número complejo con componente real `r` y componente imaginario `i`. |

### Acceso y Consulta

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **magnitude** | `magnitude(self) -> double` | Devuelve la magnitud (valor absoluto) del número complejo. |
| **phase** | `phase(self) -> double` | Devuelve la fase (ángulo) en radianes. |

## Operadores

| Operador | Método | Descripción |
| :--- | :--- | :--- |
| `+` | **add** | Suma dos números complejos. |
| `-` | **sub** | Resta un número complejo de otro. |
| `*` | **mul** | Multiplica dos números complejos. |
| `/` | **div** | Divide un número complejo por otro. |
| `==` | **eq** | Comprueba si dos números complejos son estrictamente iguales. |
| `!=` | **neq** | Comprueba si dos números complejos no son iguales. |
| `{}` | **to_string** | Habilita la interpolación directa de cadenas. |

# std/math

El módulo `Math` proporciona un conjunto básico de constantes y funciones matemáticas estándar. Actúa como un envoltorio Zen-C alrededor de las operaciones matemáticas de coma flotante estándar.

## Resumen

- **Métodos Estáticos**: Todos los métodos se llaman directamente sobre la estructura `Math`.
- **Precisión**: Utiliza `double` para aritmética de coma flotante de alta precisión.
- **Exhaustivo**: Cubre trigonometría, exponenciales, logaritmos y redondeo.
- **Eficiente**: Envuelve directamente funciones optimizadas de la biblioteca C.

## Uso

```zc
import "std/math.zc"

fn main() {
    let radio = 5.0;
    let area = Math::PI() * Math::pow(radio, 2.0);
    println "Área del círculo: {area}";
}
```

## Constantes

Todas las constantes son funciones estáticas que devuelven un `double`.

| Constante | Descripción |
| :--- | :--- |
| **Math::PI()** | Constante de Arquímedes (aproximadamente 3.14159). |
| **Math::E()** | Número de Euler (aproximadamente 2.71828). |

## Métodos

### Aritmética

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **abs** | `abs(x: double) -> double` | Devuelve el valor absoluto de `x`. |
| **sqrt** | `sqrt(x: double) -> double` | Devuelve la raíz cuadrada de `x`. |
| **pow** | `pow(base: double, exp: double) -> double` | Devuelve la `base` elevada a la potencia de `exp`. |
| **exp** | `exp(x: double) -> double` | Devuelve `e` elevado a la potencia de `x`. |
| **log** | `log(x: double) -> double` | Devuelve el logaritmo natural (base-e) de `x`. |
| **log10** | `log10(x: double) -> double` | Devuelve el logaritmo en base 10 de `x`. |

### Trigonometría

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **sin** | `sin(x: double) -> double` | Devuelve el seno de `x` (radianes). |
| **cos** | `cos(x: double) -> double` | Devuelve el coseno de `x` (radianes). |
| **tan** | `tan(x: double) -> double` | Devuelve la tangente de `x` (radianes). |
| **asin** | `asin(x: double) -> double` | Devuelve el arcoseno de `x`. |
| **acos** | `acos(x: double) -> double` | Devuelve el arcocoseno de `x`. |
| **atan** | `atan(x: double) -> double` | Devuelve la arcotangente de `x`. |
| **atan2** | `atan2(y: double, x: double) -> double` | Devuelve la arcotangente de `y/x`. |

### Redondeo y Resto

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **ceil** | `ceil(x: double) -> double` | Redondea hacia arriba al entero más cercano. |
| **floor** | `floor(x: double) -> double` | Redondea hacia abajo al entero más cercano. |
| **round** | `round(x: double) -> double` | Redondea al entero más próximo. |
| **mod** | `mod(x: double, y: double) -> double` | Calcula el resto de coma flotante de `x / y`. |

### Mín / Máx

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **max** | `max(a: double, b: double) -> double` | Devuelve el mayor de dos valores. |
| **min** | `min(a: double, b: double) -> double` | Devuelve el menor de dos valores. |

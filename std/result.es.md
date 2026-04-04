# std/result

`Result<T>` es el tipo estándar para el manejo de errores en Zen-C. Representa el éxito (`Ok`), que contiene un valor de tipo `T`, o el fallo (`Err`), que contiene un mensaje de error en cadena.

## Resumen

- **Seguro**: Fuerza el manejo explícito de las rutas de éxito y de fallo.
- **Informativo**: Los casos `Err` llevan un mensaje de error descriptivo.
- **Genérico**: Admite cualquier tipo de valor de éxito `T`.
- **Integrado**: Funciona perfectamente con macros y patrones basados en `Result` para una propagación de errores concisa.

## Uso

```zc
import "std/result.zc"

fn divide(a: int, b: int) -> Result<int> {
    if (b == 0) {
        return Result<int>::Err("División por cero");
    }
    return Result<int>::Ok(a / b);
}

fn main() {
    match divide(10, 0) {
        Ok(val) => println "Resultado: {val}",
        Err(e)  => println "Error: {e}"
    }
}
```

## Definición de Estructura

```zc
struct Result<T> {
    is_ok: bool;
    val: T;
    err: char*;
}
```

## Métodos

### Construcción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **Ok** | `Result<T>::Ok(v: T) -> Result<T>` | Crea un resultado de éxito que contiene `v`. |
| **Err** | `Result<T>::Err(e: char*) -> Result<T>` | Crea un resultado de error con el mensaje `e`. |

### Consulta

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **is_ok** | `is_ok(self) -> bool` | Devuelve `true` si el resultado es `Ok`. |
| **is_err** | `is_err(self) -> bool` | Devuelve `true` si el resultado es `Err`. |

### Extracción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **unwrap** | `unwrap(self) -> T` | Devuelve el valor exitoso. Lanza un pánico con el mensaje de error si es `Err`. |
| **unwrap_ref** | `unwrap_ref(self) -> T*` | Devuelve un puntero al valor exitoso. Lanza un pánico si es `Err`. |
| **expect** | `expect(self, msg: char*) -> T` | Devuelve el valor o lanza un pánico con `msg` y el mensaje de error si es `Err`. |

## Gestión de Memoria

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **forget** | `forget(self)` | Pone a cero el valor exitoso sin llamar a destructores ni liberar memoria. |

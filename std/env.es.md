# std/env

El módulo `std/env` proporciona acceso multiplataforma a las variables de entorno del proceso.

## Resumen

- **Acceso Clave-Valor**: API sencilla para obtener, establecer y eliminar variables de entorno.
- **Prestadas o Propias**: Elija entre `get` (devuelve una cadena C prestada) y `get_dup` (devuelve una `String` propia, asignada en el montón).
- **Multiplataforma**: Abstrae de forma segura las llamadas al sistema subyacentes para la manipulación del entorno.

## Uso

```zc
import "std/env.zc"

fn main() {
    // Establecer una variable de entorno
    Env::set("MY_APP_MODE", "development");

    // Recuperar (Prestada)
    match Env::get("MY_APP_MODE") {
        Some(val) => println "Modo: {val}",
        None => println "Modo no establecido"
    }

    // Recuperar (String propia para RAII)
    match Env::get_dup("HOME") {
        Some(home) => {
             println "Hogar: {home}";
             // home se libera automáticamente
        }
        None => println "HOME no encontrada"
    }
}
```

## Definición de Enum

```zc
enum EnvRes {
    OK,
    ERR,
}
```

## Métodos

### Acceso y Consulta

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **get** | `Env::get(name: char*) -> Option<char*>` | Recupera un puntero prestado a una variable de entorno. No liberar. |
| **get_dup** | `Env::get_dup(name: char*) -> Option<String>` | Recupera una variable de entorno como un nuevo objeto `String`. |

### Modificación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **set** | `Env::set(name: char*, value: char*) -> EnvRes` | Establece o actualiza una variable de entorno. |
| **unset** | `Env::unset(name: char*) -> EnvRes` | Elimina una variable de entorno del proceso actual. |

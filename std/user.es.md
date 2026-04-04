# std/sys/user

El módulo `std/sys/user` proporciona acceso a la información de identificación de usuario y grupo, envolviendo `unistd.h` de POSIX.

## Resumen

- **Identidad de Usuario**: Recupere los IDs de usuario (UID) y de grupo (GID) reales y efectivos.
- **Contexto del Proceso**: Útil para la comprobación de privilegios y la gestión de permisos en utilidades del sistema.

## Uso

```zc
import "std/sys/user.zc"
import "std/io.zc"

fn main() {
    println "UID actual: {User::get_uid()}";
    println "GID actual: {User::get_gid()}";
    
    if (User::get_euid() == 0) {
        println "Ejecutando con privilegios de root.";
    }
}
```

## Definición de Estructura

```zc
struct User {}
```

## Métodos

### Métodos de `User`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **get_uid** | `User::get_uid() -> u32` | Devuelve el ID de usuario real del proceso actual. |
| **get_gid** | `User::get_gid() -> u32` | Devuelve el ID de grupo real del proceso actual. |
| **get_euid** | `User::get_euid() -> u32` | Devuelve el ID de usuario efectivo. |
| **get_egid** | `User::get_egid() -> u32` | Devuelve el ID de grupo efectivo. |

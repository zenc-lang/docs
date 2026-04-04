# std/sys/info

El módulo `std/sys/info` proporciona utilidades para recuperar identificación e información del sistema, envolviendo `uname` de POSIX.

## Resumen

- **Identificación del Sistema**: Acceso al nombre del SO, versión del kernel, arquitectura de hardware y más.
- **Cumplimiento de RAII**: La estructura `Uname` gestiona automáticamente la memoria para sus cadenas internas.

## Uso

```zc
import "std/sys/info.zc"
import "std/io.zc"

fn main() {
    let info = SysInfo::get_uname();
    println "SO: {info.sysname}";
    println "Kernel: {info.release}";
    println "Arquitectura: {info.machine}";
}
```

## Definición de Estructura

### `Uname`
Contiene campos de identificación del sistema.
```zc
struct Uname {
    sysname: String;
    nodename: String;
    release: String;
    version: String;
    machine: String;
}
```

## Métodos

### Métodos de `SysInfo`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **get_uname** | `SysInfo::get_uname() -> Uname` | Devuelve una estructura `Uname` que contiene varias cadenas del sistema. |

## Gestión de Memoria
- `Uname` implementa `impl Drop` y liberará automáticamente sus búferes `String` internos cuando salga del alcance.

# std/sys/mman

El módulo `std/sys/mman` proporciona una interfaz Zen-C para funciones de mapeo y protección de memoria, envolviendo `sys/mman.h` de POSIX.

## Resumen

- **Mapeo de Memoria**: Mapea archivos o memoria anónima en el espacio de direcciones del proceso.
- **Control de Protección**: Cambia dinámicamente los permisos de la región de memoria (Lectura, Escritura, Ejecución).
- **Memoria Anónima**: Asigna grandes bloques de memoria directamente del SO sin un archivo.

## Uso

```zc
import "std/sys/mman.zc"
import "std/io.zc"

fn main() {
    let size: usize = 4096;
    let prot = Z_PROT_READ | Z_PROT_WRITE;
    let flags = Z_MAP_PRIVATE | Z_MAP_ANONYMOUS;
    
    let addr = Memory::mmap(size, prot, flags);
    if ((isize)addr == Z_MAP_FAILED) {
        println "Mapeo fallido";
        return;
    }
    
    // Usar memoria...
    
    Memory::munmap(addr, size);
}
```

## Definición de Estructura

```zc
struct Memory {}
```

## Métodos

### Métodos de `Memory`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **mmap** | `Memory::mmap(len: usize, prot: int, flags: int) -> void*` | Crea un nuevo mapeo en el espacio de direcciones virtuales del proceso que llama. |
| **munmap** | `Memory::munmap(addr: void*, len: usize) -> bool` | Elimina los mapeos para el rango de direcciones especificado. Devuelve `true` si tiene éxito. |
| **mprotect** | `Memory::mprotect(addr: void*, len: usize, prot: int) -> bool` | Cambia las protecciones de acceso para las páginas de memoria del proceso que llama. Devuelve `true` si tiene éxito. |

## Constantes

### Banderas de Protección
- `Z_PROT_NONE`: La página no puede ser accedida.
- `Z_PROT_READ`: La página puede ser leída.
- `Z_PROT_WRITE`: La página puede ser escrita.
- `Z_PROT_EXEC`: La página puede ser ejecutada.

### Banderas de Visibilidad
- `Z_MAP_SHARED`: Comparte este mapeo.
- `Z_MAP_PRIVATE`: Crea un mapeo de copia en escritura privado.
- `Z_MAP_ANONYMOUS`: El mapeo no está respaldado por ningún archivo.

### Valores de Error
- `Z_MAP_FAILED`: Devuelto por `mmap` en caso de error.

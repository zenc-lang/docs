# std/sys/stat

El módulo `std/sys/stat` proporciona una interfaz para recuperar metadatos extendidos de archivos e información de estado, envolviendo `sys/stat.h` de POSIX.

## Resumen

- **Metadatos de Archivo**: Recupere el tamaño del archivo, el modo (permisos) y las marcas de tiempo.
- **Marcas de Tiempo**: Acceda a los tiempos de acceso, modificación y cambio como marcas de tiempo de Unix.
- **Comprobación de Tipo**: Métodos de ayuda para determinar si un modo representa un archivo o un directorio.

## Uso

```zc
import "std/sys/stat.zc"
import "std/io.zc"

fn main() {
    let res = FileStat::stat("mi_archivo.txt");
    if (res.is_some()) {
        let st = res.unwrap();
        println "Tamaño: {st.size} bytes";
        println "Permisos: {st.mode}";
        
        if (FileStat::is_dir(st.mode)) {
            println "Es un directorio.";
        }
    }
}
```

## Definición de Estructura

### `Stat`
Contiene metadatos de archivo al estilo Unix.
```zc
struct Stat {
    mode: u32;
    size: u64;
    atime: i64;
    mtime: i64;
    ctime: i64;
    uid: u32;
    gid: u32;
}
```

## Métodos

### Métodos de `FileStat`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **stat** | `FileStat::stat(path: char*) -> Option<Stat>` | Devuelve los metadatos para la ruta dada, o `None` si falla. |
| **is_dir** | `FileStat::is_dir(mode: u32) -> bool` | Comprueba si el modo dado representa un directorio. |
| **is_file** | `FileStat::is_file(mode: u32) -> bool` | Comprueba si el modo dado representa un archivo regular. |

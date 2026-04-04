# std/fs

El módulo `std/fs` proporciona una API completa para interactuar con el sistema de archivos, incluyendo E/S de archivos, manipulación de directorios y recuperación de metadatos.

## Resumen

- **Handles Seguros**: La estructura `File` proporciona un envoltorio seguro alrededor de los descriptores de archivos crudos.
- **RAII**: Los descriptores de archivos se cierran automáticamente cuando salen del alcance a través del rasgo `Drop`.
- **Manejo de Errores**: Utiliza `Result<T>` para todas las operaciones que pueden fallar, proporcionando mensajes de error descriptivos.
- **Conveniencia**: Incluye métodos estáticos para tareas comunes como leer o escribir un archivo completo en una sola llamada.

## Uso

```zc
import "std/fs.zc"

fn main() {
    // Lectura básica de archivos usando RAII
    match File::read_all("config.txt") {
        Ok(content) => println "Configuración: {content}",
        Err(e) => println "Error al leer configuración: {e}"
    }
    
    // Descriptor de archivo explícito con cierre automático
    match File::open("data.log", "a") {
        Ok(file) => {
            file.write_string("Entrada de registro\n");
            // el archivo se cierra automáticamente aquí
        }
        Err(e) => println "Fallo al abrir el registro: {e}"
    }
}
```

## Definiciones de Estructura

### `File`
Representa un descriptor de archivo abierto.
```zc
struct File {
    handle: void*;
}
```

### `Metadata`
Metadatos de archivo o directorio.
```zc
struct Metadata {
    size: U64;
    is_dir: bool;
    is_file: bool;
}
```

### `DirEntry`
Representa una entrada en un directorio.
```zc
struct DirEntry {
    name: String;
    is_dir: bool;
}
```

## Métodos

### Abrir / Cerrar

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **open** | `File::open(path: char*, mode: char*) -> Result<File>` | Abre un archivo en `path` con el modo `mode`. |
| **close** | `close(self)` | Cierra explícitamente el descriptor de archivo. |

### Leer / Escribir

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **read_to_string** | `read_to_string(self) -> Result<String>` | Lee el archivo completo en una `String`. |
| **read_all** | `File::read_all(path: char*) -> Result<String>` | Utilidad estática para leer un archivo completamente. |
| **read_lines** | `File::read_lines(path: char*) -> Result<Vec<String>>` | Utilidad estática para leer un archivo en un vector de líneas. |
| **write_string** | `write_string(self, content: char*) -> Result<bool>` | Escribe una cadena en el archivo. |
| **write_lines** | `File::write_lines(path: char*, lines: Vec<String>*) -> Result<bool>` | Utilidad estática para escribir un vector de líneas en un archivo. |

### Utilidades de Ruta

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **exists** | `File::exists(path: char*) -> bool` | Devuelve verdadero si la ruta existe. |
| **current_dir** | `File::current_dir() -> Result<String>` | Devuelve la ruta absoluta del directorio de trabajo actual. |
| **metadata** | `File::metadata(path: char*) -> Result<Metadata>` | Recupera metadatos para la ruta especificada. |

### Operaciones de Archivo y Directorio

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **create_dir** | `File::create_dir(path: char*) -> Result<bool>` | Crea un nuevo directorio. |
| **remove_file** | `File::remove_file(path: char*) -> Result<bool>` | Elimina el archivo especificado. |
| **remove_dir** | `File::remove_dir(path: char*) -> Result<bool>` | Elimina el directorio especificado (debe estar vacío). |
| **read_dir** | `File::read_dir(path: char*) -> Result<Vec<DirEntry>>` | Devuelve una lista de entradas en un directorio. |

## Gestión de Memoria

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **Trait** | `impl Drop for File` | Cierra automáticamente el descriptor de archivo cuando sale del alcance. |

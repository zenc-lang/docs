# std/path

El módulo `std/path` proporciona utilidades multiplataforma para manipular rutas del sistema de archivos. Simplifica tareas comunes como unir rutas, extraer extensiones y encontrar directorios padres.

## Resumen

- **Multiplataforma**: Maneja adecuadamente tanto las barras inclinadas como las invertidas durante la manipulación.
- **Tipo Seguro**: La estructura `Path` encapsula la información de la ruta, distinguiéndola de las cadenas normales.
- **Análisis Conveniente**: Extraiga fácilmente componentes como `extension`, `file_name` y `parent`.
- **RAII**: La memoria se gestiona automáticamente a través del rasgo `Drop`.

## Uso

```zc
import "std/path.zc"

fn main() {
    let p = Path::new("/home/usuario");
    let ruta_completa = p.join("docs/archivo.txt");
    
    println "Ruta completa: {ruta_completa.c_str()}";
    
    match ruta_completa.extension() {
        Some(ext) => println "Extensión: {ext}",
        None => println "No se encontró extensión"
    }
} // ruta_completa y p se liberan automáticamente aquí
```

## Definición de Estructura

```zc
struct Path {
    str: String;
}
```

## Métodos

### Construcción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `Path::new(s: char*) -> Path` | Crea una nueva `Path` a partir de una cadena C. |
| **from_string** | `Path::from_string(s: String) -> Path` | Crea una `Path` tomando la propiedad de una `String`. |
| **clone** | `clone(self) -> Path` | Devuelve una copia profunda de la `Path`. |

### Manipulación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **join** | `join(self, other: char*) -> Path` | Añade `other` a la ruta utilizando el separador de directorios correcto. |

### Análisis

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **extension** | `extension(self) -> Option<String>` | Devuelve la extensión del archivo (sin el punto inicial), si la hay. |
| **file_name** | `file_name(self) -> Option<String>` | Devuelve el componente final de la ruta. |
| **parent** | `parent(self) -> Option<Path>` | Devuelve la ruta del directorio padre. |

### Acceso

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **c_str** | `c_str(self) -> char*` | Devuelve la representación de cadena C subyacente. |

## Gestión de Memoria

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera manualmente la memoria de la cadena interna de la ruta. |
| **Trait** | `impl Drop for Path` | Llama automáticamente a `free()` cuando sale del alcance. |

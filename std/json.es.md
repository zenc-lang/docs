# std/json

El módulo `std/json` proporciona una implementación de analizador y constructor JSON de estilo DOM para Zen-C. Cuenta con una API sencilla para crear, manipular y serializar datos JSON con gestión automática de memoria.

## Resumen

- **Estilo DOM**: Estructura de árbol jerárquica de nodos `JsonValue`.
- **Accesores Seguros**: Compruebe los tipos (`is_string`, `is_number`) y extraiga los valores de forma segura.
- **Limpieza Automática**: Implementa el rasgo `Drop` para una gestión de memoria recursiva y automática.
- **Cumple con los Estándares**: Admite los tipos JSON estándar, incluidos objetos, matrices, cadenas, números, booleanos y nulo.

## Uso

```zc
import "std/json.zc"

fn main() {
    // Construyendo JSON
    let obj = JsonValue::object();
    obj.set("nombre", JsonValue::string("Alicia"));
    obj.set("edad", JsonValue::number(30.0));
    obj.set("activo", JsonValue::bool(true));
    
    // Serialización
    let json_str = obj.to_string();
    println "Serializado: {json_str}";
    
    // Análisis
    let entrada = "{\"puntuación\": 100}";
    match JsonValue::parse(entrada) {
        Ok(parsed) => {
            println "Puntuación: {parsed.get(\"puntuación\").unwrap().as_int().unwrap()}";
            // parsed se libera automáticamente cuando termina este bloque
        }
        Err(e) => println "Error: {e}"
    }
} // obj se libera automáticamente aquí
```

## Definición de Estructura

```zc
struct JsonValue {
    kind: JsonType;
    // ... campos internos
}
```

## Métodos

### Construcción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **null** | `JsonValue::null() -> JsonValue` | Crea un valor nulo. |
| **bool** | `JsonValue::bool(b: bool) -> JsonValue` | Crea un valor booleano. |
| **number** | `JsonValue::number(n: double) -> JsonValue` | Crea un valor numérico. |
| **string** | `JsonValue::string(s: char*) -> JsonValue` | Crea un valor de cadena. |
| **array** | `JsonValue::array() -> JsonValue` | Crea una matriz JSON vacía. |
| **object** | `JsonValue::object() -> JsonValue` | Crea un objeto JSON vacío. |

### Análisis

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **parse** | `JsonValue::parse(json: char*) -> Result<JsonValue*>` | Analiza una cadena JSON en un árbol asignado en el montón. |

### Accesores

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **is_null** | `is_null(self) -> bool` | Devuelve verdadero si el tipo es nulo. |
| **is_bool** | `is_bool(self) -> bool` | Devuelve verdadero si el tipo es booleano. |
| **is_number** | `is_number(self) -> bool` | Devuelve verdadero si el tipo es un número. |
| **is_string** | `is_string(self) -> bool` | Devuelve verdadero si el tipo es una cadena. |
| **is_array** | `is_array(self) -> bool` | Devuelve verdadero si el tipo es una matriz. |
| **is_object** | `is_object(self) -> bool` | Devuelve verdadero si el tipo es un objeto. |
| **as_string** | `as_string(self) -> Option<char*>` | Devuelve el puntero de cadena si aplica. |
| **as_int** | `as_int(self) -> Option<int>` | Devuelve el valor entero si aplica. |
| **as_float** | `as_float(self) -> Option<double>` | Devuelve el valor numérico si aplica. |
| **as_bool** | `as_bool(self) -> Option<bool>` | Devuelve el valor booleano si aplica. |

### Modificación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **push** | `push(self, val: JsonValue)` | Añade un valor hijo a una matriz JSON. |
| **set** | `set(self, key: char*, val: JsonValue)` | Inserta o actualiza un par clave-valor en un objeto JSON. |
| **get** | `get(self, key: char*) -> Option<JsonValue*>` | Recupera un valor hijo de un objeto por clave. |
| **at** | `at(self, index: usize) -> Option<JsonValue*>` | Recupera un valor hijo de una matriz por índice. |

### Serialización

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **to_string** | `to_string(self) -> String` | Devuelve una cadena JSON serializada. |

## Gestión de Memoria

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera de forma recursiva el valor y todos los nodos descendientes. |
| **Trait** | `impl Drop for JsonValue` | Activa automáticamente el `free()` recursivo cuando sale del alcance. |

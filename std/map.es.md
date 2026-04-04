# std/map

`Map<V>` es una implementación genérica de mapa hash que mapea claves de cadena a valores de tipo `V`.

## Uso

```zc
import "std/map.zc"

fn main() {
    let m = Map<int>::new();
    
    m.put("uno", 1);
    m.put("dos", 2);
    
    if (m.contains("uno")) {
        let val = m.get("uno");
        println "{val.unwrap()}";
    }
    
    m.remove("dos");
} // m se libera automáticamente aquí
```

## Definición de Estructura

```zc
struct Map<V> {
    keys: char**;
    vals: V*;
    // ... campos internos
}
```

## Métodos

### Construcción

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **new** | `Map<V>::new() -> Map<V>` | Crea un nuevo mapa vacío. |

### Iteración

Puede iterar sobre los pares clave-valor del mapa utilizando un bucle `for`.

```zc
let m = Map<int>::new();
m.put("a", 1);

for entry in m {
    println "Clave: {entry.key}, Val: {entry.val}";
}
```

El iterador produce una estructura `MapEntry<V>`:
```zc
struct MapEntry<V> {
    key: char*;
    val: V;
}
```

### Modificación

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **put** | `put(self, key: char*, val: V)` | Inserta o actualiza un par clave-valor. |
| **remove** | `remove(self, key: char*)` | Elimina una clave y su valor del mapa. |

### Acceso y Consulta

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **get** | `get(self, key: char*) -> Option<V>` | Recupera el valor asociado con la clave. |
| **contains** | `contains(self, key: char*) -> bool` | Devuelve verdadero si la clave existe. |
| **length** | `length(self) -> usize` | Devuelve el número de elementos en el mapa. |
| **is_empty** | `is_empty(self) -> bool` | Devuelve verdadero si el mapa está vacío. |
| **capacity** | `capacity(self) -> usize` | Devuelve la capacidad actual del mapa. |

### Ayudantes de Iteración

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **is_slot_occupied** | `is_slot_occupied(self, idx: usize) -> bool` | Comprueba si un índice de ranura bruta está ocupado. |
| **key_at** | `key_at(self, idx: usize) -> char*` | Obtiene la clave en el índice de ranura bruta. |
| **val_at** | `val_at(self, idx: usize) -> V` | Obtiene el valor en el índice de ranura bruta. |

## Gestión de Memoria

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera el almacenamiento interno del mapa. **Nota**: Esto no libera los valores si son punteros/objetos. |
| **Trait** | `impl Drop for Map` | Llama automáticamente a `free()` cuando sale del alcance. |

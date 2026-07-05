+++
title = "8. Gestión de Memoria"
weight = 8
+++

# 8. Gestión de Memoria


Zen C permite la gestión manual de memoria con ayudas ergonómicas.

#### Defer
Ejecuta código cuando el ámbito actual finaliza. Las sentencias defer se ejecutan en orden LIFO (último en entrar, primero en salir).
```zc
let f = fopen("archivo.txt", "r");
defer fclose(f);
```

> Para prevenir comportamientos indefinidos, las sentencias de flujo de control (`return`, `break`, `continue`, `goto`) **no están permitidas** dentro de un bloque `defer`.

#### Autofree
Libera automáticamente la variable cuando finaliza el ámbito.
```zc
autofree let tipos = malloc(1024);
```

#### Semántica de Recursos (Movimiento por Defecto)
Zen C trata los tipos con destructores (como `File`, `Vec` o punteros de malloc) como **Recursos**. Para prevenir errores de doble liberación (double-free), los recursos no pueden duplicarse implícitamente.

- **Movimiento por Defecto**: La asignación de una variable de recurso transfiere la posesión. La variable original se vuelve inválida (Movida).
- **Tipos Copy**: Los tipos sin destructores pueden optar por el comportamiento `Copy`, haciendo que la asignación sea una duplicación.

**Diagnóstico y Filosofía**:
Si ves un error "Use of moved value", el compilador te está diciendo: *"Este tipo posee un recurso (como memoria o un manejador) y copiarlo a ciegas es inseguro."*

> **Contraste:** A diferencia de C/C++, Zen C no duplica implícitamente los valores que poseen recursos.

**Argumentos de Función**:
Pasar un valor a una función sigue las mismas reglas que la asignación: los recursos se mueven a menos que se pasen por referencia.

```zc
fn procesar(r: Recurso) { ... } // 'r' se mueve dentro de la función
fn mirar(r: Recurso*) { ... }   // 'r' es prestado (referencia)
```

**Clonación Explícita**:
Si *realmente* quieres dos copias de un recurso, hazlo explícito:

```zc
let b = a.clone(); // Llama al método 'clone' del trait Clone
```

**Optar por Copy (Tipos de Valor)**:
Para tipos pequeños sin destructores:

```zc
struct Point { x: int; y: int; }
impl Copy for Point {} // Optar por la duplicación implícita

fn main() {
    let p1 = Point { x: 1, y: 2 };
    let p2 = p1; // Copiado. p1 sigue siendo válido.
}
```

#### RAII / Drop Trait
Implementa `Drop` para ejecutar lógica de limpieza automáticamente.
```zc
impl Drop for MiEstructura {
    fn drop(self) {
        self.free();
    }
}
```

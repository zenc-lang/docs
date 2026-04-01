+++
title = "9. Programación Orientada a Objetos"
weight = 9
+++

# 9. Programación Orientada a Objetos


#### Métodos
Define métodos en los tipos usando `impl`.
```zc
impl Point {
    // Método estático (convención de constructor)
    fn new(x: int, y: int) -> Self {
        return Point{x: x, y: y};
    }

    // Método de instancia
    fn dist(self) -> float {
        return sqrt(self.x * self.x + self.y * self.y);
    }
}
```

**Atajo de Self**: En métodos con un parámetro `self`, puedes usar `.campo` como abreviatura de `self.campo`:
```zc
impl Point {
    fn dist(self) -> float {
        return sqrt(.x * .x + .y * .y);  // Equivalente a self.x, self.y
    }
}
```

#### Métodos primitivos
Zen C permite definir métodos en tipos primitivos (como `int`, `bool`, etc.) usando la misma sintaxis `impl`.

```zc
impl int {
    fn abs(self) -> int {
        return *self < 0 ? -(*self) : *self;
    }
}

let x = -10;
let y = x.abs(); // 10
let z = (-5).abs(); // 5 (Literals supported)
```

#### Traits
Define un comportamiento compartido.
```zc
struct Circle { radio: f32; }

trait Dibujable {
    fn dibujar(self);
}

impl Dibujable for Circle {
    fn dibujar(self) { ... }
}

let circulo = Circle{};
let dibujable: Dibujable = &circulo;
```

#### Traits Estándar
Zen C incluye traits estándar que se integran con la sintaxis del lenguaje.

**Iterable**

Implementa `Iterable<T>` para habilitar bucles `for-in` para tus tipos personalizados.

```zc
import "std/iter.zc"

// Define un Iterador
struct MiIter {
    actual: int;
    final: int;
}

impl MiIter {
    fn next(self) -> Option<int> {
        if self.actual < self.final {
            self.actual += 1;
            return Option<int>::Some(self.actual - 1);
        }
        return Option<int>::None();
    }
}

// Implementa Iterable
impl MiRango {
    fn iterator(self) -> MiIter {
        return MiIter{actual: self.inicio, final: self.fin};
    }
}

// Uso en un Bucle
for i in mi_rango {
    println "{i}";
}
```

**Drop**

Implementa `Drop` para definir un destructor que se ejecuta cuando el objeto sale de ámbito (RAII).

```zc
import "std/mem.zc"

struct Recurso {
    ptr: void*;
}

impl Drop for Recurso {
    fn drop(self) {
        if self.ptr != NULL {
            free(self.ptr);
        }
    }
}
```

{% alert(type="note") %}
Si una variable es movida, no se llama a `drop` en la variable original. Se adhiere a la [Semántica de Recursos](@/tour/08-memory-management.es.md#semantica-de-recursos-movimiento-por-defecto).
{% end %}

**Copy**

Trait marcador para optar por el comportamiento `Copy` (duplicación implícita) en lugar de la semántica de movimiento. Se usa mediante `@derive(Copy)`.

{% alert(type="caution") %}
**Regla:** Los tipos que implementan `Copy` no deben definir un destructor (`Drop`).
{% end %}

```zc
@derive(Copy)
struct Point { x: int; y: int; }

fn main() {
    let p1 = Point{x: 1, y: 2};
    let p2 = p1; // ¡Copiado! p1 sigue siendo válido.
}
```

**Clone**

Implementa `Clone` para permitir la duplicación explícita de tipos que poseen recursos.

```zc
import "std/mem.zc"

struct MiBox { val: int; }

impl Clone for MiBox {
    fn clone(self) -> MiBox {
        return MiBox{val: self.val};
    }
}

fn main() {
    let b1 = MiBox{val: 42};
    let b2 = b1.clone(); // Copia explícita
}
```

#### Composición
Usa `use` para embeber otros structs. Puedes mezclarlos (aplanar campos) o nombrarlos (anidar campos).

```zc
struct Entity { id: int; }

struct Player {
    // Mezcla (Mixin - Sin nombre): Aplana los campos
    use Entity;  // Añade 'id' a Player directamente
    nombre: string;
}

struct Match {
    // Composición (Con nombre): Anida los campos
    use p1: Player; // Accedido mediante match.p1
    use p2: Player; // Accedido mediante match.p2
}
```

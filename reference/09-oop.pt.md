+++
title = "9. Programação Orientada a Objetos"
weight = 9
+++

# 9. Programação Orientada a Objetos


#### Métodos
Defina métodos em tipos usando `impl`.
```zc
impl Point {
    // Método estático (convenção de construtor)
    fn new(x: int, y: int) -> Self {
        return Point{x: x, y: y};
    }

    // Método de instância
    fn dist(self) -> float {
        return sqrt(self.x * self.x + self.y * self.y);
    }
}
```

**Atalho de Self**: Em métodos com um parâmetro `self`, você pode usar `.campo` como atalho para `self.campo`:
```zc
impl Point {
    fn dist(self) -> float {
        return sqrt(.x * .x + .y * .y);  // Equivalente a self.x, self.y
    }
}
```

#### Métodos Primitivos
Zen C permite definir métodos em tipos primitivos (como `int`, `bool`, etc.) usando a mesma sintaxe `impl`.

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
Defina comportamento compartilhado.
```zc
struct Circle { radius: f32; }

trait Drawable {
    fn draw(self);
}

impl Drawable for Circle {
    fn draw(self) { ... }
}

let circle = Circle{};
let drawable: Drawable = &circle;
```

#### Traits Padrões
Zen C inclui traits padrões que se integram com a sintaxe da linguagem.

**Iterable**

Implemente `Iterable<T>` para habilitar loops `for-in` para seus tipos customizados.

```zc
import "std/iter.zc"

// Defina um Iterator
struct MyIter {
    curr: int;
    stop: int;
}

impl MyIter {
    fn next(self) -> Option<int> {
        if self.curr < self.stop {
            self.curr += 1;
            return Option<int>::Some(self.curr - 1);
        }
        return Option<int>::None();
    }
}

// Implemente Iterable
impl MyRange {
    fn iterator(self) -> MyIter {
        return MyIter{curr: self.start, stop: self.end};
    }
}

// Use no Loop
for i in my_range {
    println "{i}";
}
```

**Drop**

Implemente `Drop` para definir um destrutor que executa quando o objeto sai de escopo (RAII).

```zc
import "std/mem.zc"

struct Resource {
    ptr: void*;
}

impl Drop for Resource {
    fn drop(self) {
        if self.ptr != NULL {
            free(self.ptr);
        }
    }
}
```

> **Nota:** Se uma variável é movida, `drop` NÃO É chamado na variável original. Ela se adere à [Semântica de Recursos](#semântica-de-recursos-move-por-padrão).

**Copy**

Trait marcador para optar pelo comportamento `Copy` (duplicação implícita) em vez de semântica Move. Usado via `@derive(Copy)`.

{% alert(type="caution") %}
Tipos que implementam `Copy` não devem definir um destrutor (`Drop`).
{% end %}

```zc
@derive(Copy)
struct Point { x: int; y: int; }

fn main() {
    let p1 = Point{x: 1, y: 2};
    let p2 = p1; // Copiado! p1 permanece válido.
}
```

**Clone**

Implemente `Clone` para permitir duplicação explícita de tipos que possuem recursos.

```zc
import "std/mem.zc"

struct MyBox { val: int; }

impl Clone for MyBox {
    fn clone(self) -> MyBox {
        return MyBox{val: self.val};
    }
}

fn main() {
    let b1 = MyBox{val: 42};
    let b2 = b1.clone(); // Cópia explícita
}
```

#### Composição
Use `use` para incorporar outros structs. Você pode misturá-los (achatar campos) ou nomeá-los (aninhar campos).

```zc
struct Entity { id: int; }

struct Player {
    // Mixin (Sem nome): Achata campos
    use Entity;  // Adiciona 'id' ao Player diretamente
    name: string;
}

struct Match {
    // Composição (Nomeado): Aninha campos
    use p1: Player; // Acessado via match.p1
    use p2: Player; // Acessado via match.p2
}
```

+++
title = "3. Tipos Agregados"
weight = 3
+++

# 3. Tipos Agregados


#### Arrays
Arrays de tamaño fijo con semántica de valor.
```zc
def SIZE = 5;
let ints: int[SIZE] = [1, 2, 3, 4, 5];
let zeros: [int; SIZE]; // Inicializado a cero
```




#### Tuples

Agrupa múltiples valores en un único valor compuesto. Las tuplas admiten aridades arbitrarias (2, 3, 4, … hasta 10+), composición anidada, mutación de campos individuales y deconstrucción.

**Uso básico**

```zc
let pair = (1, "hello");
let triple = (1, "hello", 3.14);
let five = (1, 2, 3, 4, 5);
let typed: (int, string, f64) = (1, "two", 3.0);
```

**Acceso a campos**

Los elementos se acceden posicionalmente con `.0`, `.1`, `.2`, etc., o mediante los nombres de campo `.v0`, `.v1`:

```zc
let t = (1, "hello", 3.14);
assert(t.0 == 1);
assert(t.v1 == "hello");
```

**Múltiples valores de retorno**

Las funciones pueden devolver tuplas para proporcionar múltiples resultados:

```zc
fn stats(data: int) -> (int, int) {
    return (data * 2, data + 1);
}
let r = stats(5);
assert(r.0 == 10);
assert(r.1 == 6);
```

**Deconstrucción**

```zc
let (sum, diff) = add_and_subtract(3, 2);
let (a: string, b: u8) = ("hello", 42);
let (x, y: i32) = (1, 2);
```

**Tuplas anidadas**

```zc
let nested = ((1, 2), (3, 4));
let inner = nested.v0;
assert(inner.v0 == 1);
```

**Mutación**

Los campos individuales se pueden reasignar:

```zc
let t = (1, 2);
t.v0 = 99;
```

**Comparación de cadenas**

Las tuplas con campos `string` deben usar `strcmp()` para la comparación, no `==` (que compara punteros en `char*`):

```zc
let t = (1, "hello");
assert(strcmp(t.1, "hello") == 0);
```

**Tuplas en variantes de enumeración**

Las variantes de enum pueden contener datos de tupla:

```zc
enum Shape {
    Point, Line(int, int), Labeled(int, string, f64),
}
```


#### Structs
Estructuras de datos con campos de bits opcionales.
```zc
struct Point {
    x: int;
    y: int;
}

// Inicialización de struct
let p = Point { x: 10, y: 20 };

// Campos de bits
struct Flags {
    valid: U8 : 1;
    mode:  U8 : 3;
}
```

{% alert(type="note") %}
Los structs usan [Semántica de Movimiento](@/tour/08-memory-management.es.md#semantica-de-recursos-movimiento-por-defecto) por defecto. Los campos se pueden acceder mediante `.` incluso en punteros (Auto-Dereferencia).
{% end %}

#### Structs Opacos
Puedes definir un struct como `opaque` para restringir el acceso a sus campos solo al módulo que lo define, permitiendo aún que el struct sea asignado en el stack (el tamaño es conocido).

```zc
// En user.zc
opaque struct User {
    id: int;
    name: string;
}

fn new_user(name: string) -> User {
    return User{id: 1, name: name}; // OK: Dentro del módulo
}

// En main.zc
import "user.zc";

fn main() {
    let u = new_user("Alice");
    // let id = u.id; // Error: No se puede acceder al campo privado 'id'
}
```

#### Enums
Uniones etiquetadas (Tipos suma) capaces de contener datos.
```zc
enum Shape {
    Circle(float),      // Contiene el radio
    Rect(float, float), // Contiene ancho y alto
    Point               // Sin datos
}
```

#### Uniones
Uniones estándar de C (acceso inseguro).
```zc
union Data {
    i: int;
    f: float;
}
```

#### Vectores SIMD
Tipos de vectores SIMD nativos utilizando extensiones de vectores de GCC/Clang. Anota un struct con `@vector(N)` para definir un vector de N elementos.
```zc
import "std/simd.zc";

fn main() {
    let a = f32x4{v: 1.0};              // Difusión: {1.0, 1.0, 1.0, 1.0}
    let b = f32x4{1.0, 2.0, 3.0, 4.0};  // Inicialización por elemento
    let c = a + b;                       // Suma por elementos
    let x = c[0];                        // Acceso a elementos (float)
}
```
Los operadores aritméticos (`+`, `-`, `*`, `/`) y bit a bit (`&`, `|`, `^`) funcionan por elementos. Consulta [`std/simd.zc`](../std/simd.zc) para los tipos predefinidos.

#### Alias de Tipos
Crea un nuevo nombre para un tipo existente.
```zc
alias ID = int;
alias PointMap = Map<string, Point>
alias OpFunc = fn(int, int) -> int
```
> **Nota:** El punto y coma final es opcional para los alias de tipo.

#### Alias de Tipos Opacos
Puedes definir un alias de tipo como `opaque` para crear un nuevo tipo que sea distinto de su tipo subyacente fuera del módulo que lo define. Esto proporciona una fuerte encapsulación y seguridad de tipos sin la sobrecarga en tiempo de ejecución de un struct envoltorio.

```zc
// En library.zc
opaque alias Handle = int;

fn make_handle(v: int) -> Handle {
    return v; // Conversión implícita permitida dentro del módulo
}

// En main.zc
import "library.zc";

fn main() {
    let h: Handle = make_handle(42);
    // let i: int = h; // Error: Falló la validación de tipos
    // let h2: Handle = 10; // Error: Falló la validación de tipos
}
```

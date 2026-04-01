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

#### Tuplas
Agrupa múltiples valores, accede a los elementos por índice.
```zc
let pair = (1, "Hola");
let x = pair.0;  // 1
let s = pair.1;  // "Hola"
```

**Múltiples Valores de Retorno**

Las funciones pueden retornar tuplas para proporcionar múltiples resultados:
```zc
fn sumar_y_restar(a: int, b: int) -> (int, int) {
    return (a + b, a - b);
}

let resultado = sumar_y_restar(3, 2);
let suma = resultado.0;   // 5
let resta = resultado.1;  // 1
```

**Desestructuración**

Las tuplas pueden desestructurarse directamente en variables:
```zc
let (suma, resta) = sumar_y_restar(3, 2);
// suma = 5, resta = 1
```

La desestructuración tipada permite anotaciones de tipo explícitas:
```zc
let (a: string, b: u8) = ("hello", 42);
let (x, y: i32) = (1, 2);  // Mixto: x inferido, y explícito
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

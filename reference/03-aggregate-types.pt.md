+++
title = "3. Tipos Agregados"
weight = 3
+++

# 3. Tipos Agregados


#### Arrays
Arrays de tamanho fixo com semântica de valores.
```zc
def SIZE = 5;
let ints: int[SIZE] = [1, 2, 3, 4, 5];
let zeros: [int; SIZE]; // Inicialização-Zero
```




#### Tuples

Agrupa vários valores em um único valor composto. Tuplas suportam aridades arbitrárias (2, 3, 4, … até 10+), composição aninhada, mutação de campos individuais e desestruturação.

**Uso básico**

```zc
let pair = (1, "hello");
let triple = (1, "hello", 3.14);
let five = (1, 2, 3, 4, 5);
let typed: (int, string, f64) = (1, "two", 3.0);
```

**Acesso a campos**

Os elementos são acessados posicionalmente com `.0`, `.1`, `.2`, etc., ou através dos nomes de campo `.v0`, `.v1`:

```zc
let t = (1, "hello", 3.14);
assert(t.0 == 1);
assert(t.v1 == "hello");
```

**Múltiplos valores de retorno**

Funções podem retornar tuplas para fornecer múltiplos resultados:

```zc
fn stats(data: int) -> (int, int) {
    return (data * 2, data + 1);
}
let r = stats(5);
assert(r.0 == 10);
assert(r.1 == 6);
```

**Desestruturação**

```zc
let (sum, diff) = add_and_subtract(3, 2);
let (a: string, b: u8) = ("hello", 42);
let (x, y: i32) = (1, 2);
```

**Tuplas aninhadas**

```zc
let nested = ((1, 2), (3, 4));
let inner = nested.v0;
assert(inner.v0 == 1);
```

**Mutação**

Campos individuais podem ser reatribuídos:

```zc
let t = (1, 2);
t.v0 = 99;
```

**Comparação de strings**

Tuplas com campos `string` devem usar `strcmp()` para comparação, não `==` (que compara ponteiros em `char*`):

```zc
let t = (1, "hello");
assert(strcmp(t.1, "hello") == 0);
```

**Tuplas em variantes de enumeração**

Variantes de enum podem conter dados de tupla:

```zc
enum Shape {
    Point, Line(int, int), Labeled(int, string, f64),
}
```


#### Structs

Estruturas de dados com campos de bit opcionais.
```zc
struct Point {
    x: int;
    y: int;
}

// Inicialização de Struct
let p = Point { x: 10, y: 20 };

// Bitfields
struct Flags {
    valid: U8 : 1;
    mode:  U8 : 3;
}
```

{% alert(type="note") %}
Structs usam [Semântica de Move](@/tour/08-memory-management.pt.md#semantica-de-recursos-move-by-default) por padrão. Campos podem ser acessados via `.` mesmo em ponteiros (Auto-Dereferência).
{% end %}

#### Structs Opacos

Você pode definir um struct como `opaque` para restringir acesso aos seus campos exclusivamente ao módulo que o define, enquanto ainda permite que o struct seja alocado na pilha com tamanho conhecido.
```zc
// Em user.zc
opaque struct User {
    id: int;
    name: string;
}

fn new_user(name: string) -> User {
    return User{id: 1, name: name}; // OK: Dentro do módulo
}

// Em main.zc
import "user.zc";

fn main() {
    let u = new_user("Alice");
    // let id = u.id; // Erro: Acesso ao campo privado 'id' não permitido
}
```

#### Enums

Unions etiquetadas (tipos Sum) capazes de armazenar dados.
```zc
enum Shape {
    Circle(float),      // Armazena o raio
    Rect(float, float), // Armazena largura e altura
    Point               // Sem dados
}
```

#### Unions

Unions C padrão (acesso inseguro).
```zc
union Data {
    i: int;
    f: float;
}
```

#### Vetores SIMD
Tipos de vetores SIMD nativos usando extensões de vetores do GCC/Clang. Anote um struct com `@vector(N)` para definir um vetor de N elementos.
```zc
import "std/simd.zc";

fn main() {
    let a = f32x4{v: 1.0};              // Broadcast: {1.0, 1.0, 1.0, 1.0}
    let b = f32x4{1.0, 2.0, 3.0, 4.0};  // Inicialização por elemento
    let c = a + b;                       // Adição por elemento
    let x = c[0];                        // Acesso ao elemento (float)
}
```
Operadores aritméticos (`+`, `-`, `*`, `/`) e bitwise (`&`, `|`, `^`) funcionam por elemento. Veja [`std/simd.zc`](../std/simd.zc) para os tipos predefinidos.

#### Aliases de Tipos
Cria um novo nome para um tipo existente.
```zc
alias ID = int;
alias PointMap = Map<string, Point>
alias OpFunc = fn(int, int) -> int
```
> **Nota:** O ponto e vírgula final é opcional para aliases de tipo.

#### Aliases Opacos de Tipos

Você pode definir um alias como `opaque` para criar um novo tipo que é distinto de seu tipo subjacente fora do módulo que o define. Isso fornece forte encapsulamento e segurança de tipos sem o overhead de runtime de um struct wrapper.

```zc
// Em library.zc
opaque alias Handle = int;

fn make_handle(v: int) -> Handle {
    return v; // Conversão implícita permitida dentro do módulo
}

// Em main.zc
import "library.zc";

fn main() {
    let h: Handle = make_handle(42);
    // let i: int = h; // Erro: validação de tipo falhou
    // let h2: Handle = 10; // Erro: validação de tipo falhou
}
```

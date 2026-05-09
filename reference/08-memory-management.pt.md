+++
title = "8. Gerenciamento de Memória"
weight = 8
+++

# 8. Gerenciamento de Memória


Zen C permite gerenciamento manual de memória com auxílios ergonômicos.

#### Defer
Executa código quando sair do escopo atual. Declarações defer são executadas em ordem LIFO (last-in, first-out - último a entrar, primeiro a sair).
```zc
let f = fopen("file.txt", "r");
defer fclose(f);
```

{% alert(type="warning") %}
Para prevenir comportamento indefinido, declarações de fluxo de controle (`return`, `break`, `continue`, `goto`) **não são permitidas** dentro de um bloco `defer`.
{% end %}

#### Autofree
Libera automaticamente a variável quando sair do escopo.
```zc
autofree let types = malloc(1024);
```

#### Semântica de Recursos (Move by Default)
Zen C trata tipos com destrutores (como `File`, `Vec`, ou ponteiros mallocados) como **Recursos**. Para prevenir erros de double-free, recursos não podem ser implicitamente duplicados.

- **Move by Default**: Atribuir uma variável de recurso transfere propriedade. A variável original se torna inválida (Movida).
- **Copy Types**: Tipos sem destrutores podem optar pelo comportamento `Copy`, fazendo da atribuição uma duplicação.

**Diagnósticos & Filosofia**:
Se você vir um erro "Use of moved value", o compilador está dizendo: *"Este tipo possui um recurso (como memória ou um handle) e copiá-lo cegamente é inseguro."*

{% alert(type="note") %}
**Contraste:** Diferente de C/C++, Zen C não duplica implicitamente valores que possuem recursos.
{% end %}

**Argumentos de Função**:
Passar um valor para uma função segue as mesmas regras que atribuição: recursos são movidos a menos que passados por referência.

```zc
fn process(r: Resource) { ... } // 'r' é movido para a função
fn peek(r: Resource*) { ... }   // 'r' é emprestado (referência)
```

**Clonagem Explícita**:
Se você *realmente* quiser duas cópias de um recurso, torne isso explícito:

```zc
let b = a.clone(); // Chama o método 'clone' do trait Clone
```

**Opt-in Copy (Tipos de Valor)**:
Para tipos pequenos sem destrutores:

```zc
struct Point { x: int; y: int; }
impl Copy for Point {} // Opt-in para duplicação implícita

fn main() {
    let p1 = Point { x: 1, y: 2 };
    let p2 = p1; // Copiado. p1 permanece válido.
}
```

#### RAII / Drop Trait

Implement `Drop` to run cleanup logic automatically when a value goes out of scope.

```zc
impl Drop for MyStruct {
    fn drop(self) {
        self.free();
    }
}
```

**Encapsulando um tipo RAII.** Se seu struct contém um campo que já implementa `Drop` (como `Vec` ou `String`), o compilador cuida da limpeza automaticamente. Você NÃO precisa escrever `impl Drop` para o struct externo.

```zc
struct MyVecWrapper {
    inner: Vec<int>;  // Vec::drop() called automatically
}
```

{% alert(type="note") %}
**Exemplo:** `String` é definida como `struct String { vec: Vec<char>; }` — NÃO precisa de uma implementação explícita de `Drop` porque `Vec<char>` gerencia toda a memória. `Set<T>` por outro lado usa ponteiros `T*` brutos e PRECISA de `Drop` explícito.
{% end %}

**Regra prática:**
- Campos que são `Vec<T>`, `String` ou outros tipos RAII → Drop automático
- Campos que são `T*`, ponteiros `malloc` ou handles de arquivo → Drop explícito necessário

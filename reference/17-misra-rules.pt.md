+++
title = "17. Regras MISRA"
weight = 17
+++

# 17. Regras MISRA

O Zen C inclui um **modo de conformidade MISRA C:2012** ativado com a flag `--misra`.
Alem das verificacoes MISRA padrao, o compilador aplica varias **regras especificas do Zen**
que promovem codigo mais seguro e facil de manter.

#### Ativando o modo MISRA

```bash
zc build app.zc --misra
```

As violacoes sao reportadas como erros do compilador em tempo de compilacao:

```text
error: MISRA Rule Zen 2.2: tuple with 3 or more fields shall be replaced
       with a named struct (use 'struct' instead of positional tuple)
  --> app.zc:5:1
   |
 5 | fn get_stats() -> (int, int, int) { ... }
```

{% alert(type="note") %}
O texto do padrao MISRA e protegido por direitos autorais do MISRA Consortium Ltd. A
implementacao do Zen C verifica a conformidade, mas nao reproduz o padrao.
Para as definicoes oficiais das regras, consulte a documentacao do
[MISRA C:2012](https://www.misra.org.uk/).
{% end %}

#### Regras Especificas do Zen

Estas regras sao exclusivas do Zen C. Cada regra e verificada quando `--misra` esta ativo.

#### Zen 1.1 -- Sem blocos raw

Proibe blocos `raw { }` que contornam o transpilador.

```zc
// Bad:
fn main() {
    raw { int x = 10; }
}

// Good:
fn main() {
    let x = 10;
}
```

#### Zen 1.2 -- Sem blocos plugin

Proibe blocos `plugin ... end`, que executam codigo arbitrario em tempo de compilacao.

```zc
// Bad:
plugin my_plugin

// Good:
import "std/some_module.zc"
```

#### Zen 1.3 -- Match exaustivo de enums

Proibe o coringa `_` no `match` em tipos enum -- todas as variantes devem ser tratadas explicitamente.

```zc
enum Color { Red; Green; Blue; }

// Bad -- missing Blue:
fn describe(c: Color) {
    match c {
        Color::Red => { println "red"; }
        Color::Green => { println "green"; }
    }
}

// Good:
fn describe(c: Color) {
    match c {
        Color::Red => { println "red"; }
        Color::Green => { println "green"; }
        Color::Blue => { println "blue"; }
    }
}
```

#### Zen 1.4 -- Sem diretivas de pre-processador

Proibe diretivas de pre-processador C (`#define`, `#include`, `#if`, etc.).
Use `import` e `def` do Zen em vez disso.

```zc
// Bad:
#define BUFFER_SIZE 256
#include <stdio.h>

// Good:
def BUFFER_SIZE = 256;
import "std/io.zc"
```

#### Zen 1.5 -- Sem `var` / `const` para declaracoes

As palavras-chave `var` e `const` estao obsoletas para declaracoes de variaveis/constantes.
Use `let` para variaveis e `def` para constantes de tempo de compilacao.

```zc
// Bad:
var x = 10;
const MAX = 100;

// Good:
let x = 10;
def MAX = 100;
```

> `const` permanece valido como **qualificador de tipo** para interoperabilidade com C
> (ex.: `const int` em declaracoes FFI).

#### Zen 1.8 -- Sem sombreamento de identificadores

Proibe declarar um nome que oculta um de um escopo externo.

```zc
let x = 10;
if true {
    // Bad -- shadows outer x:
    let x = 20;
}

// Good:
if true {
    let inner_x = 20;
}
```

#### Zen 2.1 -- Sem identificadores reservados

Proibe identificadores que comecam com `__`, `_[A-Z]` ou `_z_`, que sao reservados
para o compilador e a implementacao C.

```zc
// Bad:
let __my_var = 10;
let _Reserved = 20;
let _z_internal = 30;

// Good:
let my_var = 10;
let reserved = 20;
let internal = 30;
```

#### Zen 2.2 -- Limite de tamanho de tuplas

Tuplas com **3 ou mais campos** nao devem ser usadas como tipos de retorno ou
parametros de funcao. Use uma estrutura nomeada em vez disso. 2-tuplas sao isentas.

```zc
// Bad -- 3-tuple as return type:
fn get_stats() -> (int, int, int) { ... }
fn process(p: (int, string, bool)) { ... }

// Good -- use a struct:
struct Stats { sum: int; avg: int; max: int; }
fn get_stats() -> Stats { ... }

// OK -- 2-tuples are exempt:
fn get_pair() -> (int, int) { ... }
```

#### Zen 2.3 -- Comparacao de strings

`string == string` nao deve ser usado. Use `strcmp()` em vez disso.

```zc
// Bad (when a, b are string):
if a == b { ... }

// Good:
if strcmp(a, b) == 0 { ... }

// OK -- int, bool, pointer comparisons are safe:
if x == y { ... }
```

## Cobertura Padrao MISRA C:2012

O compilador verifica as seguintes regras padrao MISRA C:2012.
Clique em um capitulo para expandir a lista de regras.

{% misra_table() %}

Para o texto completo das regras, consulte a documentacao oficial do
[MISRA C:2012](https://www.misra.org.uk/).

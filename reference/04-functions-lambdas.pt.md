+++
title = "4. Funções & Lambdas"
weight = 4
+++

# 4. Funções & Lambdas {#4-funcoes-lambdas}


#### Funções
```zc
fn add(a: int, b: int) -> int {
    return a + b;
}

// Argumentos nomeados são suportados na chamada
add(a: 10, b: 20);
```

{% alert(type="note") %}
Argumentos nomeados devem seguir estritamente a ordem dos parâmetros. `add(b: 20, a: 10)` é inválido.
{% end %}

#### Argumentos Const

Funções podem ser marcadas como `const` para impor semântica de apenas leitura. Isso é um qualificador de tipo, não uma constante manifest.

```zc
fn print_val(v: const int) {
    // v = 10; // Erro: atribuição a const não permitida
    println "{v}";
}
```

#### Argumentos Padrão

Funções podem definir valores-padrão para argumentos trailing. Estes podem ser literais, expressões ou código Zen C válido (como construtores struct).
```zc
// Valor padrão simples
fn increment(val: int, amount: int = 1) -> int {
    return val + amount;
}

// Expressão de valor padrão (avaliada no local da chamada)
fn offset(val: int, pad: int = 10 * 2) -> int {
    return val + pad;
}

// Valor padrão de struct
struct Config { debug: bool; }
fn init(cfg: Config = Config { debug: true }) {
    if cfg.debug { println "Debug Mode"; }
}

fn main() {
    increment(10);      // 11
    offset(5);          // 25
    init();             // Print "Debug Mode"
}
```

#### Lambdas (Fechamentos)

Funções anônimas que podem capturar seu ambiente.
```zc
let factor = 2;
let dobrar = x -> x * factor;  // Sintaxe de seta
let full = fn(x: int) -> int { return x * factor; }; // Sintaxe de bloco

// Captura por Referência (Sintaxe de Bloco)
let val = 10;
let modify = fn[&]() { val += 1; }; 
modify(); // val agora é 11

// Captura por Referência (Sintaxe de Seta)
let modify_arrow = [&] x -> val += x;
modify_arrow(5); // val agora é 16

// Captura por Referência (Sintaxe de Seta com Múltiplos Argumentos)
let sum_into = [&] (a, b) -> val += (a + b);
sum_into(2, 2); // val agora é 20

// Captura por Valor (Padrão)
let original = 100;
let implicita = x -> original + x;      // Captura implícita por valor (sem colchetes)
let explicita = [=] x -> original + x;  // Captura explícita por valor
// let fail = x -> original += x;       // Erro: não é possível atribuir a valor capturado

```

#### Ponteiros de Função Brutos

Zen C suporta ponteiros de função C brutos usando sintaxe `fn*`. Isso permite interoperabilidade ininterrupta com bibliotecas C que esperam ponteiros de função, sem overhead de fechamento.

```zc
// Função recebendo um ponteiro de função bruto 
fn set_callback(cb: fn*(int)) {
    cb(42);
}

// Função retornando um ponteiro de função bruto
fn get_callback() -> fn*(int) {
    return my_handler;
}

// Ponteiros para ponteiros de função são suportados (fn**)
let pptr: fn**(int) = &ptr;
```

#### Funções Variádicas

Funções podem aceitar um número variável de argumentos utilizando `...` e o tipo `va_list`.
```zc
fn log(lvl: int, fmt: char*, ...) {
    let ap: va_list;
    va_start(ap, fmt);
    vprintf(fmt, ap); // Use C stdio
    va_end(ap);
}
```

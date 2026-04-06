+++
title = "5. Fluxo de Controle"
weight = 5
+++

# 5. Fluxo de Controle


#### Condicionais
```zc
if x > 10 {
    print "Large";
} else if x > 5 {
    print "Medium";
} else {
    print "Small";
}

// Condicional Ternária
let y = x > 10 ? 1 : 0;

// If-Expression (para condições complexas)
let categoria = if (x > 100) { "enorme" } else if (x > 10) { "grande" } else { "pequeno" };
```

#### Correspondência de Padrões

Poderosa alternativa ao `switch`.
```zc
match val {
    1         => { print "One" },
    2 || 3    => { print "Two or Three" },    // OR com ||
    4 or 5    => { print "Four or Five" },    // OR com 'or'
    6, 7, 8   => { print "Six to Eight" },    // OR com vírgula
    10 .. 15  => { print "10 to 14" },        // Range excludente (Legado)
    10 ..< 15 => { print "10 to 14" },        // Range excludente (Explícito)
    20 ..= 25 => { print "20 to 25" },        // Range inclusivo
    _         => { print "Other" },
}

// Desestruturando Enums
match shape {
    Shape::Circle(r)   => { println "Radius: {r}" },
    Shape::Rect(w, h)  => { println "Area: {w*h}" },
    Shape::Point       => { println "Point" }
}
```

#### Associação de Referência**

Para inspecionar um valor sem tomar posse (movendo-o), use a palavra-chave `ref` no padrão. Isso é essencial para tipos que implementam semântica de movimento, como `Option`, `Result` e structs non-Copy.

```zc
let opt = Some(NonCopyVal{...});
match opt {
    Some(ref x) => {
        // 'x' é um ponteiro para o valor dentro de 'opt'
        // 'opt' NÃO É movido/consumido aqui
        println "{x.field}"; 
    },
    None => {}
}
```

#### Loops
```zc
// Range
for i in 0..10 { ... }      // Excludente (0 a 9)
for i in 0..<10 { ... }     // Excludente (Explícito)
for i in 0..=10 { ... }     // Inclusivo (0 a 10)
for i in 0..10 step 2 { ... }
for i in 10..0 step -1 { ... }  // Descending loop

// Iterador (Vec ou Iterável Customizado)
for item in vec { ... }

// Enumerado: obtém índice e valor
for i, val in arr { ... }       // i = 0, 1, 2, ...
for i, val in 0..10 step 2 { ... } // i = 0, 1, 2, ...; val = 0, 2, 4, ...

// Itera sobre arrays de tamanho fixo diretamente
let arr: int[5] = [1, 2, 3, 4, 5];
for val in arr {
    // val é um int
    println "{val}";
}

// While
while x < 10 { ... }

// Do-While
do { ... } while x < 10;

// Infinito com label
outer: loop {
    if done { break outer; }
}

// Repita N vezes
for _ in 0..5 { ... }
```

#### Controle Avançado
```zc
// Guard: Executa else e return se a condição for falsa
guard ptr != NULL else { return; }

// Unless: Se não for verdadeiro
unless is_valid { return; }
```

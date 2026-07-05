+++
title = "1. Variáveis e Constantes"
weight = 1
+++

# 1. Variáveis e Constantes {#1-variaveis-e-constantes}


Zen C distingue constantes em tempo de compilação e variáveis em tempo de execução.

#### Constantes Manifest (`def`)

Valores que existem apenas em tempo de compilação (encapsuladas no código). Utilize para tamanhos de arrays, configurações fixas e números mágicos.

```zc
def MAX_SIZE = 1024;
let buffer: char[MAX_SIZE]; // Tamanho de array válido
```

#### Variáveis (`let`, `const`)

Armazenam localizações na memória. Podem ser mutáveis (`let`) ou apenas leitura (`const`).

```zc
let x = 10;             // Mutável
x = 20;                 // OK

let y: const int = 10;  // Apenas leitura (tipo qualificado)
// y = 20;              // Erro: atribuição a const não permitida
```

{% alert(type="tip") %}
**Inferência de Tipo**: Zen C automaticamente infere tipos de variáveis inicializadas. Compila para C23 `auto` em compiladores suportados, ou para `__auto_type` da extensão GCC alternativamente.
{% end %}

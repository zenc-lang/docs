+++
title = "14. Interoperabilidade com C"
weight = 14
+++

# 14. Interoperabilidade com C {#14-interoperabilidade-com-c}


Zen C oferece duas formas  de interagir com código C: **Trusted Imports** (Forma conveniente) e **Explicit FFI** (Forma segura/precisa).

#### Método 1: Trusted Imports (Conveniente)

Você pode importar um header C diretamente utilizando a palavra-chave `import` com a extensão `.h`. Isso trata o header como um módulo e assume que todos os símbolos acessados através dele existem.

```zc
//> link: -lm
import "math.h" as c_math;

fn main() {
    // Compilador confia na precisão; emite 'cos(...)' diretamente
    let x = c_math::cos(3.14159);
}
```

> **Prós**: Zero boilerplate. Acessa tudo no header imediatamente.
> **Contras**: Sem segurança de tipos por parte do Zen C (erros capturados apenas posteriormente, pelo compilador C).

#### Método 2: Explicit FFI (Segura)

Para checagem estrita de tipos ou quando você não quer incluir o texto de um header, utilize `extern fn`.

```zc
include <stdio.h> // Emite  #include <stdio.h> no C gerado

// Define assinatura estrita
extern fn printf(fmt: char*, ...) -> c_int;

fn main() {
    printf("Olá FFI: %d\n", 42); // Tipos checados pelo Zen C
}
```

> **Prós**: Zen C garante que os tipos correspondam.
> **Contras**: Requer declaração manual de funções.

#### `import` vs `include`

- **`import "file.h"`**: Registra o header como um módulo nomeado. Permite acesso implícito aos símbolos (ex: `file::function()`).
- **`include <file.h>`**: Apenas emite `#include <file.h>` no código C gerado. Não introduz símbolos no compilador Zen C; você deve usar `extern fn` para acessá-los.

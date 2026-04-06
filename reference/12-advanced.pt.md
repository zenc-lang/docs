+++
title = "12. Avançado e Metaprogramação"
weight = 12
+++

# 12. Avançado e Metaprogramação


### Metaprogramação

#### Comptime
Execute código em tempo de compilação para gerar código ou imprimir mensagens.
```zc
comptime {
    // Gera código em tempo de compilação (escrito em stdout)
    println "let data_compilacao = \"2024-01-01\";";
}

println "Data de compilação: {data_compilacao}";
```

**Funções Auxiliares**

Funções especiais disponíveis dentro de blocos `comptime`:
- **`yield(str)`** - Emite explicitamente código gerado (alternativa a `printf`)
- **`compile_error(msg)`** - Interrompe a compilação com uma mensagem de erro fatal
- **`compile_warn(msg)`** - Emite um aviso em tempo de compilação (permite continuar a compilação)

```zc
comptime {
    compile_warn("Gerando código otimizado...");
    
    let ENABLE_FEATURE = 1;
    if (ENABLE_FEATURE == 0) {
        compile_error("O recurso deve estar habilitado!");
    }
    
    println "let FEATURE_ENABLED = 1;";
}
```

**Metadados de Build**

Acesse informações de build do compilador em tempo de compilação:
- **`__COMPTIME_TARGET__`** - String da plataforma: `"linux"`, `"windows"` ou `"macos"`
- **`__COMPTIME_FILE__`** - Nome do arquivo fonte atual sendo compilado

```zc
comptime {
    // Geração de código específica da plataforma
    println "let PLATFORM = \"{__COMPTIME_TARGET__}\";";
}

println "Executando em: {PLATFORM}";
```

> **Dica:** Use raw strings (`r"..."`) em comptime para evitar escapar chaves: `code(r"fn test() { return 42; }")`. De lo contrario, use `{{` e `}}` para escapar chaves em strings regulares.

#### Embed
Incorpore arquivos como tipos especificados.
```zc
// Padrão (Slice_char)
let data = embed "assets/logo.png";

// Embed Tipado
let text = embed "shader.glsl" as string;    // Incorporado como C-string
let rom  = embed "bios.bin" as u8[1024];     // Incorporado como array fixa
let wav  = embed "sound.wav" as u8[];        // Incorporado como Slice_u8
```

#### Plugins
Importe plugins de compilação para sintaxe estendida
```zc
import plugin "regex"
let re = regex! { ^[a-z]+$ };
```

#### Macros Genéricos de C
Passe macros pré-processamento para o C.

> **Dica**: Para constantes simples, utilize `def` em vez disso. Utilize `#define` quando você precisar de macros pré-processamento em C ou de flags condicionais de compilação.

```zc
#define MAX_BUFFER 1024
```

#### Compilação Condicional
Use `@cfg()` para incluir ou excluir condicionalmente qualquer declaração de nível superior com base em flags `-D`.

```zc
// Compilar com: zc build app.zc -DUSE_OPENGL

@cfg(USE_OPENGL)
import "opengl_backend.zc";

@cfg(USE_VULKAN)
import "vulkan_backend.zc";

@cfg(not(USE_OPENGL))
@cfg(not(USE_VULKAN))
fn fallback_init() { println "Nenhum backend selecionado"; }
```

| Forma | Significado |
|:---|:---|
| `@cfg(NAME)` | Incluir se `-DNAME` estiver definido |
| `@cfg(not(NAME))` | Incluir se `-DNAME` NÃO estiver definido |
| `@cfg(any(A, B, ...))` | Incluir se QUALQUER condição for verdadeira (OR) |
| `@cfg(all(A, B, ...))` | Incluir se TODAS as condições forem verdadeiras (AND) |

Múltiplos `@cfg` em uma declaração são combinados com AND. `not()` pode ser usado dentro de `any()` e `all()`. Funciona com qualquer declaração de nível superior: `fn`, `struct`, `import`, `impl`, `raw`, `def`, `test`, etc.

### Atributos
Decore funções e structs para modificar o comportamento do compilador.

| Atributo | Escopo | Descrição |
|:---|:---|:---|
| `@required` | Fn | Avisa se o valor de retorno é ignorado. |
| `@deprecated("msg")` | Fn/Struct | Aviso sobre o uso com mensagem. |
| `@inline` | Fn | Sugere compilador para inline. |
| `@noinline` | Fn | Previne inline. |
| `@packed` | Struct | Remove padding entre campos. |
| `@align(N)` | Struct | Força alinhamento para N bytes. |
| `@constructor` | Fn | Executa antes de main. |
| `@destructor` | Fn | Executa após sair de main. |
| `@unused` | Fn/Var | Suprime avisos de variáveis não utilizadas. |
| `@weak` | Fn | Linkagem fraca de símbolos. |
| `@section("name")` | Fn | Coloca código em seção específica. |
| `@noreturn` | Fn | Função não retorna (e.g. exit). |
| `@pure` | Fn | Função sem efeitos colaterais (sugestão de otimização). |
| `@cold` | Fn | Função provavelmente não é executada (sugestão de predição de branch). |
| `@hot` | Fn | Função é frequentemente executada (sugestão de otimização). |
| `@export` | Fn/Struct | Exporta símbolo (visibilidade padrão). |
| `@global` | Fn | CUDA: Entry point do Kernel (`__global__`). |
| `@device` | Fn | CUDA: Função de dispositivo (`__device__`). |
| `@host` | Fn | CUDA: Função Host (`__host__`). |
| `@comptime` | Fn | Função auxiliar disponível para execução em tempo de compilação. |
| `@cfg(NAME)` | Qualquer | Compilação condicional: inclui apenas se `-DNAME` for passado. Suporta `not()`, `any()`, `all()`. |
| `@derive(...)` | Struct | Auto-implementa traits. Supporta `Debug`, `Eq` (Smart Derive), `Copy`, `Clone`. |
| `@ctype("type")` | Fn Param | Sobreescreve tipo C gerado para um parâmetro. |
| `@<custom>` | Any | Passa atributos genéricos para o C (e.g. `@flatten`, `@alias("name")`). |

### Atributos Customizados

Zen C suporta um sistema poderoso de **Atributos Customizados** que te permite usar qualquer `__attribute__` de GCC/Clang diretamente no seu código. Qualquer atributo que não seja explicitamente reconhecido pelo compilador de Zen C é tratado como um atributo genérico e passado para o código C gerado.

Isso fornece acesso para funcionalidades avançadas do compilador, otimizações, e diretivas de linker sem precisar de suporte explícito para a linguagem núcleo.

#### Mapeamento de Sintaxe
Os atributos Zen C são mapeados diretamente para atributos C:
- `@name` → `__attribute__((name))`
- `@name(args)` → `__attribute__((name(args)))`
- `@name("string")` → `__attribute__((name("string")))`

### Smart Derives

Zen C fornece "Smart Derives" que respeitam a Semântica de Move (Move Semantics):

- **`@derive(Eq)`**: Gera um método de igualdade que recebe argumentos por referência (`fn eq(self, other: T*)`).
    - Ao comparar dois structs non-Copy (`a == b`), o compilador automaticamente passa `b` por referência (`&b`) para evitar que ele seja movido.
    - Checagens recursivas de igualdade nos campos também preferem acesso ao ponteiro para prevenir transferência de propriedade.
    
### Assembly Inline

Zen C fornece suporte de primeira classe para assembly inline, transpilando diretamente para `asm`de estilo GCC estendido.

#### Uso Básico
Escreva assembly bruto dentro de blocos `asm`. Strings são concatenadas automaticamente.
```zc
asm {
    "nop"
    "mfence"
}
```

#### Volatile
Use `volatile` para prevenir otimizações do compilador em assembly com efeitos colaterais.
```zc
asm volatile {
    "rdtsc"
}
```

#### Restrições Nomeadas
Zen C simplifica a complexa restrição sintática do GCC com associações nomeadas.
```zc
// Syntax: : out(variable) : in(variable) : clobber(reg)
// Uses {variable} placeholder syntax for readability

fn add_five(x: int) -> int {
    let result: int;
    asm {
        "mov {x}, {result}"
        "add $5, {result}"
        : out(result)
        : in(x)
        : clobber("cc")
    }
    return result;
}
```

| Tipo | Sintaxe | Equivalente GCC |
|:---|:---|:---|
| **Output** | `: out(variable)` | `"=r"(variable)` |
| **Input** | `: in(variable)` | `"r"(variable)` |
| **Clobber** | `: clobber("rax")` | `"rax"` |
| **Memory** | `: clobber("memory")` | `"memory"` |

> **Nota:** Ao utilizar sintaxe Intel (via `-masm=intel`), você deve garantir que seu build esteja configurado corretamente (por exemplo, `//> cflags: -masm=intel`). O TCC não suporta sintaxe assembly da Intel.

### Diretivas de Build

Zen C suporta comentários especiais no topo de seu arquivo-fonte para configurar o processo de build sem precisar de um sistema de build complexo ou um Makefile.

| Diretiva | Argumentos | Descrição |
|:---|:---|:---|
| `//> link:` | `-lfoo` ou `path/to/lib.a` | Link uma biblioteca ou arquivo objeto. |
| `//> lib:` | `path/to/libs` | Adiciona um caminho de busca por bibliotecas (`-L`). |
| `//> include:` | `path/to/headers` | Adiciona um caminho de inclusão de buscas (`-I`). |
| `//> framework:` | `Cocoa` | Link para um framework macOS. |
| `//> cflags:` | `-Wall -O3` | Passa flags arbitrárias para o compilador C. |
| `//> define:` | `MACRO` ou `KEY=VAL` | Define um macro preprocessador (`-D`). |
| `//> pkg-config:` | `gtk+-3.0` | Executa `pkg-config` e acrescenta `--cflags` e `--libs`. |
| `//> shell:` | `command` | Executa um comando shell durante o build. |
| `//> get:` | `http://url/file` | Baixa um arquivo se o arquivo específico não existir. |

#### Features

**1. OS Guarding**
Diretivas de prefixo com o nome de um SO para aplicá-las apenas em plataformas específicas.
Prefixos suportados: `linux:`, `windows:`, `macos:` (or `darwin:`).

```zc
//> linux: link: -lm
//> windows: link: -lws2_32
//> macos: framework: Cocoa
```

**2. Expansão de Variáveis de Ambiente**
Use a sintaxe `${VAR}` para expandir as variáveis de ambiente em suas diretivas.

```zc
//> include: ${HOME}/mylib/include
//> lib: ${ZC_ROOT}/std
```

#### Exemplos

```zc
//> include: ./include
//> lib: ./libs
//> link: -lraylib -lm
//> cflags: -Ofast
//> pkg-config: gtk+-3.0

import "raylib.h"

fn main() { ... }
```

### Palavras-chave

Zen C reserva as seguintes palavras-chave:

#### Declarações
`alias`, `def`, `enum`, `fn`, `impl`, `import`, `let`, `module`, `opaque`, `struct`, `trait`, `union`, `use`

#### Fluxo de Control
`async`, `await`, `break`, `catch`, `continue`, `defer`, `do`, `else`, `for`, `goto`, `guard`, `if`, `loop`, `match`, `return`, `try`, `unless`, `while`

#### Especiais
`asm`, `assert`, `autofree`, `comptime`, `const`, `embed`, `launch`, `ref`, `sizeof`, `static`, `test`, `volatile`

#### Constantes
`true`, `false`, `null`

#### Reservado pelo C
Os seguintes identificadores são reservados porque são palavras-chave em C11:
`auto`, `case`, `char`, `default`, `double`, `extern`, `float`, `inline`, `int`, `long`, `register`, `restrict`, `short`, `signed`, `switch`, `typedef`, `unsigned`, `void`, `_Atomic`, `_Bool`, `_Complex`, `_Generic`, `_Imaginary`, `_Noreturn`, `_Static_assert`, `_Thread_local`

#### Operadores
`and`, `or`

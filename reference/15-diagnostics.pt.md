+++
title = "15. Sistema de Diagnóstico"
weight = 15
+++

# 15. Sistema de Diagnóstico


Zen C fornece um sistema de diagnóstico categorizado que permite controle granular sobre os avisos (warnings) do compilador. Isso permite manter altos padrões de qualidade de código enquanto reduz a fricção ao interagir com código C externo.

#### Categorias de Diagnóstico

Os avisos são agrupados em categorias lógicas. Cada categoria pode ser habilitada ou desabilitada globalmente usando flags do compilador.

| Categoria | Descrição | Padrão |
| :--- | :--- | :--- |
| **`INTEROP`** | Avisos relacionados à importação de headers C e funções externas não definidas. | **OFF** |
| **`PEDANTIC`** | Checagens extras rigorosas para potenciais problemas ou qualidade de código. | **OFF** |
| **`UNUSED`** | Avisos para variáveis, parâmetros ou funções definidos mas não utilizados. | **ON** |
| **`SAFETY`** | Avisos de segurança críticos, como acesso a ponteiros nulos ou divisão por zero. | **ON** |
| **`LOGIC`** | Avisos relacionados à lógica, como código inalcançável ou comparações de constantes. | **ON** |
| **`CONVERSION`** | Avisos para conversões de tipo implícitas ou estreitas (narrowing). | **ON** |
| **`STYLE`** | Avisos de estilo de codificação, como sombreamento de variáveis (shadowing). | **ON** |

#### Flags do Compilador

Você pode controlar o diagnóstico usando as flags `-W` (habilitar) e `-Wno-` (desabilitar) seguidas por um nome de categoria ou um ID de diagnóstico específico.

##### Flags de Categoria

- `-Winterop`: Habilita todos os avisos relacionados à interoperabilidade.
- `-Wno-unused`: Silencia especificamente avisos de variáveis/parâmetros não utilizados.
- `-Wsafety`: Garante que todas as checagens de segurança estejam ativas.
- `-Wall`: Habilita todas as principais categorias de diagnóstico.
- `-Wextra`: Habilita diagnósticos ainda mais rigorosos (equivalente a `-Wpedantic`).

##### Exemplo de Uso

```bash
# Compila com avisos de interoperabilidade C habilitados
zc app.zc -Winterop

# Compila com todos os avisos habilitados, exceto para código não utilizado
zc app.zc -Wall -Wno-unused
```

#### Fricção na Interoperabilidade C

Por padrão, Zen C suprime avisos de "Função não definida" para funções que provavelmente estão em bibliotecas padrão C (a categoria `INTEROP` está **OFF**).

Se você deseja que o compilador sinalize rigorosamente cada função não definida (por exemplo, para encontrar erros de digitação), habilite a categoria interop:

```bash
zc main.zc -Winterop
```

Quando habilitado, o compilador fornecerá sugestões úteis para funções C comuns:
```text
warning: Undefined function 'abs'
  --> main.zc:5:13
   |
5  |     let x = abs(-5);
   |             ^ here
   |
   = note: If this is a C function, it might need to be whitelisted in 'zenc.json'
```

#### Whitelisting

Se você usa frequentemente uma biblioteca C específica e deseja manter `-Winterop` habilitado sem ser incomodado por funções específicas, você pode adicioná-las no `c_function_whitelist` no arquivo de configuração `zenc.json`.

---

## Biblioteca Padrão

O Zen C inclui a biblioteca padrão (`std`), que cobre as funcionalidades essenciais.

[Navegue pela Documentação da Biblioteca Padrão](../docs/std/README.md)

### Módulos Principais

<details>
<summary>Clique para ver todos os módulos da Biblioteca Padrão</summary>

| Módulo | Descrição | Docs |
| :--- | :--- | :--- |
| **`std/bigfloat.zc`** | Aritmética de ponto flutuante de precisão arbitrária. | [Docs](../docs/std/bigfloat.md) |
| **`std/bigint.zc`** | Inteiro de precisão arbitrária `BigInt`. | [Docs](../docs/std/bigint.md) |
| **`std/bits.zc`** | Operações bit-a-bit de baixo nível (`rotl`, `rotr`, etc). | [Docs](../docs/std/bits.md) |
| **`std/complex.zc`** | Aritmética de números complexos `Complex`. | [Docs](../docs/std/complex.md) |
| **`std/vec.zc`** | Growable dynamic array `Vec<T>`. | [Docs](../docs/std/vec.md) |
| **`std/string.zc`** | Heap-allocated `String` type with UTF-8 support. | [Docs](../docs/std/string.md) |
| **`std/queue.zc`** | FIFO queue (Ring Buffer). | [Docs](../docs/std/queue.md) |
| **`std/map.zc`** | Generic Hash Map `Map<V>`. | [Docs](../docs/std/map.md) |
| **`std/fs.zc`** | File system operations. | [Docs](../docs/std/fs.md) |
| **`std/io.zc`** | Standard Input/Output (`print`/`println`). | [Docs](../docs/std/io.md) |
| **`std/option.zc`** | Optional values (`Some`/`None`). | [Docs](../docs/std/option.md) |
| **`std/result.zc`** | Error handling (`Ok`/`Err`). | [Docs](../docs/std/result.md) |
| **`std/path.zc`** | Cross-platform path manipulation. | [Docs](../docs/std/path.md) |
| **`std/env.zc`** | Process environment variables. | [Docs](../docs/std/env.md) |
| **`std/net/`** | TCP, UDP, HTTP, DNS, URL. | [Docs](../docs/std/net.md) |
| **`std/thread.zc`** | Threads and Synchronization. | [Docs](../docs/std/thread.md) |
| **`std/time.zc`** | Time measurement and sleep. | [Docs](../docs/std/time.md) |
| **`std/json.zc`** | JSON parsing and serialization. | [Docs](../docs/std/json.md) |
| **`std/stack.zc`** | LIFO Stack `Stack<T>`. | [Docs](../docs/std/stack.md) |
| **`std/set.zc`** | Generic Hash Set `Set<T>`. | [Docs](../docs/std/set.md) |
| **`std/process.zc`** | Process execution and management. | [Docs](../docs/std/process.md) |
| **`std/regex.zc`** | Expressões Regulares (baseado em TRE). | [Docs](../docs/std/regex.md) |
| **`std/simd.zc`** | Tipos de vetores SIMD nativos. | [Docs](../docs/std/simd.md) |

</details>

---

## Further Reading

- **Language Server**: Veja a [documentação LSP](LSP.md) para integração com o editor.
- **MISRA Compliance**: Veja [MISRA Rules](../reference/16-misra-rules) para a referência completa de regras.
- **Contributing**: Veja [CONTRIBUTING_PT_BR.md](../CONTRIBUTING_PT_BR.md) para as diretrizes de contribuição.

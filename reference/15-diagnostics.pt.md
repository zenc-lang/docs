+++
title = "15. Sistema de Diagnóstico"
weight = 15
+++

# 15. Sistema de Diagnóstico

O Zen C possui um sistema de diagnóstico categorizado que fornece controle granular sobre os avisos (warnings) do compilador. Isso permite manter altos padrões de qualidade de código, reduzindo o atrito ao interagir com código C externo.

## Categorias de Diagnóstico

Os avisos são agrupados em categorias lógicas. Cada categoria pode ser ativada ou desativada globalmente usando sinalizadores (flags) do compilador.

| Categoria | Descrição | Padrão |
| :--- | :--- | :--- |
| **`INTEROP`** | Avisos relacionados à importação de cabeçalhos C e funções externas não definidas. | **OFF** |
| **`PEDANTIC`** | Verificações extra rigorosas para possíveis problemas ou qualidade do código. | **OFF** |
| **`UNUSED`** | Avisos para variáveis, parâmetros ou funções definidos, mas não utilizados. | **ON** |
| **`SAFETY`** | Avisos de segurança críticos, como acesso a ponteiros nulos ou divisão por zero. | **ON** |
| **`LOGIC`** | Avisos relacionados à lógica, como código inacessível ou comparações de constantes. | **ON** |
| **`CONVERSION`** | Avisos para conversões de tipo implícitas ou de estreitamento. | **ON** |
| **`STYLE`** | Avisos de estilo de codificação, como sombreamento de variáveis (shadowing). | **ON** |

## Sinalizadores do Compilador

Você pode controlar os diagnósticos usando os sinalizadores `-W` (ativar) e `-Wno-` (desativar) seguidos pelo nome de uma categoria ou por um ID de diagnóstico específico.

### Sinalizadores de Categoria

- `-Winterop`: Ativa todos os avisos relacionados à interoperabilidade.
- `-Wno-unused`: Silencia especificamente avisos de variáveis/parâmetros não utilizados.
- `-Wsafety`: Garante que todas as verificações de segurança estejam ativas.
- `-Wall`: Ativa todas as principais categorias de diagnóstico.
- `-Wextra`: Ativa diagnósticos ainda mais rigorosos (equivalente a `-Wpedantic`).

### Exemplo de Uso

```bash
# Compilar com avisos de interoperabilidade C ativados
zc app.zc -Winterop

# Compilar com todos os avisos ativados, exceto avisos de código não utilizado
zc app.zc -Wall -Wno-unused
```

## Atrito na Interoperabilidade C

Por padrão, o Zen C suprime os avisos de "Função não definida" para funções que provavelmente serão encontradas nas bibliotecas padrão C (a categoria `INTEROP` está **OFF**).

Se você deseja que o compilador relate estritamente cada função não definida (por exemplo, para encontrar erros de digitação), ative a categoria de interoperabilidade:

```bash
zc main.zc -Winterop
```

Quando ativado, o compilador fornecerá dicas úteis para funções C comuns:
```text
warning: Undefined function 'abs'
  --> main.zc:5:13
   |
5  |     let x = abs(-5);
   |             ^ here
   |
   = note: If this is a C function, it might need to be whitelisted in 'zenc.json'
```

## Lista Branca (Whitelisting)

Se você usa uma biblioteca C específica com frequência e deseja manter o `-Winterop` ativado sem ser incomodado por funções específicas, pode adicioná-las à `c_function_whitelist` no seu arquivo de configuração `zenc.json`.

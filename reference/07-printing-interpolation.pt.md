+++
title = "7. Print e Interpolação de Strings"
weight = 7
+++

# 7. Print e Interpolação de Strings {#7-print-e-interpolacao-de-strings}


Zen C fornece opções versáteis para print no console, incluindo palavras-chave e abreviações concisas.

#### Palavras-Chave

| Palavra-chave | Descrição |
|:---|:---|
| `print` | Imprime na saída padrão (sem newline) |
| `println` | Imprime na saída padrão (com newline) |
| `eprint` | Imprime no erro padrão (sem newline) |
| `eprintln` | Imprime no erro padrão (com newline) |

#### Abreviações

Zen C permite utilizar literais string diretamente como declarações para print rápido:

| Sintaxe | Equivalente | Descrição |
|:---|:---|:---|
| `"Hello"` | `println "Hello"` | Implicitamente adiciona newline. |
| `"Hello"..` | `print "Hello"` | Sem trailing newline. |
| `!"Error"` | `eprintln "Error"` | Output para stderr. |
| `!"Error"..` | `eprint "Error"` | Output para stderr, sem newline. |

#### Interpolação de Strings

Você pode incorporar expressões diretamente em literais de string usando sintaxe `{}`. Isso funciona com todos os métodos de print e abreviações de string.

Interpolação de strings em Zen C é **implícita**: se sua string contém `{...}`, ela será automaticamente analisada como uma string interpolada. Você também pode explicitar o uso do prefixo `f` (e.g., `f"..."`) para forçar a semântica de interpolação.

```zc
let x = 42;
let name = "Zen";
println "Value: {x}, Name: {name}";
"Value: {x}, Name: {name}"; // abreviação de println
```

**Escapando Chaves**: Use `{{` para produzir uma chave literal `{` e `}}` para uma `}` literal:

```zc
let json = "JSON: {{\"chave\": \"valor\"}}";
// Saída: JSON: {"chave": "valor"}
```

**Strings Brutas (Raw Strings)**: Para definir uma string na qual sequências de extrapolação e metacaracteres são completamente ignorados, utilize o prefixo `r` (e.g., `r"..."`):

```zc
let regex = r"\w+"; // Contêm exatamente \ w +
let raw_json = r'{"chave": "valor"}'; // Não requer escapar chaves
```

#### Strings Multilinha

Zen C suporta blocos puros sem preenchimentos usando strings multilinha com o delimitador `"""`. Isso é extremamente útil para escrever linguagens embarcadas (GLSL, HTML) ou para geração de código C em um bloco `comptime` sem necessidade de interativamente escapar recuos da linha ou interpolação de aspas no interior da string.

De forma similar as string em padrão normal, string multilinha suportam **interpolação implícita**. Elas também podem ter atributos explicitos através do prefixo para strings puras e impuras (formatação normal):
- `f"""..."""`: Explicitamente marca qual deve ser do respectivo tipo bloco de formatação ou String Impura.
- `r"""..."""`: Explicitamente marca como um bloco literal de String Bruta (nada será processado entre eles ou ignorar caracateres especiais).

```zc
let prompt = """
  Por favor, insira o seu nome:
  Digite "exit" para sair da área ou cancelar.
""";

let mundo = "mundo";
let script = """
  fn ola() {
      println "olá, {mundo}!";
  }
""";

let pure_raw = r"""
  Aqui a reprentância da variável de {chaves} é pura sendo só texto, e o \n é só as letras barra-n de modo linear na sua impressão
""";
```

#### Prompts de Input (`?`)

Zen C suporta uma abreviação para solicitar entrada do usuário usando o prefixo `?`.

- `? "Prompt text"`: Imprime o prompt (sem newline) e aguarda entrada (lê uma linha).
- `? "Enter age: " (age)`: Imprime prompt e escaneia entrada para a variável `age`.
    - Especificadores de formato são automaticamente inferidos com base no tipo da variável.

```zc
let age: int;
? "How old are you? " (age);
println "You are {age} years old.";
```

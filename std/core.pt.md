# std/core

O módulo `std/core` fornece as pedras basilares e os tipos fundamentais da biblioteca padrão de Zen-C.

## Visão Geral

- **Tipos Fundamentais**: Define tipos e interfaces essenciais utilizados por todos os outros módulos.
- **Macros Essenciais**: Inclui macros para asserções e manipulação de erros.
- **Independência de Plataforma**: Fornece uma camada de abstração sobre as funcionalidades intrínsecas do compilador.

## Uso

```zc
import "std/core.zc"

fn main() {
    // Assert garante que uma condição seja verdadeira em execução
    assert(1 + 1 == 2);
}
```

## Funções e Macros

| Método | Assinatura | Descrizione |
| :--- | :--- | :--- |
| **assert** | `assert(condition: bool)` | Se a condição for falsa, imprime uma mensagem de erro e aborta a execução. |
| **panic** | `panic(message: char*)` | Aborta o programa imediatamente com a mensagem fornecida. |
| **exit** | `exit(code: int)` | Termina o processo com o código de saída fornecido. |
走

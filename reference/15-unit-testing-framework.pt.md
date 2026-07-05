+++
title = "15. Framework de Testes Unitários"
weight = 15
+++

# 15. Framework de Testes Unitários


Zen C inclui um framework de testes integrado que permite que você escreva testes unitários diretamente em seus arquivos fonte usando a palavra-chave `test`.

#### Sintaxe
Um bloco `test` contém um nome descritivo e um corpo de código para execução. Testes não precisam de uma função `main` para rodar.

```zc
test "unittest1" {
    "Isso é um teste unitário";

    let a = 3;
    assert(a > 0, "a deve ser um inteiro positivo");

    "unittest1 passou.";
}
```

#### Executando Testes
Para rodar todos os testes em um arquivo, utilize o comando `run`. O compilador irá automaticamente detectar e executar todos os blocos `test` de nível superior.

```bash
zc run meu_arquivo.zc
```

#### Asserções
Utilize a função embutida `assert(condition, message)` para verificar expectativas. Se a condição for falsa, o teste irá falhar e imprimir a mensagem fornecida.

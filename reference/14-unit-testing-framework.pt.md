+++
title = "14. Framework de Testes Unitários"
weight = 14
+++

# 14. Framework de Testes Unitários


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


#### Executar testes

```bash
zc run meu_arquivo.zc
```

A saída mostra cada teste pelo nome:
```
  TEST: nome descritivo ... OK
  TEST: outro teste ... FALHOU

1 test(s) failed
```

#### Asserções

| Função | Comportamento |
|:---|:---|
| `assert(cond, msg)` | Registra falha, continua para o próximo teste |
| `expect(cond, msg)` | Não fatal — registra falha mas continua no mesmo teste |

```zc
test "exemplo" {
    expect(resultado != null, "o resultado não deveria ser nulo");
    expect(codigo == 200, "o status deveria ser 200");
}
```

#### Código de saída

O binário termina com o número de testes falhos (0 = todos aprovados).

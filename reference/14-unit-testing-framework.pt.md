+++
title = "14. Framework de Testes Unitários"
weight = 14
+++

# 14. Framework de Testes Unitários


O Zen C inclui um framework de testes integrado que permite escrever testes unitários diretamente nos arquivos-fonte usando a palavra-chave `test`.

#### Sintaxe
Um bloco `test` contém um nome descritivo e um corpo de código para execução. Os testes não exigem uma função `main` para serem executados.

```zc
test "unittest1" {
    "Este é um teste unitário";

    let a = 3;
    assert(a > 0, "a deve ser um inteiro positivo");

    "unittest1 passou.";
}
```

#### Executando Testes
Para executar todos os testes em um arquivo, use o comando `run`. O compilador detectará e executará automaticamente todos os blocos `test` de nível superior.

```bash
zc run meu_arquivo.zc
```

#### Asserções
Use a função integrada `assert(condição, mensagem)` para verificar as expectativas. Se a condição for falsa, o teste falhará e imprimirá a mensagem fornecida.

---

## Contribuindo

Nós damos boas-vindas a contribuições! Seja consertando bugs, adicionando documentação ou propondo novas funcionalidades.

Por favor, veja [CONTRIBUTING_PT_BR.md](CONTRIBUTING_PT_BR.md) para diretrizes detalhadas sobre como contribuir, executar testes e submeter pull requests.

---

## Segurança

Para instruções sobre relatórios de segurança, por favor veja [SECURITY_PT_BR.md](SECURITY_PT_BR.md).

---

## Atribuições

Este projeto usa bibliotecas de terceiros. Textos completos de licença podem ser encontrados no diretório `LICENSES/`.

*   **[cJSON](https://github.com/DaveGamble/cJSON)** (Licença MIT): Usado para parsing e geração JSON no Language Server.
*   **[zc-ape](https://github.com/OEvgeny/zc-ape)** (Licença MIT): O port original Actually Portable Executable do Zen-C por [Eugene Olonov](https://github.com/OEvgeny).
*   **[Cosmopolitan Libc](https://github.com/jart/cosmopolitan)** (Licença ISC): A biblioteca fundadora que torna APE possível.
*   **[TRE](https://github.com/laurikari/tre)** (Licença BSD): Usado para o motor de expressões regulares na biblioteca padrão.
*   **[zenc.vim](https://github.com/zenc-lang/zenc.vim)** (Licença MIT): O plugin oficial para Vim/Neovim, escrito principalmente por **[davidscholberg](https://github.com/davidscholberg)**.

---

<div align="center">
  <p>
    Copyright © 2026 Linguagem de Programação Zen C.<br>
    Comece sua jornada hoje.
  </p>
  <p>
    <a href="https://discord.com/invite/q6wEsCmkJP">Discord</a> •
    <a href="https://github.com/zenc-lang/zenc">GitHub</a> •
    <a href="https://github.com/zenc-lang/docs">Documentação</a> •
    <a href="https://github.com/zenc-lang/awesome-zenc">Exemplos</a> •
    <a href="https://github.com/zenc-lang/rfcs">RFCs</a> •
    <a href="CONTRIBUTING_PT_BR.md">Contribuir</a>
  </p>
</div>

# std/crypto

O módulo `std/crypto` fornece uma API de alto nível para algoritmos criptográficos comuns, incluindo hashing e encriptação.

## Uso

```zc
import "std/crypto/sha256.zc"

fn main() {
    let hash = Sha256::hash("hello world");
    println "SHA-256: {hash}";
}
```

## Submódulos

O `std/crypto` está organizado em submódulos específicos para cada algoritmo:

- **std/crypto/sha256.zc**: Algoritmo de hash SHA-256.
- **std/crypto/aes.zc**: Encriptação AES (Advanced Encryption Standard).
- **std/crypto/rand.zc**: Gerador de números aleatórios criptograficamente seguro.

## Tipos e Interfaces

Muitos submódulos de criptografia seguem um padrão comum para processamento incremental de dados:

### Interface de Hashing (Exemplo: Sha256)

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `new() -> Context` | Inicializa um novo contexto de hash. |
| **update** | `update(self, data: u8*, len: usize)` | Adiciona dados ao contexto. |
| **finalize** | `finalize(self, out: u8*)` | Finaliza o hash e escreve o resultado no buffer de saída. |

## Segurança

> [!WARNING]
> Certifique-se sempre de utilizar tamanhos de chave e modos de operação recomendados (ex: AES-GCM) para aplicações sensíveis à segurança.
走

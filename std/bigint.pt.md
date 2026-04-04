# std/bigint

O módulo `std/bigint` fornece aritmética de precisão arbitrária para números inteiros (bignums).

## Uso

```zc
import "std/bigint.zc"

fn main() {
    let a = BigInt::from_string("123456789012345678901234567890");
    let b = BigInt::from_int(10);
    
    let c = a.mul(&b);
    println "{c.to_string()}";
} // c, b e a são libertados automaticamente aqui
```

## Métodos

### Construção

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `BigInt::new() -> BigInt` | Cria um novo `BigInt` inicializado a zero. |
| **from_int** | `BigInt::from_int(v: int) -> BigInt` | Cria um `BigInt` a partir de um valor de 32 bits. |
| **from_long** | `BigInt::from_long(v: long) -> BigInt` | Cria um `BigInt` a partir de um valor de 64 bits. |
| **from_string** | `BigInt::from_string(s: char*) -> BigInt` | Cria um `BigInt` a partir de uma representação em string. |

### Operações Aritméticas

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **add** | `add(self, other: BigInt*) -> BigInt` | Adiciona dois `BigInt`. |
| **sub** | `sub(self, other: BigInt*) -> BigInt` | Subtrai `other` de `self`. |
| **mul** | `mul(self, other: BigInt*) -> BigInt` | Multiplica dois `BigInt`. |
| **div** | `div(self, other: BigInt*) -> BigInt` | Divide `self` por `other`. |
| **mod** | `mod(self, other: BigInt*) -> BigInt` | Retorna o resto da divisão. |

### Utilitários

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **to_string** | `to_string(self) -> char*` | Retorna a representação decimal em string. |
| **to_hex** | `to_hex(self) -> char*` | Retorna a representação hexadecimal em string. |

## Gerenciamento de Memória

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **free** | `free(self)` | Liberta manualmente a memória interna. |
| **Trait** | `impl Drop for BigInt` | Chama automaticamente `free()` quando sai do escopo. |
走

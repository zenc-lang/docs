# std/bigfloat

O módulo `std/bigfloat` fornece aritmética de vírgula flutuante de precisão arbitrária.

## Uso

```zc
import "std/bigfloat.zc"

fn main() {
    let a = BigFloat::from_string("1.2345678901234567890");
    let b = BigFloat::from_int(2);
    
    let c = a.add(&b); 
    println "{c.to_string()}"; 
} // c, b e a são libertados automaticamente aqui
```

## Métodos

### Construção

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `BigFloat::new() -> BigFloat` | Cria um novo `BigFloat` inicializado a zero. |
| **from_int** | `BigFloat::from_int(v: int) -> BigFloat` | Cria um `BigFloat` a partir de um valor inteiro. |
| **from_string** | `BigFloat::from_string(s: char*) -> BigFloat` | Cria um `BigFloat` a partir de uma representação em string. |

### Operações Aritméticas

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **add** | `add(self, other: BigFloat*) -> BigFloat` | Adiciona dois `BigFloat`. |
| **sub** | `sub(self, other: BigFloat*) -> BigFloat` | Subtrai `other` de `self`. |
| **mul** | `mul(self, other: BigFloat*) -> BigFloat` | Multiplica dois `BigFloat`. |
| **div** | `div(self, other: BigFloat*) -> BigFloat` | Divide `self` por `other`. |

### Utilitários

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **to_string** | `to_string(self) -> char*` | Retorna a representação em string do `BigFloat`. |

## Gerenciamento de Memória

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **free** | `free(self)` | Liberta manualmente a memória interna. |
| **Trait** | `impl Drop for BigFloat` | Chama automaticamente `free()`. |
走

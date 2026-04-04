# std/bits

O módulo `std/bits` fornece utilitários para manipulação de bits em tipos inteiros.

## Uso

```zc
import "std/bits.zc"

fn main() {
    let n = 0b0000_1010;
    
    // Contagem de bits e manipulação
    let count = Bits::count_ones(n); // 2
    let reversed = Bits::reverse_bits(n);
    
    // Operações em nível de bit
    if (Bits::is_set(n, 3)) {
        println "O bit 3 está definido!";
    }
}
```

## Funções

### Contagem e Verificação

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **count_ones** | `count_ones(v: u32) -> int` | Retorna o número de bits definidos (`1`). |
| **count_zeros** | `count_zeros(v: u32) -> int` | Retorna o número de bits não definidos (`0`). |
| **is_set** | `is_set(v: u32, bit: int) -> bool` | Verifica se o bit especificado está em `1`. |

### Manipulação

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **set_bit** | `set_bit(v: u32, bit: int) -> u32` | Define o bit especificado para `1`. |
| **clear_bit** | `clear_bit(v: u32, bit: int) -> u32` | Define o bit especificado para `0`. |
| **toggle_bit** | `toggle_bit(v: u32, bit: int) -> u32` | Inverte o bit especificado. |
| **reverse_bits** | `reverse_bits(v: u32) -> u32` | Reverte a ordem dos bits. |

### Miscelânea

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **is_power_of_two** | `is_power_of_two(v: u32) -> bool` | Retorna true se `v` for uma potência de 2. |
走

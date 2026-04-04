# std/bits

El módulo `std/bits` proporciona operaciones bit a bit de bajo nivel, rotaciones, recuentos de población e inversiones de bits.

## Resumen

- **Multiplataforma**: Implementa correctamente las operaciones bit a bit en diferentes arquitecturas.
- **Eficiente**: Utiliza algoritmos optimizados de manipulación de bits.
- **Exhaustivo**: Admite enteros sin signo de 8, 16, 32, 64 y 128 bits.
- **Utilidades de Endianness**: Incluye funciones para invertir el orden de los bytes (intercambio de endianness).

## Uso

```zc
import "std/bits.zc"

fn main() {
    let a: u32 = 0x80000001;
    
    // Rotar entero de 32 bits a la izquierda por 1
    let rotated = Bits::rotl32(a, 1); // 0x00000003
    
    // Contar bits establecidos (conteo de población)
    let count = Bits::popcount32(0b1011); // 3
    
    // Invertir orden de bytes (bswap)
    let swapped = Bits::bswap32(0x12345678); // 0x78563412
}
```

## Métodos

### Rotación de Bits

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **rotl[N]** | `Bits::rotl[N](n: u[N], c: u[N]) -> u[N]` | Rota `n` a la izquierda `c` bits (N=8, 16, 32, 64, 128). |
| **rotr[N]** | `Bits::rotr[N](n: u[N], c: u[N]) -> u[N]` | Rota `n` a la derecha `c` bits (N=8, 16, 32, 64, 128). |

### Conteo de Población

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **popcount[N]** | `Bits::popcount[N](n: u[N]) -> u[N]` | Devuelve el número de bits establecidos (1s) en `n` (N=8, 16, 32, 64, 128). |

### Conteo de Ceros a la Izquierda/Derecha

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **clz[N]** | `Bits::clz[N](n: u[N]) -> u[N]` | Devuelve el número de bits cero a la izquierda (N=8, 16, 32, 64, 128). |
| **ctz[N]** | `Bits::ctz[N](n: u[N]) -> u[N]` | Devuelve el número de bits cero a la derecha (N=8, 16, 32, 64, 128). |

### Intercambio de Bytes e Inversión de Bits

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **bswap[N]** | `Bits::bswap[N](n: u[N]) -> u[N]` | Invierte el orden de los bytes de `n` (N=16, 32, 64, 128). |
| **reverse_bits[N]** | `Bits::reverse_bits[N](n: u[N]) -> u[N]` | Invierte el orden de los bits de `n` (N=8, 16, 32, 64, 128). |

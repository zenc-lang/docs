# std/simd

O módulo `std/simd` fornece tipos e operações SIMD (Single Instruction, Multiple Data) portáteis para paralelismo ao nível de dados.

## Visão Geral

- **Vetores Portáteis**: Tipos vetoriais que mapeiam para instruções SSE, AVX ou NEON dependendo do hardware de destino.
- **Alto Desempenho**: Execute a mesma operação em múltiplos elementos de dados simultaneamente.
- **Alinhamento Automático**: Garante o alinhamento de memória necessário para operações SIMD eficientes.

## Uso

```zc
import "std/simd.zc"

fn main() {
    let a = f32x4::new(1.0, 2.0, 3.0, 4.0);
    let b = f32x4::new(5.0, 6.0, 7.0, 8.0);
    
    // Todas as 4 adições ocorrem numa única instrução de CPU
    let c = a.add(b);
}
```

## Tipos Vetoriais

### Vetores de Vírgula Flutuante
- `f32x4`: Vetor de 4 floats de 32 bits (128 bits).
- `f32x8`: Vetor de 8 floats de 32 bits (256 bits).
- `f64x2`: Vetor de 2 doubles de 64 bits (128 bits).
- `f64x4`: Vetor de 4 doubles de 64 bits (256 bits).

### Vetores Inteiros
- `i32x4`, `u32x4`, `i32x8`, `u32x8`.
- `i64x2`, `u64x2`, `i64x4`, `u64x4`.

## Métodos (Comuns a todos os tipos)

### Construção

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `Type::new(...args) -> Vector` | Cria um vetor a partir de componentes individuais. |
| **splat**| `Type::splat(val) -> Vector` | Cria um vetor onde todos os elementos são preenchidos com `val`. |
| **load** | `Type::load(ptr: T*) -> Vector` | Carrega um vetor da memória. O ponteiro deve estar alinhado. |

### Operações Aritméticas

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **add** | `add(self, other: Vector) -> Vector` | Adição elemento a elemento. |
| **sub** | `sub(self, other: Vector) -> Vector` | Subtração elemento a elemento. |
| **mul** | `mul(self, other: Vector) -> Vector` | Multiplicação elemento a elemento. |
| **div** | `div(self, other: Vector) -> Vector` | Divisão elemento a elemento. |

### Operações Horizontais

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **sum** | `sum(self) -> T` | Retorna a soma de todos os elementos no vetor. |
走

# std/simd

Zen-C proporciona tipos vectoriales SIMD (Instrucción Única, Datos Múltiples) nativos que se compilan directamente en instrucciones vectoriales optimizadas por hardware (SSE, AVX, NEON, etc.) compatibles con el backend de destino.

## Resumen

- **Rendimiento Nativo**: Aprovecha las extensiones vectoriales de LLVM/GCC para una máxima eficiencia.
- **Portabilidad Implícita**: Tipos como `f32x4` se mapean al mejor hardware de 128 bits disponible específico para la arquitectura.
- **Aritmética por Elementos**: Los operadores estándar (`+`, `-`, `*`, `/`) se aplican a todas las vías (lanes) simultáneamente.
- **Difusión (Broadcasting)**: Inicializar con un solo valor lo difunde a todas las vías.

## Uso

```zc
import "std/simd.zc"

fn main() {
    // Inicialización (vías explícitas)
    let a = f32x4 { 1.0, 2.0, 3.0, 4.0 };
    
    // Difusión (un solo valor para todas las vías)
    let b = f32x4 { v: 2.0 };
    
    // Suma por elementos
    let c = a + b;   // Resultado: { 3.0, 4.0, 5.0, 6.0 }
    
    // Acceso a Vías
    let primera = c[0];
}
```

## Tipos Vectoriales

La biblioteca estándar define varios tipos vectoriales de 128 y 256 bits. También puede definir tipos personalizados utilizando el atributo `@vector(N)`.

### Vectores de 128 bits (SSE / NEON)

| Tipo | Tipo de Elemento | Vías | Tamaño en Bytes |
| :--- | :--- | :--- | :--- |
| `f32x4` | `f32` | 4 | 16 |
| `f64x2` | `f64` | 2 | 16 |
| `i32x4` | `i32` | 4 | 16 |
| `u32x4` | `u32` | 4 | 16 |
| `i64x2` | `i64` | 2 | 16 |
| `u64x2` | `u64` | 2 | 16 |
| `i16x8` | `i16` | 8 | 16 |
| `u16x8` | `u16` | 8 | 16 |
| `i8x16` | `i8` | 16 | 16 |
| `u8x16` | `u8` | 16 | 16 |

### Vectores de 256 bits (AVX / AVX2)

| Tipo | Tipo de Elemento | Vías | Tamaño en Bytes |
| :--- | :--- | :--- | :--- |
| `f32x8` | `f32` | 8 | 32 |
| `f64x4` | `f64` | 4 | 32 |
| `i32x8` | `i32` | 8 | 32 |
| `u32x8` | `u32` | 8 | 32 |
| `i64x4` | `i64` | 4 | 32 |
| `u64x4" | `u64` | 4 | 32 |
| `i16x16` | `i16` | 16 | 32 |
| `u16x16` | `u16` | 16 | 32 |
| `i8x32` | `i8` | 32 | 32 |
| `u8x32` | `u8` | 32 | 32 |

## Operaciones

| Categoría | Operador | Descripción |
| :--- | :--- | :--- |
| **Aritmética** | `+`, `-`, `*`, `/` | Suma, resta, multiplicación y división estándar por elemento. |
| **Bit a Bit** | `&`, `\|`, `^`, `~` | AND, OR, XOR y NOT a nivel de bits en todas las vías. |
| **Indexación** | `[i]` | Acceder o modificar vías individuales por índice. |
| **Comparación** | `==`, `!=`, `<`, `>` | Devuelve un vector de máscara booleana (los resultados varían según el backend). |

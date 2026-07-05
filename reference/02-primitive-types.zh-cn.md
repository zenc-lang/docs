+++
title = "2. 原始类型"
weight = 2
+++

# 2. 原始类型 {#2-yuan-shi-lei-xing}


| 类型 | C 等效类型 | 描述 |
|:---|:---|:---|
| `int`, `uint` | `int32_t`, `uint32_t` | 32位有符号/无符号整数 |
| `c_char`, `c_uchar` | `char`, `unsigned char` | C char (互操作) |
| `c_short`, `c_ushort` | `short`, `unsigned short` | C short (互操作) |
| `c_int`, `c_uint` | `int`, `unsigned int` | C int (互操作) |
| `c_long`, `c_ulong` | `long`, `unsigned long` | C long (互操作) |
| `c_longlong`, `c_ulonglong` | `long long`, `unsigned long long` | C long long / unsigned long long (互操作) |
| `I8` .. `I128` 或 `i8` .. `i128` | `int8_t` .. `__int128_t` | 有符号固定宽度整数 |
| `U8` .. `U128` 或 `u8` .. `u128` | `uint8_t` .. `__uint128_t` | 无符号固定宽度整数 |
| `isize`, `usize` | `ptrdiff_t`, `size_t` | 指针大小的整数 |
| `byte` | `uint8_t` | U8 的别名 |
| `F32`, `F64` 或 `f32`, `f64`  | `float`, `double` | 浮点数 |
| `bool` | `bool` | `true` 或 `false` |
| `char` | `char` | 单个字符 |
| `string` | `char*` | C-string (以 null 结尾) |
| `U0`, `u0`, `void` | `void` | 空类型 |
| `iN` (例如 `i256`) | `_BitInt(N)` | 任意位宽有符号整数 (C23) |
| `uN` (例如 `u42`) | `unsigned _BitInt(N)` | 任意位宽无符号整数 (C23) |
| `rune` | `uint32_t` | Unicode 标量值 (UTF-32 码点) |

#### 字面量
- **整数**: 十进制 (`123`), 十六进制 (`0xFF`), 八进制 (`0o755`), 二进制 (`0b1011`).
  - *注意*: 带有前导零的数字被视为十进制（`0123` 即 `123`），这与 C 语言不同。
  - *注意*: 数字可以包含下划线以提高可读性 (`1_000_000`, `0b_1111_0000`).
- **浮点数**: 标准格式 (`3.14`), 科学计数法 (`1e-5`, `1.2E3`)。浮点数同样支持下划线 (`3_14.15_92`)。

#### Unicode 与 Rune

Zen C 通过 `rune` 类型提供对 Unicode 标量值的一等支持。一个 `rune` 代表一个 Unicode 码点（编码为 32 位无符号整数）。

| 字面量 | 描述 |
|:---|:---|
| `'a'` | 标准 ASCII 字符 |
| `'🚀'` | 多字节 Unicode 字符 |
| `'\u{2764}'` | Unicode 转义序列 (十六进制) |

```zc
import "std.zc"

fn main() {
    let c = 'a';
    println "字符 '{c}' 的 ASCII/Unicode 编码为 {(int)c}";

    let code = 97;
    println "编码 {code} 对应的字符为 {(char)code}";

    let r: rune = '🚀';
    println "Rune '{r}' 的 Unicode 编码为 {(uint)r}";
    
    let r_code: uint = 128640;
    println "编码 {r_code} 对应的 Rune 为 '{(rune)r_code}'";

    let r_esc: rune = '\u{2764}';
    println "Rune '{r_esc}' 的编码为 {(uint)r_esc} (0x{(uint)r_esc:X})";
}
```

{% alert(type="important") %}
**可移植代码最佳实践**
- 对于所有纯 Zen C 逻辑，请使用 **可移植类型** (`int`、`uint`、`i64`、`u8` 等)。`int` 保证在所有架构上都是 32 位有符号整数。
- 仅在与 C 库 (FFI) 交互时使用 **C 互操作类型** (`c_int`、`c_char`、`c_long`, ``c_ulong``, ``c_longlong``, ``c_ulonglong``)。它们的大小因平台和 C 编译器而异。
- 使用 `isize` 和 `usize` 进行数组索引和内存指针运算。
{% end %}

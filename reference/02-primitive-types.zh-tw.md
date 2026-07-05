+++
title = "2. 原始類型"
weight = 2
+++

# 2. 原始類型 {#2-yuan-shi-lei-xing}


| 類型 | C 等效類型 | 描述 |
|:---|:---|:---|
| `int`, `uint` | `int32_t`, `uint32_t` | 32位元有號/無號整數 |
| `c_char`, `c_uchar` | `char`, `unsigned char` | C char (互操作) |
| `c_short`, `c_ushort` | `short`, `unsigned short` | C short (互操作) |
| `c_int`, `c_uint` | `int`, `unsigned int` | C int (互操作) |
| `c_long`, `c_ulong` | `long`, `unsigned long` | C long (互操作) |
| `c_longlong`, `c_ulonglong` | `long long`, `unsigned long long` | C long long / unsigned long long (互操作) |
| `I8` .. `I128` 或 `i8` .. `i128` | `int8_t` .. `__int128_t` | 有符號固定寬度整數 |
| `U8` .. `U128` 或 `u8` .. `u128` | `uint8_t` .. `__uint128_t` | 無符號固定寬度整數 |
| `isize`, `usize` | `ptrdiff_t`, `size_t` | 指針大小的整數 |
| `byte` | `uint8_t` | U8 的別名 |
| `F32`, `F64` 或 `f32`, `f64`  | `float`, `double` | 浮點數 |
| `bool` | `bool` | `true` 或 `false` |
| `char` | `char` | 單個字符 |
| `string` | `char*` | C-string (以 null 結尾) |
| `U0`, `u0`, `void` | `void` | 空類型 |
| `iN` (例如 `i256`) | `_BitInt(N)` | 任意位寬有符號整數 (C23) |
| `uN` (例如 `u42`) | `unsigned _BitInt(N)` | 任意位寬無符號整數 (C23) |
| `rune` | `uint32_t` | Unicode 標量值 (UTF-32 碼點) |

#### 字面量
- **整數**: 十進制 (`123`), 十六進制 (`0xFF`), 八進制 (`0o755`), 二進制 (`0b1011`).
  - *注意*: 帶有前導零的數字被視為十進制（`0123` 即 `123`），這與 C 語言不同。
  - *注意*: 數字可以包含底線以提高可讀性 (`1_000_000`, `0b_1111_0000`).
- **浮點數**: 標準格式 (`3.14`), 科學計數法 (`1e-5`, `1.2E3`)。浮點數同樣支持下劃線 (`3_14.15_92`)。

#### Unicode 與 Rune

Zen C 通過 `rune` 類型提供對 Unicode 標量值的一等支持。一個 `rune` 代表一個 Unicode 碼點（編碼為 32 位無符號整數）。

| 字面量 | 描述 |
|:---|:---|
| `'a'` | 標準 ASCII 字符 |
| `'🚀'` | 多字節 Unicode 字符 |
| `'\u{2764}'` | Unicode 轉義序列 (十六進制) |

```zc
import "std.zc"

fn main() {
    let c = 'a';
    println "字符 '{c}' 的 ASCII/Unicode 編碼為 {(int)c}";

    let code = 97;
    println "編碼 {code} 對應的字符為 {(char)code}";

    let r: rune = '🚀';
    println "Rune '{r}' 的 Unicode 編碼為 {(uint)r}";
    
    let r_code: uint = 128640;
    println "編碼 {r_code} 對應的 Rune 為 '{(rune)r_code}'";

    let r_esc: rune = '\u{2764}';
    println "Rune '{r_esc}' 的編碼為 {(uint)r_esc} (0x{(uint)r_esc:X})";
}
```

{% alert(type="important") %}
**可移植代碼最佳實踐**
- 對於所有純 Zen C 邏輯，請使用 **可移植類型** (`int`、`uint`、`i64`、`u8` 等)。`int` 保證在所有架構上都是 32 位元有號整數。
- 僅在與 C 庫 (FFI) 交互時使用 **C 互操作類型** (`c_int`、`c_char`、`c_long`, `c_ulong`, `c_longlong`, `c_ulonglong`)。它們的大小因平台和 C 編譯器而異。
- 使用 `isize` 和 `usize` 進行數組索引和內存指針運算。
{% end %}

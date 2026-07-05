+++
title = "17. MISRA 規則"
weight = 17
+++

# 17. MISRA 規則

Zen C 包含一個 **MISRA C:2012 合規模式**，透過 `--misra` 標誌啟用。
除了標準的 MISRA 檢查外，編譯器還強制執行若干 **Zen 特有規則**，
以促進更安全、更易於維護的程式碼。

#### 啟用 MISRA 模式

```bash
zc build app.zc --misra
```

違規將在編譯時報告為編譯器錯誤：

```
error: MISRA Rule Zen 2.2: tuple with 3 or more fields shall be replaced
       with a named struct (use 'struct' instead of positional tuple)
  --> app.zc:5:1
   |
 5 | fn get_stats() -> (int, int, int) { ... }
```

{% alert(type="note") %}
MISRA 標準文字版權歸 MISRA Consortium Ltd 所有。Zen C 的實作檢查合規性，
但不複製標準內容。請參閱 [MISRA C:2012](https://www.misra.org.uk/) 文件
獲取官方規則定義。
{% end %}

#### Zen 特有規則

這些規則是 Zen C 獨有的。每條規則在 `--misra` 啟用時進行檢查。

#### Zen 1.1 -- 禁止 raw 區塊

禁止繞過轉譯器的 `raw { }` 區塊。

```zc
// Bad:
fn main() {
    raw { int x = 10; }
}

// Good:
fn main() {
    let x = 10;
}
```

#### Zen 1.2 -- 禁止 plugin 區塊

禁止 `plugin ... end` 區塊，這些區塊會執行任意的建置時代碼。

```zc
// Bad:
plugin my_plugin

// Good:
import "std/some_module.zc"
```

#### Zen 1.3 -- 列舉匹配必須窮盡

禁止在列舉型別的 `match` 中使用 `_` 萬用字元 -- 所有變體必須明確處理。

```zc
enum Color { Red; Green; Blue; }

// Bad -- missing Blue:
fn describe(c: Color) {
    match c {
        Color::Red => { println "red"; }
        Color::Green => { println "green"; }
    }
}

// Good:
fn describe(c: Color) {
    match c {
        Color::Red => { println "red"; }
        Color::Green => { println "green"; }
        Color::Blue => { println "blue"; }
    }
}
```

#### Zen 1.4 -- 禁止預處理器指令

禁止 C 預處理器指令（`#define`、`#include`、`#if` 等）。
請使用 Zen 的 `import` 和 `def` 代替。

```zc
// Bad:
#define BUFFER_SIZE 256
#include <stdio.h>

// Good:
def BUFFER_SIZE = 256;
import "std/io.zc"
```

#### Zen 1.5 -- 禁止 `var` / `const` 宣告

關鍵字 `var` 和 `const` 已棄用於變數/常數宣告。
使用 `let` 宣告變數，使用 `def` 宣告編譯時常數。

```zc
// Bad:
var x = 10;
const MAX = 100;

// Good:
let x = 10;
def MAX = 100;
```

> `const` 作為 **型別限定符** 在 C 互操作中仍然有效
> （例如 FFI 宣告中的 `const int`）。

#### Zen 1.8 -- 禁止識別碼遮蔽

禁止宣告會遮蔽外部作用域中同名識別碼的名稱。

```zc
let x = 10;
if true {
    // Bad -- shadows outer x:
    let x = 20;
}

// Good:
if true {
    let inner_x = 20;
}
```

#### Zen 2.1 -- 禁止保留識別碼

禁止以 `__`、`_[A-Z]` 或 `_z_` 開頭的識別碼，這些是為編譯器
和 C 實作保留的。

```zc
// Bad:
let __my_var = 10;
let _Reserved = 20;
let _z_internal = 30;

// Good:
let my_var = 10;
let reserved = 20;
let internal = 30;
```

#### Zen 2.2 -- 元組大小限制

具有 **3 個或更多欄位** 的元組不得用作函數返回型別或參數。
請使用命名結構體代替。2 元組除外。

```zc
// Bad -- 3-tuple as return type:
fn get_stats() -> (int, int, int) { ... }
fn process(p: (int, string, bool)) { ... }

// Good -- use a struct:
struct Stats { sum: int; avg: int; max: int; }
fn get_stats() -> Stats { ... }

// OK -- 2-tuples are exempt:
fn get_pair() -> (int, int) { ... }
```

#### Zen 2.3 -- 字串比較

`string == string` 不得使用。請改用 `strcmp()`。

```zc
// Bad (when a, b are string):
if a == b { ... }

// Good:
if strcmp(a, b) == 0 { ... }

// OK -- int, bool, pointer comparisons are safe:
if x == y { ... }
```

## 標準 MISRA C:2012 覆蓋範圍

編譯器檢查以下標準 MISRA C:2012 規則。
點擊章節展開規則列表。

{% misra_table() %}

完整規則文字請參閱官方 [MISRA C:2012](https://www.misra.org.uk/) 文件。

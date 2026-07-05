+++
title = "17. MISRA 规则"
weight = 17
+++

# 17. MISRA 规则

Zen C 包含一个 **MISRA C:2012 合规模式**，通过 `--misra` 标志激活。
除了标准的 MISRA 检查外，编译器还强制执行若干 **Zen 特有规则**，
以促进更安全、更易于维护的代码。

#### 启用 MISRA 模式

```bash
zc build app.zc --misra
```

违规将在编译时报告为编译器错误：

```
error: MISRA Rule Zen 2.2: tuple with 3 or more fields shall be replaced
       with a named struct (use 'struct' instead of positional tuple)
  --> app.zc:5:1
   |
 5 | fn get_stats() -> (int, int, int) { ... }
```

{% alert(type="note") %}
MISRA 标准文本版权归 MISRA Consortium Ltd 所有。Zen C 的实现检查合规性，
但不复制标准内容。请参阅 [MISRA C:2012](https://www.misra.org.uk/) 文档
获取官方规则定义。
{% end %}

#### Zen 特有规则

这些规则是 Zen C 独有的。每条规则在 `--misra` 激活时进行检查。

#### Zen 1.1 -- 禁止 raw 块

禁止绕过转译器的 `raw { }` 块。

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

#### Zen 1.2 -- 禁止 plugin 块

禁止 `plugin ... end` 块，这些块会执行任意的构建时代码。

```zc
// Bad:
plugin my_plugin

// Good:
import "std/some_module.zc"
```

#### Zen 1.3 -- 枚举匹配必须穷尽

禁止在枚举类型的 `match` 中使用 `_` 通配符 -- 所有变体必须显式处理。

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

#### Zen 1.4 -- 禁止预处理器指令

禁止 C 预处理器指令（`#define`、`#include`、`#if` 等）。
请使用 Zen 的 `import` 和 `def` 代替。

```zc
// Bad:
#define BUFFER_SIZE 256
#include <stdio.h>

// Good:
def BUFFER_SIZE = 256;
import "std/io.zc"
```

#### Zen 1.5 -- 禁止 `var` / `const` 声明

关键字 `var` 和 `const` 已弃用于变量/常量声明。
使用 `let` 声明变量，使用 `def` 声明编译时常量。

```zc
// Bad:
var x = 10;
const MAX = 100;

// Good:
let x = 10;
def MAX = 100;
```

> `const` 作为 **类型限定符** 在 C 互操作中仍然有效
> （例如 FFI 声明中的 `const int`）。

#### Zen 1.8 -- 禁止标识符遮蔽

禁止声明会遮蔽外部作用域中同名标识符的名称。

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

#### Zen 2.1 -- 禁止保留标识符

禁止以 `__`、`_[A-Z]` 或 `_z_` 开头的标识符，这些是为编译器
和 C 实现保留的。

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

#### Zen 2.2 -- 元组大小限制

具有 **3 个或更多字段** 的元组不得用作函数返回类型或参数。
请使用命名结构体代替。2 元组除外。

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

#### Zen 2.3 -- 字符串比较

`string == string` 不得使用。请改用 `strcmp()`。

```zc
// Bad (when a, b are string):
if a == b { ... }

// Good:
if strcmp(a, b) == 0 { ... }

// OK -- int, bool, pointer comparisons are safe:
if x == y { ... }
```

## 标准 MISRA C:2012 覆盖范围

编译器检查以下标准 MISRA C:2012 规则。
点击章节展开规则列表。

{% misra_table() %}

完整规则文本请参阅官方 [MISRA C:2012](https://www.misra.org.uk/) 文档。

+++
title = "14. C 互操作性"
weight = 14
+++

# 14. C 互操作性 {#14-c-hu-cao-zuo-xing}


Zen C 提供了两种与 C 代码交互的方式：**信任导入 (Trusted Imports)** (方便) 和 **显式 FFI** (安全/精确)。

#### 方法 1: 信任导入 (方便)

你可以使用 `import` 关键字直接导入 `.h` 扩展名的 C 头文件。这会将头文件视为一个模块，并假设通过它访问的所有符号都存在。

```zc
//> link: -lm
import "math.h" as c_math;

fn main() {
    // 编译器不仅信任其正确性；还会直接生成 'cos(...)'
    let x = c_math::cos(3.14159);
}
```

{% alert(type="note") %}
零样板代码。立即访问头文件中的所有内容。
**缺点**: Zen C 不提供类型安全 (错误将在稍后由 C 编译器捕获)。
{% end %}

#### 方法 2: 显式 FFI (安全)

对于严格的类型检查或当你不想包含头文件文本时，请使用 `extern fn`。

```zc
include <stdio.h> // 在生成的 C 代码中发出 #include <stdio.h>

// 定义严格的签名
extern fn printf(fmt: char*, ...) -> c_int;

fn main() {
    printf("Hello FFI: %d\n", 42); // 由 Zen C 进行类型检查
}
```

{% alert(type="note") %}
Zen C 确保类型匹配。
**缺点**: 需要手动声明函数。
{% end %}

#### `import` vs `include`

- **`import "file.h"`**: 将头文件注册为命名模块。启用对符号的隐式访问 (例如 `file::function()`)。
- **`include <file.h>`**: 仅在生成的 C 代码中发出 `#include <file.h>`。不会向 Zen C 编译器引入任何符号；你必须使用 `extern fn` 来访问它们。

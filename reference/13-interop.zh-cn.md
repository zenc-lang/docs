+++
title = "17. C 互操作性"
weight = 13
+++

# 17. C 互操作性


Zen C 提供了两种与 C 代码交互的方式：**信任导入 (Trusted Imports)** (方便) 和 **显式 FFI** (安全/精确)。

#### 方法 1: 信任导入 (方便)

你可以使用 `import` 关键字直接导入 `.h` 扩展名的 C 头文件。这会将头文件视为一个模块，并假设通过它访问的所有符号都存在。

```zc
//> link: -lm
import "math.h" as c_math;

fn main() {
    // 编译器信任不仅正确；直接生成 'cos(...)'
    let x = c_math::cos(3.14159);
}
```

{% alert(type="note") %}
零样板代码。立即访问头文件中的所有内容。
**缺点**: Zen C 不提供类型安全 (错误将在稍后由 C 编译器捕获)。
{% end %}

#### 方法 2: 显式 FFI (安全)

对于严格的类型检查，或当你不想包含头文件文本时，请使用 `extern fn`.

```zc
include <stdio.h> // 在生成的 C 代码中发出 #include <stdio.h>

// 定义严格签名
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
- **`include <file.h>`**: 纯粹在生成的 C 代码中发出 `#include <file.h>`。不向 Zen C 编译器引入任何符号；必须使用 `extern fn` 才能访问它们。

---

## 标准库

Zen C 包含一个涵盖基本功能的标准库 (`std`)。

[浏览标准库文档](../docs/std/README.md)

### 核心模块

<details>
<summary>点击查看所有标准库模块</summary>

| 模块 | 描述 | 文档 |
| :--- | :--- | :--- |
| **`std/bigfloat.zc`** | 任意精度浮点运算。 | [文档](../docs/std/bigfloat.md) |
| **`std/bigint.zc`** | 任意精度整数 `BigInt`。 | [文档](../docs/std/bigint.md) |
| **`std/bits.zc`** | 底层位运算操作 (`rotl`, `rotr` 等)。 | [文档](../docs/std/bits.md) |
| **`std/complex.zc`** | 复数算术 `Complex`。 | [文档](../docs/std/complex.md) |
| **`std/vec.zc`** | 可增长动态数组 `Vec<T>`。 | [文档](../docs/std/vec.md) |
| **`std/string.zc`** | 堆分配的 `String` 类型，支持 UTF-8。 | [文档](../docs/std/string.md) |
| **`std/queue.zc`** | 先进先出队列 (环形缓冲区)。 | [文档](../docs/std/queue.md) |
| **`std/map.zc`** | 泛型哈希表 `Map<V>`。 | [文档](../docs/std/map.md) |
| **`std/fs.zc`** | 文件系统操作。 | [文档](../docs/std/fs.md) |
| **`std/io.zc`** | 标准输入/输出 (`print`/`println`)。 | [文档](../docs/std/io.md) |
| **`std/option.zc`** | 可选值 (`Some`/`None`)。 | [文档](../docs/std/option.md) |
| **`std/result.zc`** | 错误处理 (`Ok`/`Err`)。 | [文档](../docs/std/result.md) |
| **`std/path.zc`** | 跨平台路径操作。 | [文档](../docs/std/path.md) |
| **`std/env.zc`** | 进程环境变量。 | [文档](../docs/std/env.md) |
| **`std/net/`** | TCP, UDP, HTTP, DNS, URL. | [文档](../docs/std/net.md) |
| **`std/thread.zc`** | 线程与同步。 | [文档](../docs/std/thread.md) |
| **`std/time.zc`** | 时间测量与睡眠。 | [文档](../docs/std/time.md) |
| **`std/json.zc`** | JSON 解析与序列化。 | [文档](../docs/std/json.md) |
| **`std/stack.zc`** | 后进先出栈 `Stack<T>`。 | [文档](../docs/std/stack.md) |
| **`std/set.zc`** | 泛型哈希集合 `Set<T>`。 | [文档](../docs/std/set.md) |
| **`std/process.zc`** | 进程执行与管理。 | [文档](../docs/std/process.md) |
| **`std/regex.zc`** | 正则表达式 (基于 TRE)。 | [文档](../docs/std/regex.md) |
| **`std/simd.zc`** | 原生 SIMD 向量类型。 | [文档](../docs/std/simd.md) |

</details>

---

## 工具链

Zen C 提供内置的语言服务器 (LSP) 和 REPL 以增强开发体验。

### 语言服务器 (LSP)

Zen C 语言服务器 (LSP) 支持标准的 LSP 特性，用于编辑器集成：

*   **转到定义**
*   **查找引用**
*   **悬停信息**
*   **补全** (函数/结构体名，方法/字段的点补全)
*   **文档符号** (大纲)
*   **签名帮助**
*   **诊断** (语法/语义错误)

启动语言服务器（通常在编辑器的 LSP 设置中配置）：

```bash
zc lsp
```

它通过标准 I/O (JSON-RPC 2.0) 进行通信。

### REPL

Read-Eval-Print Loop 允许你交互式地尝试 Zen C 代码。

```bash
zc repl
```

#### 特性

*   **交互式编码**：输入表达式或语句以立即求值。
*   **持久历史**：命令保存在 `~/.zprep_history` 中。
*   **启动脚本**：自动加载 `~/.zprep_init.zc` 中的命令。

#### 命令

| 命令 | 描述 |
|:---|:---|
| `:help` | 显示可用命令。 |
| `:reset` | 清除当前会话历史 (变量/函数)。 |
| `:vars` | 显示活跃变量。 |
| `:funcs` | 显示用户定义的函数。 |
| `:structs` | 显示用户定义的结构体。 |
| `:imports` | 显示活跃导入。 |
| `:history` | 显示会话输入历史。 |
| `:type <expr>` | 显示表达式的类型。 |
| `:c <stmt>` | 显示语句生成的 C 代码。 |
| `:time <expr>` | 基准测试表达式 (运行 1000 次迭代)。 |
| `:edit [n]` | 在 `$EDITOR` 中编辑命令 `n` (默认：最后一条)。 |
| `:save <file>` | 将当前会话保存到 `.zc` 文件。 |
| `:load <file>` | 将 `.zc` 文件加载并执行到会话中。 |
| `:watch <expr>` | 监视表达式 (每次输入后重新求值)。 |
| `:unwatch <n>` | 移除监视。 |
| `:undo` | 从会话中移除最后一条命令。 |
| `:delete <n>` | 移除索引为 `n` 的命令。 |
| `:clear` | 清屏。 |
| `:quit` | 退出 REPL。 |
| `! <cmd>` | 运行 shell 命令 (如 `!ls`)。 |

---

### 语言服务器协议 (LSP)

Zen C 包含一个内置的语言服务器，用于编辑器集成。

- **[安装与设置指南](translations/LSP_ZH_CN.md)**
- **支持的编辑器**: VS Code, Neovim, Vim, Zed, 以及任何支持 LSP 的编辑器。

使用 `zc lsp` 启动服务器。

### Zen C 调试

Zen C 程序可以使用标准的 C 调试器（如 **LLDB** 或 **GDB**）进行调试。

#### Visual Studio Code

为了在 VS Code 中获得最佳体验，请安装官方的 [Zen C 扩展](https://marketplace.visualstudio.com/items?itemName=Z-libs.zenc)。对于调试，您可以使用 **C/C++**（由 Microsoft 提供）或 **CodeLLDB** 扩展。

将这些配置添加到您的 `.vscode` 目录中，以启用一键调试：

**`tasks.json`** (构建任务):
```json
{
    "label": "Zen C: Build Debug",
    "type": "shell",
    "command": "zc",
    "args": [ "${file}", "-g", "-o", "${fileDirname}/app", "-O0" ],
    "group": { "kind": "build", "isDefault": true }
}
```

**`launch.json`** (调试器):
```json
{
    "name": "Zen C: Debug (LLDB)",
    "type": "lldb",
    "request": "launch",
    "program": "${fileDirname}/app",
    "preLaunchTask": "Zen C: Build Debug"
}
```

## 编译器支持与兼容性

Zen C 旨在与大多数 C11 编译器配合使用。某些特性依赖于 GNU C 扩展，但这些扩展通常在其他编译器中也能工作。使用 `--cc` 标志切换后端。

```bash
zc run app.zc --cc clang
zc run app.zc --cc zig
```

### 测试套件状态

<details>
<summary>点击查看编译器支持详情</summary>

| 编译器 | 通过率 | 受支持特性 | 已知局限性 |
|:---|:---:|:---|:---|
| **GCC** | **100% (全面)** | 所有特性 | 无. |
| **Clang** | **100% (全面)** | 所有特性 | 无. |
| **Zig** | **100% (全面)** | 所有特性 | 无. 使用 `zig cc` 作为替代 C 编译器. |
| **TCC** | **98% (高)** | 结构体, 泛型, Trait, 模式匹配 | 不支持 Intel ASM, 不支持 `__attribute__((constructor))`. |

</details>

{% alert(type="warning") %}
**编译器构建警告：** 虽然 **Zig CC** 作为 Zen C 程序的后端非常出色，但使用它构建 *Zen C 编译器本身*可能会通过验证，但会生成无法通过测试的不稳定二进制文件。我们建议使用 **GCC** 或 **Clang** 构建编译器，并仅将 Zig 用作操作代码的后端。
{% end %}

{% alert(type="tip") %}
### 使用 Zig 构建
{% end %}

Zig 的 `zig cc` 命令提供了 GCC/Clang 的替代方案，具有出色的跨平台编译支持。使用 Zig：

```bash
# 使用 Zig 编译并运行 Zen C 程序
zc run app.zc --cc zig

# 使用 Zig 构建 Zen C 编译器本身
make zig
```

### C++ 互操作

Zen C 可以通过 `--cpp` 标志生成 C++ 兼容的代码，从而实现与 C++ 库的无缝集成。

```bash
# 直接使用 g++ 编译
zc app.zc --cpp

# 或者转译用于手动构建
zc transpile app.zc --cpp
g++ out.c my_cpp_lib.o -o app
```

#### 在 Zen C 中使用 C++

包含 C++ 头文件并在 `raw` 块中使用 C++ 代码：

```zc
include <vector>
include <iostream>

raw {
    std::vector<int> make_vec(int a, int b) {
        return {a, b};
    }
}

fn main() {
    let v = make_vec(1, 2);
    raw { std::cout << "Size: " << v.size() << std::endl; }
}
```

{% alert(type="note") %}
--cpp 标志会将后端切换为 `g++` 并发出 C++ 兼容的代码（使用 `auto` 代替 `__auto_type`，使用函数重载代替 `_Generic`，以及对 `void*` 进行显式转换）。
{% end %}

#### CUDA 互操作

Zen C 通过转译为 **CUDA C++** 来支持 GPU 编程。这使你在维持 Zen C 人体工程学语法的同时，能够利用内核中的强大 C++ 特性（模板、constexpr）。

```bash
# 直接使用 nvcc 编译
zc run app.zc --cuda

# 或者转译用于手动构建
zc transpile app.zc --cuda -o app.cu
nvcc app.cu -o app
```

#### CUDA 特定属性

| 属性 | CUDA 等效项 | 描述 |
|:---|:---|:---|
| `@global` | `__global__` | 内核函数 (运行在 GPU，从主机调用) |
| `@device` | `__device__` | 设备函数 (运行在 GPU，从 GPU 调用) |
| `@host` | `__host__` | 主机函数 (明确仅 CPU 运行) |

#### 内核启动语法

Zen C 提供了一个简洁的 `launch` 语句用于调用 CUDA 内核：

```zc
launch kernel_name(args) with {
    grid: num_blocks,
    block: threads_per_block,
    shared_mem: 1024,  // 可选
    stream: my_stream   // 可选
};
```

这转译为：`kernel_name<<<grid, block, shared, stream>>>(args);`

#### 编写 CUDA 内核

使用带有 `@global` 的 Zen C 函数语法和 `launch` 语句：

```zc
import "std/cuda.zc"

@global
fn add_kernel(a: float*, b: float*, c: float*, n: int) {
    let i = thread_id();
    if i < n {
        c[i] = a[i] + b[i];
    }
}

fn main() {
    def N = 1024;
    let d_a = cuda_alloc<float>(N);
    let d_b = cuda_alloc<float>(N); 
    let d_c = cuda_alloc<float>(N);
    defer cuda_free(d_a);
    defer cuda_free(d_b);
    defer cuda_free(d_c);

    // ... 初始化数据 ...
    
    launch add_kernel(d_a, d_b, d_c, N) with {
        grid: (N + 255) / 256,
        block: 256
    };
    
    cuda_sync();
}
```

#### 标准库 (`std/cuda.zc`)
Zen C 为常见的 CUDA 操作提供了一个标准库，以减少 `raw` 块的使用：

```zc
import "std/cuda.zc"

// 内存管理
let d_ptr = cuda_alloc<float>(1024);
cuda_copy_to_device(d_ptr, h_ptr, 1024 * sizeof(float));
defer cuda_free(d_ptr);

// 同步
cuda_sync();

// 线程索引 (在内核内部使用)
let i = thread_id(); // 全局索引
let bid = block_id();
let tid = local_id();
```

{% alert(type="note") %}
**注意：** `--cuda` 标志设置 `nvcc` 为编译器并隐含 `--cpp` 模式。需要安装 NVIDIA CUDA Toolkit。
{% end %}

### C23 支持

当使用兼容的后端编译器（GCC 14+, Clang 14+）时，Zen C 支持现代 C23特性。

- **`auto`**: 如果 `__STDC_VERSION__ >= 202300L`，Zen C 会自动将类型推导映射到标准 C23 `auto`。
- **`_BitInt(N)`**: 使用 `iN` 和 `uN` 类型（例如 `i256`, `u12`, `i24`）访问 C23 任意位宽整数。

### Objective-C 互操作

Zen C 可以通过 `--objc` 标志编译为 Objective-C (`.m`)，允许你使用 Objective-C 框架（如 Cocoa/Foundation）和语法。

```bash
# 使用 clang (或 gcc/gnustep) 编译
zc app.zc --objc --cc clang
```

#### 在 Zen C 中使用 Objective-C

使用 `include` 包含头文件，并在 `raw` 块中使用 Objective-C 语法 (`@interface`, `[...]`, `@""`)。

```zc
//> macos: framework: Foundation
//> linux: cflags: -fconstant-string-class=NSConstantString -D_NATIVE_OBJC_EXCEPTIONS
//> linux: link: -lgnustep-base -lobjc

include <Foundation/Foundation.h>

fn main() {
    raw {
        NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
        NSLog(@"来自 Objective-C 的问候！");
        [pool drain];
    }
    println "Zen C 也能正常工作！";
}
```

{% alert(type="note") %}
**注意：** Zen C 字符串插值通过调用 `debugDescription` 或 `description` 同样适用于 Objective-C 对象 (`id`)。
{% end %}

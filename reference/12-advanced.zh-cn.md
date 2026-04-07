+++
title = "12. 高级与元编程"
weight = 12
+++

# 12. 高级与元编程


### 12.1 元编程

#### Comptime
在编译时运行代码以生成源代码或打印消息。
```zc
comptime {
    // 在编译时生成代码(写入 stdout)
    println "let build_date = \"2024-01-01\";";
}

println "Build Date: {build_date}";
```

**辅助函数**

`comptime` 块内可用的特殊函数:
- **`yield(str)`** - 显式输出生成的代码(printf 的替代方案)
- **`compile_error(msg)`** - 以致命错误消息停止编译
- **`compile_warn(msg)`** - 发出编译时警告(允许继续编译)

```zc
comptime {
    compile_warn("正在生成优化代码...");
    
    let ENABLE_FEATURE = 1;
    if (ENABLE_FEATURE == 0) {
        compile_error("必须启用功能!");
    }
    
    println "let FEATURE_ENABLED = 1;";
}
```

**构建元数据**

在编译时访问编译器构建信息:
- **`__COMPTIME_TARGET__`** - 平台字符串: `"linux"`, `"windows"` 或 `"macos"`
- **`__COMPTIME_FILE__`** - 当前正在编译的源文件名

```zc
comptime {
    // 平台特定的代码生成
    println "let PLATFORM = \"{__COMPTIME_TARGET__}\";";
}

println "运行于: {PLATFORM}";
```

{% alert(type="tip") %}
在 comptime 字符串内使用 `{{` 和 `}}` 来转义花括号。
{% end %}

#### Embed
将文件嵌入为指定类型。
```zc
// 默认 (Slice_char)
let data = embed "assets/logo.png";

// 类型化嵌入
let text = embed "shader.glsl" as string;    // 嵌入为 C-string
let rom  = embed "bios.bin" as u8[1024];     // 嵌入为固定数组
let wav  = embed "sound.wav" as u8[];        // 嵌入为 Slice_u8
```

#### 插件
导入编译器插件以扩展语法。
```zc
import plugin "regex"
let re = regex! { ^[a-z]+$ };
```

#### 泛型 C 宏
将预处理器宏传递给 C。

{% alert(type="tip") %}
对于简单的常量，请使用 `def`。当你需要 C 预处理器宏或条件编译标志时，请使用 `#define`。
{% end %}

```zc
#define MAX_BUFFER 1024
```

#### 条件编译
使用 `@cfg()` 根据 `-D` 标志有条件地包含或排除任何顶层声明。

```zc
// 编译: zc build app.zc -DUSE_OPENGL

@cfg(USE_OPENGL)
import "opengl_backend.zc";

@cfg(USE_VULKAN)
import "vulkan_backend.zc";

@cfg(not(USE_OPENGL))
@cfg(not(USE_VULKAN))
fn fallback_init() { println "未选择后端"; }
```

| 形式 | 含义 |
|:---|:---|
| `@cfg(NAME)` | 如果设置了 `-DNAME` 则包含 |
| `@cfg(not(NAME))` | 如果未设置 `-DNAME` 则包含 |
| `@cfg(any(A, B, ...))` | 如果任意条件为真则包含 (OR) |
| `@cfg(all(A, B, ...))` | 如果所有条件为真则包含 (AND) |

一个声明上的多个 `@cfg` 使用 AND 组合。`not()` 可以在 `any()` 和 `all()` 内部使用。适用于任何顶层声明：`fn`、`struct`、`import`、`impl`、`raw`、`def`、`test` 等。

### 12.2 属性

修饰函数和结构体以修改编译器行为。

| 属性 | 作用域 | 描述 |
|:---|:---|:---|
| `@required` | 函数 | 如果忽略返回值则发出警告。 |
| `@deprecated("msg")` | 函数/结构体 | 使用时发出带有消息的警告。 |
| `@inline` | 函数 | 提示编译器进行内联。 |
| `@noinline` | 函数 | 防止内联。 |
| `@packed` | 结构体 | 移除字段间的填充。 |
| `@align(N)` | 结构体 | 强制按 N 字节对齐。 |
| `@constructor` | 函数 | 在 main 之前运行。 |
| `@destructor` | 函数 | 在 main 退出后运行。 |
| `@unused` | 函数/变量 | 抑制未使用变量警告。 |
| `@weak` | 函数 | 弱符号链接。 |
| `@section("name")` | 函数 | 将代码放置在特定段中。 |
| `@noreturn` | 函数 | 函数不会返回 (例如 exit)。 |
| `@pure` | 函数 | 函数无副作用 (优化提示)。 |
| `@cold` | 函数 | 函数不太可能被执行 (分支预测提示)。 |
| `@hot` | 函数 | 函数频繁执行 (优化提示)。 |
| `@export` | 函数/结构体 | 导出符号 (默认可见性)。 |
| `@global` | 函数 | CUDA: 内核入口点 (`__global__`)。 |
| `@device` | 函数 | CUDA: 设备函数 (`__device__`)。 |
| `@host` | 函数 | CUDA: 主机函数 (`__host__`)。 |
| `@comptime` | 函数 | 用于编译时执行的辅助函数。 |
| `@cfg(NAME)` | 任意 | 条件编译：仅在传递 `-DNAME` 时包含。支持 `not()`、`any()`、`all()`。 |
| `@derive(...)` | 结构体 | 自动实现 Trait。支持 `Debug`, `Eq` (智能派生), `Copy`, `Clone`。 |
| `@ctype("type")` | 函数参数 | 覆盖参数生成的 C 类型。 |
| `@<custom>` | 任意 | 将泛型属性传递给 C (例如 `@flatten`, `@alias("name")`)。 |

#### 自定义属性

Zen C 支持强大的 **自定义属性** 系统，允许你在代码中直接使用任何 GCC/Clang 的 `__attribute__`。任何不被 Zen C 编译器显式识别的属性都会被视为泛型属性并传递给生成的 C 代码。

这提供了对高级编译器特性、优化和链接器指令的访问，而无需在语言核心中提供显式支持。

#### 语法映射
Zen C 属性直接映射到 C 属性：
- `@name` → `__attribute__((name))`
- `@name(args)` → `__attribute__((name(args)))`
- `@name("string")` → `__attribute__((name("string")))`

#### 智能派生

Zen C 提供了尊重移动语义的 "智能派生"：

- **`@derive(Eq)`**：生成一个通过引用获取参数的相等性方法 (`fn eq(self, other: T*)`)。
    - 当比较两个非 Copy 结构体 (`a == b`) 时，编译器会自动通过引用传递 `b` (`&b`) 以避免移动它。
    - 字段上的递归相等性检查也会优先使用指针访问，以防止所有权转移。

### 12.3 内联汇编

Zen C 为内联汇编提供了一流支持，直接转译为 GCC 风格的扩展 `asm`。

#### 基本用法
在 `asm` 块内编写原始汇编。字符串会自动拼接。
```zc
asm {
    "nop"
    "mfence"
}
```

#### Volatile
防止编译器优化掉具有副作用的汇编代码。
```zc
asm volatile {
    "rdtsc"

}
```

#### 命名约束
Zen C 通过命名绑定简化了复杂的 GCC 约束语法。

```zc
// 语法: : out(变量) : in(变量) : clobber(寄存器)
// 使用 {变量} 占位符语法以提高可读性

fn add_five(x: int) -> int {
    let result: int;
    asm {
        "mov {x}, {result}"
        "add $5, {result}"
        : out(result)
        : in(x)
        : clobber("cc")
    }
    return result;
}
```

| 类型 | 语法 | GCC 等效项 |
|:---|:---|:---|
| **输出** | `: out(variable)` | `"=r"(variable)` |
| **输入** | `: in(variable)` | `"r"(variable)` |
| **破坏** | `: clobber("rax")` | `"rax"` |
| **内存** | `: clobber("memory")` | `"memory"` |

{% alert(type="note") %}
使用 Intel 语法时（通过 `-masm=intel`），必须确保你的构建配置正确（例如，`//> cflags: -masm=intel`）。TCC 不支持 Intel 语法的汇编。
{% end %}

### 12.4 诊断系统

Zen C 提供了一个分类诊断系统，可以通过 `-W` 和 `-Wno-` 标志进行控制。这对于管理与安全、未使用代码和 C 互操作相关的警告非常有用。

[阅读更多关于诊断系统的信息](15-diagnostics.zh-cn.md)

### 12.5 构建指令

Zen C 支持在源文件顶部使用特殊注释来配置构建过程，无需复杂的构建系统或 Makefile。

| 指令 | 参数 | 描述 |
|:---|:---|:---|
| `//> link:` | `-lfoo` 或 `path/to/lib.a` | 链接库或对象文件。 |
| `//> lib:` | `path/to/libs` | 添加库搜索路径 (`-L`)。 |
| `//> include:` | `path/to/headers` | 添加包含头文件搜索路径 (`-I`)。 |
| `//> framework:` | `Cocoa` | 链接 macOS Framework。 |
| `//> cflags:` | `-Wall -O3` | 向 C 编译器传递任意标志。 |
| `//> define:` | `MACRO` 或 `KEY=VAL` | 定义预处理器宏 (`-D`)。 |
| `//> pkg-config:` | `gtk+-3.0` | 运行 `pkg-config` 并追加 `--cflags` 和 `--libs`。 |
| `//> shell:` | `command` | 在构建期间执行 shell 命令。 |
| `//> get:` | `http://url/file` | 如果特定文件不存在，则下载该文件。 |

#### 特性

**1. 操作系统守护 (OS Guarding)**
在指令前加上操作系统名称，以使其仅在特定平台上应用。
受支持的前缀：`linux:`, `windows:`, `macos:` (或 `darwin:`)。

```zc
//> linux: link: -lm
//> windows: link: -lws2_32
//> macos: framework: Cocoa
```

**2. 环境变量展开**
使用 `${VAR}` 语法在指令中展开环境变量。

```zc
//> include: ${HOME}/mylib/include
//> lib: ${ZC_ROOT}/std
```

#### 示例

```zc
//> include: ./include
//> lib: ./libs
//> link: -lraylib -lm
//> cflags: -Ofast
//> pkg-config: gtk+-3.0

import "raylib.h"

fn main() { ... }
```

### 12.6 关键字

以下关键字在 Zen C 中是保留的。

#### 声明
`alias`, `def`, `enum`, `fn`, `impl`, `import`, `let`, `module`, `opaque`, `struct`, `trait`, `union`, `use`

#### 控制流
`async`, `await`, `break`, `catch`, `continue`, `defer`, `do`, `else`, `for`, `goto`, `guard`, `if`, `loop`, `match`, `return`, `try`, `unless`, `while`

#### 特殊
`asm`, `assert`, `autofree`, `comptime`, `const`, `embed`, `launch`, `ref`, `sizeof`, `static`, `test`, `volatile`

#### 常量
`true`, `false`, `null`

#### C 保留字
以下标识符是保留的，因为它们是 C11 中的关键字：
`auto`, `case`, `char`, `default`, `double`, `extern`, `float`, `inline`, `int`, `long`, `register`, `restrict`, `short`, `signed`, `switch`, `typedef`, `unsigned`, `void`, `_Atomic`, `_Bool`, `_Complex`, `_Generic`, `_Imaginary`, `_Noreturn`, `_Static_assert`, `_Thread_local`

#### 运算符
`and`, `or`

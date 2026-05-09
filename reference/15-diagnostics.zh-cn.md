+++
title = "15. 诊断系统"
weight = 15
+++

# 15. 诊断系统


Zen C 提供了一个分类诊断系统，可以对编译器警告进行粒度控制。这有助于在保持高代码质量标准的同时，减少与外部 C 代码交互时的摩擦。

#### 诊断类别

警告按逻辑类别分组。可以使用编译器标志全局启用或禁用每个类别。

| 类别 | 描述 | 默认值 |
| :--- | :--- | :--- |
| **`INTEROP`** | 与导入 C 头文件和未定义的外部函数相关的警告。 | **OFF** |
| **`PEDANTIC`** | 针对潜在问题或代码质量的额外严格检查。 | **OFF** |
| **`UNUSED`** | 对已定义但未使用的变量、参数或函数的警告。 | **ON** |
| **`SAFETY`** | 关键安全警告，如空指针访问或除以零。 | **ON** |
| **`LOGIC`** | 与逻辑相关的警告，如不可达代码或常量比较。 | **ON** |
| **`CONVERSION`** | 隐式或窄化类型转换的警告。 | **ON** |
| **`STYLE`** | 编码风格警告，如变量遮蔽 (shadowing)。 | **ON** |

#### 编译器标志

你可以使用 `-W`（启用）和 `-Wno-`（禁用）标志，后跟类别名称或特定诊断 ID 来控制诊断。

##### 类别标志

- `-Winterop`: 启用所有与互操作性相关的警告。
- `-Wno-unused`: 特别静音未使用变量/参数的警告。
- `-Wsafety`: 确保所有安全检查都处于活动状态。
- `-Wall`: 启用所有主要的诊断类别。
- `-Wextra`: 启用更严格的诊断（相当于 `-Wpedantic`）。

##### 使用示例

```bash
# 启用 C 互操作性警告进行编译
zc app.zc -Winterop

# 启用除未使用代码外的所有警告进行编译
zc app.zc -Wall -Wno-unused
```

#### C 互操作性摩擦

默认情况下，Zen C 会抑制可能属于 C 标准库的函数的“未定义函数”警告（`INTEROP` 类别为 **OFF**）。

如果你希望编译器严格标记每个未定义的函数（例如，为了发现拼写错误），请启用 interop 类别：

```bash
zc main.zc -Winterop
```

启用后，编译器将为常见的 C 函数提供有用的建议：
```text
warning: Undefined function 'abs'
  --> main.zc:5:13
   |
5  |     let x = abs(-5);
   |             ^ here
   |
   = note: If this is a C function, it might need to be whitelisted in 'zenc.json'
```

#### 白名单

如果你经常使用特定的 C 库，并希望在启用 `-Winterop` 的情况下不被特定函数干扰，可以在 `zenc.json` 配置文件中的 `c_function_whitelist` 中添加它们。

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

## Further Reading

- **Language Server**: 查看 [LSP 文档](LSP.md) 了解编辑器集成。
- **MISRA Compliance**: 查看 [MISRA Rules](../reference/16-misra-rules) 获取完整规则参考。
- **Contributing**: 查看 [CONTRIBUTING.md](../CONTRIBUTING.md) 了解贡献指南。

+++
title = "1. 变量与常量"
weight = 1
+++

# 1. 变量与常量 {#1-bian-liang-yu-chang-liang}


Zen C 区分编译时常量和运行时变量。

#### 清单常量 (`def`)
仅在编译时存在的值（折叠到代码中）。用于数组大小、固定配置和魔术数字。

```zc
def MAX_SIZE = 1024;
let buffer: char[MAX_SIZE]; // 有效的数组大小
```

#### 变量 (`let`)
内存中的存储位置。可以是可变的或只读的 (`const`)。

```zc
let x = 10;             // 可变
x = 20;                 // 允许

let y: const int = 10;  // 只读 (类型修饰)
// y = 20;              // 错误：无法赋值给 const 变量
```

{% alert(type="tip") %}
**类型推导**：Zen C 自动推导初始化变量的类型。在支持的编译器上编译为 C23 的 `auto`，否则使用 GCC 的 `__auto_type` 扩展。
{% end %}

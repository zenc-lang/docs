+++
title = "4. 函数与 Lambda"
weight = 4
+++

# 4. 函数与 Lambda {#4-han-shu-yu-lambda}


#### 函数
```zc
fn add(a: int, b: int) -> int {
    return a + b;
}

// 调用时支持命名参数
add(a: 10, b: 20);
```

{% alert(type="note") %}
命名参数必须严格遵循定义的参数顺序。`add(b: 20, a: 10)` 是无效的。
{% end %}

#### 常量参数
函数参数可以标记为 `const` 以强制执行只读语义。这是一个类型修饰符，而不是清单常量。

```zc
fn print_val(v: const int) {
    // v = 10; // 错误：无法赋值给 const 变量
    println "{v}";
}
```

#### 默认参数
函数可以为尾部参数定义默认值。这些值可以是字面量、表达式或有效的 Zen C 代码（如结构体构造函数）。
```zc
// 简单默认值
fn increment(val: int, amount: int = 1) -> int {
    return val + amount;
}

// 表达式默认值（在调用处计算）
fn offset(val: int, pad: int = 10 * 2) -> int {
    return val + pad;
}

// 结构体默认值
struct Config { debug: bool; }
fn init(cfg: Config = Config { debug: true }) {
    if cfg.debug { println "调试模式"; }
}

fn main() {
    increment(10);      // 11
    offset(5);          // 25
    init();             // 打印 "调试模式"
}
```

#### Lambda (闭包)
可以捕获环境的匿名函数。
```zc
let factor = 2;
let doubler = x -> x * factor;  // 箭头语法
let full = fn(x: int) -> int { return x * factor; }; // 块语法

// 引用捕获（块语法）
let val = 10;
let modify = fn[&]() { val += 1; }; 
modify(); // val 现在是 11

// 引用捕获（箭头语法）
let modify_arrow = [&] x -> val += x;
modify_arrow(5); // val 现在是 16

// 引用捕获（多参数箭头语法）
let sum_into = [&] (a, b) -> val += (a + b);
sum_into(2, 2); // val 现在是 20

// 值捕获（默认）
let original = 100;
let implicit = x -> original + x;       // 隐式值捕获（无括号）
let explicit = [=] x -> original + x;   // 显式值捕获
// let fail = x -> original += x;       // 错误：无法赋值给捕获的值

```

#### 原始函数指针
Zen C 使用 `fn*` 语法支持原始 C 函数指针。这允许与期望函数指针且没有闭包开销的 C 库进行无缝互操作。

```zc
// 接受原始函数指针的函数
fn set_callback(cb: fn*(int)) {
    cb(42);
}

// 返回原始函数指针的函数
fn get_callback() -> fn*(int) {
    return my_handler;
}

// 支持指向函数指针的指针 (fn**)
let pptr: fn**(int) = &ptr;
```

#### 变参函数
函数可以使用 `...` 和 `va_list` 类型接受可变数量的参数。
```zc
fn log(lvl: int, fmt: char*, ...) {
    let ap: va_list;
    va_start(ap, fmt);
    vprintf(fmt, ap); // 使用 C stdio
    va_end(ap);
}
```

+++
title = "8. 内存管理"
weight = 8
+++

# 8. 内存管理


Zen C 允许带有符合人体工程学辅助的手动内存管理。

#### Defer
在当前作用域退出时执行代码。Defer 语句按照后进先出 (LIFO) 的顺序执行。
```zc
let f = fopen("file.txt", "r");
defer fclose(f);
```

{% alert(type="warning") %}
为了防止未定义行为，`defer` 块内不允许使用控制流语句（`return`, `break`, `continue`, `goto`）。
{% end %}

#### Autofree
在作用域退出时自动释放变量。
```zc
autofree let types = malloc(1024);
```

#### 资源语义 (默认移动)
Zen C 将带有析构函数（如 `File`, `Vec`, 或 malloc 的指针）的类型视为 **资源**。为了防止双重释放错误，资源不能被隐式复制。

- **默认移动**：分配资源变量会转移所有权。原始变量变得无效（已移动）。
- **复制类型**：没有析构函数的类型可以申请参与 `Copy` 行为，使赋值变成复制。

**诊断与哲学**：
如果你看到错误 "Use of moved value"，编译器是在告诉你：*"此类型拥有一个资源（如内存或句柄），盲目复制它是不安全的。"*

{% alert(type="note") %}
**对比：** 与 C/C++ 不同，Zen C 不会隐式复制拥有资源的值。
{% end %}

**函数参数**：
将值传递给函数遵循与赋值相同的规则：资源会被移动，除非通过引用传递。

```zc
fn process(r: Resource) { ... } // 'r' 被移动进函数
fn peek(r: Resource*) { ... }   // 'r' 被借用 (引用)
```

**显式克隆**：
如果你 *确实* 想要一个资源的两个副本，请显式执行：

```zc
let b = a.clone(); // 调用 Clone trait 中的 'clone' 方法
```

**选择性复制 (值类型)**：
对于没有析构函数的小型类型：

```zc
struct Point { x: int; y: int; }
impl Copy for Point {} // 选择参与隐式复制

fn main() {
    let p1 = Point { x: 1, y: 2 };
    let p2 = p1; // 已复制。p1 保持有效。
}
```

#### RAII / Drop Trait
实现 `Drop` 以自动运行清理逻辑。
```zc
impl Drop for MyStruct {
    fn drop(self) {
        self.free();
    }
}
```

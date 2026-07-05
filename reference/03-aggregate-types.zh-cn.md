+++
title = "3. 复合类型"
weight = 3
+++

# 3. 复合类型


#### 数组
具有值语义的固定大小数组。
```zc
def SIZE = 5;
let ints: int[SIZE] = [1, 2, 3, 4, 5];
let zeros: [int; SIZE]; // 零初始化的
```

#### 元组
将多个值组合在一起，通过索引访问元素。
```zc
let pair = (1, "Hello");
let x = pair.0;  // 1
let s = pair.1;  // "Hello"
```

**多个返回值**

函数可以返回元组以提供多个结果：
```zc
fn add_and_subtract(a: int, b: int) -> (int, int) {
    return (a + b, a - b);
}

let result = add_and_subtract(3, 2);
let sum = result.0;   // 5
let diff = result.1;  // 1
```

**解构**

元组可以直接解构为多个变量：
```zc
let (sum, diff) = add_and_subtract(3, 2);
// sum = 5, diff = 1
```

带类型的解构允许显式类型注解：
```zc
let (a: string, b: u8) = ("hello", 42);
let (x, y: i32) = (1, 2);  // 混合：x 推断，y 显式
```

#### 结构体
带有可选位域的数据结构。
```zc
struct Point {
    x: int;
    y: int;
}

// 结构体初始化
let p = Point { x: 10, y: 20 };

// 位域
struct Flags {
    valid: U8 : 1;
    mode:  U8 : 3;
}
```

{% alert(type="note") %}
结构体默认使用 [移动语义](@/tour/08-memory-management.zh-cn.md#zi-yuan-yu-yi-mo-ren-yi-dong)。即使是指针，也可以通过 `.` 访问字段（自动解引用）。
{% end %}

#### 不透明结构体
你可以将结构体定义为 `opaque`，以将对其字段的访问限制在定义该结构体的模块内部，同时仍允许在栈上分配该结构体（大小已知）。

```zc
// 在 user.zc 中
opaque struct User {
    id: int;
    name: string;
}

fn new_user(name: string) -> User {
    return User{id: 1, name: name}; // 允许：在模块内部
}

// 在 main.zc 中
import "user.zc";

fn main() {
    let u = new_user("Alice");
    // let id = u.id; // 错误：无法访问私有字段 'id'
}
```

#### 枚举
能够持有数据的标签联合 (Sum types)。
```zc
enum Shape {
    Circle(float),      // 持有半径
    Rect(float, float), // 持有宽、高
    Point               // 不带数据
}
```

#### 联合体
标准 C 联合体（不安全访问）。
```zc
union Data {
    i: int;
    f: float;
}
```

#### SIMD 向量
使用 GCC/Clang 向量扩展的原生 SIMD 向量类型。使用 `@vector(N)` 注解一个结构体来定义包含 N 个元素的向量。
```zc
import "std/simd.zc";

fn main() {
    let a = f32x4{v: 1.0};              // 广播: {1.0, 1.0, 1.0, 1.0}
    let b = f32x4{1.0, 2.0, 3.0, 4.0};  // 逐元素初始化
    let c = a + b;                       // 逐元素加法
    let x = c[0];                        // 元素访问 (float)
}
```
算术运算符（`+`, `-`, `*`, `/`）和位运算符（`&`, `|`, `^`）逐元素运算。预定义类型请参阅 [`std/simd.zc`](../std/simd.zc)。

#### 类型别名
为现有类型创建新名称。
```zc
alias ID = int;
alias PointMap = Map<string, Point>
alias OpFunc = fn(int, int) -> int
```
> **注意：** 类型别名末尾的分号是可选的。

#### 不透明类型别名
你可以将类型别名定义为 `opaque`，从而在定义模块之外创建一个与基础类型不同的新类型。这提供了强大的封装和类型安全性，而没有包装结构体的运行时开销。

```zc
// 在 library.zc 中
opaque alias Handle = int;

fn make_handle(v: int) -> Handle {
    return v; // 允许在模块内部进行隐式转换
}

// 在 main.zc 中
import "library.zc";

fn main() {
    let h: Handle = make_handle(42);
    // let i: int = h; // 错误：类型验证失败
    // let h2: Handle = 10; // 错误：类型验证失败
}
```

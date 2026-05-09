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




#### Tuples

将多个值组合成一个复合值。元组支持任意元数（2、3、4…最多10+）、嵌套组合、单个字段的修改和解构。

**基本用法**

```zc
let pair = (1, "hello");          // 2-tuple, types inferred
let triple = (1, "hello", 3.14);  // 3-tuple
let five = (1, 2, 3, 4, 5);      // 5-tuple
let typed: (int, string, f64) = (1, "two", 3.0);  // explicit annotation
```

**字段访问**

元素通过位置访问，使用 `.0`, `.1`, `.2` 等，或通过原始结构字段名 `.v0`, `.v1`：

```zc
let t = (1, "hello", 3.14);
assert(t.0 == 1);       // positional
assert(t.v1 == "hello"); // raw field name
```

**多个返回值**

函数可以返回元组以提供多个结果：

```zc
fn stats(data: int) -> (int, int) {
    return (data * 2, data + 1);
}

let r = stats(5);
assert(r.0 == 10);
assert(r.1 == 6);
```

**解构**

```zc
let (sum, diff) = add_and_subtract(3, 2);
// sum = 5, diff = 1

let (a: string, b: u8) = ("hello", 42);  // typed destructuring
let (x, y: i32) = (1, 2);                // mixed: x inferred, y explicit
```

**嵌套元组**

```zc
let nested = ((1, 2), (3, 4));
let inner = nested.v0;
assert(inner.v0 == 1);
assert(inner.v1 == 2);
```

**修改**

可以重新分配单个字段：

```zc
let t = (1, 2);
t.v0 = 99;
assert(t.v0 == 99);
```

**字符串比较**

包含 `string` 字段的元组必须使用 `strcmp()` 进行比较，而不是 `==`（`==` 对 `char*` 进行指针比较）：

```zc
let t = (1, "hello");
assert(strcmp(t.1, "hello") == 0);
```

**枚举元组负载**

枚举变体可以携带元组数据：

```zc
enum Shape {
    Point,
    Line(int, int),
    Labeled(int, string, f64),
}

match shape {
    Shape::Line(x, y) => { ... }
    Shape::Labeled(id, name, val) => { ... }
}
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

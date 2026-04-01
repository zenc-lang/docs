+++
title = "9. 面向对象编程"
weight = 9
+++

# 9. 面向对象编程


#### 方法
使用 `impl` 为类型定义方法。
```zc
impl Point {
    // 静态方法 (构造函数惯例)
    fn new(x: int, y: int) -> Self {
        return Point{x: x, y: y};
    }

    // 实例方法
    fn dist(self) -> float {
        return sqrt(self.x * self.x + self.y * self.y);
    }
}
```

**Self 简写**: 在具有 `self` 参数的方法中，可以使用 `.字段` 作为 `self.字段` 的简写：
```zc
impl Point {
    fn dist(self) -> float {
        return sqrt(.x * .x + .y * .y);  // 等同于 self.x, self.y
    }
}
```

#### 原始类型方法
Zen C 允许你使用相同的 `impl` 语法定义原始类型（如 `int`, `bool` 等）的方法。

```zc
impl int {
    fn abs(self) -> int {
        return *self < 0 ? -(*self) : *self;
    }
}

let x = -10;
let y = x.abs(); // 10
let z = (-5).abs(); // 5 (Literals supported)
```

#### Trait
定义共享行为。
```zc
struct Circle { radius: f32; }

trait Drawable {
    fn draw(self);
}

impl Drawable for Circle {
    fn draw(self) { ... }
}

let circle = Circle{};
let drawable: Drawable = &circle;
```

#### 标准 Trait
Zen C 包含与语言语法集成的标准 Trait。

**Iterable**

实现 `Iterable<T>` 以便为你的自定义类型启用 `for-in` 循环。

```zc
import "std/iter.zc"

// 定义一个迭代器
struct MyIter {
    curr: int;
    stop: int;
}

impl MyIter {
    fn next(self) -> Option<int> {
        if self.curr < self.stop {
            self.curr += 1;
            return Option<int>::Some(self.curr - 1);
        }
        return Option<int>::None();
    }
}

// 实现 Iterable
impl MyRange {
    fn iterator(self) -> MyIter {
        return MyIter{curr: self.start, stop: self.end};
    }
}

// 在循环中使用
for i in my_range {
    println "{i}";
}
```

**Drop**

实现 `Drop` 来定义一个在对象超出范围时运行的析构函数 (RAII)。

```zc
import "std/mem.zc"

struct Resource {
    ptr: void*;
}

impl Drop for Resource {
    fn drop(self) {
        if self.ptr != NULL {
            free(self.ptr);
        }
    }
}
```

{% alert(type="note") %}
如果一个变量被移动，则原始变量不会调用 `drop`。它遵循 [资源语义](@/tour/08-memory-management.zh-cn.md#zi-yuan-yu-yi-mo-ren-yi-dong)。
{% end %}

**Copy**

标记 Trait，用于选择支持 `Copy` 行为（隐式复制）而不是移动语义。通过 `@derive(Copy)` 使用。

{% alert(type="caution") %}
实现了 `Copy` 的类型不得定义析构函数 (`Drop`)。
{% end %}

```zc
@derive(Copy)
struct Point { x: int; y: int; }

fn main() {
    let p1 = Point{x: 1, y: 2};
    let p2 = p1; // 已复制！p1 保持有效。
}
```

**Clone**

实现 `Clone` 以允许显式复制拥有资源的类型。

```zc
import "std/mem.zc"

struct MyBox { val: int; }

impl Clone for MyBox {
    fn clone(self) -> MyBox {
        return MyBox{val: self.val};
    }
}

fn main() {
    let b1 = MyBox{val: 42};
    let b2 = b1.clone(); // 显式复制
}
```

#### 组合
使用 `use` 嵌入其他结构体。你可以将它们混合进来（展平字段）或者为它们命名（嵌套字段）。

```zc
struct Entity { id: int; }

struct Player {
    // 混入 (未命名): 展平字段
    use Entity;  // 直接将 'id' 添加到 Player
    name: string;
}

struct Match {
    // 组合 (命名): 嵌套字段
    use p1: Player; // 通过 match.p1 访问
    use p2: Player; // 通过 match.p2 访问
}
```

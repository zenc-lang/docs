+++
title = "9. 面向對象編程"
weight = 9
+++

# 9. 面向對象編程


#### 方法
使用 `impl` 為類型定義方法。
```zc
impl Point {
    // 靜態方法 (構造函數慣例)
    fn new(x: int, y: int) -> Self {
        return Point{x: x, y: y};
    }

    // 實例方法
    fn dist(self) -> float {
        return sqrt(self.x * self.x + self.y * self.y);
    }
}
```

**Self 簡寫**: 在具有 `self` 參數的方法中，可以使用 `.欄位` 作為 `self.欄位` 的簡寫：
```zc
impl Point {
    fn dist(self) -> float {
        return sqrt(.x * .x + .y * .y);  // 等同於 self.x, self.y
    }
}
```

#### 原始類型方法
Zen C 允許你使用相同的 `impl` 語法在原始類型（如 `int`、`bool` 等）上定義方法。

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
定義共享行為。
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

#### 標準 Trait
Zen C 包含與語言語法集成的標準 Trait。

**Iterable**

實現 `Iterable<T>` 以便為你的自定義類型啟用 `for-in` 循環。

```zc
import "std/iter.zc"

// 定義一個迭代器
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

// 實現 Iterable
impl MyRange {
    fn iterator(self) -> MyIter {
        return MyIter{curr: self.start, stop: self.end};
    }
}

// 在循環中使用
for i in my_range {
    println "{i}";
}
```

**Drop**

實現 `Drop` 來定義一個在對象超出範圍時運行的析構函數 (RAII)。

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
如果一個變量被移動，則原始變量不會調用 `drop`。它遵循 [資源語義](@/tour/08-memory-management.zh-tw.md#zi-yuan-yu-yi-mo-ren-yi-dong)。
{% end %}

**Copy**

標記 Trait，用於選擇支持 `Copy` 行為（隱式複製）而不是移動語義。通過 `@derive(Copy)` 使用。

{% alert(type="caution") %}
實現了 `Copy` 的類型不得定義析構函數 (`Drop`)。
{% end %}

```zc
@derive(Copy)
struct Point { x: int; y: int; }

fn main() {
    let p1 = Point{x: 1, y: 2};
    let p2 = p1; // 已複製！p1 保持有效。
}
```

**Clone**

實現 `Clone` 以允許顯式複製擁有資源的類型。

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
    let b2 = b1.clone(); // 顯式複製
}
```

#### 組合
使用 `use` 嵌入其他結構體。你可以將它們混合進來（展平字段）或者為它們命名（嵌套字段）。

```zc
struct Entity { id: int; }

struct Player {
    // 混入 (未命名): 展平字段
    use Entity;  // 直接將 'id' 添加到 Player
    name: string;
}

struct Match {
    // 組合 (命名): 嵌套字段
    use p1: Player; // 通過 match.p1 訪問
    use p2: Player; // 通過 match.p2 訪問
}
```

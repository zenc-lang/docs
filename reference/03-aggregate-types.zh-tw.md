+++
title = "3. 複合類型"
weight = 3
+++

# 3. 複合類型


#### 數組
具有值語義的固定大小數組。
```zc
def SIZE = 5;
let ints: int[SIZE] = [1, 2, 3, 4, 5];
let zeros: [int; SIZE]; // 零初始化的
```

#### 元組
將多個值組合在一起，通過索引訪問元素。
```zc
let pair = (1, "Hello");
let x = pair.0;  // 1
let s = pair.1;  // "Hello"
```

**多個返回值**

函數可以返回元組以提供多個結果：
```zc
fn add_and_subtract(a: int, b: int) -> (int, int) {
    return (a + b, a - b);
}

let result = add_and_subtract(3, 2);
let sum = result.0;   // 5
let diff = result.1;  // 1
```

**解構**

元組可以直接解構為多個變量：
```zc
let (sum, diff) = add_and_subtract(3, 2);
// sum = 5, diff = 1
```

帶類型的解構允許顯式類型注解：
```zc
let (a: string, b: u8) = ("hello", 42);
let (x, y: i32) = (1, 2);  // 混合：x 推斷，y 顯式
```

#### 結構體
帶有可選位域的數據結構。
```zc
struct Point {
    x: int;
    y: int;
}

// 結構體初始化
let p = Point { x: 10, y: 20 };

// 位域
struct Flags {
    valid: U8 : 1;
    mode:  U8 : 3;
}
```

{% alert(type="note") %}
結構体默認使用 [移動語義](@/tour/08-memory-management.zh-tw.md#zi-yuan-yu-yi-mo-ren-yi-dong)。即使是指針，也可以通過 `.` 訪問字段（自動解引用）。
{% end %}

#### 不透明結構體
你可以將結構體定義為 `opaque`，以將對其字段的訪問限制在定義該結構體的模塊內部，同時仍允許在棧上分配該結構體（大小已知）。

```zc
// 在 user.zc 中
opaque struct User {
    id: int;
    name: string;
}

fn new_user(name: string) -> User {
    return User{id: 1, name: name}; // 允許：在模塊內部
}

// 在 main.zc 中
import "user.zc";

fn main() {
    let u = new_user("Alice");
    // let id = u.id; // 錯誤：無法訪問私有字段 'id'
}
```

#### 枚舉
能夠持有數據的標籤聯合 (Sum types)。
```zc
enum Shape {
    Circle(float),      // 持有半徑
    Rect(float, float), // 持有寬、高
    Point               // 不帶數據
}
```

#### 聯合體
標準 C 聯合體（不安全訪問）。
```zc
union Data {
    i: int;
    f: float;
}
```

#### SIMD 向量
使用 GCC/Clang 向量擴展的原生 SIMD 向量類型。使用 `@vector(N)` 註解一個結構體來定義包含 N 個元素的向量。
```zc
import "std/simd.zc";

fn main() {
    let a = f32x4{v: 1.0};              // 廣播: {1.0, 1.0, 1.0, 1.0}
    let b = f32x4{1.0, 2.0, 3.0, 4.0};  // 逐元素初始化
    let c = a + b;                       // 逐元素加法
    let x = c[0];                        // 元素存取 (float)
}
```
算術運算符（`+`, `-`, `*`, `/`）和位元運算符（`&`, `|`, `^`）逐元素運算。預定義類型請參閱 [`std/simd.zc`](../std/simd.zc)。

#### 類型別名
為現有類型創建新名稱。
```zc
alias ID = int;
alias PointMap = Map<string, Point>
alias OpFunc = fn(int, int) -> int
```
> **注意：** 型別別名結尾的分號是可選項的。

#### 不透明類型別名
你可以將類型別名定義為 `opaque`，從而在定義模塊之外創建一個與基礎類型不同的新類型。這提供了強大的封裝和類型安全性，而沒有包裝結構體的運行時開銷。

```zc
// 在 library.zc 中
opaque alias Handle = int;

fn make_handle(v: int) -> Handle {
    return v; // 允許在模塊內部進行隱式轉換
}

// 在 main.zc 中
import "library.zc";

fn main() {
    let h: Handle = make_handle(42);
    // let i: int = h; // 錯誤：類型驗證失敗
    // let h2: Handle = 10; // 錯誤：類型驗證失敗
}
```

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




#### Tuples

將多個值組合成一個複合值。元組支援任意元數（2、3、4…最多10+）、巢狀組合、單個欄位的修改和解構。

**基本用法**

```zc
let pair = (1, "hello");          // 2-tuple, types inferred
let triple = (1, "hello", 3.14);  // 3-tuple
let five = (1, 2, 3, 4, 5);      // 5-tuple
let typed: (int, string, f64) = (1, "two", 3.0);  // explicit annotation
```

**欄位存取**

元素透過位置存取，使用 `.0`, `.1`, `.2` 等，或透過原始結構欄位名稱 `.v0`, `.v1`：

```zc
let t = (1, "hello", 3.14);
assert(t.0 == 1);       // positional
assert(t.v1 == "hello"); // raw field name
```

**多個回傳值**

函數可以回傳元組以提供多個結果：

```zc
fn stats(data: int) -> (int, int) {
    return (data * 2, data + 1);
}

let r = stats(5);
assert(r.0 == 10);
assert(r.1 == 6);
```

**解構**

```zc
let (sum, diff) = add_and_subtract(3, 2);
// sum = 5, diff = 1

let (a: string, b: u8) = ("hello", 42);  // typed destructuring
let (x, y: i32) = (1, 2);                // mixed: x inferred, y explicit
```

**巢狀元組**

```zc
let nested = ((1, 2), (3, 4));
let inner = nested.v0;
assert(inner.v0 == 1);
assert(inner.v1 == 2);
```

**修改**

可以重新指派單個欄位：

```zc
let t = (1, 2);
t.v0 = 99;
assert(t.v0 == 99);
```

**字串比較**

包含 `string` 欄位的元組必須使用 `strcmp()` 進行比較，而不是 `==`（`==` 對 `char*` 進行指標比較）：

```zc
let t = (1, "hello");
assert(strcmp(t.1, "hello") == 0);
```

**列舉元組載荷**

列舉變體可以攜帶元組資料：

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

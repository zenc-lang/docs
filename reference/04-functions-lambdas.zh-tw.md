+++
title = "4. 函數與 Lambda"
weight = 4
+++

# 4. 函數與 Lambda {#4-han-shu-yu-lambda}


#### 函數
```zc
fn add(a: int, b: int) -> int {
    return a + b;
}

// 調用時支持命名參數
add(a: 10, b: 20);
```

{% alert(type="note") %}
命名參數必須嚴格遵循定義的參數順序。`add(b: 20, a: 10)` 是無效的。
{% end %}

#### 常量參數
函數參數可以標記為 `const` 以強制執行只讀語義。這是一個類型修飾符，而不是清單常量。

```zc
fn print_val(v: const int) {
    // v = 10; // 錯誤：無法賦值給 const 變量
    println "{v}";
}
```

#### 默認參數
函數可以為尾部參數定義默認值。這些值可以是字面量、表達式或有效的 Zen C 代碼（如結構體構造函數）。
```zc
// 簡單默認值
fn increment(val: int, amount: int = 1) -> int {
    return val + amount;
}

// 表達式默認值（在調用處計算）
fn offset(val: int, pad: int = 10 * 2) -> int {
    return val + pad;
}

// 結構體默認值
struct Config { debug: bool; }
fn init(cfg: Config = Config { debug: true }) {
    if cfg.debug { println "調試模式"; }
}

fn main() {
    increment(10);      // 11
    offset(5);          // 25
    init();             // 打印 "調試模式"
}
```

#### Lambda (閉包)
可以捕獲環境的匿名函數。
```zc
let factor = 2;
let doubler = x -> x * factor;  // 箭頭語法
let full = fn(x: int) -> int { return x * factor; }; // 區塊語法

// 引用捕獲（區塊語法）
let val = 10;
let modify = fn[&]() { val += 1; }; 
modify(); // val 現在是 11

// 引用捕獲（箭頭語法）
let modify_arrow = [&] x -> val += x;
modify_arrow(5); // val 現在是 16

// 引用捕獲（多參數箭頭語法）
let sum_into = [&] (a, b) -> val += (a + b);
sum_into(2, 2); // val 現在是 20

// 值捕獲（默認）
let original = 100;
let implicit = x -> original + x;       // 隱式值捕獲（無括號）
let explicit = [=] x -> original + x;   // 顯式值捕獲
// let fail = x -> original += x;       // 錯誤：無法賦值給捕獲的值

```

#### 原始函數指針
Zen C 使用 `fn*` 語法支持原始 C 函數指針。這允許與期望函數指針且沒有閉包開銷的 C 庫進行無縫互操作。

```zc
// 接受原始函數指針的函數
fn set_callback(cb: fn*(int)) {
    cb(42);
}

// 返回原始函數指針的函數
fn get_callback() -> fn*(int) {
    return my_handler;
}

// 支持指向函數指針的指針 (fn**)
let pptr: fn**(int) = &ptr;
```

#### 變參函數
函數可以使用 `...` 和 `va_list` 類型接受可變數量的參數。
```zc
fn log(lvl: int, fmt: char*, ...) {
    let ap: va_list;
    va_start(ap, fmt);
    vprintf(fmt, ap); // 使用 C stdio
    va_end(ap);
}
```

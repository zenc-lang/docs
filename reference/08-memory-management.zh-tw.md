+++
title = "8. 內存管理"
weight = 8
+++

# 8. 內存管理


Zen C 允許帶有符合人體工程學輔助的手動內存管理。

#### Defer
在當前作用域退出時執行代碼。Defer 語句按照後進先出 (LIFO) 的順序執行。
```zc
let f = fopen("file.txt", "r");
defer fclose(f);
```

{% alert(type="warning") %}
為了防止未定義行為，`defer` 塊內不允許使用控制流語句（`return`, `break`, `continue`, `goto`）。
{% end %}

#### Autofree
在作用域退出時自動釋放變量。
```zc
autofree let types = malloc(1024);
```

#### 資源語義 (默認移動)
Zen C 將帶有析構函數（如 `File`, `Vec`, 或 malloc 的指針）的類型視為 **資源**。為了防止雙重釋放錯誤，資源不能被隱式複製。

- **默認移動**：分配資源變量會轉移所有權。原始變量變得無效（已移動）。
- **複製類型**：沒有析構函數的類型可以申請參與 `Copy` 行為，使賦值變成複製。

**診斷與哲學**：
如果你看到錯誤 "Use of moved value"，編譯器是在告訴你：*"此類型擁有一個資源（如內存或句柄），盲目複製它是不安全的。"*

{% alert(type="note") %}
**對比：** 與 C/C++ 不同，Zen C 不會隱式複製擁有資源的值。
{% end %}

**函數參數**：
將值傳遞給函數遵循與賦值相同的規則：資源會被移動，除非通過引用傳遞。

```zc
fn process(r: Resource) { ... } // 'r' 被移動進函數
fn peek(r: Resource*) { ... }   // 'r' 被借用 (引用)
```

**顯式克隆**：
如果你 *確實* 想要一個資源的兩個副本，請顯式執行：

```zc
let b = a.clone(); // 調用 Clone trait 中的 'clone' 方法
```

**選擇性複製 (值類型)**：
對於沒有析構函數的小型類型：

```zc
struct Point { x: int; y: int; }
impl Copy for Point {} // 選擇參與隱式複製

fn main() {
    let p1 = Point { x: 1, y: 2 };
    let p2 = p1; // 已複製。p1 保持有效。
}
```

#### RAII / Drop Trait
實現 `Drop` 以自動運行清理邏輯。
```zc
impl Drop for MyStruct {
    fn drop(self) {
        self.free();
    }
}
```

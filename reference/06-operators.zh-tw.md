+++
title = "6. 運算符"
weight = 6
+++

# 6. 運算符


Zen C 通過實現特定的方法名來支持用戶定義結構體的運算符重載。

#### 可重載運算符

| 類別 | 運算符 | 方法名 |
|:---|:---|:---|
| **算術** | `+`, `-`, `*`, `/`, `%`, `**` | `add`, `sub`, `mul`, `div`, `rem`, `pow` |
| **比較** | `==`, `!=` | `eq`, `neq` |
| | `<`, `>`, `<=`, `>=` | `lt`, `gt`, `le`, `ge` |
| **位運算** | `&`, `|`, `^` | `bitand`, `bitor`, `bitxor` |
| | `<<`, `>>` | `shl`, `shr` |
| **一元** | `-` | `neg` |
| | `!` | `not` |
| | `~` | `bitnot` |
| **索引** | `a[i]` | `get(a, i)` |
| | `a[i, j]` | `get(a, i, j)` |
| | `a[i] = v` | `set(a, i, v)` |

{% alert(type="note") %}
**關於字符串相等性的說明**：
- `string == string` 進行 **值比較**（等同於 `strcmp`）。
- `char* == char*` 進行 **指針比較**（檢查內存地址）。
- 混合比較（例如 `string == char*`）默認為 **指針比較**。
{% end %}

**示例：**
```zc
impl Point {
    fn add(self, other: Point) -> Point {
        return Point{x: self.x + other.x, y: self.y + other.y};
    }
}

let p3 = p1 + p2; // 調用 p1.add(p2)
```

**多索引示例：**
```zc
struct Matrix {
    data: int[9];
}

impl Matrix {
    fn get(self, row: int, col: int) -> int {
        return self.data[row * 3 + col];
    }
}

let m = Matrix{data: [1,0,0, 0,1,0, 0,0,1]};
let val = m[1, 2]; // 調用 Matrix.get(m, 1, 2)
```

#### 語法糖

這些運算符是內置語言特性，不能直接重載。

| 運算符 | 名稱 | 描述 |
|:---|:---|:---|
| `|>` | 管道 | `x |> f(y)` 脫糖為 `f(x, y)` |
| `??` | 空合併 | 如果 `val` 為 NULL，`val ?? default` 返回 `default` (用於指針) |
| `??=` | 空賦值 | 如果 `val` 為 NULL 則賦值 |
| `?.` | 安全導航 | 僅當 `ptr` 不為 NULL 時訪問字段 |
| `?` | Try 運算符 | 如果存在錯誤則返回 (用於 Result/Option 類型) |

**自動解引用**：
指針字段訪問 (`ptr.field`) 和方法調用 (`ptr.method()`) 會自動解引用指針，等同於 `(*ptr).field`。

+++
title = "6. 运算符"
weight = 6
+++

# 6. 运算符


Zen C 通过实现特定的方法名来支持用户定义结构体的运算符重载。

#### 可重载运算符

| 类别 | 运算符 | 方法名 |
|:---|:---|:---|
| **算术** | `+`, `-`, `*`, `/`, `%`, `**` | `add`, `sub`, `mul`, `div`, `rem`, `pow` |
| **比较** | `==`, `!=` | `eq`, `neq` |
| | `<`, `>`, `<=`, `>=` | `lt`, `gt`, `le`, `ge` |
| **位运算** | `&`, `|`, `^` | `bitand`, `bitor`, `bitxor` |
| | `<<`, `>>` | `shl`, `shr` |
| **一元** | `-` | `neg` |
| | `!` | `not` |
| | `~` | `bitnot` |
| **索引** | `a[i]` | `get(a, i)` |
| | `a[i, j]` | `get(a, i, j)` |
| | `a[i] = v` | `set(a, i, v)` |

{% alert(type="note") %}
**关于字符串相等性的说明**：
- `string == string` 进行 **值比较**（等同于 `strcmp`）。
- `char* == char*` 进行 **指针比较**（检查内存地址）。
- 混合比较（例如 `string == char*`）默认为 **指针比较**。
{% end %}

**示例：**
```zc
impl Point {
    fn add(self, other: Point) -> Point {
        return Point{x: self.x + other.x, y: self.y + other.y};
    }
}

let p3 = p1 + p2; // 调用 p1.add(p2)
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
let val = m[1, 2]; // 调用 Matrix.get(m, 1, 2)
```

#### 语法糖

这些运算符是内置语言特性，不能直接重载。

| 运算符 | 名称 | 描述 |
|:---|:---|:---|
| `|>` | 管道 | `x |> f(y)` 脱糖为 `f(x, y)` |
| `??` | 空合并 | 如果 `val` 为 NULL，`val ?? default` 返回 `default` (用于指针) |
| `??=` | 空赋值 | 如果 `val` 为 NULL 则赋值 |
| `?.` | 安全导航 | 仅当 `ptr` 不为 NULL 时访问字段 |
| `?` | Try 运算符 | 如果存在错误则返回 (用于 Result/Option 类型) |

**自动解引用**：
指针字段访问 (`ptr.field`) 和方法调用 (`ptr.method()`) 会自动解引用指针，等同于 `(*ptr).field`。

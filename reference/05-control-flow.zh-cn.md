+++
title = "5. 控制流"
weight = 5
+++

# 5. 控制流 {#5-kong-zhi-liu}


#### 条件语句
```zc
if x > 10 {
    print "Large";
} else if x > 5 {
    print "Medium";
} else {
    print "Small";
}

// 三元运算符
let y = x > 10 ? 1 : 0;

// If-表达式 (用于复杂条件)
let 类别 = if (x > 100) { "巨大" } else if (x > 10) { "大" } else { "小" };
```

#### 模式匹配
`switch` 的强大替代方案。
```zc
match val {
    1         => { print "One" },
    2 || 3    => { print "Two or Three" },    // 使用 || 进行 或 操作
    4 or 5    => { print "Four or Five" },    // 使用 'or' 进行 或 操作
    6, 7, 8   => { print "Six to Eight" },    // 使用逗号进行 或 操作
    10 .. 15  => { print "10 to 14" },        // 左闭右开区间 (旧语法)
    10 ..< 15 => { print "10 to 14" },        // 左闭右开区间 (显式)
    20 ..= 25 => { print "20 to 25" },        // 全闭区间
    _         => { print "Other" },
}

// 解构枚举
match shape {
    Shape::Circle(r)   => { println "半径: {r}" },
    Shape::Rect(w, h)  => { println "面积: {w*h}" },
    Shape::Point       => { println "点" },
}
```

#### 引用绑定
为了在不获取所有权（移动）的情况下检查一个值，在模式中使用 `ref` 关键字。这对于实现了移动语义的类型（如 `Option`, `Result`, 非 Copy 结构体）至关重要。

```zc
let opt = Some(NonCopyVal{...});
match opt {
    Some(ref x) => {
        // 'x' 是指向 'opt' 内部值的指针
        // 'opt' 在此处不会被移动/消耗
        println "{x.field}"; 
    },
    None => {}
}
```

#### 循環
```zc
// 區間迭代
for i in 0..10 { ... }      // 左閉右開 (0 到 9)
for i in 0..<10 { ... }     // 左閉右開 (顯式)
for i in 0..=10 { ... }     // 全閉 (0 到 10)
for i in 0..10 step 2 { ... }
for i in 10..0 step -1 { ... }  // Descending loop

// 迭代器 (Vec 或自定義 Iterable)
for item in vec { ... }

// 枚举：获取索引和值
for i, val in arr { ... }       // i = 0, 1, 2, ...
for i, val in 0..10 step 2 { ... } // i = 0, 1, 2, ...; val = 0, 2, 4, ...

// 直接迭代固定大小数组
let arr: int[5] = [1, 2, 3, 4, 5];
for val in arr {
    // val 是 int
    println "{val}";
}

// While 循環
while x < 10 { ... }

// Do-While
do { ... } while x < 10;

// 帶標籤的無限循環
outer: loop {
    if done { break outer; }
}

// 重複 N 次
for _ in 0..5 { ... }
```

#### 高级控制
```zc
// Guard: 如果条件为假，则执行 else 块并返回
guard ptr != NULL else { return; }

// Unless: 除非为真（即如果为假）
unless is_valid { return; }
```

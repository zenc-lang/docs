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

// 三元運算符
let y = x > 10 ? 1 : 0;

// If-表達式 (用於複雜條件)
let 類別 = if (x > 100) { "巨大" } else if (x > 10) { "大" } else { "小" };
```

#### 模式匹配
`switch` 的強大替代方案。
```zc
match val {
    1         => { print "One" },
    2 || 3    => { print "Two or Three" },    // 使用 || 進行 或 操作
    4 or 5    => { print "Four or Five" },    // 使用 'or' 進行 或 操作
    6, 7, 8   => { print "Six to Eight" },    // 使用逗號進行 或 操作
    10 .. 15  => { print "10 to 14" },        // 左閉右開區間 (舊語法)
    10 ..< 15 => { print "10 to 14" },        // 左閉右開區間 (顯式)
    20 ..= 25 => { print "20 to 25" },        // 全閉區間
    _         => { print "Other" },
}

// 解構枚舉
match shape {
    Shape::Circle(r)   => { println "半徑: {r}" },
    Shape::Rect(w, h)  => { println "面積: {w*h}" },
    Shape::Point       => { println "點" },
}
```

#### 引用綁定
為了在不獲取所有權（移動）的情況下檢查一個值，在模式中使用 `ref` 關鍵字。這對於實現了移動語義的類型（如 `Option`, `Result`, 非 Copy 結構體）至關重要。

```zc
let opt = Some(NonCopyVal{...});
match opt {
    Some(ref x) => {
        // 'x' 是指向 'opt' 內部值的指針
        // 'opt' 在此處不會被移動/消耗
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

// 枚舉：獲取索引和值
for i, val in arr { ... }       // i = 0, 1, 2, ...
for i, val in 0..10 step 2 { ... } // i = 0, 1, 2, ...; val = 0, 2, 4, ...

// 直接迭代固定大小數組
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

#### 高級控制
```zc
// Guard: 如果條件為假，則執行 else 塊並返回
guard ptr != NULL else { return; }

// Unless: 除非為真（即如果為假）
unless is_valid { return; }
```

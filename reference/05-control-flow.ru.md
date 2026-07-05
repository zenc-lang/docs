+++
title = "5. Управление потоком"
weight = 5
+++

# 5. Управление потоком {#5-upravlenie-potokom}


#### Условные операторы
```zc
if x > 10 {
    print "Large";
} else if x > 5 {
    print "Medium";
} else {
    print "Small";
}

// Тернарно
let y = x > 10 ? 1 : 0;

// If-выражение (для сложных условий)
let категория = if (x > 100) { "огромный" } else if (x > 10) { "большой" } else { "маленький" };
```

#### Сопоставление с образцом
Мощная альтернатива `switch`.
```zc
match val {
    1         => { print "One" },
    2 || 3    => { print "Two or Three" },    // ИЛИ с ||
    4 or 5    => { print "Four or Five" },    // ИЛИ с 'or'
    6, 7, 8   => { print "Six to Eight" },    // ИЛИ с запятой
    10 .. 15  => { print "10 to 14" },        // Исключающий диапазон (устаревший)
    10 ..< 15 => { print "10 to 14" },        // Исключающий диапазон (явно)
    20 ..= 25 => { print "20 to 25" },        // Включающий диапазон
    _         => { print "Other" },
}

// Деструктуризация перечислений
match shape {
    Shape::Circle(r)   => { println "Radius: {r}" },
    Shape::Rect(w, h)  => { println "Area: {w*h}" },
    Shape::Point       => { println "Point" },
}
```

#### Привязка ссылок
Чтобы проверить значение без передачи владения (перемещения), используйте ключевое слово `ref` в паттерне. Это необходимо для типов, которые реализуют Move Semantics (такие как `Option`, `Result`, структуры без Copy).

```zc
let opt = Some(NonCopyVal{...});
match opt {
    Some(ref x) => {
        // 'x' - это указатель на значение внутри 'opt'
        // 'opt' НЕ перемещается/не потребляется здесь
        println "{x.field}"; 
    },
    None => {}
}
```

#### Циклы
```zc
// Диапазон
for i in 0..10 { ... }      // Исключительно (0 до 9)
for i in 0..<10 { ... }     // Исключительно (явно)
for i in 0..=10 { ... }     // Включительно (0 до 10)
for i in 0..10 step 2 { ... }
for i in 10..0 step -1 { ... }  // Descending loop

// Итератор (Vec или пользовательский Iterable)
for item in vec { ... }

// Нумерованный: получить индекс и значение
for i, val in arr { ... }       // i = 0, 1, 2, ...
for i, val in 0..10 step 2 { ... } // i = 0, 1, 2, ...; val = 0, 2, 4, ...

// Итерация по массивам фиксированного размера напрямую
let arr: int[5] = [1, 2, 3, 4, 5];
for val in arr {
    // val - это int
    println "{val}";
}

// While
while x < 10 { ... }

// Бесконечный цикл с меткой
outer: loop {
    if done { break outer; }
}

// Повторить N раз
for _ in 0..5 { ... }
```

#### Продвинутое управление
```zc
// Guard: выполнить else и вернуться, если условие ложно
guard ptr != NULL else { return; }

// Unless: если не верно
unless is_valid { return; }
```

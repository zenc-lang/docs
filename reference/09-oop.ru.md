+++
title = "9. Объектно-ориентированное программирование"
weight = 9
+++

# 9. Объектно-ориентированное программирование


#### Методы
Определяйте методы на типах с помощью `impl`.
```zc
impl Point {
    // Статический метод (соглашение конструктора)
    fn new(x: int, y: int) -> Self {
        return Point{x: x, y: y};
    }

    // Метод экземпляра
    fn dist(self) -> float {
        return sqrt(self.x * self.x + self.y * self.y);
    }
}
```

**Сокращение self**: В методах с параметром `self` можно использовать `.поле` как сокращение для `self.поле`:
```zc
impl Point {
    fn dist(self) -> float {
        return sqrt(.x * .x + .y * .y);  // Эквивалентно self.x, self.y
    }
}
```

#### Методы примитивных типов
Zen C позволяет определить методы на примитивных типах (например, `int`, `bool`, и т.д.) с помощью той же синтаксиса `impl`.

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

#### Трейты
Определяйте общее поведение.
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

#### Стандартные трейты
Zen C включает стандартные трейты, которые интегрируются с синтаксисом языка.

**Iterable**

Реализуйте `Iterable<T>` для включения циклов `for-in` для ваших пользовательских типов.

```zc
import "std/iter.zc"

// Определите итератор
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

// Реализуйте Iterable
impl MyRange {
    fn iterator(self) -> MyIter {
        return MyIter{curr: self.start, stop: self.end};
    }
}

// Используйте в цикле
for i in my_range {
    println "{i}";
}
```

**Drop**

Реализуйте `Drop` для определения деструктора, который запускается при выходе объекта из области видимости (RAII).

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
Если переменная перемещена, `drop` не вызывается для оригинала. Подробнее в [семантике ресурсов](@/tour/08-memory-management.ru.md#semantika-resursov-move-po-umolchaniiu).
{% end %}

**Copy**

Маркерный трейт для выбора поведения `Copy` (неявное дублирование) вместо Move семантики. Используется через `@derive(Copy)`.

{% alert(type="caution") %}
Типы, которые реализуют `Copy`, не должны определять деструктор (`Drop`).
{% end %}

```zc
@derive(Copy)
struct Point { x: int; y: int; }

fn main() {
    let p1 = Point{x: 1, y: 2};
    let p2 = p1; // Скопирована! p1 остаётся допустимой.
}
```

**Clone**

Реализуйте `Clone` для разрешения явного дублирования типов, владеющих ресурсами.

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
    let b2 = b1.clone(); // Явное копирование
}
```

#### Композиция
Используйте `use` для встраивания других структур. Вы можете либо смешивать их (уплощение полей), либо давать им названия (вложение полей).

```zc
struct Entity { id: int; }

struct Player {
    // Миксин (без имени): уплощает поля
    use Entity;  // добавляет 'id' в Player напрямую
    name: string;
}

struct Match {
    // Композиция (с именем): вложение полей
    use p1: Player; // доступ через match.p1
    use p2: Player; // доступ через match.p2
}
```

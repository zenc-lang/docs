+++
title = "17. Правила MISRA"
weight = 17
+++

# 17. Правила MISRA

Zen C включает **режим соответствия MISRA C:2012**, активируемый флагом `--misra`.
В дополнение к стандартным проверкам MISRA, компилятор применяет несколько **специфичных для Zen правил**,
которые способствуют созданию более безопасного и удобного в сопровождении кода.

#### Включение режима MISRA

```bash
zc build app.zc --misra
```

Нарушения выводятся как ошибки компилятора на этапе компиляции:

```text
error: MISRA Rule Zen 2.2: tuple with 3 or more fields shall be replaced
       with a named struct (use 'struct' instead of positional tuple)
  --> app.zc:5:1
   |
 5 | fn get_stats() -> (int, int, int) { ... }
```

{% alert(type="note") %}
Текст стандарта MISRA защищён авторским правом MISRA Consortium Ltd. Реализация Zen C
проверяет соответствие, но не воспроизводит стандарт. Официальные определения правил
см. в документации [MISRA C:2012](https://www.misra.org.uk/).
{% end %}

#### Специфичные правила Zen

Эти правила уникальны для Zen C. Каждое правило проверяется, когда активен `--misra`.

#### Zen 1.1 -- Запрет блоков raw

Запрещает блоки `raw { }`, которые обходят транспилятор.

```zc
// Bad:
fn main() {
    raw { int x = 10; }
}

// Good:
fn main() {
    let x = 10;
}
```

#### Zen 1.2 -- Запрет блоков plugin

Запрещает блоки `plugin ... end`, которые выполняют произвольный код на этапе сборки.

```zc
// Bad:
plugin my_plugin

// Good:
import "std/some_module.zc"
```

#### Zen 1.3 -- Исчерпывающий match для перечислений

Запрещает подстановочный знак `_` в `match` для типов перечислений -- все варианты должны быть обработаны явно.

```zc
enum Color { Red; Green; Blue; }

// Bad -- missing Blue:
fn describe(c: Color) {
    match c {
        Color::Red => { println "red"; }
        Color::Green => { println "green"; }
    }
}

// Good:
fn describe(c: Color) {
    match c {
        Color::Red => { println "red"; }
        Color::Green => { println "green"; }
        Color::Blue => { println "blue"; }
    }
}
```

#### Zen 1.4 -- Запрет директив препроцессора

Запрещает директивы препроцессора C (`#define`, `#include`, `#if` и т.д.).
Используйте `import` и `def` Zen вместо них.

```zc
// Bad:
#define BUFFER_SIZE 256
#include <stdio.h>

// Good:
def BUFFER_SIZE = 256;
import "std/io.zc"
```

#### Zen 1.5 -- Запрет `var` / `const` для объявлений

Ключевые слова `var` и `const` устарели для объявлений переменных/констант.
Используйте `let` для переменных и `def` для констант времени компиляции.

```zc
// Bad:
var x = 10;
const MAX = 100;

// Good:
let x = 10;
def MAX = 100;
```

> `const` остаётся допустимым как **квалификатор типа** для взаимодействия с C
> (например, `const int` в объявлениях FFI).

#### Zen 1.8 -- Запрет затенения идентификаторов

Запрещает объявление имени, которое скрывает имя из внешней области видимости.

```zc
let x = 10;
if true {
    // Bad -- shadows outer x:
    let x = 20;
}

// Good:
if true {
    let inner_x = 20;
}
```

#### Zen 2.1 -- Запрет зарезервированных идентификаторов

Запрещает идентификаторы, начинающиеся с `__`, `_[A-Z]` или `_z_`, которые зарезервированы
для компилятора и реализации C.

```zc
// Bad:
let __my_var = 10;
let _Reserved = 20;
let _z_internal = 30;

// Good:
let my_var = 10;
let reserved = 20;
let internal = 30;
```

#### Zen 2.2 -- Ограничение размера кортежей

Кортежи с **3 и более полями** не должны использоваться в качестве возвращаемых типов или
параметров функций. Используйте именованную структуру. 2-кортежи исключены.

```zc
// Bad -- 3-tuple as return type:
fn get_stats() -> (int, int, int) { ... }
fn process(p: (int, string, bool)) { ... }

// Good -- use a struct:
struct Stats { sum: int; avg: int; max: int; }
fn get_stats() -> Stats { ... }

// OK -- 2-tuples are exempt:
fn get_pair() -> (int, int) { ... }
```

#### Zen 2.3 -- Сравнение строк

`string == string` не должно использоваться. Используйте `strcmp()` вместо этого.

```zc
// Bad (when a, b are string):
if a == b { ... }

// Good:
if strcmp(a, b) == 0 { ... }

// OK -- int, bool, pointer comparisons are safe:
if x == y { ... }
```

## Охват стандарта MISRA C:2012

Компилятор проверяет следующие стандартные правила MISRA C:2012.
Нажмите на главу, чтобы развернуть список правил.

{% misra_table() %}

Полный текст правил см. в официальной документации
[MISRA C:2012](https://www.misra.org.uk/).

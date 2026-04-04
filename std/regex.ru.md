# std/regex

Модуль `std/regex` обеспечивает поддержку регулярных выражений на основе POSIX-стандарта `regex.h`.

## Использование

```zc
import "std/regex.zc"

fn main() {
    if regex_match("^[a-z]+$", "привет") {
        println "Соответствует!";
    }
    
    let re = Regex::compile("\\d+");
    let count = re.count("123 abc 456");
    re.destroy();
}
```

## Определения структур

### `Regex`

Представляет скомпилированное регулярное выражение.

```zc
struct Regex {
    // Внутренние поля
}
```

### `Match`

Представляет успешное совпадение.

```zc
struct Match {
    text: char*;
    start: int;
    len: int;
}
```

## Методы

### Работа с Regex

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **compile** | `Regex::compile(pattern: char*) -> Regex` | Компилирует выражение с флагами по умолчанию. |
| **compile_with_flags** | `Regex::compile_with_flags(pattern: char*, flags: int) -> Regex` | Компилирует выражение с пользовательскими POSIX-флагами. |
| **destroy** | `destroy(self)` | Освобождает скомпилированное выражение. |

### Поиск и сопоставление

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **match** | `match(self, text: char*) -> bool` | Возвращает true, если шаблон найден в тексте. |
| **find** | `find(self, text: char*) -> Option<Match>` | Находит первое совпадение, включая позицию и длину. |
| **count** | `count(self, text: char*) -> int` | Возвращает количество неперекрывающихся совпадений. |
| **split** | `split(self, text: char*) -> Vec<String>` | Разделяет текст по шаблону. |

### Доступ к результатам

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **as_string** | `as_string(self) -> char*` | Возвращает указатель на начало совпадения. |
| **end** | `end(self) -> int` | Возвращает индекс сразу за последним символом совпадения. |

### Статические утилиты

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **regex_match** | `regex_match(pattern: char*, text: char*) -> bool` | Быстрая проверка на соответствие. |
| **regex_find** | `regex_find(pattern: char*, text: char*) -> Option<Match>` | Находит первое совпадение. |
| **regex_count** | `regex_count(pattern: char*, text: char*) -> int` | Считает все совпадения. |
| **regex_split** | `regex_split(pattern: char*, text: char*) -> Vec<String>` | Разделяет текст по шаблону. |
走
走
走
走
走
走
走
走
走
走

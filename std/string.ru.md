# std/string

`String` — это тип строки, размещаемой в куче (heap) и имеющей динамически изменяемый размер. Является оберткой над `Vec<char>` и гарантирует наличие нулевого терминатора для совместимости с C.

## Использование

```zc
import "std/string.zc"

fn main() {
    let s = String::from("Привет");

    // Для добавления нужен указатель на другую String
    let part = String::from(" Мир");
    s.append(&part);
    
    // Итерация (поддержка UTF-8)
    for c in s {
        println "{c}";
    }

    // Используйте c_str() для вывода
    println "{s.c_str()}"; // Выведет "Привет Мир"
    
    if (s.starts_with("Привет")) {
        // ...
    }
} // s освобождается автоматически здесь
```

## Определение структуры

```zc
struct String {
    vec: Vec<char>;
}
```

## Методы

### Создание

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **new** | `String::new(s: char*) -> String` | Создает новую String из C-строки. |
| **from** | `String::from(s: char*) -> String` | Псевдоним для `new`. |
| **from_rune** | `String::from_rune(r: rune) -> String` | Создает новую String из одного символа `rune`. |
| **from_runes** | `String::from_runes(runes: rune*, count: usize) -> String` | Создает String из массива `runes`. |

### Модификация

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **append** | `append(self, other: String*)` | Добавляет другую строку к текущей. |
| **append_c** | `append_c(self, s: char*)` | Добавляет C-строку. |
| **push_rune** | `push_rune(self, r: rune)` | Добавляет один Unicode-символ (`rune`) в конец. |
| **clear** | `clear(self)` | Очищает строку. |

### Доступ и свойства

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **c_str** | `c_str(self) -> char*` | Возвращает указатель на внутреннюю C-строку. |
| **length** | `length(self) -> usize` | Возвращает длину строки (без нулевого терминатора). |
| **is_empty** | `is_empty(self) -> bool` | Возвращает true, если длина равна 0. |
| **starts_with** | `starts_with(self, prefix: char*) -> bool` | Проверяет, начинается ли строка с указанного префикса. |
| **substring** | `substring(self, start: usize, len: usize) -> String` | Возвращает новую подстроку. |

### Поддержка UTF-8

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **utf8_len** | `utf8_len(self) -> usize` | Возвращает количество Unicode-символов. |
| **runes** | `runes(self) -> Vec<rune>` | Возвращает вектор всех Unicode-символов строки. |

## Управление памятью

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **free** | `free(self)` | Вручную освобождает память строки. |
| **Trait** | `impl Drop for String` | Автоматически вызывает `free()` при выходе из области видимости. |
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

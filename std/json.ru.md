# std/json

Модуль `std/json` предоставляет высокоуровневый API для парсинга, генерации и манипуляции данными в формате JSON.

## Обзор

- **Парсинг**: Преобразование строк JSON в древовидную структуру `JsonValue`.
- **Сериализация**: Генерация строк JSON из объектов `JsonValue`.
- **Удобная навигация**: Доступ к полям объектов и элементам массивов.
- **Обработка ошибок**: Подробные сообщения об ошибках парсинга с указанием позиции.

## Использование

```zc
import "std/json.zc"

fn main() {
    let raw = "{\"имя\": \"Zen\", \"версия\": 1}";
    
    // Парсинг JSON
    match Json::parse(raw) {
        Ok(json) => {
            println "Имя: {json.get(\"имя\").as_string()}";
            // json освобождается автоматически через Drop
        },
        Err(e) => println "Ошибка: {e}"
    }

    // Создание JSON
    let obj = JsonValue::object();
    obj.set("статус", JsonValue::string("ок"));
    println "Вывод: {obj.stringify()}";
}
```

## Типы данных (`JsonValue`)

Тип `JsonValue` представляет собой объединение (enum) для всех типов JSON:

| Тип | Проверка | Получение значения |
| :--- | :--- | :--- |
| **String** | `is_string()` | `as_string() -> char*` |
| **Number** | `is_number()` | `as_double() -> double` |
| **Object** | `is_object()` | `get(key: char*) -> JsonValue*` |
| **Array** | `is_array()` | `at(idx: usize) -> JsonValue*` |
| **Boolean**| `is_bool()` | `as_bool() -> bool` |
| **Null** | `is_null()` | - |

## Методы

### Парсинг и генерация

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **parse** | `Json::parse(s: char*) -> Result<JsonValue>` | Парсит строку JSON. |
| **stringify**| `stringify(self) -> String` | Преобразует `JsonValue` в максимально компактную строку JSON. |
| **pretty** | `pretty(self) -> String` | Преобразует `JsonValue` в форматированную (pretty-print) строку. |

### Манипуляция объектами и массивами

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **set** | `set(self, key: char*, val: JsonValue)` | Устанавливает поле в объекте. |
| **push** | `push(self, val: JsonValue)` | Добавляет элемент в массив. |
| **length** | `length(self) -> usize` | Возвращает количество элементов (для объектов и массивов). |

## Управление памятью

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **free** | `free(self)` | Вручную освобождает все ресурсы `JsonValue` рекурсивно. |
| **Trait** | `impl Drop for JsonValue` | Автоматически вызывает `free()` при выходе из области видимости. |
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

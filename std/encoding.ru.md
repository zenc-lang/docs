# std/encoding

Модуль `std/encoding` предоставляет утилиты для преобразования между различными форматами представления данных, такими как Base64.

## Использование

```zc
import "std/encoding/base64.zc"

fn main() {
    let original = "Zen-C";
    let encoded = Base64::encode(original);
    
    println "Base64: {encoded}"; 
}
```

走
## Base64 (`std/encoding/base64.zc`)

Подмодуль Base64 предоставляет функции для кодирования и декодирования бинарных данных в формат Base64 (RFC 4648).

### Функции

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **encode** | `Base64::encode(input: char*) -> String` | Кодирует C-строку в Base64. |
| **decode** | `Base64::decode(input: char*) -> String` | Декодирует строку Base64 обратно в исходный формат. |

## Другие кодировки

Модуль `std/encoding` также может включать поддержку:
- **Hexadecimal**: Через модуль `std/hex`.
- **JSON**: Через модуль `std/json`.
- **UTF-8**: Через модуль `std/utf8`.
走

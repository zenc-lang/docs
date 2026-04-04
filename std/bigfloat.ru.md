# std/bigfloat

Модуль `std/bigfloat` предоставляет арифметику чисел с плавающей запятой произвольной точности.

## Использование

```zc
import "std/bigfloat.zc"

fn main() {
    let a = BigFloat::from_string("1.2345678901234567890");
    let b = BigFloat::from_int(2);
    
    let c = a.add(&b); 
    println "{c.to_string()}"; 
} // c, b и a освобождаются автоматически здесь
```

## Методы

### Создание

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **new** | `BigFloat::new() -> BigFloat` | Создает новый `BigFloat`, инициализированный нулем. |
| **from_int** | `BigFloat::from_int(v: int) -> BigFloat` | Создает `BigFloat` из целого значения. |
| **from_string** | `BigFloat::from_string(s: char*) -> BigFloat` | Создает `BigFloat` из строкового представления. |

### Арифметические операции

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **add** | `add(self, other: BigFloat*) -> BigFloat` | Складывает два `BigFloat`. |
| **sub** | `sub(self, other: BigFloat*) -> BigFloat` | Вычитает `other` из `self`. |
| **mul** | `mul(self, other: BigFloat*) -> BigFloat` | Перемножает два `BigFloat`. |
| **div** | `div(self, other: BigFloat*) -> BigFloat` | Делит `self` на `other`. |

### Утилиты

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **to_string** | `to_string(self) -> char*` | Возвращает строковое представление `BigFloat`. |

## Управление памятью

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **free** | `free(self)` | Вручную освобождает внутреннюю память. |
| **Trait** | `impl Drop for BigFloat` | Автоматически вызывает `free()`. |
走

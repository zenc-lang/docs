# std/bigint

Модуль `std/bigint` предоставляет арифметику целых чисел произвольной точности (bignums).

## Использование

```zc
import "std/bigint.zc"

fn main() {
    let a = BigInt::from_string("123456789012345678901234567890");
    let b = BigInt::from_int(10);
    
    let c = a.mul(&b);
    println "{c.to_string()}";
} // c, b и a освобождаются автоматически здесь
```

## Методы

### Создание

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **new** | `BigInt::new() -> BigInt` | Создает новый `BigInt`, инициализированный нулем. |
| **from_int** | `BigInt::from_int(v: int) -> BigInt` | Создает `BigInt` из 32-битного значения. |
| **from_long** | `BigInt::from_long(v: long) -> BigInt` | Создает `BigInt` из 64-битного значения. |
| **from_string** | `BigInt::from_string(s: char*) -> BigInt` | Создает `BigInt` из строкового представления. |

### Арифметические операции

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **add** | `add(self, other: BigInt*) -> BigInt` | Складывает два `BigInt`. |
| **sub** | `sub(self, other: BigInt*) -> BigInt` | Вычитает `other` из `self`. |
| **mul** | `mul(self, other: BigInt*) -> BigInt` | Перемножает два `BigInt`. |
| **div** | `div(self, other: BigInt*) -> BigInt` | Делит `self` на `other`. |
| **mod** | `mod(self, other: BigInt*) -> BigInt` | Возвращает остаток от деления. |

### Утилиты

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **to_string** | `to_string(self) -> char*` | Возвращает десятичное строковое представление. |
| **to_hex** | `to_hex(self) -> char*` | Возвращает шестнадцатеричное строковое представление. |

## Управление памятью

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **free** | `free(self)` | Вручную освобождает внутреннюю память. |
| **Trait** | `impl Drop for BigInt` | Автоматически вызывает `free()` при выходе из области видимости. |
走

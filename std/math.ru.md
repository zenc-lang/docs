# std/math

Модуль `std/math` предоставляет стандартные математические константы и функции для работы с числами с плавающей запятой.

## Использование

```zc
import "std/math.zc"

fn main() {
    let r = 5.0;
    let area = PI * Math::pow(r, 2.0);
    
    println "Площадь: {area}"; 
    println "Квадратный корень из 16: {Math::sqrt(16.0)}";
}
```

## Константы

| Имя | Значение | Описание |
| :--- | :--- | :--- |
| **PI** | 3.14159265... | Число Пи. |
| **E** | 2.71828182... | Число Эйлера. |
| **SQRT2** | 1.41421356... | Квадратный корень из 2. |

## Функции

### Основные операции

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **abs** | `Math::abs(v: double) -> double` | Абсолютная величина. |
| **sqrt** | `Math::sqrt(v: double) -> double` | Квадратный корень. |
| **pow** | `Math::pow(base: double, exp: double) -> double` | Возведение в степень. |
| **exp** | `Math::exp(v: double) -> double` | Экспонента (e^v). |
| **log** | `Math::log(v: double) -> double` | Натуральный логарифм. |

### Тригонометрия

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **sin** | `Math::sin(rad: double) -> double` | Синус (в радианах). |
| **cos** | `Math::cos(rad: double) -> double` | Косинус (в радианах). |
| **tan** | `Math::tan(rad: double) -> double` | Тангенс (в радианах). |
| **asin** | `Math::asin(v: double) -> double` | Арксинус. |
| **acos** | `Math::acos(v: double) -> double` | Арккосинус. |
| **atan2**| `Math::atan2(y: double, x: double) -> double` | Арктангенс от y/x. |

### Округление

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **ceil** | `Math::ceil(v: double) -> double` | Округление вверх. |
| **floor**| `Math::floor(v: double) -> double` | Округление вниз. |
| **round**| `Math::round(v: double) -> double` | Округление к ближайшему целому. |
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

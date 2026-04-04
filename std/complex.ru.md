# std/complex

Модуль `std/complex` предоставляет поддержку арифметики комплексных чисел двойной точности.

## Использование

```zc
import "std/complex.zc"

fn main() {
    let z1 = Complex::new(1.0, 2.0); // 1 + 2i
    let z2 = Complex::new(3.0, 4.0); // 3 + 4i
    
    let sum = z1.add(z2); 
    println "Результат: {sum.real} + {sum.imag}i";
}
```

## Определение структуры

```zc
struct Complex {
    real: double;
    imag: double;
}
```

## Методы

### Создание

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **new** | `Complex::new(re: double, im: double) -> Complex` | Создает новое комплексное число. |

### Арифметические операции

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **add** | `add(self, other: Complex) -> Complex` | Складывает два комплексных числа. |
| **sub** | `sub(self, other: Complex) -> Complex` | Вычитает `other` из `self`. |
| **mul** | `mul(self, other: Complex) -> Complex` | Перемножает два комплексных числа. |
| **div** | `div(self, other: Complex) -> Complex` | Делит `self` на `other`. |

### Математические функции

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **abs** | `abs(self) -> double` | Вычисляет модуль (абсолютную величину). |
| **arg** | `arg(self) -> double` | Вычисляет аргумент (фазу). |
| **conj** | `conj(self) -> Complex` | Возвращает комплексно-сопряженное число. |
| **exp** | `exp(self) -> Complex` | Вычисляет комплексную экспоненту. |
| **sqrt** | `sqrt(self) -> Complex` | Вычисляет комплексный квадратный корень. |
走

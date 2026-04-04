# std/mem

Модуль `std/mem` предоставляет низкоуровневые примитивы для прямого управления памятью в Zen-C.

## Использование

```zc
import "std/mem.zc"

fn main() {
    // Выделение памяти под 10 целых чисел
    let ptr = mem_alloc(10 * sizeof(int));
    
    // Инициализация нулями
    mem_set(ptr, 0, 10 * sizeof(int));
    
    mem_free(ptr);
}
```

## Функции аллокации

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **mem_alloc** | `mem_alloc(size: usize) -> void*` | Выделяет блок памяти указанного размера. |
| **mem_calloc**| `mem_calloc(count: usize, size: usize) -> void*` | Выделяет обнуленную память для массива. |
| **mem_realloc**| `mem_realloc(ptr: void*, size: usize) -> void*` | Изменяет размер ранее выделенного блока. |
| **mem_free** | `mem_free(ptr: void*)` | Освобождает блок памяти. Безопасно для `null`. |

## Манипуляции с памятью

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **mem_copy** | `mem_copy(dst: void*, src: void*, size: usize)` | Копирует блок памяти. Перекрывающиеся области не поддерживаются. |
| **mem_move** | `mem_move(dst: void*, src: void*, size: usize)` | Копирует блок памяти. Безопасно для перекрывающихся областей. |
| **mem_set** | `mem_set(ptr: void*, value: int, size: usize)` | Заполняет блок памяти байтом `value`. |
| **mem_cmp** | `mem_cmp(s1: void*, s2: void*, size: usize) -> int` | Сравнивает два блока памяти. |

## Утилиты

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **sizeof** | `sizeof(type T) -> usize` | Встроенный макрос для получения размера типа в байтах. |
| **alignof** | `alignof(type T) -> usize` | Возвращает требования к выравниванию для указанного типа. |
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

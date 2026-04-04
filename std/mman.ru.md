# std/sys/mman

Модуль `std/sys/mman` предоставляет доступ к функциям управления виртуальной памятью POSIX, включая отображение файлов в память (memory-mapped files).

## Обзор

- **Отображение памяти (mmap)**: Отображает файлы или устройства в адресное пространство процесса.
- **Управление защитой**: Установка прав доступа (чтение, запись, выполнение) для страниц памяти.
- **Синхронизация**: Сброс изменений в отображенной памяти обратно в файл с помощью `msync`.

## Использование

```zc
import "std/sys/mman.zc"
import "std/fs.zc"

fn main() {
    let f = File::open("data.bin").unwrap();
    let size = 4096;
    
    // Отображение файла в память
    let ptr = Mman::mmap(null, size, PROT_READ | PROT_WRITE, MAP_SHARED, f.fd, 0);
    
    if (ptr != MAP_FAILED) {
        // Доступ к данным файла через указатель ptr
        Mman::munmap(ptr, size);
    }
}
```

## Константы защиты (Prot)

| Константа | Описание |
| :--- | :--- |
| **PROT_READ** | Страница доступна для чтения. |
| **PROT_WRITE** | Страница доступна для записи. |
| **PROT_EXEC** | Страница доступна для выполнения. |
| **PROT_NONE** | Доступ к странице запрещен. |

## Методы

| Метод | Сигнатура | Описание |
| :--- | :--- | :--- |
| **mmap** | `Mman::mmap(addr: void*, len: usize, prot: int, flags: int, fd: int, offset: i64) -> void*` | Создает новое отображение в памяти. |
| **munmap** | `Mman::munmap(addr: void*, len: usize) -> int` | Удаляет отображение для указанного диапазона. |
| **mprotect**| `Mman::mprotect(addr: void*, len: usize, prot: int) -> int` | Изменяет права доступа для страниц памяти. |
| **msync** | `Mman::msync(addr: void*, len: usize, flags: int) -> int` | Синхронизирует отображение с файлом на диске. |
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

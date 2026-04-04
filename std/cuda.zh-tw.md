# std/cuda

`std/cuda` 模組提供對 NVIDIA CUDA 的绑定，允許直接在 Zen-C 中進行 GPU 加速計算。

## 使用

```zc
import "std/cuda.zc"

fn main() {
    // 初始化 CUDA 運行時
    if (Cuda::init() != 0) {
        println "CUDA 初始化失敗";
        return;
    }
    
    let device_count = Cuda::get_device_count();
    println "找到 {device_count} 個 CUDA 設備";
}
```

## 設備管理

| 方法 | 簽名 | 描述 |
| :--- | :--- | :--- |
| **init** | `Cuda::init() -> int` | 初始化 CUDA 驅動程序。 |
| **get_device_count**| `Cuda::get_device_count() -> int` | 返回可用 GPU 的數量。 |
| **set_device** | `Cuda::set_device(id: int)` | 選擇要使用的 GPU。 |

## 内存管理

| 方法 | 簽名 | 描述 |
| :--- | :--- | :--- |
| **alloc** | `Cuda::alloc(size: usize) -> void*` | 在 GPU 顯存上分配內存。 |
| **free** | `Cuda::free(ptr: void*)` | 釋放 GPU 內存。 |
| **copy_to_device** | `Cuda::copy_to(dst: void*, src: void*, n: usize)` | 將數據從主機 (RAM) 複製到設備 (VRAM)。 |
| **copy_to_host** | `Cuda::copy_from(dst: void*, src: void*, n: usize)`| 將數據從設備 (VRAM) 複製到主機 (RAM)。 |

走
> [!IMPORTANT]
> 使用此模組需要安裝 NVIDIA 驅動程序和 CUDA 工具包。
走

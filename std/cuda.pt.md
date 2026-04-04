# std/cuda

O módulo `std/cuda` fornece uma interface Zen-C para computação acelerada por GPU utilizando a plataforma NVIDIA CUDA.

## Visão Geral

- **Gerenciamento de Dispositivos**: Enumeração e seleção de GPUs CUDA.
- **Gerenciamento de Memória**: Alocação e transferência de dados entre o Host (CPU) e o Dispositivo (GPU).
- **Lançamento de Kernels**: Execução de código paralelo em milhares de cores da GPU.

## Uso

```zc
import "std/cuda.zc"

fn main() {
    // Inicializar dispositivo
    Cuda::init(0);
    
    // Alocar memória na GPU
    let d_ptr = Cuda::malloc(1024);
    
    // Transferir dados para a GPU
    let h_data: float[256];
    Cuda::memcpy_to_device(d_ptr, &h_data[0], 1024);
    
    // Configurar e lançar kernel (pseudocódigo)
    // kernel<<<blocks, threads>>>(d_ptr);
    
    Cuda::free(d_ptr);
}
```

## Métodos

### Gerenciamento de Dispositivos

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **init** | `Cuda::init(device_id: int) -> Result<bool>` | Inicializa o driver CUDA para o dispositivo especificado. |
| **get_device_count**| `Cuda::get_device_count() -> int` | Retorna o número de dispositivos CUDA disponíveis. |

### Memória do Dispositivo

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **malloc** | `Cuda::malloc(size: usize) -> void*` | Aloca memória linear no dispositivo. |
| **free** | `Cuda::free(ptr: void*)` | Liberta memória alocada no dispositivo. |
| **memcpy_to_device** | `Cuda::memcpy_to_device(dst: void*, src: void*, size: usize)` | Copia dados do host para o dispositivo. |
| **memcpy_to_host** | `Cuda::memcpy_to_host(dst: void*, src: void*, size: usize)` | Copia dados do dispositivo para o host. |

## Tratamento de Erros

A maioria das funções do `std/cuda` retorna um tipo `Result` ou define um código de erro global que pode ser verificado através de `Cuda::get_last_error()`.
走

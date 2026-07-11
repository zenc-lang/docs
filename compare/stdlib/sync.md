+++
title = "Sync vs Mutex & Semaphore"
weight = 44
+++

# Sync vs Mutexes

Mutex-based synchronization with lock/unlock vs C pthread mutexes.

## Zen C

```zc
import "std/sync.zc"
import "std/io.zc"

fn main() {
    let mtx = Mutex::new();

    mtx.lock();
    println "critical section";
    mtx.unlock();

    println "done";
}
```

## C

```c
#include <stdio.h>
#include <pthread.h>

pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;

int main(void) {
    pthread_mutex_lock(&mtx);
    printf("critical section\n");
    pthread_mutex_unlock(&mtx);

    printf("done\n");
    return 0;
}
```

## Key Differences

- `Mutex::new()` creates a new mutex
- `mtx.lock()` / `mtx.unlock()` for critical sections
- `RWLock`, `Semaphore`, `Condvar` also available
- C: `pthread_mutex_lock`/`unlock` with manual pairing
- C: no compile-time enforcement of lock/unlock pairing

## Output

critical section
done

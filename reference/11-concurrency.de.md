+++
title = "11. Nebenläufigkeit (Async/Await)"
weight = 11
+++

# 11. Nebenläufigkeit (Async/Await) {#11-nebenlaufigkeit-asyncawait}


Basierend auf pthreads.

```zc
async fn fetch_data() -> string {
    // Läuft im Hintergrund
    return "Daten";
}

fn main() {
    let future = fetch_data();
    let result = await future;
}
```

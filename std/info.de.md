# std/sys/info

Das Modul `std/sys/info` bietet Hilfsprogramme zum Abrufen von Systemidentifikationen und -informationen und kapselt POSIX `uname`.

## Überblick

- **Systemidentifikation**: Zugriff auf OS-Name, Kernel-Version, Hardware-Architektur und mehr.
- **RAII-Konformität**: Die Struktur `Uname` verwaltet den Speicher für ihre internen Strings automatisch.

## Verwendung

```zc
import "std/sys/info.zc"
import "std/io.zc"

fn main() {
    let info = SysInfo::get_uname();
    println "BS: {info.sysname}";
    println "Kernel: {info.release}";
    println "Architektur: {info.machine}";
}
```

## Struktur-Definition

### `Uname`
Enthält Systemidentifikationsfelder.
```zc
struct Uname {
    sysname: String;
    nodename: String;
    release: String;
    version: String;
    machine: String;
}
```

## Methoden

### `SysInfo` Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **get_uname** | `SysInfo::get_uname() -> Uname` | Gibt eine `Uname`-Struktur zurück, die verschiedene System-Strings enthält. |

## Speicherverwaltung
- `Uname` implementiert `impl Drop` und gibt seine internen `String`-Puffer automatisch frei, wenn es den Gültigkeitsbereich verlässt.

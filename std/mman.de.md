# std/sys/mman

Das Modul `std/sys/mman` bietet eine Zen-C-Schnittstelle für Speicherzuordnungs- und Schutzfunktionen und kapselt POSIX `sys/mman.h`.

## Überblick

- **Speicherzuordnung**: Ordnet Dateien oder anonymen Speicher dem Adressraum des Prozesses zu.
- **Schutzsteuerung**: Dynamisches Ändern der Berechtigungen für Speicherbereiche (Lesen, Schreiben, Ausführen).
- **Anonymer Speicher**: Allokiert große Speicherblöcke direkt vom Betriebssystem ohne Datei-Bezug.

## Verwendung

```zc
import "std/sys/mman.zc"
import "std/io.zc"

fn main() {
    let size: usize = 4096;
    let prot = Z_PROT_READ | Z_PROT_WRITE;
    let flags = Z_MAP_PRIVATE | Z_MAP_ANONYMOUS;
    
    let addr = Memory::mmap(size, prot, flags);
    if ((isize)addr == Z_MAP_FAILED) {
        println "Zuordnung fehlgeschlagen";
        return;
    }
    
    // Speicher verwenden...
    
    Memory::munmap(addr, size);
}
```

## Struktur-Definition

```zc
struct Memory {}
```

## Methoden

### `Memory` Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **mmap** | `Memory::mmap(len: usize, prot: int, flags: int) -> void*` | Erstellt eine neue Zuordnung im virtuellen Adressraum des aufrufenden Prozesses. |
| **munmap** | `Memory::munmap(addr: void*, len: usize) -> bool` | Löscht die Zuordnungen für den angegebenen Adressbereich. Gibt `true` bei Erfolg zurück. |
| **mprotect** | `Memory::mprotect(addr: void*, len: usize, prot: int) -> bool` | Ändert den Zugriffsschutz für die Speicherseiten des aufrufenden Prozesses. Gibt `true` bei Erfolg zurück. |

## Konstanten

### Schutz-Flags
- `Z_PROT_NONE`: Seite kann nicht zugegriffen werden.
- `Z_PROT_READ`: Seite kann gelesen werden.
- `Z_PROT_WRITE`: Seite kann beschrieben werden.
- `Z_PROT_EXEC`: Seite kann ausgeführt werden.

### Sichtbarkeits-Flags
- `Z_MAP_SHARED`: Diese Zuordnung teilen.
- `Z_MAP_PRIVATE`: Eine private Copy-on-Write-Zuordnung erstellen.
- `Z_MAP_ANONYMOUS`: Die Zuordnung ist nicht durch eine Datei gedeckt.

### Fehlerwerte
- `Z_MAP_FAILED`: Wird von `mmap` im Fehlerfall zurückgegeben.

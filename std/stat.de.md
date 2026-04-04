# std/sys/stat

Das Modul `std/sys/stat` bietet eine Schnittstelle zum Abrufen erweiterter Dateimetadaten und Statusinformationen und kapselt POSIX `sys/stat.h` ein.

## Überblick

- **Dateimetadaten**: Abrufen von Dateigröße, Modus (Berechtigungen) und Zeitstempeln.
- **Zeitstempel**: Zugriff auf Zugriffs-, Modifikations- und Änderungszeiten als Unix-Zeitstempel.
- **Typenprüfung**: Hilfsmethoden zur Feststellung, ob ein Modus eine Datei oder ein Verzeichnis darstellt.

## Verwendung

```zc
import "std/sys/stat.zc"
import "std/io.zc"

fn main() {
    let res = FileStat::stat("myfile.txt");
    if (res.is_some()) {
        let st = res.unwrap();
        println "Größe: {st.size} Bytes";
        println "Berechtigungen: {st.mode}";
        
        if (FileStat::is_dir(st.mode)) {
            println "Es ist ein Verzeichnis.";
        }
    }
}
```

## Struktur-Definition

### `Stat`
Enthält Dateimetadaten im Unix-Stil.
```zc
struct Stat {
    mode: u32;
    size: u64;
    atime: i64;
    mtime: i64;
    ctime: i64;
    uid: u32;
    gid: u32;
}
```

## Methoden

### `FileStat` Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **stat** | `FileStat::stat(path: char*) -> Option<Stat>` | Gibt Metadaten für den angegebenen Pfad zurück, oder `None` im Fehlerfall. |
| **is_dir** | `FileStat::is_dir(mode: u32) -> bool` | Prüft, ob der angegebene Modus ein Verzeichnis darstellt. |
| **is_file** | `FileStat::is_file(mode: u32) -> bool` | Prüft, ob der angegebene Modus eine reguläre Datei darstellt. |

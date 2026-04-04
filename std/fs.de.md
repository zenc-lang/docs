# std/fs

Das Modul `std/fs` bietet eine umfassende API für die Interaktion mit dem Dateisystem, einschließlich Datei-E/A, Verzeichnismanipulation und Metadatenabruf.

## Überblick

- **Sichere Handles**: Die Struktur `File` bietet einen sicheren Wrapper um rohe Datei-Handles.
- **RAII**: Datei-Handles werden automatisch geschlossen, wenn sie über das `Drop`-Trait den Gültigkeitsbereich verlassen.
- **Fehlerbehandlung**: Verwendet `Result<T>` für alle fehlgeschlagenen Operationen und bietet beschreibende Fehlermeldungen.
- **Komfort**: Enthält statische Methoden für häufige Aufgaben wie das Lesen oder Schreiben einer gesamten Datei in einem Aufruf.

## Verwendung

```zc
import "std/fs.zc"

fn main() {
    // Grundlegendes Dateilesen mit RAII
    match File::read_all("config.txt") {
        Ok(content) => println "Konfiguration: {content}",
        Err(e) => println "Fehler beim Lesen der Konfiguration: {e}"
    }
    
    // Explizites Datei-Handle mit automatischem Schließen
    match File::open("data.log", "a") {
        Ok(file) => {
            file.write_string("Log-Eintrag\n");
            // Datei wird hier automatisch geschlossen
        }
        Err(e) => println "Fehler beim Öffnen des Logs: {e}"
    }
}
```

## Struktur-Definitionen

### `File`
Repräsentiert ein geöffnetes Datei-Handle.
```zc
struct File {
    handle: void*;
}
```

### `Metadata`
Datei- oder Verzeichnismetadaten.
```zc
struct Metadata {
    size: U64;
    is_dir: bool;
    is_file: bool;
}
```

### `DirEntry`
Repräsentiert einen Eintrag in einem Verzeichnis.
```zc
struct DirEntry {
    name: String;
    is_dir: bool;
}
```

## Methoden

### Öffnen / Schließen

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **open** | `File::open(path: char*, mode: char*) -> Result<File>` | Öffnet eine Datei unter `path` mit `mode`. |
| **close** | `close(self)` | Schließt das Datei-Handle explizit. |

### Lesen / Schreiben

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **read_to_string** | `read_to_string(self) -> Result<String>` | Liest die gesamte Datei in einen `String`. |
| **read_all** | `File::read_all(path: char*) -> Result<String>` | Statische Hilfsfunktion zum vollständigen Lesen einer Datei. |
| **read_lines** | `File::read_lines(path: char*) -> Result<Vec<String>>` | Statische Hilfsfunktion zum Lesen einer Datei in einen Vektor von Zeilen. |
| **write_string** | `write_string(self, content: char*) -> Result<bool>` | Schreibt einen String in die Datei. |
| **write_lines** | `File::write_lines(path: char*, lines: Vec<String>*) -> Result<bool>` | Statische Hilfsfunktion zum Schreiben eines Vektors von Zeilen in eine Datei. |

### Pfad-Hilfsprogramme

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **exists** | `File::exists(path: char*) -> bool` | Gibt wahr zurück, wenn der Pfad existiert. |
| **current_dir** | `File::current_dir() -> Result<String>` | Gibt den absoluten Pfad des aktuellen Arbeitsverzeichnisses zurück. |
| **metadata** | `File::metadata(path: char*) -> Result<Metadata>` | Ruft Metadaten für den angegebenen Pfad ab. |

### Datei- & Verzeichnisoperationen

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **create_dir** | `File::create_dir(path: char*) -> Result<bool>` | Erstellt ein neues Verzeichnis. |
| **remove_file** | `File::remove_file(path: char*) -> Result<bool>` | Löscht die angegebene Datei. |
| **remove_dir** | `File::remove_dir(path: char*) -> Result<bool>` | Löscht das angegebene Verzeichnis (muss leer sein). |
| **read_dir** | `File::read_dir(path: char*) -> Result<Vec<DirEntry>>` | Gibt eine Liste von Einträgen in einem Verzeichnis zurück. |

## Speicherverwaltung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **Trait** | `impl Drop for File` | Schließt das Datei-Handle automatisch, wenn es den Gültigkeitsbereich verlässt. |

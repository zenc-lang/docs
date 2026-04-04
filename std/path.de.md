# std/path

Das Modul `std/path` bietet plattformübergreifende Hilfsprogramme zur Manipulation von Dateisystempfaden. Es vereinfacht häufige Aufgaben wie das Zusammenfügen von Pfaden, das Extrahieren von Endungen und das Finden von übergeordneten Verzeichnissen.

## Überblick

- **Plattformübergreifend**: Berücksichtigt bei der Manipulation sowohl Vorwärts- als auch Rückwärtsschrägstriche angemessen.
- **Typsicher**: Die Struktur `Path` kapselt Pfadinformationen und unterscheidet sie von regulären Strings.
- **Bequemes Parsing**: Einfaches Extrahieren von Komponenten wie `extension`, `file_name` und `parent`.
- **RAII**: Speicher wird automatisch über das `Drop`-Trait verwaltet.

## Verwendung

```zc
import "std/path.zc"

fn main() {
    let p = Path::new("/home/user");
    let full_path = p.join("docs/file.txt");
    
    println "Vollständiger Pfad: {full_path.c_str()}";
    
    match full_path.extension() {
        Some(ext) => println "Dateiendung: {ext}",
        None => println "Keine Endung gefunden"
    }
} // full_path und p werden hier automatisch freigegeben
```

## Struktur-Definition

```zc
struct Path {
    str: String;
}
```

## Methoden

### Konstruktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `Path::new(s: char*) -> Path` | Erstellt einen neuen `Path` aus einem C-String. |
| **from_string** | `Path::from_string(s: String) -> Path` | Erstellt einen `Path` durch Übernahme des Besitzes eines `String`. |
| **clone** | `clone(self) -> Path` | Gibt eine tiefe Kopie des `Path` zurück. |

### Manipulation

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **join** | `join(self, other: char*) -> Path` | Hängt `other` unter Verwendung des korrekten Verzeichnistrenners an den Pfad an. |

### Parsing

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **extension** | `extension(self) -> Option<String>` | Gibt die Dateiendung zurück (ohne den führenden Punkt), falls vorhanden. |
| **file_name** | `file_name(self) -> Option<String>` | Gibt die letzte Komponente des Pfades zurück. |
| **parent** | `parent(self) -> Option<Path>` | Gibt den Pfad des übergeordneten Verzeichnisses zurück. |

### Zugriff

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **c_str** | `c_str(self) -> char*` | Gibt die zugrunde liegende C-String-Darstellung zurück. |

## Speicherverwaltung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **free** | `free(self)` | Gibt den internen Stringspeicher des Pfades manuell frei. |
| **Trait** | `impl Drop for Path` | Ruft beim Verlassen des Gültigkeitsbereichs automatisch `free()` auf. |

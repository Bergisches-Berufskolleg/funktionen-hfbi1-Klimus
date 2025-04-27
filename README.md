# Python: Funktionen
Funktionen werden verwendet, um Quellcode, der an mehreren Stellen im Programm benötugt wird, nur einmal programmieren zu müssen.

## Definition einer Funktion
Eine Funktion wird mit dem Schlüsselwort *def* gefolgt vom Funktionsnamen und runden Klammern erstellt. Alles was danach eingerückt ist, gehört zur Funktion. **Der Funktionsname sollte immer mit einem Kleinbuchstaben beginnen!** Das machen alle Programmierer so ;)
```
def printText()
    print("Dies ist Inhalt einer Funktion, ")
    print("welche sich über zwei Zeilen erstreckt")
```

## Parameter einer Funktion
Eine Funktion kann beliebig viele Parameter übergeben bekommen. Allerdings sollte man aus Gründen der Übersicht die Anzahl möglichst nicht über zwei gehen lassen
```
def sum(number1, number2):
    print(f"{number1} + {number2} = {number1 + number2}")
```

## Rückgabewert einer Funktion
Eine Funktion kann genau EINEN Wert beliebigen Typs mit Hilfe der Anweisung *return* zurückgeben.
```
def smallerOne(number1, number2):
    if(number1 < number2)
        return number1
    else 
        return number2
```

## Aufruf einer Funktion
Eine Funktion kann aufgerufen werden, indem der Name samt runder Klammern (und Parameterwerte) angegeben wird.
```
printText()     # Gibt den Text (s.o.) aus
sum(2, 4)       # Berechnet das Ergebis der Summe (s.o.)

# Die kleinere der beiden eingegebenen Zahlen wird bestimmt und in smallerNumber gespeichert
num1 = float(input("Geben Zahl 1 ein: ")
num2 = float(input("Geben Zahl 2 ein: ")
smallNumber = smallerOne(num1, num2)    
```

## Aufgabe
Schreiben Sie eine kleine Python Funktion `isLeapYear(year)`, welche
- die übergebene Jahreszahl prüft, ob es sich um ein Schaltjahr handelt
- und True zurückgibt, wenn es ein Schaltjahr ist
- und False zurückgibt, wenn es kein Schaltjahr ist

Erweitern Sie main:
- Der User wird nach einer Jahreszahl gefragt
- Dann erhält der User eine Antwort  
Achtung: Die Funktionalität von main wird nicht automatisch getestet.

### Wann ist ein Jahr ein Schaltjahr?????
- Ist eine Jahreszahl duch 400 teilbar, ist das Jahr ein Schaltjahr!
- Ist das Jahr durch 100 teilbar (aber nicht durch 400), ist das Jahr KEIN Schaltjahr
- Ist das Jahr durch 4 teilbar (aber nicht durch 100 bzw. 400) , ist das Jahr ein Schaltjahr

**Beispiele**
| Jahr | Ergebnis |
|-----------|------------|
| 2000 | Schaltjahr        (durch 400 teilbar) |
| 2100 | Kein Schaltjahr   (durch 100 teilbar, aber nicht 400)|
| 2024 | Schaltjahr        (nur durch 4 teilbar) |
| 1900 | kein Schaltjahr   (durch 100 teilbar, aber nicht 400) |
| 8    | Schaltjahr			|
| 100  | kein Schaltjahr	|

**Achtung**
In der Funktion *isLeapYear(year)* sollte keine Ausgabe stehen. Die Funktion gibt lediglich einen Bool-Wert zurück.

**WICHTIG:** Ändere **NICHT** die anderen Dateien

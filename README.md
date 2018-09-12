# gta5ki

GTA 5 KI in Python

## Vorraussetzungen:

* Python 3.5
* numpy
* opencv
* pandas
* win32api
* Tensorflow
* tflearn
* ctypes

## Für Versionen > V0.3.2:
* Daten sammeln:
```
gta5ki.py record {Fensterbreite} {Fensterhöhe} {Dateiname}
```
* Daten ausgleichen:
```
gta5ki.py balance {Dateiname Trainingsdaten} {Dateiname ausgeglichene Daten}
```
* Neural Network trainieren:
```
gta5ki.py train {Fensterbreite} {Fensterhöhe} {Lernrate} {Epochen} {Dateiname ausgeglichene Daten}
```
* Neural Network testen:
```
gta5ki.py test {Fensterbreite} {Fensterhöhe} {Lernrate} {Epochen}
```

## Für Versionen > V0.6.0:
RUN.bat starten

## WICHTIG! GTA 5 im Fenstermodus in die obere linke Bildschirmecke.

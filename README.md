# gta5ki

GTA 5 KI in Python

## Vorraussetzungen:

* Python 3.5
* numpy
* opencv-python
* pandas
* win32api
* tensorflow
* tflearn
* ctypes

## Anleitung:
1. Neuste Version der KI aus /Versions herunterladen
1. tensorflow installieren
  1. tensorflow cpu: `pip install --upgrade tensorflow` - langsam, nur wenn keine GPU mit CUDA vorhanden ist installieren
  1. tensorflow gpu: `pip install --upgrade tensorflow-gpu` - wesentlich schneller, aber nur mit kompatibler CUDA GPU
  Wichtig: Cuda Development Kit und cuDNN müssen installiert sein! Weiter Infos: [Tensorflow Documentation](https://www.tensorflow.org/install/install_windows)
1. restliche Abhängigkeiten installieren -> siehe Vorraussetzungen
1. ScriptHook V und Nativ Trainer für GTA installieren
1. GTA 5 im Fenstermodus mit einer Auflösung von 960x540 starten (falls Auflösung im Spiel nicht vorhanden, die Konfigurationsdatei anpassen) `C:\Users\{Benutzer}\Documents\Rockstar Games\GTA V\settings.xml`
1. GTA 5 in die obere linke Ecke des Hauptmonitors
1. Native Trainer mit F4 starten (Spieler unverwundbar, Kein Fahrzeugschaden und Zeit fest auf 12 Uhr Mittags stellen)
1. Die KI starten, beginnend bei Daten sammeln im nächsten Punkt:

### Für Versionen > V0.3.2:
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

### Für Versionen > V0.6.0:
RUN.bat starten
__Daten ab Version 0.6.0 nicht mehr ausgleichen!__

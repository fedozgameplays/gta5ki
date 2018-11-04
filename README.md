# gta5ki

GTA 5 KI in Python
Trainieren eines selbstfahrenden Autos mithilfe einen Neural Networks

## Vorraussetzungen:

* Grand Theft Auto V (möglicherweise auch auf andere Spiele anwendbar)
* Python 3.5 oder höher: [Download](https://www.python.org/downloads/release/python-354/)
* Mindestens 8GB RAM, Empfohlen: 16GB oder mehr
* numpy: `pip install numpy`
* opencv: `pip install opencv-python`
* win32api: `pip install pip install pywin32` und `pip install pypiwin32`
* tensorflow: _siehe unten_
* tflearn: `pip install tflearn`
* h5py: `pip install h5py`

## Anleitung:
1. Neuste Version der KI aus /Versions herunterladen
1. tensorflow installieren
   1. tensorflow cpu: `pip install --upgrade tensorflow` - langsam, nur wenn keine GPU mit CUDA vorhanden ist installieren
   1. tensorflow gpu: `pip install --upgrade tensorflow-gpu` - wesentlich schneller, aber nur mit kompatibler CUDA GPU
  Wichtig: Cuda Development Kit und cuDNN müssen installiert sein! Weiter Infos: [Tensorflow Documentation](https://www.tensorflow.org/install/install_windows)
1. restliche Abhängigkeiten installieren -> siehe Vorraussetzungen
1. ScriptHook V und Nativ Trainer für GTA installieren: [Download](http://www.dev-c.com/gtav/scripthookv/)
1. GTA 5 im Fenstermodus mit einer Auflösung von 960x540 starten (falls Auflösung im Spiel nicht vorhanden, die Konfigurationsdatei anpassen `C:\Users\{Benutzer}\Documents\Rockstar Games\GTA V\settings.xml`)
1. GTA 5 in die obere linke Ecke des Hauptmonitors
1. Native Trainer mit F4 starten (Spieler unverwundbar, Kein Fahrzeugschaden und Zeit fest auf 12 Uhr Mittags stellen)
1. Die KI starten, beginnend bei __record.py__ um Trainingsdaten zu sammeln _(Anleitung zum starten unten)_
1. Ungefähr 200k Trainingsdaten sammeln (400 Trainingsdateien)
1. Das Neural Network trainieren mit __train.py__: _(Anleitung zum starten unten)_
   Wichtig: Das Neural Network dauert gerade bei Mittelklassehardware sehr lange zum trainieren!
   Parameter-Hilfe:
   1. Je mehr Epochen, desto länger dauert das trainieren des Neural Networks, es hat aber eine höhere Genauigkeit
   1. Die Lernrate sollte bei `1E-3` liegen
1. Am Schluss das Neural Network testen:
   1. GTA starten wie in den Punkten 5-7 beschrieben
   1. __test.py__ starten _(Anleitung zum starten unten)_, auf den Countdown warten und in das Fenster tabben

### gta5ki starten für Versionen > V0.3.2 und < V0.6.0:
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

### gta5ki starten für Versionen > V0.6.0:
RUN.bat starten
Im Menü die gewünschte Option auswählen!

## Bugs / Verbesserungen / Probleme
* Für Verbesserungen gern ein Pull request öffnen
* Bei Bugs und Problemen einen Issue öffnen

# Viel Spaß beim Probieren!

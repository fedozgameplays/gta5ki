@echo off
goto menu
:menu
echo -- GTA5KI MenÅ --
echo 1. Daten sammeln
echo 2. Daten trainieren
echo 3. Model testen
echo 4. Daten ansehen
echo 5. Beenden
set /p Auswahl=

if "%Auswahl%"=="1" goto record
if "%Auswahl%"=="2" goto train
if "%Auswahl%"=="3" goto test
if "%Auswahl%"=="4" goto open
if "%Auswahl%"=="5" exit
if not "%Auswahl%"=="1;2;3;4;5" goto error

:record
cls
echo Fensterbreite:
set /p width=
cls
echo Fensterhîhe:
set /p height=
cls
echo Dateiname:
set /p filename=
cls
py gta5ki.py record %width% %height% %filename%

:train
cls
py -m pip uninstall tensorflow -y -q
py -m pip install tensorflow-gpu==1.10.0 -q
cls
echo Fensterbreite:
set /p width=
cls
echo Fensterhîhe:
set /p height=
cls
echo Lernrate:
set /p lr=
cls
echo Epochen:
set /p epochs=
cls
echo Dateiname:
set /p filename=
cls
py gta5ki.py train %width% %height% %lr% %epochs% %filename%
pause

:test
cls
py -m pip uninstall tensorflow-gpu -y -q
py -m pip install tensorflow -q
cls
echo Fensterbreite:
set /p width=
cls
echo Fensterhîhe:
set /p height=
cls
echo Lernrate:
set /p lr=
cls
echo Epochen:
set /p epochs=
cls
py gta5ki.py test %width% %height% %lr% %epochs%

:open
cls
echo Welche Daten wollen sie sehen?
set /p Auswahl=
cls
py view_data.py %Auswahl%

:error
echo Falsche Eingabe
cls
goto menu



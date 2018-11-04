@echo off
goto menu
:menu
echo -- GTA5KI Menue --
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
py gta5ki.py record
pause
cls
goto menu

:train
cls
echo Lernrate:
set /p lr=
cls
echo Epochen:
set /p epochs=
cls
echo Anzahl der Trainingsdaten:
set /p amount=
cls
echo Vorheriges Model laden? True/False
set /p load=
cls
py gta5ki.py train %lr% %epochs% %amount% %load%
pause
cls
goto menu

:test
cls
echo Lernrate:
set /p lr=
cls
echo Epochen:
set /p epochs=
cls
py gta5ki.py test %lr% %epochs%
pause
cls
goto menu

:open
cls
py view_data.py
pause
cls
goto menu

:error
echo Falsche Eingabe
cls
goto menu



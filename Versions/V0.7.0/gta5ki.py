import record
#import daten_ausgleichen
import train
import test
import sys


if sys.argv[1] == "record" or sys.argv[0] == "record":
    if len(sys.argv) > 3:
        #dateiname = sys.argv[4] + ".npy"
        record.run(sys.argv[2],sys.argv[3])
    else:
        print("Geben sie alle Parameter an.")
        print("{Fensterbreite} {Fensterhöhe} {Dateiname}")
        sys.exit()
##elif sys.argv[1] == "balance" or sys.argv[0] == "balance":
##    if len(sys.argv) > 3:
##        dateiname1 = sys.argv[2] + ".npy"
##        dateiname2 = sys.argv[3] + ".npy"
##        daten_ausgleichen.run(dateiname1, dateiname2)
##    else:
##        print("Geben sie alle Parameter an.")
##        print("{Dateiname Trainingsdaten} {Dateiname ausgeglichene Daten}")
##        sys.exit()
elif sys.argv[1] == "train" or sys.argv[0] == "train":
    if len(sys.argv) > 5:
        #dateiname = sys.argv[6] + ".npy"
        train.run(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
    else:
        print("Geben sie alle Parameter an.")
        print("{Fensterbreite} {Fensterhöhe} {Lernrate} {Epochen} {Dateiname ausgeglichene Daten}")
        sys.exit()
elif sys.argv[1] == "test" or sys.argv[0] == "test":
    if len(sys.argv) > 5:
       test.run(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
    else:
        print("Geben sie alle Parameter an.")
        print("{Fensterbreite} {Fensterhöhe} {Lernrate} {Epochen}")
        sys.exit()      
else:
    sys.exit()
        


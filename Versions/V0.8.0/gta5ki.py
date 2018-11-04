import record
import train
import test
import sys


if sys.argv[1] == "record" or sys.argv[0] == "record":
    print("RECORD")
    record.run()
elif sys.argv[1] == "train" or sys.argv[0] == "train":
    print("TRAIN")
    if len(sys.argv) > 5:
        train.run(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        print("Geben sie alle Parameter an.")
        print("{Lernrate} {Epochen} {Anzahl der Trainingsdaten}")
        sys.exit()
elif sys.argv[1] == "test" or sys.argv[0] == "test":
    print("TEST")
    if len(sys.argv) > 5:
        test.run(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        print("Geben sie alle Parameter an.")
        print("{Fensterbreite} {Fensterhöhe} {Lernrate} {Epochen}")
        sys.exit()
else:
    sys.exit()

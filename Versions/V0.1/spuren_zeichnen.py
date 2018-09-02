from numpy import ones, vstack
from numpy.linalg import lstsq
from statistics import mean
import numpy as np


def spuren_zeichnen(image, linien, color=[0,255,0], thickness=3):
    try:
        ys = []
        for i in linien:
            for ii in i:
                ys += [ii[1],ii[3]]
        min_y = min(ys)
        max_y = 600
        #neue_linien=[]
        linien_dict = {}  

        for idx,i in enumerate(linien):
            for xyxy in i:
                x_koordinaten = (xyxy[0],xyxy[2])
                y_koordinaten = (xyxy[1],xyxy[3])
                A = vstack([x_koordinaten,ones(len(x_koordinaten))]).T
                m, b = lstsq(A, y_koordinaten, rcond=None)[0]
                #if m < 0.0000001:
                #    print("HEy")
                #    return
                #else:
                #    pass
                x1 = (min_y-b) / m
                x2 = (max_y-b) / m
                linien_dict[idx] = [m,b,[int(x1), min_y, int(x2), max_y]]
                #neue_linien.append([int(x1), min_y, int(x2), max_y])
        finale_spuren = {}

        for idx in linien_dict:
            finale_spuren_kopie = finale_spuren.copy()
            m = linien_dict[idx][0]
            b = linien_dict[idx][1]
            linie = linien_dict[idx][2]

            if len(finale_spuren) == 0:
                finale_spuren[m] = [ [m,b,linie] ]
            else:
                kopie_gefunden = False

                for other_ms in finale_spuren_kopie:

                    if not kopie_gefunden:
                        if abs(other_ms*1.2) > abs(m) > abs(other_ms*0.8):
                            if abs(finale_spuren_kopie[other_ms][0][1]*1.2) > abs(b) > abs(finale_spuren_kopie[other_ms][0][1]*0.8):
                                finale_spuren[other_ms].append([m,b,linie])
                                kopie_gefunden = True
                                break
                        else:
                            finale_spuren[m] = [ [m,b,linie] ]

        linien_anzahl = {}

        for spuren in finale_spuren:
            linien_anzahl[spuren] = len(finale_spuren[spuren])

        obere_spuren = sorted(linien_anzahl.items(), key=lambda item: item[1])[::-1][:2]
        spur1_id = obere_spuren[0][0]
        spur2_id = obere_spuren[1][0]

        def durchschnitt_spur(spurdaten):
            x1s = []
            y1s = []
            x2s = []
            y2s = []
            for daten in spurdaten:
                x1s.append(daten[2][0])
                y1s.append(daten[2][1])
                x2s.append(daten[2][2])
                y2s.append(daten[2][3])
            return int(mean(x1s)), int(mean(y1s)), int(mean(x2s)), int(mean(y2s))

        l1_x1, l1_y1, l1_x2, l1_y2 = durchschnitt_spur(finale_spuren[spur1_id])
        l2_x1, l2_y1, l2_x2, l2_y2 = durchschnitt_spur(finale_spuren[spur2_id])
        return [l1_x1, l1_y1, l1_x2, l1_y2], [l2_x1, l2_y1, l2_x2, l2_y2], spur1_id, spur2_id
    except Exception as e:
        #print("Teil 1: "+str(e))
        pass

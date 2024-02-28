import matplotlib.pyplot as plt
import math, csv


anzahl = int(input('Anzahl der Punkte, die zur Stationierung verwendet wurden: '))
dateinamen = []

for j in range(1, anzahl + 1):
    punkte = []
    y_werte = []
    x_werte = []
    neuer_punkt = []

    for i in range(1, 3):
        # Erst Standpunkt, dann Festpunkt eingeben
        name = input(f'{i}. Punktname: '); punkte.append(name)
        y_value = float(input('\tY-Wert: ')); y_werte.append(y_value)
        x_value = float(input('\tX-Wert: ')); x_werte.append(x_value)

    neuer_punktname = input('Neuer Punkt: '); neuer_punkt.append(neuer_punktname)
    winkel = float(input(f'Winkel vom Festpunkt {punkte[1]} zum neuen Punkt {neuer_punktname}: '))
    strecke = float(input(f'Strecke vom Standpunkt {punkte[0]} zum neuen Punkt {neuer_punktname}: '))

    print('-'* 15)

    # Differenzen ausrechnen
    diff_y = y_werte[1] - y_werte[0]
    diff_x = x_werte[1] - x_werte[0]
    sum_xy = (diff_y / diff_x)

    # Richtungswinkel des Festpunktes
    richtungswinkel_fp = round(math.atan(sum_xy) * 200 / math.pi, 4)

    # Quadrantenregeln beachten
    if diff_y > 0 and diff_x < 0:
        richtungswinkel_fp = round(richtungswinkel_fp + 200, 4)
    elif diff_y and diff_x < 0:
        richtungswinkel_fp = round(richtungswinkel_fp + 200, 4)
    elif diff_y < 0 and diff_x > 0:
        richtungswinkel_fp = round(richtungswinkel_fp + 400, 4)

    # Richtungswinkel des gesuchten Punktes
    richtungswinkel_S = round(richtungswinkel_fp + winkel, 4)

    # Falls der Winkel größer als 400 gon sein sollte, werden 400 gon abgezogen
    if richtungswinkel_S >= 400:
        richtungswinkel_S = round(richtungswinkel_S - 400, 4)
    else:
        pass

    # Umwandlung des zweiten Winkels, damit man den Sinus/Kosinus berechnen kann
    def conversion(richtungswinkel_S):
        return richtungswinkel_S * math.pi / 200

    # Bildung der Deltas
    delta_y = round(strecke * math.sin(conversion(richtungswinkel_S)), 4)
    delta_x = round(strecke * math.cos(conversion(richtungswinkel_S)), 4)

    # Streckenkontrolle mit Satz des Pythagoras und den Deltas
    streckenkontrolle = round(math.sqrt(delta_y**2 + delta_x**2), 3)

    # Analyse des Ergebnisses der Streckenkontrolle
    if streckenkontrolle - strecke <= abs(0.002):
        pass
    else:
        print(f'Die Abweichung in der Strecke ist zu groß ({streckenkontrolle - strecke}). Lieber nicht weiterrechnen.')
        exit()

    # Bildung der neuen Koordinaten
    new_y = round(y_werte[0] + delta_y, 3)
    new_x = round(x_werte[0] + delta_x, 3)

    # Wiedergabe für den Benutzer
    print(f'- Richtungswinkel t({punkte[0]}_{punkte[1]}) = {richtungswinkel_fp} gon')
    print(f'- Richtungswinkel t({punkte[0]}_{neuer_punktname}) = {richtungswinkel_S} gon')
    print(f'- Delta Y = {delta_y}')
    print(f'- Delta X = {delta_x}')
    print(f'- Errechnete Strecke: {streckenkontrolle} m')
    print(f'- Der neue Punkt {neuer_punktname} hat die Koordinaten ({new_y} | {new_x}).')
    print('-'* 15); print('-'* 15)



    with open(f'polar_{j}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Punktname', 'Y-Wert', 'X-Wert'])

        for i in range(2):
            writer.writerow([punkte[i], y_werte[i], x_werte[i]])

        writer.writerow([neuer_punktname, new_y, new_x])
        dateinamen.append(f'polar_{j}.csv')



    fig, ax = plt.subplots()
    ax.scatter(y_werte, x_werte); ax.scatter(new_y, new_x)

    for i, txt in enumerate(punkte):
        ax.annotate(txt, (y_werte[i], x_werte[i]))
    for i, txt in enumerate(neuer_punktname):
        ax.annotate(txt, (new_y, new_x))

    ax.set_aspect('equal')
    plt.plot(y_werte, x_werte, linestyle='--'); plt.plot([y_werte[0], new_y], [x_werte[0], new_x])
    plt.title(f'- Polares Anhängen des Punktes {neuer_punktname} -')
    plt.ylabel('X-Wert (Nord)')
    plt.xlabel('Y-Wert (Ost)')
    plt.savefig(f'polar_{j}.png', dpi=300)
    plt.show()



with open('polar.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    writer.writerow(['Punktname', 'Y-Wert', 'X-Wert'])

    for datei in dateinamen:
        with open(datei, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            letzte_zeile = next(reader, None)
            for zeile in reader:
                letzte_zeile = zeile

        writer.writerow(letzte_zeile)



fixpunkt_name = []
fixpunkt_y = []
fixpunkt_x = []

with open('polar.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)
    for row in reader:
        fixpunkt_name.append(row[0])
        fixpunkt_y.append(float(row[1]))
        fixpunkt_x.append(float(row[2]))

if len(fixpunkt_name) == 1:
    medium_y = fixpunkt_y[0]
    medium_x = fixpunkt_x[0]
    print(f'Koordinaten des neuen Standpunktes sind ({medium_y} | {medium_x}).')
elif len(fixpunkt_name) == 2:
    medium_y = round(sum(fixpunkt_y) / 2, 3)
    medium_x = round(sum(fixpunkt_x) / 2, 3)
    print(f'Die gemittleten Koordinaten des neuen Standpunktes sind ({medium_y} | {medium_x}).')
elif len(fixpunkt_name) == 3:
    medium_y = round(sum(fixpunkt_y) / 3, 3)
    medium_x = round(sum(fixpunkt_x) / 3, 3)
    print(f'Koordinaten des Dreieckszentrums sind ({medium_y} | {medium_x}).')
elif len(fixpunkt_name) == 4:
    medium_y = round(sum(fixpunkt_y) / 4, 3)
    medium_x = round(sum(fixpunkt_x) / 4, 3)
    print(f'Koordinaten des Viereckszentrums sind ({medium_y} | {medium_x}).')

with open('polar.csv', 'a', newline='') as csvfile:
    writer1 = csv.writer(csvfile, delimiter=',')
    writer2 = csv.writer(csvfile, delimiter='-')

    if anzahl > 1:
        writer2.writerow('----------')
        writer1.writerow(['S', medium_y, medium_x])
    


fig, ax = plt.subplots()
ax.scatter(fixpunkt_y, fixpunkt_x); ax.scatter(medium_y, medium_x)

for i, txt in enumerate(fixpunkt_name):
    ax.annotate(txt, (fixpunkt_y[i], fixpunkt_x[i]))

if anzahl == 1:
    for i, txt in enumerate(fixpunkt_name):
        ax.annotate(txt, (medium_y, medium_x))

for i in range(len(fixpunkt_name)):
    plt.plot([fixpunkt_y[i], medium_y], [fixpunkt_x[i], medium_x], color='orange', linestyle='--')

ax.set_aspect('equal')
plt.savefig('polar.png', dpi=300)
plt.show()

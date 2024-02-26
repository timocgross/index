import math

name = []
y = []
x = []

for i in range(2):
    # Erst Standpunkt, dann Festpunkt
    names = input(f'{i+1}. Punktname: '); name.append(names)
    y_value = float(input('\tY-Wert: ')); y.append(y_value)
    x_value = float(input('\tX-Wert: ')); x.append(x_value)

new_name = input('Neuer Punkt: ')
winkel = float(input(f'Winkel vom Festpunkt {name[1]} zum neuen Punkt {new_name}: '))
strecke = float(input(f'Strecke vom Standpunkt {name[0]} zum neuen Punkt {new_name}: '))

print('-'* 15)

diff_y = y[1] - y[0]
diff_x = x[1] - x[0]
sum_xy = diff_y / diff_x

richtungswinkel_fp = round(math.atan(sum_xy) * 200 / math.pi, 4)

if diff_y > 0 and diff_x < 0:
    richtungswinkel_fp = round(richtungswinkel_fp + 200, 4)
elif diff_y and diff_x < 0:
    richtungswinkel_fp = round(richtungswinkel_fp + 200, 4)
elif diff_y < 0 and diff_x > 0:
    richtungswinkel_fp = round(richtungswinkel_fp + 400, 4)

richtungswinkel_S = round(richtungswinkel_fp + winkel, 4)

if richtungswinkel_S >= 400:
    richtungswinkel_S = round(richtungswinkel_S - 400, 4)
else:
    pass

def conversion(richtungswinkel_S):
    # Umwandlung des zweiten Winkels, damit man den Sinus/Kosinus berechnen kann
    return richtungswinkel_S * math.pi / 200

delta_y = round(strecke * math.sin(conversion(richtungswinkel_S)), 4)
delta_x = round(strecke * math.cos(conversion(richtungswinkel_S)), 4)

streckenkontrolle = round(math.sqrt(delta_y**2 + delta_x**2), 3)

if streckenkontrolle - strecke <= abs(0.002):
    pass
else:
    print(f'Die Abweichung in der Strecke ist zu groß ({streckenkontrolle - strecke}). Lieber nicht weiterrechnen.')
    exit()

new_y = round(y[0] + delta_y, 3)
new_x = round(x[0] + delta_x, 3)

print(f'- Richtungswinkel t({name[0]}_{name[1]}) = {richtungswinkel_fp} gon')
print(f'- Richtungswinkel t({name[0]}_{new_name}) = {richtungswinkel_S} gon')
print(f'- Delta Y = {delta_y}')
print(f'- Delta X = {delta_x}')
print(f'- Errechnete Strecke: {streckenkontrolle} m')
print(f'- Der neue Punkt {new_name} hat die Koordinaten ({new_y} | {new_x}).')

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter(y, x); ax.scatter(new_y, new_x)

for i, txt in enumerate(name):
    ax.annotate(txt, (y[i], x[i]))
for i, txt in enumerate(new_name):
    ax.annotate(txt, (new_y, new_x))

ax.set_aspect('equal')
plt.plot(y, x, linestyle='--'); plt.plot([y[0], new_y], [x[0], new_x])
plt.show()

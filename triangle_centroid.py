names = []
y_values = []
x_values = []

for i in range(1, 4):
    name = input(f'Gib den {i}. Punktnamen ein: '); names.append(name)
    y = float(input('Y-Wert: ')); y_values.append(y)
    x = float(input('X-Wert: ')); x_values.append(x)

medium_y = round(sum(y_values) / 3, 3)
medium_x = round(sum(x_values) / 3, 3)

print(f'Koordinaten des Dreieckszentrums sind ({medium_y} | {medium_x}).')

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter(y_values, x_values); ax.scatter(medium_y, medium_x)

for i, txt in enumerate(names):
    ax.annotate(txt, (y_values[i], x_values[i]))
for i, txt in enumerate('S'):
    ax.annotate(txt, (medium_y, medium_x))

for i in range(3):
    plt.plot([y_values[i], medium_y], [x_values[i], medium_x], color='orange', linestyle='--')

ax.set_aspect('equal')
plt.show()

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from characters.dragislav import Dragislav

armor_classes = [15, 18, 20, 22, 25]

plt.xticks(np.arange(1, 20, 1.0))

for ac in armor_classes:
    dragislav = Dragislav()
    damage_done = []
    for i in range(20): # simulate 20 rounds of combat
        damage_done.append(dragislav.calculate_damage_for_round(ac, i))
        if i > 0:
            damage_done[i] += damage_done[i - 1]
        print(f"dragislav has done {damage_done} damage on an AC {ac} creature by round {i}")
    plt.plot(damage_done, label=f"AC {ac}")
    damage_done = 0

plt.legend()
plt.show()

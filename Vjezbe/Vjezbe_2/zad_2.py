import numpy as np
import matplotlib.pyplot as plt
from particle import Particle
p = Particle(10, 60, 0, 0)
domet_analiticki = p.v0**2 * np.sin(2 * p.kut) / p.g
vrem_korak = np.linspace(0.001, 0.1, 200)
rel_pogreska = []
for i in vrem_korak:
    domet_numericki = p.range(i)
    pogreska = abs(domet_numericki-domet_analiticki)/domet_analiticki
    rel_pogreska.append(pogreska)
plt.plot(vrem_korak, rel_pogreska)
plt.xlabel("dt [s]")
plt.ylabel("Relativna pogreska")
plt.title("Ovisnost relativne pogreske o vremenskom koraku dt")
plt.grid()
plt.show()
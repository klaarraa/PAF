import numpy as np
import matplotlib.pyplot as plt
from particle import Particle
p = Particle(10, 60, 0, 0)
domet_analiticki = p.v0**2 * np.sin(2 *np.radians(p.kut)) / p.g
vrem_korak = np.array([0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.001])
rel_pogreska = []
for i in vrem_korak:
    domet_numericki = p.range(i)
    pogreska = abs(domet_numericki-domet_analiticki)/domet_analiticki
    rel_pogreska.append(pogreska)
plt.loglog(vrem_korak, rel_pogreska, 'o-')
plt.xlabel("dt [s]")
plt.ylabel("Relativna pogreska")
plt.title("Ovisnost relativne pogreske o vremenskom koraku dt")
plt.grid()
plt.show()
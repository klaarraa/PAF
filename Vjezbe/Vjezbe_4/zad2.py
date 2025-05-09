from particle import Particle
import numpy as np
import matplotlib.pyplot as plt
v0 = 10
kut = 60
x = 0
y = 0

p = Particle(v0, kut, x, y)
err = []
dts = []
dt = 0

while dt <= 1:
    dt += 0.001
    dts.append(dt)
    p = Particle(v0, kut, x, y)

    numericki_domet = p.range(dt)
    analiticki_domet = ((v0 ** 2) * np.sin(2 * np.radians(kut))) / 9.81
    
    odstupanje = abs(analiticki_domet - numericki_domet)
    err.append((odstupanje / analiticki_domet) * 100)

plt.plot(dts, err)
plt.xlabel("dt [s]")
plt.ylabel("Greška [%]")
plt.title("Relativna greška dometa projektila u ovisnosti o dt")
plt.ylim(-1, max(err) + 5)
plt.grid()
plt.show()
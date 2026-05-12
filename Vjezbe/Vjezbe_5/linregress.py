import numpy as np
import matplotlib.pyplot as plt
M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336])
fi = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472])
br_tocaka = len(M)
xy_srednje = np.mean(fi * M)
x2_srednje = np.mean(fi**2)
y2_srednje = np.mean(M**2)
a = xy_srednje/x2_srednje
sigma = np.sqrt((1/br_tocaka)*((y2_srednje/x2_srednje)-a**2))
plt.scatter(fi,M,label="podaci")
fi_pravac = np.linspace(0, max(fi), 100)
M_pravac = a*fi_pravac
plt.plot(fi_pravac,M_pravac,label="Dt*fi")
plt.xlabel("fi [rad]")
plt.ylabel("M [Nm]")
plt.title("Linearna regresija")
plt.legend()
plt.grid()
plt.show()
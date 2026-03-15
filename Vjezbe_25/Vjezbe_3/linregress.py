import numpy as np
import matplotlib.pyplot as plt
M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336])
phi = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472])
a = np.polyfit(phi, M, 1)[0]
print(f"Dt = {a} Nm/rad")

phi_lin = np.linspace(0, max(phi), 100)
plt.plot(phi, M, 'ro', label='Podaci')
plt.plot(phi_lin, a * phi_lin, 'b-', label=f'M = {a}·φ')
plt.xlabel('φ (rad)')
plt.ylabel('M (Nm)')
plt.title('Linearna regresija')
plt.grid()
plt.legend()
plt.show()
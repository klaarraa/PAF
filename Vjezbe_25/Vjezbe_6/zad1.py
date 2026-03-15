import numpy as np
import matplotlib.pyplot as plt
from harmonic_oscillator import HarmonicOscillator

mass = 1.0    
k = 4.0      
x0 = 0.0  
v0 = 1.0      
osc = HarmonicOscillator(mass, k, x0, v0)
t = np.linspace(0, 10, 1000)
x = osc.pomak(t)
v = osc.brzina(t)
a = osc.akceleracija(t)

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, x, color='blue')
plt.title('x-t graf')
plt.ylabel('x [m]')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, v, color='orange')
plt.title('v-t graf')
plt.ylabel('v [m/s]')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, a, color='red')
plt.title('a-t graf)')
plt.ylabel('a [m/s^2]')
plt.xlabel('Vrijeme [s]')
plt.grid(True)

plt.tight_layout()
plt.show()
dt_values = [0.5, 0.1, 0.05, 0.01, 0.001]

print("Preciznost numerickog rjesenja:\n")
print(f"{'Korak dt':>10} | {'Maks. greska':>15}")
print("-" * 30)

for dt in dt_values:
    t = np.arange(0, 10, dt)

    x_analytical = osc.pomak(t)
    x_numerical = osc.numericki(t)
    max_error = max(abs(x_analytical - x_numerical))

    print(f"{dt:10.4f} | {max_error:15.8f}")
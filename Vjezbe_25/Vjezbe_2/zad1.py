import numpy as np
import matplotlib.pyplot as plt
F = float(input("Unesi silu u N: "))
m = float(input("Unesi masu u kg: "))
a = F / m  
v0 = 0     
x0 = 0     
dt = 0.1 
t_max = 10
t = np.arange(0, t_max + dt, dt)
x = [0] * len(t)
v = [0] * len(t)
a_array = [a] * len(t) 

for i in range(1, len(t)):
    v[i] = v[i-1] + a * dt
    x[i] = x[i-1] + v[i-1] * dt 

plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, x, 'b')
plt.title('Položaj - vrijeme (x - t)')
plt.xlabel('Vrijeme [s]')
plt.ylabel('Položaj [m]')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, v, 'g')
plt.title('Brzina - vrijeme (v - t)')
plt.xlabel('Vrijeme [s]')
plt.ylabel('Brzina [m/s]')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, a_array, 'r')
plt.title('Ubrzanje - vrijeme (a - t)')
plt.xlabel('Vrijeme [s]')
plt.ylabel('Ubrzanje [m/s²]')
plt.grid(True)

plt.tight_layout()
plt.show()

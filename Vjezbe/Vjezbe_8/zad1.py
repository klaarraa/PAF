import numpy as np
import matplotlib.pyplot as plt

q_elektron = -1.602e-19
q_pozitron = 1.602e-19
m = 9.109e-31
B = np.array([0, 0, 1.0]) 
E = np.array([0, 0, 0])   
v0 = np.array([2e6, 2e6, 4e6])
r0 = np.array([0.0, 0.0, 0.0])
dt = 1e-13
N = 1500

def lorentzova_sila(q, v, E, B):
    return q * (E + np.cross(v, B))

def runge_kutta(q, m, r0, v0, E, B, dt, N):
    r = np.zeros((N, 3))
    v = np.zeros((N, 3))
    r[0], v[0] = r0, v0

    for i in range(1, N):
        k1v = dt * lorentzova_sila(q, v[i-1], E, B) / m
        k1r = dt * v[i-1]

        k2v = dt * lorentzova_sila(q, v[i-1] + 0.5*k1v, E, B) / m
        k2r = dt * (v[i-1] + 0.5*k1v)

        k3v = dt * lorentzova_sila(q, v[i-1] + 0.5*k2v, E, B) / m
        k3r = dt * (v[i-1] + 0.5*k2v)

        k4v = dt * lorentzova_sila(q, v[i-1] + k3v, E, B) / m
        k4r = dt * (v[i-1] + k3v)

        v[i] = v[i-1] + (k1v + 2*k2v + 2*k3v + k4v) / 6
        r[i] = r[i-1] + (k1r + 2*k2r + 2*k3r + k4r) / 6

    return r
r_elektron = runge_kutta(q_elektron, m, r0, v0, E, B, dt, N)
r_pozitron = runge_kutta(q_pozitron, m, r0, v0, E, B, dt, N)

fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

ax1.plot(r_elektron[:, 0], r_elektron[:, 1], r_elektron[:, 2], color='blue', linewidth=0.8)
ax1.set_title('Putanja elektrona')
ax1.set_xlabel('x [m]')
ax1.set_ylabel('y [m]')
ax1.set_zlabel('z [m]')

ax2.plot(r_pozitron[:, 0], r_pozitron[:, 1], r_pozitron[:, 2], color='red', linewidth=0.8)
ax2.set_title('Putanja pozitrona')
ax2.set_xlabel('x [m]')
ax2.set_ylabel('y [m]')
ax2.set_zlabel('z [m]')

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

def jednoliko_gibanje(brzina, vrijeme):
    t = np.linspace(0, vrijeme, 100)
    s = brzina * t
    v = [brzina] * len(t)
    a = [0] * len(t)

    plt.figure(figsize=(8, 5))
    plt.plot(t, s, label='s = v * t')
    plt.title('Jednoliko gibanje: x-t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Prijeđeni put (m)')
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(t, v, label='v = konst.')
    plt.title('Jednoliko gibanje: v-t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Brzina (m/s)')
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(t, a, label='a = 0')
    plt.title('Jednoliko gibanje: a-t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Ubrzanje (m/s²)')
    plt.grid(True)
    plt.legend()
    plt.show()

def kosi_hitac(brzina, kut, masa, vrijeme):
    g = 9.81
    kut_rad = np.radians(kut)
    v0x = brzina * np.cos(kut_rad)
    v0y = brzina * np.sin(kut_rad)

    dt = 0.01
    t = 0
    x_vals = []
    y_vals = []
    v_x_vals = []
    v_y_vals = []
    a_x_vals = []
    a_y_vals = []

    while t <= vrijeme:
        x = v0x * t
        y = v0y * t - 0.5 * g * t**2
        v_x = v0x
        v_y = v0y - g * t
        a_x = 0
        a_y = -g 

        if y < 0:
            break 

        x_vals.append(x)
        y_vals.append(y)
        v_x_vals.append(v_x)
        v_y_vals.append(v_y)
        a_x_vals.append(a_x)
        a_y_vals.append(a_y)
        t += dt

    plt.figure(figsize=(8, 5))
    plt.plot(np.arange(0, t, dt), x_vals, label='x(t) - horizontalna udaljenost')
    plt.title('Kosi hitac: x-t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Udaljenost (m)')
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(np.arange(0, t, dt), y_vals, label='y(t) - visina')
    plt.title('Kosi hitac: y-t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Visina (m)')
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(np.arange(0, t, dt), v_x_vals, label='v_x(t) - horizontalna brzina')
    plt.plot(np.arange(0, t, dt), v_y_vals, label='v_y(t) - vertikalna brzina')
    plt.title('Kosi hitac: v-t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Brzina (m/s)')
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(np.arange(0, t, dt), a_x_vals, label='a_x(t) - horizontalno ubrzanje')
    plt.plot(np.arange(0, t, dt), a_y_vals, label='a_y(t) - vertikalno ubrzanje')
    plt.title('Kosi hitac: a-t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Ubrzanje (m/s²)')
    plt.grid(True)
    plt.legend()
    plt.show()
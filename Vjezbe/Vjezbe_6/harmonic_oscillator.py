import numpy as np

class HarmonicOscillator:
    def __init__(self, mass, k, x0, v0):
        self.m = mass
        self.k = k
        self.x0 = x0
        self.v0 = v0
        self.omega = np.sqrt(k / mass)

    def pomak(self, t):
        A = self.x0
        B = self.v0 / self.omega
        return A * np.cos(self.omega * t) + B * np.sin(self.omega * t)

    def brzina(self, t):
        A = self.x0
        B = self.v0 / self.omega
        return -A * self.omega * np.sin(self.omega * t) + B * self.omega * np.cos(self.omega * t)

    def akceleracija(self, t):
        return -self.omega**2 * self.pomak(t)

    def numericki(self, t):
        dt = t[1] - t[0]
        x = np.zeros(len(t))
        v = np.zeros(len(t))
        x[0] = self.x0
        v[0] = self.v0
        for i in range(1, len(t)):
            a = -self.omega**2 * x[i - 1]
            v[i] = v[i - 1] + a * dt
            x[i] = x[i - 1] + v[i - 1] * dt

        return x
    def numericki_period(self, t):
        x = self.numericki(t)
        zero_times = []

        for i in range(1, len(x)):
            if x[i - 1] < 0 and x[i] >= 0:
                zero_times.append(t[i])

        if len(zero_times) < 2:
            return None

        return zero_times[2] - zero_times[0]

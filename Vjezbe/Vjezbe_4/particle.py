import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, kut, x0=0, y0=0):
        self.v0=v0
        self.kut=np.radians(kut)
        self.x_poc=x0
        self.y_poc=y0
        self.x_tren=x0
        self.y_tren=y0
        self.vx=v0*np.cos(self.kut)
        self.vy=v0*np.sin(self.kut)
        self.g=9.81
        self.t=0

    def reset(self):
        del self.v0
        del self.kut
        del self.x_poc
        del self.y_poc
        del self.x_tren
        del self.y_tren
        del self.vx
        del self.vy
        del self.t
        del self.g

    def __move(self, dt):
        self.x_tren+=self.vx*dt
        self.y_tren+=self.vy*dt
        self.vy-=self.g*dt
        self.t+=dt

    def range(self, dt=0.01):
        x=self.x_poc
        y=self.y_poc
        vx=self.vx
        vy=self.vy
        t=self.t

        while self.y_tren >= 0:
            self.__move(dt)

        domet=self.x_tren
        self.x_tren=x
        self.y_tren=y
        self.vx=vx
        self.vy=vy
        self.t=t

        return domet
    
    def plot_trajectory(self, dt=0.01):
        x=self.x_tren
        y=self.y_tren
        vx=self.vx
        vy=self.vy
        t=self.t

        x_vals=[self.x_tren]
        y_vals=[self.y_tren]

        while self.y_tren >= 0:
            self.__move(dt)
            x_vals.append(self.x_tren)
            y_vals.append(self.y_tren)

        plt.plot(x_vals, y_vals)
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.title("Putanja čestice")
        plt.grid()
        plt.show()

        self.trenutni_x=x
        self.trenutni_y=y
        self.vx=vx
        self.vy=vy
        self.t=t

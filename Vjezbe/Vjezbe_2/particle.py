import numpy as np
import matplotlib.pyplot as plt
class Particle:
    def __init__(self, v0, kut, x0, y0):
        self.v0 = v0
        self.kut = np.radians(kut)
        self.x0 = x0
        self.y0 = y0
        self.g = 9.81
        self.reset()

    def reset(self):
        self.t = 0
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0*np.cos(self.kut)
        self.vy = self.v0*np.sin(self.kut)
        self.x_koordinate = [self.x]
        self.y_koordinate = [self.y]

    def __move(self, dt):
        self.x += self.vx*dt
        self.y += self.vy*dt 
        self.vy -= self.g*dt
        self.t += dt
        self.x_koordinate.append(self.x)
        self.y_koordinate.append(self.y)
        
    def range(self, dt=0.001):  
        self.reset()
        while self.y >= 0:
            self.__move(dt)
        return self.x

    def plot_trajectory(self, dt=0.001):
        self.reset()
        while self.y >=0:
            self.__move(dt)
        plt.plot(self.x_koordinate, self.y_koordinate)
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.title("Putanja cestice")
        plt.grid()
        plt.show()
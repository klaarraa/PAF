import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, v0, kut, koef_otpora, m, A, gustoca=1.225, g=9.81):
        self.v0 = v0
        self.kut = np.radians(kut)
        self.koef_otpora = koef_otpora
        self.m = m
        self.g = g
        self.gustoca = gustoca
        self.A = A
        self.reset()

    def reset(self):
        self.x = 0
        self.y = 0
        self.vx = self.v0*np.cos(self.kut)
        self.vy = self.v0*np.sin(self.kut)
        self.putanja = [(self.x, self.y)]

    def otpor_zraka(self, vx, vy):
        v = np.sqrt(vx**2+vy**2)
        F = 0.5*self.gustoca*self.koef_otpora*self.A*v**2
        ax = -F*vx/(v*self.m)
        ay = -F*vy/(v*self.m)
        return ax, ay
    
    def euler(self, dt):
        ax_zrak, ay_zrak = self.otpor_zraka(self.vx, self.vy)
        ax = ax_zrak
        ay = ay_zrak - self.g
        self.vx += ax*dt
        self.vy += ay*dt
        self.x += self.vx*dt
        self.y += self.vy*dt
        self.putanja.append((self.x,self.y))

    def simuliraj_euler(self, dt):
        self.reset()
        while self.y >= 0:
            self.euler(dt)
        return np.array(self.putanja)

    def derivacije(self, stanje):
        x,y,vx,vy = stanje
        ax_zrak,ay_zrak = self.otpor_zraka(vx,vy)
        ax = ax_zrak
        ay = ay_zrak - self.g
        return np.array([vx,vy,ax,ay])
        
    def rk4(self, dt):
        stanje = np.array([self.x,self.y,self.vx,self.vy])
        k1 = self.derivacije(stanje)
        k2 = self.derivacije(stanje+0.5*dt*k1)
        k3 = self.derivacije(stanje+0.5*dt*k2)
        k4 = self.derivacije(stanje+dt*k3)
        stanje = stanje+(dt/6)*(k1+2*k2+2*k3+k4)
        self.x,self.y,self.vx,self.vy = stanje
        self.putanja.append((self.x, self.y))

    def simuliraj_rk4(self, dt):
        self.reset()
        while self.y >= 0:
            self.rk4(dt)
        return np.array(self.putanja)
    
def testiraj():
    dt = [0.001, 0.8, 0.1, 0.05]
    for i in dt:
        p = Projectile(v0=50,kut=45,koef_otpora=0.47,m=5,A=0.01)
        putanja = p.simuliraj_euler(i)
        plt.plot(putanja[:, 0],putanja[:, 1],label=f"dt={i}")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Putanje projektila za razlicite dt (Eulerova metoda)")
    plt.legend()
    plt.grid()
    plt.show()

def usporedba():
    dt = 0.01
    p1 = Projectile(v0=50,kut=45,koef_otpora=0.47,m=5,A=0.01)
    putanja1 = p1.simuliraj_euler(dt)
    p2 = Projectile(v0=50,kut=45,koef_otpora=0.47,m=5,A=0.01)
    putanja2 = p2.simuliraj_rk4(dt)
    plt.plot(putanja1[:, 0],putanja1[:, 1],label="Euler")
    plt.plot(putanja2[:, 0],putanja2[:, 1],label="Runge-Kutta 4")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Usporedba Eulerove i Runge-Kutta metode")
    plt.legend()
    plt.grid()
    plt.show()
testiraj()
usporedba()
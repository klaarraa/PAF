import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, v0, kut, masa, povrsina, koef_otpora, gustoća_zraka=1.225, gravitacija=9.81):
        self.v0 = v0
        self.kut = np.radians(kut)
        self.masa = masa
        self.povrsina = povrsina
        self.Cd = koef_otpora
        self.ro = gustoća_zraka
        self.g = gravitacija
        self.resetiraj()

    def resetiraj(self):
        self.x = 0
        self.y = 0
        self.vx = self.v0 * np.cos(self.kut)
        self.vy = self.v0 * np.sin(self.kut)
        self.putanja = [(self.x, self.y)]

    def otpor_zraka(self, vx, vy):
        v = (vx**2 + vy**2)**0.5
        Fd = 0.5 * self.ro * self.Cd * self.povrsina * v**2
        ax = -Fd * vx / (v * self.masa)
        ay = -Fd * vy / (v * self.masa)
        return ax, ay

    def korak_euler(self, dt):
        ax_zrak, ay_zrak = self.otpor_zraka(self.vx, self.vy)
        ax = ax_zrak
        ay = ay_zrak - self.g

        self.vx += ax * dt
        self.vy += ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt

        self.putanja.append((self.x, self.y))

    def simuliraj_euler(self, dt):
        self.resetiraj()
        while self.y >= 0:
            self.korak_euler(dt)
        return np.array(self.putanja)
    
    def korak_rk4(self, dt):
        def derivacije(vx, vy):
            ax_zrak, ay_zrak = self.otpor_zraka(vx, vy)
            return ax_zrak, ay_zrak - self.g

    
        k1_vx, k1_vy = derivacije(self.vx, self.vy)
        k1_x, k1_y = self.vx, self.vy

        
        vx2 = self.vx + 0.5 * dt * k1_vx
        vy2 = self.vy + 0.5 * dt * k1_vy
        k2_vx, k2_vy = derivacije(vx2, vy2)
        k2_x, k2_y = vx2, vy2

    
        vx3 = self.vx + 0.5 * dt * k2_vx
        vy3 = self.vy + 0.5 * dt * k2_vy
        k3_vx, k3_vy = derivacije(vx3, vy3)
        k3_x, k3_y = vx3, vy3

        
        vx4 = self.vx + dt * k3_vx
        vy4 = self.vy + dt * k3_vy
        k4_vx, k4_vy = derivacije(vx4, vy4)
        k4_x, k4_y = vx4, vy4

        
        self.vx += dt * (k1_vx + 2 * k2_vx + 2 * k3_vx + k4_vx) / 6
        self.vy += dt * (k1_vy + 2 * k2_vy + 2 * k3_vy + k4_vy) / 6
        self.x += dt * (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6
        self.y += dt * (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6

        self.putanja.append((self.x, self.y))

    def simuliraj_rk4(self, dt):
        self.resetiraj()
        while self.y >= 0:
            self.korak_rk4(dt)
        return np.array(self.putanja)
    
def testiraj_dt_vrijednosti():
    dt_vrijednosti = [0.1, 0.05, 0.01, 0.005]
    plt.figure(figsize=(10, 6))

    for dt in dt_vrijednosti:
        p = Projectile(v0=50, kut=45, masa=1, povrsina=0.01, koef_otpora=0.47)
        putanja = p.simuliraj_euler(dt)
        plt.plot(putanja[:, 0], putanja[:, 1], label=f"dt = {dt}")

    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Putanje projektila za različite dt (Eulerova metoda)")
    plt.legend()
    plt.grid()
    plt.show()

def usporedi_metode(dt=0.01):
    p_euler = Projectile(v0=50, kut=45, masa=1, povrsina=0.01, koef_otpora=0.47)
    putanja_euler = p_euler.simuliraj_euler(dt)    
    p_rk4 = Projectile(v0=50, kut=45, masa=1, povrsina=0.01, koef_otpora=0.47)
    putanja_rk4 = p_rk4.simuliraj_rk4(dt)

    plt.figure(figsize=(10, 6))
    plt.plot(putanja_euler[:, 0], putanja_euler[:, 1], '--', label="Eulerova metoda")
    plt.plot(putanja_rk4[:, 0], putanja_rk4[:, 1], '-', label="Runge-Kutta 4. reda")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title(f"Usporedba numeričkih metoda za dt = {dt}")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    testiraj_dt_vrijednosti()    
    usporedi_metode(0.01)  
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
G = 6.67430e-11
AU = 1.496e11
dt = 24*60*60
class Planet:
    def __init__(self, ime, masa, x, y, vx, vy):
        self.ime = ime
        self.masa = masa
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = 0
        self.ay = 0
        self.x_pomak = [x]
        self.y_pomak = [y]

class Universe:
    def __init__(self):
        self.planeti = []

    def dodaj_planet(self, planet):
        self.planeti.append(planet)
    
    def evolucija(self, dt):
        for planet in self.planeti:
            ax = 0
            ay = 0
            for drugi in self.planeti:
                if drugi != planet:
                    dx = drugi.x - planet.x
                    dy = drugi.y - planet.y
                    r = np.sqrt(dx**2+dy**2)
                    ax += G*drugi.masa*dx/r**3
                    ay += G*drugi.masa*dy/r**3
            planet.ax = ax
            planet.ay = ay

        for planet in self.planeti:
            planet.vx += planet.ax*dt
            planet.vy += planet.ay*dt
            planet.x += planet.vx*dt
            planet.y += planet.vy*dt
            planet.x_pomak.append(planet.x)
            planet.y_pomak.append(planet.y)

sunce = Planet("Sunce", 1.989e30, 0, 0, 0, 0)     
merkur = Planet("Merkur", 3.285e23, 0.387*AU, 0, 0, 47.87e3)   
venera = Planet("Venera", 4.867e24, 0.72*AU, 0, 0, 35.02e3)   
zemlja = Planet("Zemlja", 5.972e24, 1*AU, 0, 0, 29.78e3)   
mars = Planet("Mars", 6.419310e23, 1.524*AU, 0, 0, 24.07e3)          
svemir = Universe()
svemir.dodaj_planet(sunce)
svemir.dodaj_planet(merkur)
svemir.dodaj_planet(venera)
svemir.dodaj_planet(zemlja)
svemir.dodaj_planet(mars)

for i in range(5*365):
    svemir.evolucija(dt)
for planet in svemir.planeti:
    plt.plot(np.array(planet.x_pomak)/AU, np.array(planet.y_pomak)/AU, label=planet.ime)
    plt.scatter(planet.x/AU, planet.y/AU)
plt.axis("equal")       
plt.xlabel("x [AU]")
plt.ylabel("y [AU]")
plt.title("Putanje planeta oko Sunca")
plt.grid()
plt.legend()
plt.show()

fig, ax = plt.subplots()
tocke = []
putanje = []
for planet in svemir.planeti:
    putanja = ax.plot([],[], label=planet.ime)[0]
    tocka = ax.plot([],[], "o")[0]
    putanje.append(putanja)
    tocke.append(tocka)
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_aspect("equal")
ax.set_xlabel("x [AU]")
ax.set_ylabel("y [AU]")
ax.set_title("Gibanje planeta oko Sunca")
ax.grid()
ax.legend()

def init():
    for putanja in putanje:
        putanja.set_data([],[])
    for tocka in tocke:
        tocka.set_data([],[])
    return putanje + tocke

def animacija(frame):
    for i in range(len(svemir.planeti)):
        planet = svemir.planeti[i]
        putanja = putanje[i]
        tocka = tocke[i]
        x = np.array(planet.x_pomak[:frame])/AU
        y = np.array(planet.y_pomak[:frame])/AU
        putanja.set_data(x, y)
        x_trenutno = planet.x_pomak[frame]/AU
        y_trenutno = planet.y_pomak[frame]/AU
        tocka.set_data([x_trenutno], [y_trenutno])
    return putanje + tocke
ani = FuncAnimation(fig, animacija, frames=len(zemlja.x_pomak), init_func=init, interval=10, repeat=False)
plt.show()
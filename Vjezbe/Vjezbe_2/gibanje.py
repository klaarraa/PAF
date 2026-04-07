import numpy as np
from particle import Particle
p=Particle(10,45,0,5)
domet_numericki = p.range()
theta = np.radians(p.kut)
t = (p.v0*np.sin(theta)+np.sqrt((p.v0*np.sin(theta))**2+2*p.g*p.y0))/p.g
domet_analiticki = p.v0*np.cos(theta)*t
print(f"Numericki domet: {domet_numericki} m")
domet_analiticki = p.v0**2*np.sin(2*np.radians(p.kut))/p.g
print(f"Analiticki domet: {domet_analiticki} m")
odstupanje = abs(domet_numericki - domet_analiticki)
print(f"Odstupanje: {odstupanje} m")
relativno = odstupanje/domet_analiticki*100
print(f"Relativno: {relativno} %")
p.plot_trajectory()
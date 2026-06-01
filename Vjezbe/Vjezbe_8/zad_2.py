import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
kut_deg = [0 , 5 , 10 , 15 , 20 , 25 , 30 , 35 , 40 , 45 , 50 , 55 , 60 , 65 , 70 , 75 , 80 , 85]
T_120 = [0.8020 , 0.8187 , 0.8327 , 0.8660 , 0.8980 , 0.9153 , 0.9293 , 0.9653 ,
0.9747 , 1.0200 , 1.0373 , 1.1160 , 1.1780 , 1.2733 , 1.4180 , 1.6373 , 1.9100 ,
2.5460]
T_240 = [1.0140 , 1.0320 , 1.0433 , 1.0673 , 1.0840 , 1.1320 , 1.1440 , 1.1720 ,
1.1980 , 1.2293 , 1.2813 , 1.3573 , 1.4200 , 1.5600 , 1.7413 , 1.9840 , 2.4473 ,
3.1573]
kut_rad = np.radians(kut_deg)
g=9.81
def T_teorija(theta,l):
    return 2*np.pi*np.sqrt(l/(g*np.cos(theta)))
parametri120,_ = curve_fit(T_teorija,kut_rad,T_120)
l120_fit = parametri120[0]
parametri240,_ = curve_fit(T_teorija,kut_rad,T_240)
l240_fit = parametri240[0]
print(f"Fitirana duljina za L=120 mm: {l120_fit} m")
print(f"Fitirana duljina za L=240 mm: {l240_fit} m")
theta = np.linspace(0,np.radians(85),500)
T_teorija120 = T_teorija(theta,0.120)
T_teorija240 = T_teorija(theta,0.240)
T_fit120 = T_teorija(theta,l120_fit)
T_fit240 = T_teorija(theta,l240_fit)
plt.scatter(kut_deg,T_120,label="Mjereni podaci L=120 mm")
plt.plot(np.degrees(theta),T_fit120,label="curve_fit L=120 mm")
plt.scatter(kut_deg,T_240,label="Mjereni podaci L=240 mm")
plt.plot(np.degrees(theta),T_fit240,label="curve_fit L=240 mm")
plt.plot(np.degrees(theta),T_teorija120,"--",label="Teorija L=120 mm")
plt.plot(np.degrees(theta),T_teorija240,"--",label="Teorija L=240 mm")
plt.xlabel("Kut theta(°)")
plt.ylabel("Period T(s)")
plt.title("Ovisnost perioda o kutu")
plt.grid()
plt.legend()
plt.show()
delta120 = abs(l120_fit-0.120)/0.120*100
delta240 = abs(l240_fit-0.240)/0.240*100
print(f"Relativna pogreska za L=120 mm: {delta120:.2f} %")
print(f"Relativna pogreska za L=240 mm: {delta240:.2f} %")
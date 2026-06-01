import numpy as np
import matplotlib.pyplot as plt
h0 = 0.54 
m = 0.5257 
r = 4.025*10**-3
h = [0.14 , 0.17 , 0.19 , 0.22 , 0.25 , 0.28 , 0.31 , 0.34 , 0.37 , 0.40] 
t_mean = [1.740 , 1.793 , 2.043 , 2.190 , 2.280 , 2.417 , 2.540 , 2.640 , 2.670 , 2.813] 
h = np.array(h)
t_mean = np.array(t_mean)
log_h = np.log(h)
log_t = np.log(t_mean)
n = len(log_t)
a = (n*np.sum(log_t*log_h)-np.sum(log_t)*np.sum(log_h))/(n*np.sum(log_t**2)-(np.sum(log_t))**2)
b = (np.sum(log_h)-a*np.sum(log_t))/n
x_sr1 = np.mean(log_t)
y_sr1 = np.mean(log_h)
x2_sr1 = np.mean(log_t**2)
y2_sr1 = np.mean(log_h**2)
sigma_a1 = np.sqrt((1/n)*((y2_sr1-y_sr1**2)/(x2_sr1-x_sr1**2)-a**2))
sigma_b1 = sigma_a1*np.sqrt(x2_sr1)
print(f"Nagib a={a}")
print(f"Odsjecak b={b}")
print(f"sigma_a={sigma_a1}")
print(f"sigma_b={sigma_b1}")
plt.scatter(log_t,log_h,label="Mjerenja")
x = np.linspace(min(log_t),max(log_t),100)
y = a*x+b
plt.plot(x,y,label="Pravac")
plt.xlabel("log(t)")
plt.ylabel("log(h)")
plt.title("graf log(h)-log(t)")
plt.grid()
plt.legend()
plt.show()

t2 = t_mean**2
n = len(t2)
a = (n*np.sum(t2*h)-np.sum(t2)*np.sum(h))/(n*np.sum(t2**2)-(np.sum(t2))**2)
b = (np.sum(h)-a*np.sum(t2))/n
x_sr2 = np.mean(t2)
y_sr2 = np.mean(h)
x2_sr2 = np.mean(t2**2)
y2_sr2 = np.mean(h**2)
sigma_a2 = np.sqrt((1/n)*((y2_sr2-y_sr2**2)/(x2_sr2-x_sr2**2)-a**2))
sigma_b2 = sigma_a2*np.sqrt(x2_sr2)
print(f"a={a}")
print(f"b={b}")
print(f"sigma_a={sigma_a2}")
print(f"sigma_b={sigma_b2}")
plt.scatter(t2,h,label="Mjerenja")
x = np.linspace(min(t2),max(t2),100)
y = a*x +b
plt.plot(x,y,label="Linearni fit")
plt.xlabel("t^2")
plt.ylabel("h")
plt.title("graf h-t^2")
plt.grid()
plt.legend()
plt.show()

a_ef = 2*a
print(f"a_ef={a_ef}")
sigma_a_ef = 2*sigma_a2
print(f"sigma_a_ef={sigma_a_ef}")
g = 9.81
Iz = m*r**2*(g/a_ef-1)
print(f"Iz={Iz}")
sigma_Iz = (m*r**2*g/a_ef**2)*sigma_a_ef
print(f"sigma_Iz={sigma_Iz}")
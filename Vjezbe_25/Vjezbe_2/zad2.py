import numpy as np
import matplotlib.pyplot as plt
v0=float(input("Unesi početnu brzinu u m/s: "))
kut=float(input("Unesi kut u stupnjevima: "))
theta=np.radians(kut)
x0=0
y0=0
dt=0.1
t_max=10
g=9.81
t=np.arange(0, t_max + dt, dt)
v0x=v0*np.cos(theta)
v0y=v0*np.sin(theta)
x = [0] * len(t)
y = [0] * len(t)
vx = [0] * len(t)
vy = [0] * len(t)

vx[0]=v0x
vy[0]=v0y
for i in range(1, len(t)):
    vx[i]=vx[i-1]
    vy[i]=vy[i-1]-g*dt
    x[i]=x[i-1]+vx[i-1]*dt
    y[i]=y[i-1]+vy[i-1]*dt-0.5*g*dt**2
    if y[i] < 0:
        y[i] = 0
        break
plt.figure(figsize=(12, 8))
plt.subplot(3,1,1)
plt.plot(y,x,'r')
plt.title("Graf položaja (x-y)")
plt.xlabel("Horizontalni položaj x [m]")
plt.ylabel("Vertikalni položaj y [m]")
plt.grid(True)
plt.subplot(3, 2, 1)
plt.plot(t,x,'g')
plt.title('Graf x-vrijeme (x-t)')
plt.xlabel('Vrijeme [s]')
plt.ylabel('Položaj x [m]')
plt.grid(True)

plt.subplot(3, 3, 1)
plt.plot(t,y,'b')
plt.title('Graf y-vrijeme (y-t)')
plt.xlabel('Vrijeme [s]')
plt.ylabel('Položaj y [m]')
plt.grid(True)
plt.tight_layout()
plt.show()
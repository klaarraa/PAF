import matplotlib.pyplot as plt
v0 = [1.9,0.5,3.2]
t = 50
dt = 0.001
def simulacija(q, m, E, B, x0, y0, z0, dt, t):
    t0 = 0
    x = [x0]
    y = [y0]
    z = [z0]
    vx = [v0[0]]
    vy = [v0[1]]
    vz = [v0[2]]
    Ex,Ey,Ez = E[0],E[1],E[2]
    Bx,By,Bz = B[0],B[1],B[2]
    while t0 < t:
        Fx = q*(Ex+vy[-1]*Bz-vz[-1]*By)
        Fy = q*(Ey+vz[-1]*Bx-vx[-1]*Bz)
        Fz = q*(Ez+vx[-1]*By-vy[-1]*Bx)
        ax = Fx/m
        ay = Fy/m
        az = Fz/m
        vx.append(vx[-1]+ax*dt)
        vy.append(vy[-1]+ay*dt)
        vz.append(vz[-1]+az*dt)
        x.append(x[-1]+vx[-1]*dt)
        y.append(y[-1]+vy[-1]*dt)
        z.append(z[-1]+vz[-1]*dt)
        t0 += dt
    return x,y,z

def crtaj(E, B, naslov):
    xe,ye,ze = simulacija(-1, 1, E, B, 0, 0, 0, dt, t)
    xp,yp,zp = simulacija(1, 1, E, B, 0, 0, 0, dt, t)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(xe,ye,ze,label="elektron")
    ax.plot(xp,yp,zp,label="pozitron")
    ax.set_title(naslov)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.legend()
    plt.show()
crtaj([0, 0, 0],[0, 0, 1],"Samo B")
crtaj([0, 0, 0.2],[0, 0, 1],"E paralelno s B")
crtaj([0.2, 0, 0],[0, 0, 1],"E okomito na B")
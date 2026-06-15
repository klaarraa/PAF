import numpy as np
m1 = [138.92, 138.98, 139.20, 138.90, 138.92]
m2 = [128.65, 128.60, 128.65, 128.35, 128.50]
m3 = [71.89, 71.90, 71.79, 71.85, 71.70]
D1 = [19.98, 20.18, 20.10, 20.08, 19.74]
D2 = [19.92, 19.82, 19.96, 19.98, 19.88]
D3 = [24.96, 24.98, 24.98, 24.92, 24.94]
L1 = [49.80, 49.00, 50.48, 49.80, 49.96]
L2 = [52.56, 52.50, 52.62, 52.58, 52.54]
L3 = [55.34, 55.40, 55.30, 55.44, 55.48]
R1 = [i/2 for i in D1]
R2 = [i/2 for i in D2]
R3 = [i/2 for i in D3]
def srednje(lista):
    aritm_sredina = sum(lista)/len(lista)
    stand_dev = (sum((i-aritm_sredina)**2 for i in lista)/(len(lista)*(len(lista)-1)))**0.5
    return aritm_sredina, stand_dev
R1_sred,sigmaR1 = srednje(R1)
R2_sred,sigmaR2 = srednje(R2)
R3_sred,sigmaR3 = srednje(R3)
L1_sred,sigmaL1 = srednje(L1)
L2_sred,sigmaL2 = srednje(L2)
L3_sred,sigmaL3 = srednje(L3)
m1_sred, sigmam1 = srednje(m1)
m2_sred, sigmam2 = srednje(m2)
m3_sred, sigmam3 = srednje(m3)
valjci = [(R1_sred/10, sigmaR1/10, L1_sred/10, sigmaL1/10, m1_sred, sigmam1),(R2_sred/10, sigmaR2/10, L2_sred/10, sigmaL2/10, m2_sred, sigmam2),(R3_sred/10, sigmaR3/10, L3_sred/10, sigmaL3/10, m3_sred, sigmam3)]
def volumen_valjka(R, L):
    V = np.pi*R**2*L
    return V
def sigma_volumena(R, sigma_R, L, sigma_L):
    dV_dR = 2*np.pi*R*L
    dV_dL = np.pi*R**2
    sigma_V = np.sqrt((dV_dR*sigma_R)**2 +(dV_dL*sigma_L)**2)
    return sigma_V
def gustoca_valjka(V,m):
    ro = m/V
    return ro
def sigma_gustoce(m,sigmam,V,sigmaV):
    sigma_ro = np.sqrt((sigmam/V)**2+((m*sigmaV)/(V**2))**2)
    return sigma_ro
gustoce = []
for i in range(len(valjci)):
    R,sR,L,sL,m,sm = valjci[i]
    V = volumen_valjka(R,L)
    sV = sigma_volumena(R,sR,L,sL)
    ro = gustoca_valjka(V,m)
    sro = sigma_gustoce(m,sm,V,sV)
    gustoce.append(ro)
    print(f"Valjak {i+1}:")
    print(f"V = ({V:.3e} ± {sV:.3e}) cm^3")
    print(f"ro = ({ro:.3e} ± {sro:.3e}) g/cm^3")
ro_aluminij = 2.7
ro_bakar = 8.92
ro_celik = 7.75 
print(f"Valjak 1: ro = {gustoce[0]:.2f} g/cm^3 - odgovara bakru")
print(f"Valjak 2: ro = {gustoce[1]:.2f} g/cm^3 - odgovara celiku")
print(f"Valjak 3: ro = {gustoce[2]:.2f} g/cm^3 - odgovara aluminiju")
rel_pogreska1 = abs(gustoce[0]-ro_bakar)/ro_bakar*100
rel_pogreska2 = abs(gustoce[1]-ro_celik)/ro_celik*100
rel_pogreska3 = abs(gustoce[2]-ro_aluminij)/ro_aluminij*100
print(f"Valjak 1: relativna pogreska = {rel_pogreska1:.2f}%")
print(f"Valjak 2: relativna pogreska = {rel_pogreska2:.2f}%")
print(f"Valjak 3: relativna pogreska = {rel_pogreska3:.2f}%")
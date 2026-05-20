import numpy as np
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
def volumen_valjka(R, L):
    V = np.pi*R**2*L
    return V
def sigma_volumena(R, sigma_R, L, sigma_L):
    dV_dR = 2*np.pi*R*L
    dV_dL = np.pi*R**2
    sigma_V = np.sqrt((dV_dR*sigma_R)**2 +(dV_dL*sigma_L)**2)
    return sigma_V
valjci = [(R1_sred/10, sigmaR1/10, L1_sred/10, sigmaL1/10),(R2_sred/10, sigmaR2/10, L2_sred/10, sigmaL2/10),(R3_sred/10, sigmaR3/10, L3_sred/10, sigmaL3/10)]
for i in range(len(valjci)):
    R,sR,L,sL = valjci[i]
    V = volumen_valjka(R,L)
    sV = sigma_volumena(R,sR,L,sL)
    print(f"Valjak {i+1}:")
    print(f"V = ({V:.3e} ± {sV:.3e}) cm³")
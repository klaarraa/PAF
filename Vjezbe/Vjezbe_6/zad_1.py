D1 = [19.98, 20.18, 20.10, 20.08, 19.74]
D2 = [19.92, 19.82, 19.96, 19.98, 19.88]
D3 = [24.96, 24.98, 24.98, 24.92, 24.94]
L1 = [49.80, 49.00, 50.48, 49.80, 49.96]
L2 = [52.56, 52.50, 52.62, 52.58, 52.54]
L3 = [55.34, 55.40, 55.30, 55.44, 55.48]
m1 = [138.92, 138.98, 139.20, 138.90, 138.92]
m2 = [128.65, 128.60, 128.65, 128.35, 128.50]
m3 = [71.89, 71.90, 71.79, 71.85, 71.70]
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
m1_sred,sigmam1 = srednje(m1)
m2_sred,sigmam2 = srednje(m2)
m3_sred,sigmam3 = srednje(m3)
print(f"Valjak 1: R1: {R1_sred}, sigmaR1: {sigmaR1}, L1: {L1_sred}, sigmaL1: {sigmaL1}, m1: {m1_sred}, sigmam1: {sigmam1}")
print(f"Valjak 2: R2: {R2_sred}, sigmaR2: {sigmaR2}, L2: {L2_sred}, sigmaL2: {sigmaL2}, m2: {m2_sred}, sigmam2: {sigmam2}")
print(f"Valjak 3: R3: {R3_sred}, sigmaR3: {sigmaR3}, L3: {L3_sred}, sigmaL3: {sigmaL3}, m3: {m3_sred}, sigmam3: {sigmam3}")
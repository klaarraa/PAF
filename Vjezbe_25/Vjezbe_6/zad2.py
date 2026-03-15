import numpy as np
from harmonic_oscillator import HarmonicOscillator

m = 1.0
k = 4.0
x0 = 1.0
v0 = 0.0

osc = HarmonicOscillator(m, k, x0, v0)
T_analiticki = 2 * np.pi / osc.omega

dt_values = [0.5, 0.1, 0.05, 0.01, 0.001]

print("dt        T_numerički     Greška")
for dt in dt_values:
    t = np.arange(0, 20, dt)
    T_num = osc.numericki_period(t)

    if T_num is None:
        print(f"{dt:.4f}    Nije pronađeno")
    else:
        greska = abs(T_num - T_analiticki)
        print(f"{dt:.4f}    {T_num:.6f}     {greska:.6f}")

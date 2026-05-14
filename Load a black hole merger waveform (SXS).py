import sxs  # pip install sxs
import matplotlib.pyplot as plt
import numpy as np

# Example: load a specific SXS simulation by ID
sim = sxs.load("SXS:BBH:0305")  # equal-mass, nonspinning example

# Extract the dominant (l,m) = (2,2) mode of the strain
h = sim.waveform("Strain")
h22 = h[:, 2, 2]  # (time, l, m)

t = h.t  # time array in simulation units (M)

plt.figure(figsize=(8, 4))
plt.plot(t, h22.real, label="Re(h22)")
plt.plot(t, h22.imag, label="Im(h22)", alpha=0.7)
plt.xlabel("t / M")
plt.ylabel("Strain")
plt.legend()
plt.title("SXS Binary Black Hole Merger Waveform (2,2 mode)")
plt.tight_layout()
plt.show()

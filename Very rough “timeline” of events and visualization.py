import numpy as np

def generate_synthetic_timeline(n_events=50):
    events = []
    for _ in range(n_events):
        z = np.random.uniform(0, 3)  # redshift
        m1 = 10 ** np.random.uniform(0.7, 1.5)  # ~5–30 Msun
        m2 = 10 ** np.random.uniform(0.7, 1.5)
        chi1z = np.random.uniform(-0.9, 0.9)
        chi2z = np.random.uniform(-0.9, 0.9)
        events.append(BHMergerEvent(z, m1, m2, chi1z, chi2z))
    # Sort by cosmic time (monotonic with decreasing z in simple models)
    events.sort(key=lambda e: e.z, reverse=True)
    return events

timeline = generate_synthetic_timeline()

zs = [e.z for e in timeline]
mass_totals = [e.m1 + e.m2 for e in timeline]

plt.figure(figsize=(6, 4))
plt.scatter(zs, mass_totals, c=mass_totals, cmap="plasma")
plt.gca().invert_xaxis()
plt.xlabel("Redshift z (earlier → right)")
plt.ylabel("Total mass (Msun)")
plt.title("Synthetic Timeline of BH Mergers")
plt.colorbar(label="Total mass (Msun)")
plt.tight_layout()
plt.show()

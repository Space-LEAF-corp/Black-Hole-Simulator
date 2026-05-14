Cosmic Event Reconstruction & Black Hole Merger Simulation Framework

A research‑grade toolkit for generating, analyzing, and visualizing cosmic‑scale gravitational events using real astrophysical data.
This project provides a modular pipeline for:

• Reverse‑mapping gravity fields from known black hole mergers
• Synthesizing cosmic timelines of stellar collapse and compact‑object mergers
• Attaching full numerical‑relativity waveforms from public catalogs
• Simulating supernovae, black hole formation, and binary mergers
• Building interactive, data‑driven visualizations for scientific exploration


The goal is to give researchers, students, and developers a digitized universe sandbox where they can explore realistic astrophysical events without waiting for rare cosmic occurrences.

---

🚀 Features

• Population Synthesis Engine
Generates statistically realistic black hole and neutron star populations across cosmic time.
• Numerical Relativity Integration
Automatically matches events to the closest waveform in the SXS, RIT, or Georgia Tech catalogs.
• Gravity‑Field Reverse Mapping
Extracts waveform modes, remnant properties, and spacetime dynamics for pattern analysis.
• Supernova → Black Hole Pipeline
Converts progenitor stars into compact remnants using metallicity‑dependent mass‑loss models.
• Interactive Simulation Interface
Lets users “blow up” stars, merge black holes, and visualize gravitational waves.
• Modular Python API
Designed for research, teaching, and rapid experimentation.


---

📦 Installation

pip install sxs numpy matplotlib


Additional optional packages:

pip install gwpy h5py scipy


---

📚 Project Structure

cosmic-sim/
│
├── population/          # Event generators & cosmic timeline synthesis
├── waveforms/           # NR catalog loaders & waveform utilities
├── physics/             # Stellar evolution, collapse models, remnant mapping
├── interface/           # Interactive simulation & visualization tools
├── examples/            # Jupyter notebooks & demo scripts
└── README.md


---

🌀 Quick Start Example

Load a real black hole merger waveform

import sxs
import matplotlib.pyplot as plt

sim = sxs.load("SXS:BBH:0305")
h = sim.waveform("Strain")
h22 = h[:, 2, 2]

plt.plot(h.t, h22.real)
plt.title("SXS (2,2) Mode — Binary Black Hole Merger")
plt.xlabel("t / M")
plt.ylabel("Strain")
plt.show()


---

🌌 Generate a Synthetic Cosmic Timeline

from population.timeline import generate_synthetic_timeline

events = generate_synthetic_timeline(n_events=50)

for e in events[:5]:
    print(e)


---

🧲 Attach a GR Waveform to an Event

from waveforms.attach import attach_waveform

event = events[0]
waveform = attach_waveform(event)


---

🔥 Simulate a Star Explosion → Black Hole Formation

from physics.supernova import progenitor_to_bh_mass

M_star = 40.0   # Msun
Z = 0.004       # metallicity
M_bh = progenitor_to_bh_mass(M_star, Z)

print("BH mass:", M_bh)


---

📈 Visualizing the Cosmic Event Timeline

from interface.visualize import plot_timeline

plot_timeline(events)


---

🔍 Research Applications

• Black hole population studies
• Gravitational‑wave astrophysics
• Stellar evolution modeling
• Cosmological event‑rate predictions
• Educational visualization tools
• Machine‑learning datasets for waveform prediction


---

🧭 Roadmap

• Add eccentric binary support
• Integrate MESA stellar evolution tracks
• GPU‑accelerated waveform interpolation
• Web‑based simulation UI
• Support for neutron‑star EOS models


---

🤝 Contributing

Pull requests are welcome.
If you’d like to add new physics modules, waveform catalogs, or visualization tools, open an issue to discuss your ideas.

---

📜 License

MIT License — see LICENSE for details.

---

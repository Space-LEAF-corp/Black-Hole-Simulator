from dataclasses import dataclass

@dataclass
class BHMergerEvent:
    z: float
    m1: float
    m2: float
    chi1z: float
    chi2z: float
    catalog_id: str | None = None

def choose_closest_sxs_sim(m1, m2, chi1z, chi2z):
    # Placeholder: in reality you’d query the SXS metadata
    # and minimize distance in (mass ratio, spins, etc.)
    q = m1 / m2 if m1 >= m2 else m2 / m1
    if abs(q - 1.0) < 0.1 and abs(chi1z) < 0.1 and abs(chi2z) < 0.1:
        return "SXS:BBH:0305"
    # Fallback or more sophisticated matching here
    return "SXS:BBH:0001"

def attach_waveform(event: BHMergerEvent):
    if event.catalog_id is None:
        event.catalog_id = choose_closest_sxs_sim(
            event.m1, event.m2, event.chi1z, event.chi2z
        )
    sim = sxs.load(event.catalog_id)
    h = sim.waveform("Strain")
    return h

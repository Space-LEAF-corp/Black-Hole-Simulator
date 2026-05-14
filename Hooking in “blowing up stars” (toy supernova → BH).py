def progenitor_to_bh_mass(M_star, metallicity):
    # Very rough toy mapping: lower metallicity → weaker winds → heavier BH
    wind_factor = 0.3 + 0.5 * (metallicity / 0.02)  # 0.02 ~ solar
    wind_factor = np.clip(wind_factor, 0.1, 0.8)
    return M_star * (1 - wind_factor)

M_star = 40.0  # Msun
Z = 0.004      # low metallicity
M_bh = progenitor_to_bh_mass(M_star, Z)
print("Progenitor:", M_star, "Msun → BH:", M_bh, "Msun")

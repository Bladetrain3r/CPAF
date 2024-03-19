import math

# Constants
radius_ly = 46.5e9  # Radius of the observable universe in light-years
ly_to_pc = 0.306601  # Conversion factor from light-years to parsecs
num_galaxies = 2e12  # Estimated number of galaxies in the observable universe

# Calculations
radius_pc = radius_ly * ly_to_pc
volume_pc3 = (4/3) * math.pi * (radius_pc ** 3)
density_galaxies_per_pc3 = num_galaxies / volume_pc3

print(density_galaxies_per_pc3)

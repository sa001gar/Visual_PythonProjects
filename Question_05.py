#program to calculate the mass m in a chemical reaction
import matplotlib.pyplot as plt
import numpy as np

def calculate_mass(t):
    return 60 / (t + 2)

# Generate time values from 0 to 10 hours
time_values = np.arange(0, 11, 1)

# Calculate mass values using the formula
mass_values = calculate_mass(time_values)

# Plotting the graph
plt.plot(time_values, mass_values, marker='o')
plt.title('Mass vs. Time')
plt.xlabel('Time (hours)')
plt.ylabel('Mass (g)')
plt.grid(True)
plt.show()

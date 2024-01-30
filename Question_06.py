# Plotting P vs t graph for the specified time interval
import matplotlib.pyplot as plt 
import numpy as np

def calculate_population(t):
    return (15000 * (1 + t)) / (15 + np.exp(1))

# Generate time values for the specified time interval (e.g., 0 to 10 hours)
time_values = np.arange(0, 11, 1)

# Calculate population using the formula
population_values = calculate_population(time_values)

# Plotting the graph
plt.plot(time_values, population_values, marker='o')
plt.title('Population vs. Time')
plt.xlabel('Time (hours)')
plt.ylabel('Population')
plt.grid(True)
plt.show()

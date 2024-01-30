#Plotting the graphs of the equations of motion
import matplotlib.pyplot as plt
import numpy as np

def velocity_vs_time(u, a, t_values):
    return u + a * t_values

def distance_vs_time(u, a, t_values):
    return u * t_values + 0.5 * a * t_values**2

def distance_vs_velocity(u, v_values, a):
    return (v_values**2 - u**2) / (2 * a)

# Input initial velocity (u) and acceleration (a)
u = float(input("Enter initial velocity (u): "))
a = float(input("Enter acceleration (a): "))

# Generating time values for the specified time interval (e.g., 0 to 10 seconds)
t_values = np.arange(0, 11, 1)

# Calculating velocity, distance vs. time, and distance vs. velocity
velocity_values = velocity_vs_time(u, a, t_values)
distance_time_values = distance_vs_time(u, a, t_values)
distance_velocity_values = distance_vs_velocity(u, velocity_values, a)

# Plotting the graphs
plt.figure(figsize=(15, 5))

# Plot velocity vs. time
plt.subplot(1, 3, 1)
plt.plot(t_values, velocity_values, marker='o')
plt.title('Velocity vs. Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity')

# Plot Distance vs. time
plt.subplot(1, 3, 2)
plt.plot(t_values, distance_time_values, marker='o')
plt.title('Distance vs. Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Distance')

# Plot Distance vs. velocity
plt.subplot(1, 3, 3)
plt.plot(velocity_values, distance_velocity_values, marker='o')
plt.title('Distance vs. Velocity')
plt.xlabel('Velocity')
plt.ylabel('Distance')

plt.tight_layout()
plt.show()

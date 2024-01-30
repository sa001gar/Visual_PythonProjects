#graph of people with pulse rate p vs. height h
import matplotlib.pyplot as plt
#create 
def plot_pulse_rate_vs_height():
    num_people = int(input("Enter the number of people: "))
    # Lists to store pulse rate and height values
    pulse_rates = []
    heights = []
    
    for i in range(num_people):
        pulse_rate = float(input(f"Enter pulse rate for person {i + 1}: "))
        height = float(input(f"Enter height for person {i + 1} (in cm): "))

        pulse_rates.append(pulse_rate)
        heights.append(height)

    # Plotting the graph
    plt.plot(heights, pulse_rates, color='blue', marker='o')
    plt.title('Pulse Rate vs. Height')
    plt.xlabel('Height (cm)')
    plt.ylabel('Pulse Rate')
    plt.grid(True)
    plt.show()

# Calling the function to plot the graph
plot_pulse_rate_vs_height()

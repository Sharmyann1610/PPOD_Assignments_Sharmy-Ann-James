import matplotlib.pyplot as plt

# Data
algorithms = ['Generalisation', 'k-means', 'Incognito', 'Combination Discovery']
# time obtained from execution_time.py
times = [1.39750, 3.18931, 1.77211, 0.81400]

# Plotting
plt.bar(algorithms, times, color='blue')

# Customizing the plot
plt.title('Time taken by anonymisation algorithms')
plt.xlabel('Anonymisation algorithms')
plt.ylabel('Time taken (in seconds)')

# Displaying the plot
plt.show()
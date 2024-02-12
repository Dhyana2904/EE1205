import numpy as np
import matplotlib.pyplot as plt

# Define the time values
t = np.linspace(0, 6*np.pi, 1000)

# Define the function sin^3(wt)
w = 1  # You can adjust the value of w as needed
y = (np.sin(w * t))**3

# Plot the graph
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('sin^3(wt)')
plt.title('Graph of sin^3(wt)')
plt.savefig('a1_fig2.png')


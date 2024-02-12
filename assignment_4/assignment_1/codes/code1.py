import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 2*np.pi, 1000)  # You can adjust the range and number of points as needed
omega = 1.0  
y = np.sin(omega * t) - np.cos(omega * t)
plt.plot(t, y)
plt.title(r'$\sin(\omega t) - \cos(\omega t)$')
plt.xlabel('Time (t)')
plt.ylabel('Function Value')
plt.grid(True)
plt.savefig('a1_fig1.png')

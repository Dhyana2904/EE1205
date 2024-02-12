import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)
omega = 1.0
y = 3 * np.cos(np.pi/4 - 2 * omega * t)

plt.plot(t, y)
plt.title(r'$3 \cos\left(\frac{\pi}{4} - 2\omega t\right)$')
plt.xlabel('Time (t)')
plt.ylabel('Function Value')
plt.grid(True)

plt.savefig('a1_fig3.png')

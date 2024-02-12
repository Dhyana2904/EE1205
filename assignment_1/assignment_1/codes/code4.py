import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)
omega = 1.0
y = np.cos(omega * t) + np.cos(3 * omega * t) + np.cos(5 * omega * t)

plt.plot(t, y)
plt.title(r'$\cos(\omega t) + \cos(3\omega t) + \cos(5\omega t)$')
plt.xlabel('Time (t)')
plt.ylabel('Function Value')
plt.grid(True)

plt.savefig('a1_fig4.png')

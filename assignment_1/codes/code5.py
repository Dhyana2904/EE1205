import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-3, 3, 1000)
omega = 1.0
y = np.exp(-omega**2 * t**2)

plt.plot(t, y)
plt.title(r'$e^{-\omega^2 t^2}$')
plt.xlabel('Time (t)')
plt.ylabel('Function Value')
plt.grid(True)

plt.savefig('a1_fig5.png')

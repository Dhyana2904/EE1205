import matplotlib.pyplot as plt
import numpy as np

def plot_and_save(file_path, function_label, save_filename):
    data = np.loadtxt(file_path)
    t = data[:, 0]
    function_data = data[:, 1]
    plt.plot(t, function_data)
    plt.xlabel('Time (t)')
    plt.ylabel('Function Value')
    plt.title(function_label)
    plt.grid(True)
    plt.savefig(save_filename)
    plt.clf()

# Plot and save each function in a separate graph
plot_and_save('function1_data.txt', r'$\sin(\omega t) - \cos(\omega t)$', 'fig1.png')
plot_and_save('function2_data.txt', r'$\sin^3(\omega t)$', 'fig2.png')
plot_and_save('function3_data.txt', r'$3\cos\left(\frac{\pi}{4} - 2\omega t\right)$', 'fig3.png')
plot_and_save('function4_data.txt', r'$\cos(\omega t) + \cos(3\omega t) + \cos(5\omega t)$', 'fig4.png')
plot_and_save('function5_data.txt', r'$\exp(-\omega^2 t^2)$', 'fig5.png')
plot_and_save('function6_data.txt', r'$1 + \omega t + \omega^2 t^2$', 'fig6.png')


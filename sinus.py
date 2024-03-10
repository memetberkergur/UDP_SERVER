import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Veriyi oluştur
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Grafiği oluştur
fig, ax = plt.subplots()
line, = ax.plot(x, y)
ax.set_ylim(-1.5, 1.5)  # Y eksenini sınırla

# Animasyonu güncelleme fonksiyonu
def update(frame):
    y = np.sin(x + frame * 0.1)
    line.set_ydata(y)
    return line,

# FuncAnimation kullanarak animasyonu oluştur
ani = FuncAnimation(fig, update, frames=range(100), blit=True)

# Grafik penceresini göster
plt.show()

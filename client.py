import socket
import numpy as np
import time

# Server ayarları
server_host = '192.168.1.4'  # Server'ın IP adresi
server_port = 12345           # Server'ın portu

# UDP soketini oluştur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Veriyi oluştur
sampling_rate = 100  # Örnekleme oranı (örneğin, 100 örnek/s)
periyot = 2 * np.pi
num_samples = 100  # Bir periyotta kaç örnek olacak
x = np.linspace(0, periyot, num_samples)
y = np.sin(x)

try:
    while True:
        for sample in y:
            # Veriyi server'a gönder
            
            client_socket.sendto((str(round(sample, 6))+'\r').encode(), (server_host, server_port))
            
            # Bekleme süresi, örnekleme oranına göre ayarlanmalı
            time.sleep(1 / sampling_rate)
except KeyboardInterrupt:
    print("Client kapatılıyor...")
finally:
    # Soketi kapat
    client_socket.close()

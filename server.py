import socket

# Server ayarları
server_host = '0.0.0.0'  # Tüm ağ arayüzleri üzerinden dinleme
server_port = 12345       # Dinlenecek port

# UDP soketini oluştur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server'ı belirtilen adreste ve portta dinle
server_socket.bind((server_host, server_port))

print(f"Server dinleniyor... ({server_host}:{server_port})")

try:
    while True:
        # Gelen veriyi al
        data, addr = server_socket.recvfrom(1024)
        print(f"Received data from {addr}: {data.decode()}")
except KeyboardInterrupt:
    print("Server kapatılıyor...")
finally:
    # Soketi kapat
    server_socket.close()

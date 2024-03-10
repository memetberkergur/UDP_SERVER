import socket

# Server ayarları
server_host = '192.168.1.55'  # Server'ın IP adresi
server_port = 12345             # Server'ın portu

# UDP soketini oluştur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_host, server_port))

print(f"UDP server dinleniyor. Host: {server_host}, Port: {server_port}")

try:
    while True:
        data, address = server_socket.recvfrom(1024)
        print(f"Gelen veri ({address}): {data.decode()}")
except KeyboardInterrupt:
    print("Server kapatılıyor...")
finally:
    # Soketi kapat
    server_socket.close()

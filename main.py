import socket

# Sunucu ayarları
host = '127.0.0.1'  # localhost
port = 12345

# UDP soketini oluştur
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Soketi belirtilen host ve port'a bağla
udp_socket.bind((host, port))

print(f"UDP Sunucu {host}:{port}'ta dinleniyor...")

try:
    while True:
        # Gelen veriyi al
        data, addr = udp_socket.recvfrom(1024)
        
        # Alınan veriyi ekrana yazdır
        print(f"Gelen veri: {data.decode()} from {addr}")
except KeyboardInterrupt:
    print("Sunucu kapatılıyor...")
finally:
    # Soketi kapat
    udp_socket.close()

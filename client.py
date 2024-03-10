import socket

# Server ayarları
server_host = '192.168.1.100'  # Server'ın IP adresi
server_port = 12345             # Server'ın portu

# UDP soketini oluştur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        # Gönderilecek veriyi kullanıcıdan al
        message = input("Gönderilecek veri: ")

        # Veriyi belirtilen server'a gönder
        client_socket.sendto(message.encode(), (server_host, server_port))
except KeyboardInterrupt:
    print("Client kapatılıyor...")
finally:
    # Soketi kapat
    client_socket.close()

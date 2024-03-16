import socket

class UDP_Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))
        print(f"UDP server dinleniyor. Host: {self.host}, Port: {self.port}")

    def idle(self):
        print("UDP server idle durumunda...")
        while True:
            data, address = self.server_socket.recvfrom(1024)
            print(f"Gelen veri ({address}): {data.decode()}")

    def response(self, message, target_host, target_port):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(message.encode(), (target_host, target_port))
        print(f"Mesaj gönderildi: {message}")

    def close(self):
        self.server_socket.close()
        print("UDP server kapatıldı.")

# Kullanım örneği
if __name__ == "__main__":
    host = '192.168.1.4'  # Server'ın IP adresi
    port = 12345           # Server'ın portu

    server = UDP_Server(host, port)
    try:
        server.idle()
    except KeyboardInterrupt:
        print("Server kapatılıyor...")
    finally:
        server.close()

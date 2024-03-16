import socket
import threading
import time

class UDP_Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))
        self.clients = []  # Gelen bağlantıların adres ve portunu tutacak liste
        print(f"UDP server dinleniyor. Host: {self.host}, Port: {self.port}")

    def idle(self):
        print("UDP server idle durumunda...")
        while True:
            data, address = self.server_socket.recvfrom(1024)
            print(f"Gelen veri ({address}): {data.decode()}")
            if address not in self.clients:
                self.clients.append(address)  # Yeni bağlantıyı listeye ekle

    def response(self, message, interval=2):
        while True:
            for client in self.clients:
                client_host, client_port = client
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                client_socket.sendto(message.encode(), (client_host, client_port))
                print(f"Mesaj gönderildi: {message} - {client_host}:{client_port}")
            time.sleep(interval)

    def close(self):
        self.server_socket.close()
        print("UDP server kapatıldı.")

# Kullanım örneği
if __name__ == "__main__":
    host = '192.168.1.4'  # Server'ın IP adresi
    port = 12345           # Server'ın portu

    server = UDP_Server(host, port)
    try:
        # Veri gönderme işlemi başlatılıyor
        response_thread = threading.Thread(target=server.response, args=("Merhaba!",))
        response_thread.start()

        # Ana döngü
        server.idle()
    except KeyboardInterrupt:
        print("Server kapatılıyor...")
    finally:
        server.close()

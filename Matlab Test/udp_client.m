% Hedef UDP sunucu IP adresi ve port numarası
serverIP = '192.168.1.4'; % Sunucu IP'si
serverPort = 12345; % Sunucu port numarası

% UDP nesnesini oluşturun
udpClient = udp(serverIP, serverPort, 'LocalPort', 0, 'OutputBufferSize', 1024);

% UDP nesnesini açın
fopen(udpClient);

try
    disp(['UDP İstemci başlatıldı. Bağlanılan Sunucu IP: ', serverIP, ', Port: ', num2str(serverPort)]);
    i = 0;
    while true
        % Gönderilecek mesaj
        messageToSend = strcat('TEST',num2str(i));
        
        % Mesajı gönderin
        fwrite(udpClient, messageToSend, 'char');
        
        disp(['Mesaj Gönderildi: ', messageToSend]);
        i = i+1
        % Belirli bir süre bekleyin (örneğin, 1 saniye)
        pause(0.1)
    end
catch
    % Hata oluştuğunda veya kullanıcı Ctrl+C yaparsa çalışacak kod
    disp('UDP İstemci kapatıldı.');
    fclose(udpClient);
    delete(udpClient);
end

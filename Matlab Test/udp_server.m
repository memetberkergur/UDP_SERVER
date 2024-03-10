% Server ayarları
serverHost = '192.168.1.4';  % Server'ın IP adresi
serverPort = 12345;      % Server'ın portu

% UDP nesnesini oluştur
udpServer = udp(serverHost, serverPort, 'LocalPort', serverPort, 'Timeout',1)
udpServer.Status
disp(['UDP Sunucu dinleniyor. Host: ', serverHost, ', Port: ', num2str(serverPort)]);
try
    % UDP nesnesini aç
    fopen(udpServer)

    while true
        % Gelen veriyi al
        receivedData = fread(udpServer, udpServer.BytesAvailable, 'char');
        
        % Eğer veri geldiyse ekrana yazdır
        if ~isempty(receivedData)
            disp(['Gelen Veri: ', char(receivedData')]);
        end
        
    end
catch
    % Hata oluştuğunda veya kullanıcı Ctrl+C yaparsa çalışacak kod
    disp('UDP Sunucu kapatıldı.');
    fclose(udpServer);
    delete(udpServer);
end

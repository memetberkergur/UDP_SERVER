clear all;
clear;
clc;

% UDP sunucu için IP adresi ve port numarası
localIP = '192.168.1.55';
localPort = 12345;

% UDP nesnesini oluşturun
udpServer = udpport("LocalPort", localPort);
configureTerminator(udpServer, "CR");

% Queue oluştur
udpQueue = cell(1, 0);

% Grafik için bir figure oluştur
figure;

while true
    % UDP'den veriyi oku
    receivedData = readline(udpServer);
    
    % Okunan veriyi queue'e ekle
    udpQueue{end+1} = receivedData;
    
    % Ekrana yazdır (isteğe bağlı)
    disp(['Alınan Veri: ', receivedData]);
    
    % Grafik güncelleme
    plot(1:length(udpQueue), cellfun(@str2double, udpQueue));
    title('UDP Veri Grafiği');
    xlabel('Okunan Veri Sayısı');
    ylabel('Okunan Veri Değeri');
    
    drawnow; % Grafik güncellemesini sağla
end

% UDP nesnesini temizle
clear udpServer;

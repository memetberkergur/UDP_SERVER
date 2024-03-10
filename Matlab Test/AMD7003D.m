classdef AMD7003D
    properties (Access = private)
        deviceParams
    end
    properties (Access = public)
        deviceData
    end

    %Public Methods
    methods (Access = public)
        %Constructor for AMD7003D
        function obj = AMD7003D(deviceIP, devicePort)
            obj.deviceParams = struct('deviceIP', deviceIP, 'devicePORT', devicePort);
            obj.deviceData = struct("acceleration",[],"encoder",[],"temperature",[]);
        end
    
        function [port,error] = connectAMD(obj)
            % Bu fonksiyon cihaza ilk bağlantıyı yapar.
            % Port değerini ve error'u döndürür.
            port = 1000;
            error = true;
        end

        function [data] = getData(obj,device,data)
            obj.udpRead();
        end

        function info(obj)
            disp(['Cihaz IP: ', obj.deviceParams.deviceIP, ' Cihaz Port: ', obj.deviceParams.devicePORT]);
            disp(obj.deviceData);
        end
    end

end

from DataBase import *
from Modbus.ModbusBase import *
from Modbus.ReadRequest import *
from Modbus.Signal import *

def packRequest(base_info,signal_info):
    unitID = base_info["station_address"]
    signals_in_list = list(signal_info.values())
    list_of_request = list()
    for i in range(0,len(signals_in_list)):
        function_code = -1
        match signals_in_list[i].SignalType:
            case "DO":
                function_code = 1
            case "DI":
                function_code = 2
            case "AO":
                function_code = 3
            case "AI":
                function_code = 4
        base = ModbusBase(unitID,function_code)
        request = ModbusReadRequest(base,signals_in_list[i].StartAddress,signals_in_list[i].Num_reg)
        list_of_request.append(repack(request))
        request = repack(request)
        print(f"Length of the byte array: {len(request)} bytes")

        for byte in request:
            print(hex(byte), end=' ')
    print(list_of_request[0])
    return list_of_request




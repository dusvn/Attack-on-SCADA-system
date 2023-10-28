import socket

import main
from Modbus.ReadResponse import *
from DataBase import *
from Modbus.ModbusBase import *
from Modbus.ReadRequest import *
from Modbus.Signal import *
from SendReadRequest import *
from main import *

def findAddres(repackRequest : bytearray):
    address = socket.ntohs(repackRequest[8:10])
    print(address)
    return address

def Acquisition(base_info,signal_info):
    pack_request = packRequest(base_info,signal_info)
    for message in pack_request:
        read = findAddres(message)
        main.client.send(message.encode())
        response = main.client.recv(1024)
        response_message = ResponseMessage(response.decode())
        parseResponse(response_message,read,signal_info)
        print(signal_info[1000].__str__())

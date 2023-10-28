import socket

import main
from Modbus.ReadResponse import *
from DataBase import *
from Modbus.ModbusBase import *
from Modbus.ReadRequest import *
from Modbus.Signal import *
from SendReadRequest import *
from main import *

def repackToReadRequest(request : bytearray):
    base = ModbusBase(socket.ntohs(request[6]),socket.ntohs(request[7]))
    read = ModbusReadRequest(base,int.from_bytes(socket.ntohs(request[8:10]),byteorder="big",signed=False),
                             int.from_bytes(socket.ntohs(request[10:12]),byteorder="big",signed=False))
    return read

def Acquisition(base_info,signal_info):
    pack_request = packRequest(base_info,signal_info)
    for message in pack_request:
        read = repackToReadRequest(message)
        main.client.send(message.encode())
        response = main.client.recv(1024)
        response_message = ResponseMessage(response.decode())
        parseResponse(response_message,read,signal_info)


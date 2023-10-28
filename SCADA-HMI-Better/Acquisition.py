import socket

import main
from Modbus.ReadResponse import *
from DataBase import *
from Modbus.ModbusBase import *
from Modbus.ReadRequest import *
from Modbus.Signal import *
from SendReadRequest import *
from main import *

def findAddres(repackRequest):
    address = socket.ntohs(repackRequest[8:10])
    return address

def Acquisition(base_info,signal_info):
    pack_request = packRequest(base_info,signal_info)
    for message in pack_request:
        address = findAddres(message) # addres od trenutnog zahteva se cuva
        main.client.send(message.encode()) # salje se poruka
        response = main.client.recv(1024) # prima se odgovor
        response_message = ResponseMessage(response.decode()) #dekodira se
        parseResponse(response_message,address,signal_info)   #cuva se globalno
        print(signal_info[1000].__str__()) # printa se promena
        print(signal_info[2000].__str__())
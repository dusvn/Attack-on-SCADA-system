import socket
import time as t

from Modbus.ReadResponse import *
from DataBase import *
from Modbus.ModbusBase import *
from Modbus.ReadRequest import *
from Modbus.Signal import *
from SendReadRequest import *
from Modbus.ReadResponse import *
def findAddres(repackRequest):
    address = int.from_bytes(repackRequest[8:10],byteorder="big",signed=False)
    return address
def Acquisition(base_info,signal_info,client):
    while True:
        pack_request = packRequest(base_info,signal_info)
        for message in pack_request:
            address = findAddres(message) # addresa koja se azurira u toj iteraciji
            client.send(message)# salje se poruka
            response = client.recv(1024) # prima se odgovor
            modbusresponse = repackReadResponse(response) # prepakuje u response objekat
            signal_info[address].setcurrentValue(modbusresponse.getData()) # azurira u dictionary
        t.sleep(1)

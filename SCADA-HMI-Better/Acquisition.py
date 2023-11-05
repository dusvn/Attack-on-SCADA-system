import socket
import time as t

from Modbus.ReadResponse import *
from DataBase import *
from Modbus.ModbusBase import *
from Modbus.ReadRequest import *
from Modbus.Signal import *
from Modbus.WriteRequest import *
from Modbus.WriteResponse import *
from SendReadRequest import *
from Modbus.ReadResponse import *
import threading
from AutomationManager import *




def findAddres(repackRequest):
    address = int.from_bytes(repackRequest[8:10],byteorder="big",signed=False)
    return address


def Acquisition(base_info,signal_info,client):
    while True:
        pack_request = packRequest(base_info,signal_info)
        for message in pack_request:
            address = findAddres(message)
            functionCode = int.from_bytes(message[7:8],byteorder="big",signed=False)
            client.send(message)
            response = client.recv(1024)
            op = eOperation(response,functionCode)
            if op==False:
                modbusresponse = repackReadResponse(response)
                signal_info[address].setcurrentValue(modbusresponse.getData())
        Automation(client,signal_info,base_info)
        t.sleep(1)

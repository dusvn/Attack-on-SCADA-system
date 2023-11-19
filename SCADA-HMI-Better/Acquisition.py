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
<<<<<<< HEAD


=======
>>>>>>> origin/moco
def Acquisition(base_info,signal_info,client):
    while True:
        pack_request = packRequest(base_info,signal_info)
        for message in pack_request:
<<<<<<< HEAD
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
=======
            address = findAddres(message) # addresa koja se azurira u toj iteraciji
            client.send(message)# salje se poruka
            response = client.recv(1024) # prima se odgovor
            modbusresponse = repackReadResponse(response) # prepakuje u response objekat
            signal_info[address].setcurrentValue(modbusresponse.getData()) # azurira u dictionary
        dict_for_update = takeAnalogDigitalOutput(signal_info) # nakon akvizicije uzimam podatke za update
        Automation(dict_for_update,client,signal_info,base_info)
        t.sleep(2)
>>>>>>> origin/moco

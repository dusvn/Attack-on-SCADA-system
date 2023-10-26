"""
Test
"""
import socket

from Modbus import ModbusBase
from Modbus.ModbusBase import *
from Modbus.ReadRequest import *
from Modbus.ReadResponse import *
from Modbus.WriteRequest import *
from Modbus.WriteResponse import *
from ByteArrayConverter import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import ctypes
import time as t
import sys
from CustomWindow import *
from DataBase import *


#base_objekat = ModbusBase(ctypes.c_ushort(1),ctypes.c_ushort(1),ctypes.c_ushort(1),ctypes.c_byte(1),ctypes.c_byte(1))
#readRequest = ModbusReadRequest(base_objekat,ctypes.c_ushort(1),ctypes.c_ushort(1))
#readResponse = ModbusReadReasponse(base_objekat,ctypes.c_byte(1),bytearray([10,11]))
#writeResponse = ModbusWriteRequest(base_objekat,ctypes.c_ushort(10),ctypes.c_ushort(80))
#print(writeResponse.__str__())

"""Konekcija scadaHMI-simulator"""
def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    try:
        client.connect(('127.0.0.1', 25252))
        return True
    except ConnectionRefusedError:
        print("Could not connect to the server. Server may not be running or address/port is incorrect.")
    except Exception as e:
        print(f"An error occurred: {e}")



#print("Veza sa SCADA simulatorom je uspostavljena")
#t.sleep(60)
#baseTest = ModbusBase(1,0,2,1,1)
#readTest = ModbusReadRequest(baseTest,1,2)

#toSend  = repack(readTest)
#print(toSend)
#client.send(toSend)
#t.sleep(40)
#bajtovi = client.recv()
#readResponseTest = decodeBytes(bajtovi)
#print(readResponseTest)
#print("Veza je prekina")
#client.close()


def testNewLength():
    testBase = ModbusBase.ModbusBase(300, 1, 1, 1)
    testRead = ModbusReadRequest(testBase,1,1)
    testOdgovor = ModbusReadReasponse(testBase,10,bytearray([10,111,1,1,1]))
    print(testOdgovor)
if __name__ == '__main__':
    main()
    #printBaseInfo(base_info)
    #printSignalInfo(signal_info)
    #makeTuplesForPrint(signal_info)
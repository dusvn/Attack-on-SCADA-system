"""
Test
"""
import socket
from ModbusBase import *
from ReadRequest import *
from ReadResponse import *
from WriteRequest import *
from WriteResponse import *
from ByteArrayConverter import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import ctypes
import time as t
import sys
from CustomWindow import *



#base_objekat = ModbusBase(ctypes.c_ushort(1),ctypes.c_ushort(1),ctypes.c_ushort(1),ctypes.c_byte(1),ctypes.c_byte(1))
#readRequest = ModbusReadRequest(base_objekat,ctypes.c_ushort(1),ctypes.c_ushort(1))
#readResponse = ModbusReadReasponse(base_objekat,ctypes.c_byte(1),bytearray([10,11]))
#writeResponse = ModbusWriteRequest(base_objekat,ctypes.c_ushort(10),ctypes.c_ushort(80))
#print(writeResponse.__str__())

"""Konekcija scadaHMI-simulator"""
#client = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
#client.connect(('127.0.0.1',25252))
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
    testBase = ModbusBase(1,1,1,1)
    testRead = ModbusReadRequest(testBase,1,1)
    print(testRead)
if __name__ == '__main__':
    #main()
    testNewLength()

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
from Connection import *

#base_objekat = ModbusBase(ctypes.c_ushort(1),ctypes.c_ushort(1),ctypes.c_ushort(1),ctypes.c_byte(1),ctypes.c_byte(1))
#readRequest = ModbusReadRequest(base_objekat,ctypes.c_ushort(1),ctypes.c_ushort(1))
#readResponse = ModbusReadReasponse(base_objekat,ctypes.c_byte(1),bytearray([10,11]))
#writeResponse = ModbusWriteRequest(base_objekat,ctypes.c_ushort(10),ctypes.c_ushort(80))
#print(writeResponse.__str__())

"""Konekcija scadaHMI-simulator"""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)





#toSend  = repack(readTest)
#print(toSend)
#client.send(toSend)
#t.sleep(40)
#bajtovi = client.recv()
#readResponseTest = decodeBytes(bajtovi)
#client.close()

if __name__ == '__main__':
    #printBaseInfo(base_info)
    is_connected = connect(client, base_info)
    main()

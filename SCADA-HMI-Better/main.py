"""
Test
"""
import socket
import threading
from Modbus import ModbusBase
from Modbus.ModbusBase import *
from Modbus.ReadRequest import *
from Modbus.ReadResponse import *
from Modbus.WriteRequest import *
from Modbus.WriteResponse import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import ctypes
import time as t
import sys
from CustomWindow import *
from DataBase import *
from Connection import *
from SendReadRequest import *
from Acquisition import *
"""Konekcija scadaHMI-simulator"""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)





#toSend  = repack(readTest)
#print(toSend)
#client.send(toSend)
#t.sleep(40)
#bajtovi = client.recv()
#readResponseTest = decodeBytes(bajtovi)





if __name__ == '__main__':
    is_connected = connect(client, base_info)
    base = ModbusBase(1,1)
    read = ModbusReadRequest(base,1000,1)
    prepakuj = repack(read)
    address = findAddres(prepakuj)
    print("Printovananje prepakovanog\n")
    print(f"{prepakuj}\n")
    prepakuj1 = repackToReadRequest(prepakuj)
    print(prepakuj1)
    main()

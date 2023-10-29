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






#toSend  = repack(readTest)
#print(toSend)
#client.send(toSend)
#t.sleep(40)
#bajtovi = client.recv()
#readResponseTest = decodeBytes(bajtovi)







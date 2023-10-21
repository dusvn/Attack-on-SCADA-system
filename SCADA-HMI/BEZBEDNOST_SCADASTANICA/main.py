"""
Test 
"""
from ModbusBase import *
from ReadRequest import *
from ReadResponse import *
from WriteRequest import * 
from WriteResponse import * 
import ctypes
base_objekat = ModbusBase(ctypes.c_ushort(1),ctypes.c_ushort(1),ctypes.c_ushort(1),ctypes.c_byte(1),ctypes.c_byte(1))
readRequest = ModbusReadRequest(base_objekat,ctypes.c_ushort(1),ctypes.c_ushort(1))
readResponse = ModbusReadReasponse(base_objekat,ctypes.c_byte(1),bytearray([10,11]))
writeResponse = ModbusWriteRequest(base_objekat,ctypes.c_ushort(10),ctypes.c_ushort(80))
print(writeResponse.__str__())

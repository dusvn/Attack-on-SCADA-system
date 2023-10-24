import ctypes
import socket

"""
Svaka klasa u okviru protokola sadrzi ovaj deo.
Request za read,write
Response na odredjeni read,write 
TransactionID - > broj transakcije 
ProtocolID ->  0 uvek za Modbus 
Length - > 
unitID - > ID slave-a(postrojenja) kojem saljemo poruku 
functionCode - >Procitaj digitalni izlaz 0x01  
                Procitaj digitalni input 0x02 
                Procitaj analogni output 0x03 
                Procitaj analogni input 0x04 
                Upisi digitalnu vrednost 0x05 
                Upisi analognu vrednost 0x06 
                Length -> unit byte + function code + remaining data 
"""
class ModbusBase:
    def __init__(self,
                 TransactionID: ctypes.c_ushort,
                 ProtocolID : ctypes.c_ushort,
                 UnitID:ctypes.c_byte,
                 FunctionCode:ctypes.c_byte):
        self.TransactionID = TransactionID
        self.ProtocolID = ProtocolID
        self.Length = bytearray([0, 2]) # unitID and function code is always 2 bytes
        self.UnitID = UnitID
        self.FunctionCode = FunctionCode
    def __str__(self):
        return f"TransactionID:{self.TransactionID},ProtocolID:{self.ProtocolID},Length:{self.Length},UnitID:{self.UnitID},FunctionCode:{self.FunctionCode}"
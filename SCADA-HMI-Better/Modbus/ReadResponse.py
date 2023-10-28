from Modbus.ModbusBase import *
import ctypes
"""
Objekat koji ce primati read odgovore 
"""

class ModbusReadReasponse(ModbusBase):
    def __init__(self,
                 base : ModbusBase,
                 ByteCount : ctypes.c_byte,
                 Data : bytearray ):
        super().__init__(base.TransactionID,base.ProtocolID,base.UnitID,base.FunctionCode)
        self.Length += 1 # byte count
        self.Length += len(Data)
        self.ByteCount = ByteCount
        self.Data = Data

    def __str__(self):
        return f"{super().__str__()},ByteCount:{self.ByteCount},Data:{self.Data}"

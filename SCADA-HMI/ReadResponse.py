from ModbusBase import *
import ctypes
"""
Objekat koji ce primati read odgovore 
"""

class ModbusReadReasponse(ModbusBase):
    def __init__(self,
                 base : ModbusBase, 
                 ByteCount : ctypes.c_byte,
                 Data : bytearray ):
        super().__init__(base.TransactionID,base.ProtocolID,base.Length,base.UnitID,base.FunctionCode) 
        self.ByteCount = ByteCount
        self.Data = Data
    def get_size_in_bytes(self):
        total_size = (super().get_size_in_bytes() +  
                      ctypes.sizeof(self.ByteCount) +
                      len(self.Data))
        return total_size 
    def __str__(self):
        return f"{super().__str__()},ByteCount:{self.ByteCount.value},Data:{self.Data}"

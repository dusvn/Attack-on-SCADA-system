from ModbusBase import *
import ctypes
"""
Klasa je samo kako bi se razlikovali Request Write i Response za Write sustinski su isti objekti
"""
class ModbusWriteResponse(ModbusBase):
    def __init__(self,
                 base : ModbusBase,
                 RegisterAdress : ctypes.c_ushort,
                 RegisterValue : ctypes.c_ushort):
        super().__init__(base.TransactionID,base.ProtocolID,base.Length,base.UnitID,base.FunctionCode)
        self.RegisterAdress = RegisterAdress
        self.RegisterValue  = RegisterValue
    def get_size_in_bytes(self):
        total_size = (super().get_size_in_bytes() +  
                      ctypes.sizeof(self.RegisterAdress) +
                      ctypes.sizeof(self.RegisterValue))
        return total_size 
    def __str__(self):
        return f"{super().__str__()},RegisterAdress:{self.RegisterAdress},RegisterValue:{self.RegisterValue}"


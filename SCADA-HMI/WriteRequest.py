from ModbusBase import *
import ctypes
"""Objekat koji se salje da bi se upisalo nesto
    RegisterAdress - > adresa registra na koji se upisuje vrednost 
    RegisterValue - > vrednost koja se upisuje u taj registar 
    Akko se uspesno izvrsi upravljanje u WriteResponse ce doci povratna poruka koja je ista kao poslata(WriteRequest)
"""

class ModbusWriteRequest(ModbusBase): 
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
        return f"{super().__str__()},RegisterAdress:{self.RegisterAdress.value},RegisterValue:{self.RegisterValue.value}"
    
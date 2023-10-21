from ModbusBase import *
import ctypes
"""
startAdress - > sa koje adrese zeli da se procita 
quantity - > sa koliko uzastopnih registara treba da cita 
Primer: start adress 1000 
        quantity 2 
        => citace sa adrese 1000 i 1001 na svakoj adresi je 16bit registar 
"""
class ModbusReadRequest(ModbusBase): 
    def __init__(self,
                 base : ModbusBase,
                 StartAdress : ctypes.c_ushort,
                 Quantity : ctypes.c_ushort):
        super().__init__(base.TransactionID,base.ProtocolID,base.Length,base.UnitID,base.FunctionCode)
        self.StartAdress = StartAdress
        self.Quantity = Quantity
    def get_size_in_bytes(self):
        total_size = (super().get_size_in_bytes() +  
                      ctypes.sizeof(self.StartAdress) +
                      ctypes.sizeof(self.Quantity))
        return total_size
    def __str__(self):
        return f"{super().__str__()},StartAdress:{self.StartAdress.value},Quantity:{self.Quantity.value}"
    
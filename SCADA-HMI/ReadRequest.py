from ModbusBase import *
import ctypes
import struct 
import socket
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
                 StartAddress : ctypes.c_ushort,
                 Quantity : ctypes.c_ushort):
        super().__init__(base.TransactionID,base.ProtocolID,base.Length,base.UnitID,base.FunctionCode)
        self.StartAddress = StartAddress
        self.Quantity = Quantity
    def get_size_in_bytes(self):
        total_size = (super().get_size_in_bytes() +  
                      ctypes.sizeof(self.StartAdress) +
                      ctypes.sizeof(self.Quantity))
        return total_size
    def __str__(self):
        return f"{super().__str__()},StartAdress:{self.StartAdress},Quantity:{self.Quantity}"
    
def repack(ReadRequest: ModbusReadRequest) -> bytearray:
    request = bytearray(12)
    request[0:2] = socket.htons(ReadRequest.TransactionID).to_bytes(2, "little")
    request[2:4] = socket.htons(ReadRequest.ProtocolID).to_bytes(2, "little")
    request[4:6] = socket.htons(ReadRequest.Length).to_bytes(2, "little")
    request[6] = ReadRequest.UnitID
    request[7] = ReadRequest.FunctionCode
    request[8:10] =  socket.htons(ReadRequest.StartAddress).to_bytes(2, "little")
    request[10:12] = socket.htons(ReadRequest.Quantity).to_bytes(2, "little")

    return request

    
 
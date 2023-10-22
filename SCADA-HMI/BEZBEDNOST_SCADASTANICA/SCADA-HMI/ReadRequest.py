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
    
    transaction_id = struct.pack('>H', ReadRequest.TransactionID)
    request[0:2] = transaction_id
    print(request[0:2])

    protocol_id = struct.pack('>H', ReadRequest.ProtocolID)
    request[2:4] = protocol_id

    length = struct.pack('>H', ReadRequest.Length)
    request[4:6] = length

    unit_id = struct.pack('B', ReadRequest.UnitID)
    request[6] = unit_id[0]

    function_code = struct.pack('B', ReadRequest.FunctionCode)
    request[7] = function_code[0]

    start_address = struct.pack('>H', ReadRequest.StartAddress)
    request[8:10] = start_address

    quantity = struct.pack('>H', ReadRequest.Quantity)
    request[10:12] = quantity

 
    return request

    
 
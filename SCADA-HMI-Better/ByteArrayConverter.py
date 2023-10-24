import socket
import ModbusBase
import ReadRequest
import ReadResponse

def decodeBytes(bajtovi : bytearray):
    transactionId = bajtovi[0:2]
    protocolId = socket.ntohs(bajtovi[2:4])
    length = socket.ntohs(bajtovi[4:6])
    unitId = bajtovi[6]
    functionCode = bajtovi[7]
    return napraviReadResponse(transactionId, protocolId, length, unitId, functionCode, bajtovi)

def napraviReadResponse(transactionId, protocolId, length, unitId, functionCode, bajtovi):
    byteCount = bajtovi[8]
    data = bajtovi[9::]
    mdbBase = ModbusBase.ModbusBase(transactionId, protocolId, length, unitId, functionCode)
    response = ReadResponse.ModbusReadReasponse(mdbBase, byteCount, data)
    return response
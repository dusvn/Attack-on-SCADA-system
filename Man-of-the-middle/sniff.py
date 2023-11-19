import pydivert
from fileFormatString import  *
"""
Imamo source port onoga ko je slao paket na DstPort 25252 
Na osnovu toga trazimo pakete koji idu na taj port i koji su duzine 11 zbog samog formata Modbus poruke
Ti pobaci se cuvaju u data.txt
"""
def sniffPackageForReplayAttack(sourcePort):
    with pydivert.WinDivert(f"tcp.DstPort == {sourcePort} and tcp.PayloadLength == 11") as w:
        for packet in w:
            dicForSave = ForFileAnalitics(packet.payload)
            result = modbusBaseAnalitics(dicForSave)
            saveOldData(result)
            w.send(packet)
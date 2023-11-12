import pydivert

#korak 1 treba uhvatiti pakete i sacuvati ih u ispravnom formatu
#takodje treba uhvatiti source port od paketa(menja se uvek kad se app pokrene) --> odradjeno
#nakon toga treba ih poslati opet


def captureSourcePort(packet):
    if packet.dst_port == 25252:
        return  packet.src_port
    else:
        return 0

def saveOldData(packet,filename):
    with open(filename, "wb") as f:
        f.write(packet.payload)




def sniffPackage():
    with pydivert.WinDivert("tcp.DstPort == 25252 and tcp.PayloadLength > 0") as w:
        for packet in w:
            src = captureSourcePort(packet)
            saveOldData(packet,"oldData.pcap")
            w.send(packet)




if __name__ == "__main__":
    sniffPackage()







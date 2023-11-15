import pydivert

#korak 1 treba uhvatiti pakete i sacuvati ih u ispravnom formatu
#takodje treba uhvatiti source port od paketa(menja se uvek kad se app pokrene) --> odradjeno
#nakon toga treba ih poslati opet

values = [10, 0, 3]

# Initialize the byte array
bytes = bytearray()
d = 350
# Convert each decimal value to bytes and add to the byte array
for decimal_value in values:
    bytes.extend((decimal_value).to_bytes(2, byteorder='big'))

# Add the last byte (0 to 255)
unitID = 100  # Adjust as needed
byteCount = 10
fc = 1
bytes.append(unitID)
bytes.append(fc)
bytes.append(byteCount)
bytes.extend(d.to_bytes(2, byteorder='big'))


def captureSourcePort(packet):
    if packet.dst_port == 25252:
        return  packet.src_port
    else:
        return 0


"""
cilj je izvuci polja sa njihovim vrednostima za print 
"""
def modbusBaseAnalitics(dic):
    transactionIDBytes = dic[0] + dic[1]
    protocolIDBytes = dic[2] + dic[3]
    protocolIDMeaning = int.from_bytes(bytes.fromhex(dic[2][1:] + dic[3][1:]),byteorder="big")
    transactionIDMeaning = int.from_bytes(bytes.fromhex(dic[0][1:] + dic[1][1:]),byteorder="big")
    lengthBytes = dic[4] + dic[5]
    lengthMeaning = int.from_bytes(bytes.fromhex(dic[4][1:] + dic[5][1:]),byteorder="big")
    unitIDBytes = dic[6]
    unitIDMeaning = int.from_bytes(bytes.fromhex(dic[6][1:]),byteorder="big")
    functionCodeBytes = dic[7]
    functionCodeMeaning = int.from_bytes(bytes.fromhex(dic[7][1:]),byteorder="big")
    byteCountBytes = dic[8]
    byteCountMeaning = int.from_bytes(bytes.fromhex(dic[8][1:]),byteorder="big")
    dataBytes = dic[9] + dic[10]
    #ovo treba doraditi da moze n bajtova mrzi me sad
    resRaw = ""
    for obj in range(0,len(dic)):
        resRaw += dic[obj]
    dataMeaning = int.from_bytes(bytes.fromhex(dic[9][1:] + dic[10][1:]),byteorder="big")
    result_string = f"=================================================\n" \
                    f"\t\t\t\t|Modbus Response Message|\n" \
                    f"Raw data of full payload: {resRaw}\n" \
                    f"TransactionID raw data: {transactionIDBytes}\n" \
                    f"TransactionID ing value: {transactionIDMeaning}\n" \
                    f"ProtocolID raw data: {protocolIDBytes}\n" \
                    f"ProtocolID ing value: {protocolIDMeaning}\n" \
                    f"Length raw data: {lengthBytes}\n" \
                    f"Length ing value: {lengthMeaning}\n" \
                    f"UnitIDBytes raw data: {unitIDBytes}\n" \
                    f"UnitID ing value: {unitIDMeaning}\n" \
                    f"Function Code raw data: {functionCodeBytes}\n" \
                    f"Function Code ing value: {functionCodeMeaning}\n" \
                    f"Byte count raw data: {byteCountBytes}\n" \
                    f"Byte count ing value: {byteCountMeaning}\n" \
                    f"Data raw: {dataBytes}\n" \
                    f"Data ing value: {dataMeaning}\n" \
                    "=================================================="

    return result_string
def bytesForFileAnalitics(bytes: bytearray):
    formatted_string = ' '.join([f'x{byte:02x}' for byte in bytes])
    splitDic = formatted_string.split(" ")
    d = {}
    #izvdvojeni podaci bajt po bajt
    for i in range(0,len(splitDic)):
        d[i] = splitDic[i]
    return d


def saveOldData(packet,filename = "data.txt"):
    with open(filename, "a") as f:
        f.write(packet)



"""
logika za hvatanje paketa malo promenjena da se posmatraju polja modbusa 
"""

def sniffPackage(sourcePort):
    with pydivert.WinDivert(f"tcp.DstPort == {sourcePort} and tcp.PayloadLength ==11") as w:
        for packet in w:
            #src = captureSourcePort(packet) #hvatam dest
            dicForSave = bytesForFileAnalitics(packet.payload)
            result = modbusBaseAnalitics(dicForSave)
            saveOldData(result)
            w.send(packet)

def grabSourcePort():
    with pydivert.WinDivert("tcp.DstPort == 25252") as w:
        for packet in w:
            if(captureSourcePort(packet)!= 0):
                return captureSourcePort(packet)


if __name__ == "__main__":
    sourcePort = grabSourcePort()
    sniffPackage(sourcePort)
   # bc = bytesForFileAnalitics(bytes)
   # result = modbusBaseAnalitics(bc)






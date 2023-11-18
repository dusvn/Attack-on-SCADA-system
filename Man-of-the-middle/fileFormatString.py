import re
import random
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
    result_string = "@{\n" \
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
                    "}\n"

    return result_string

def saveOldData(packet,filename = "data.txt"):
    with open(filename, "a") as f:
        f.write(packet)

"""
Metoda koja izdvaja bajt po bajt iz poruke i smesta ih redom 
key -> num of byte 
value ->raw value of byte 
"""
def ForFileAnalitics(bytes: bytearray):
    formatted_string = ' '.join([f'x{byte:02x}' for byte in bytes])
    splitDic = formatted_string.split(" ")
    d = {}
    #izvdvojeni podaci bajt po bajt
    for i in range(0,len(splitDic)):
        d[i] = splitDic[i]
    return d

"""
F-ja uzima podatke iz fajla za napadanje koji se salju 
"""
def takeMessagesForAttack(filename="data.txt"):
    dicForAttack = {}
    dicIngValues = list()
    counter = 0
    with open(filename,'r') as f: #iscitao fajl
        lines = f.readlines()

    for line in lines:
        if re.search("Raw data of full payload:",line) != None:
            message = re.findall(r'x[0-9a-fA-F]+',line)
            dicForAttack[counter] = ''.join(message)
            counter+=1
        if re.search("Data ing value:",line) != None:
            ing = re.findall(r'[0-9]+',line)
            dicIngValues.extend(ing)

    randomIndex = [random.randint(0, len(dicForAttack)-1) for _ in range(5)] # pravi se 5 puta random int
    attackedValues= [dicIngValues[i]  for i in randomIndex]
    print(f"Random values from file: {attackedValues}")
    attackMessages = [dicForAttack[ind] for ind in randomIndex]
    attackMessages = [bytearray.fromhex(attackMessages[i].replace("x","")) for i in range(5)]
    return attackMessages
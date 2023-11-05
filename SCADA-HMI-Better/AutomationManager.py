"""
Ideja
Napisati metodu koja ce vrsiti konstantnu kontrolu pristiglih prednosti i na osnovu toga govoriti kakvo je stanje sistema,da li treba da se upali alarm
Kad se upali alarm treba da se reaguje(npr treba da se iskljuci prekidac neki)
Ako je sistem u neispravnom stanju i istom loopu poslati write poruku za gasenjem nekog prekidaca npr...
Prima se odgovor ako je uspesno izvrsena komanda i onda se se krece sa sledecim loopom i akvizicijom
Naravno ovo sve raditi samo za digitalnim i analognim izlazima --> nad izlaznim signalima se upravlja
Dok ulazni signali --> daju izlazne informacije o sistemu
"""
from DataBase import *
from typing import Dict
from Modbus.Signal import *
from Modbus.WriteRequest import *
from Modbus.WriteResponse import *
from Modbus.ModbusBase import *

"""
Trazi addresu od control rods-a 
U slucaju da se promeni adresa iz configa 
"""
def takeControlRodsAddress(signal_info):
    for key,value in signal_info.items():
      if value[key].getSignalType() == "DO":
          return key

"""
Trazi addresu od water thermometer 
U slucaju da se promeni adresa iz configa 
"""
def takeWaterThermometerAddress(signal_info):
    for key,value in signal_info.items():
        if value[key].getSignalType() == "AI":
            return key

"""
F-ja koja se koristi da bi znali da li je uspesno izvrsen poslati write 
if writeRequest == writeResponse -> uspesno izvrseno 
else nije izvrseno 
"""
def compareWriteRequestAndResponse(writeRequest : ModbusWriteRequest,writeResponse : ModbusWriteResponse):
    if (writeRequest.TransactionID == writeResponse.TransactionID and
        writeRequest.ProtocolID == writeResponse.ProtocolID and
        writeRequest.Length == writeResponse.Length and
        writeRequest.UnitID == writeResponse.UnitID and
        writeRequest.FunctionCode == writeResponse.FunctionCode and
        writeRequest.RegisterAdress == writeResponse.RegisterAdress):
        return True
    else:
        return False


"""
Provera da li je high alarm aktiviran 
Ako je waterThermometer >=350 aktiviran
To je signal da treba da se control rods spuste u vodu --> posedi kontrol rods na 1,
Kako bi se voda ohladila 
"""
def isHighAlarmActive(waterThermometerAddress, signal_info):
    return int(signal_info[waterThermometerAddress].CurrentValue) >= int(signal_info[waterThermometerAddress].getMaxAlarm())

"""
Proverava da li je low alarm aktiviran 
Ako je waterThermometer <=250 to je znak da se control rods vade iz vode --> podesi control rods na 0 
Kako bi se povecao broj hemijskih reakcija ==> voda se zagreva 
"""
def isLowAlarmActive(waterThermometerAddress, signal_info):
    return int(signal_info[waterThermometerAddress].CurrentValue) <= int(signal_info[waterThermometerAddress].getMinAlarm())


"""
Function code je uvek 5 posto se manipulise sa control rods -> Digital output 
Formira se WriteRequest nakon cega se salje poruka za promenu stanja control rods-a 
Nakon sto dodje odgovor prepakuje se i proverava se da li ima neka ilegalna f-ja 
Ako nema porede se poslata i primljena poruka i konstatuje se da je vrednost promenjena 
"""
def AutomationLogic(client,signal_info,base_info,controlRodsAddress,command,functionCode = 5):
        base = ModbusBase(base_info["station_address"],functionCode) # 5
        request = ModbusWriteRequest(base,signal_info[controlRodsAddress].getStartAddress(),signal_info[controlRodsAddress].CurrentValue)
        modbusWriteRequest = repackWrite(request,command) # if high alarm 1 ,low alarm 0
        client.send(modbusWriteRequest)
        response = client.recv(1024)
        modbusWriteResponse = repackResponse(response)
        if (compareWriteRequestAndResponse(request, modbusWriteResponse)):
            signal_info[controlRodsAddress].setcurrentValue(command)

"""
Vrsi se provera alarma i desava se logika automatizacije 
"""
def Automation(client,signal_info,base_info):
    waterThermometerAddress = 2000
    controlRodsAddress = 1000
    if isHighAlarmActive(waterThermometerAddress,signal_info):
        print("Is high alarm")
        AutomationLogic(client,signal_info,base_info,controlRodsAddress,65280)
    elif isLowAlarmActive(waterThermometerAddress,signal_info):
        AutomationLogic(client,signal_info,base_info,controlRodsAddress,0)
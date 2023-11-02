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
Metoda uzima samo one signale nad kojima se moze vrstiti upravljanje 
"""
def takeAnalogDigitalOutput(signal_info) -> Dict[int,Signal]:
    AnalogDigitalOutput = {}
    for key,value in signal_info.items():
        if value.getSignalType() == "AO":
            AnalogDigitalOutput[key] = value
    return AnalogDigitalOutput

def takeFunctionCode(signal_info,key):
    return 6 if signal_info[key].getSignalType() == "AO" else 5

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
retu 

"""
def Automation(AnalogDigitalOutput : Dict[int,Signal],client,signal_info,base_info):
    for key,value in AnalogDigitalOutput.items():
        if int(AnalogDigitalOutput[key].CurrentValue) <= int(AnalogDigitalOutput[key].getMinAlarm()):
            functionCode = takeFunctionCode(AnalogDigitalOutput,key)
            base = ModbusBase(base_info["station_address"],functionCode)
            request = ModbusWriteRequest(base, AnalogDigitalOutput[key].StartAddress, AnalogDigitalOutput[key].CurrentValue)
            request.RegisterValue = request.RegisterValue * 1.3
            repackRequest = repackWrite(request,AnalogDigitalOutput[key].CurrentValue * 1.3)

            client.send(repackRequest)
            message = client.recv(1024)
            writeResponse = repackResponse(message)
            if(compareWriteRequestAndResponse(request,writeResponse)):
                signal_info[key].setcurrentValue(AnalogDigitalOutput[key].CurrentValue * 1.3)
            else:
                continue

        elif int(AnalogDigitalOutput[key].CurrentValue) >= int(AnalogDigitalOutput[key].getMaxAlarm()):
            functionCode = takeFunctionCode(AnalogDigitalOutput,key)
            base = ModbusBase(base_info["station_address"],functionCode)
            request = ModbusWriteRequest(base, AnalogDigitalOutput[key].getStartAddress(), AnalogDigitalOutput[key].CurrentValue)
            request.RegisterValue = int(request.RegisterValue * 0.7)
            repackRequest = repackWrite(request,int(AnalogDigitalOutput[key].CurrentValue * 0.7))
            print(f"Value after changed:{int(AnalogDigitalOutput[key].CurrentValue * 0.7)}")
            print(f"Request{repackRequest}")
            client.send(repackRequest)
            message = client.recv(1024)
            writeResponse = repackResponse(message)
            print(f"Response:{writeResponse}")
            if(compareWriteRequestAndResponse(request,writeResponse)):
                signal_info[key].setcurrentValue(AnalogDigitalOutput[key].CurrentValue * 0.7)
            else:
                continue
        else:
            pass
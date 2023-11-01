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
"""
Metoda uzima samo one signale nad kojima se moze vrstiti upravljanje 
"""
def takeAnalogDigitalOutput(signal_info) -> Dict[int,Signal]:
    AnalogDigitalOutput = {}
    for key,value in signal_info.items():
        if value.getSignalType == "AO" or "DO":
            AnalogDigitalOutput[key] = value
    return AnalogDigitalOutput

"""
retu 

"""
def checkAlarm(AnalogDigitalOutput : Dict[int,Signal]):
    for key,value in AnalogDigitalOutput.items():
        if int(AnalogDigitalOutput[key].CurrentValue) <= int(AnalogDigitalOutput[key].MinAlarm()):
            return 1
        elif int(AnalogDigitalOutput[key].CurrentValue) >= int(AnalogDigitalOutput[key].MaxAlarm()):
            return 2
        else:
            return 0
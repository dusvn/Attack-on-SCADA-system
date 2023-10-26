class Signal():
    def __init__(self, reg_type, num_reg, StartAddress, MinV, MaxV, StartV, SignalType, MinAlarm, MaxAlarm,name):
        self._Reg_type = reg_type
        self._Num_reg = num_reg
        self._StartAddress = StartAddress
        self._MinValue = MinV
        self._MaxValue = MaxV
        self._StartV = StartV
        self._SignalType = SignalType
        self._MinAlarm = MinAlarm
        self._MaxAlarm = MaxAlarm
        self._Name = name
        self._AlarmNow = "NO ALARM"

    def Modify_Alrm(self,alarm):
        self._AlarmNow = alarm

    def Name(self):
        return self.Name

    def Name(self,name):
        self.Name = name

    def Reg_type(self):
        return self._Reg_type

    def Reg_type(self, value):
        self._Reg_type = value

    def Num_reg(self):
        return self._Num_reg

    def Num_reg(self, value):
        self._Num_reg = value

    def StartAddress(self):
        return self._StartAddress

    def StartAddress(self, value):
        self._StartAddress = value

    def MinValue(self):
        return self._MinValue

    def MinValue(self, value):
        self._MinValue = value

    def MaxValue(self):
        return self._MaxValue

    def MaxValue(self, value):
        self._MaxValue = value

    def StartV(self):
        return self._StartV

    def StartV(self, value):
        self._StartV = value

    def SignalType(self):
        return self._SignalType

    def SignalType(self, value):
        self._SignalType = value

    def MinAlarm(self):
        return self._MinAlarm

    def MinAlarm(self, value):
        self._MinAlarm = value

    def MaxAlarm(self):
        return self._MaxAlarm

    def MaxAlarm(self, value):
        self._MaxAlarm = value
    def __str__(self):
        return f"Signal Info: Reg_type: {self._Reg_type},Num_reg: {self._Num_reg},StartAddress: {self._StartAddress},MinValue: {self._MinValue},MaxValue: {self._MaxValue},StartV: {self._StartV},SignalType: {self._SignalType},MinAlarm: {self._MinAlarm},MaxAlarm: {self._MaxAlarm},Name:{self._Name}"

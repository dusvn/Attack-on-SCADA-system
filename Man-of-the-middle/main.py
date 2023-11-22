import pydivert
import re
import random
from fileFormatString import *
from grabPort import *
from sniff import *
import time as t
from replayAttack import  *
from commandInjection import *

fineInject = loadMessagesForAttack()


if __name__ == "__main__":
    sourcePort = grabSourcePort() # vraca port onoga koga trebamo napasti
    replayAttack(sourcePort,fineInject)
    #comandInjection(sourcePort)
    #sniffPackageForReplayAttack(sourcePort)






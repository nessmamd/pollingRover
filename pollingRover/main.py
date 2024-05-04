from motor__init import *
import threading
import time
import os

# dont forget to remove the prev section 

sizeS = len(motors_S)
sizeDC = len(motors)
inputDC = [False]*sizeDC
inputS = [False]*sizeS
connectionDC = [False]*sizeDC
connectionS = [False]*sizeS
groundDC = [False]*sizeDC
groundS = [False]*sizeS

#the Index: the Port , I AM NOT SURE HOW ACCURATE THIS IS TO THE PORTS
mapping = {0:3, 1:5, 2:1, 3:2}
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, num, *args, **kwargs):
        if num not in cls._instances:
            cls._instances[num] = super().__call__(num, *args, **kwargs)
        return cls._instances[num]

class Singleton(metaclass=SingletonMeta):
    def __init__(self, num):
        self.num = num
        self.theInstance = 0
        self.VHubSerial_motors = 697178

    def createInstance(self):
        ch_lsdm = VoltageInput()
        print("made voltage sensor")
        VHubSerial_motors = 697178
        ch_lsdm.setDeviceSerialNumber(VHubSerial_motors)
        print("set voltage sensor vinthub as: ", VHubSerial_motors)
        numInstance = mapping[self.num]
        ch_lsdm.setHubPort(numInstance)
        print("set voltage sensror hub port as", ch_lsdm.getHubPort())
        self.theInstance = ch_lsdm
        # ch_lsdm.openWaitForAttachment(5000)
        print("ch_lsdm attached: ", ch_lsdm.getAttached())
    def useThatInstance(self):
        self.theInstance.getVoltage()
        print(f"motorsch[{self.num}] is attached: {self.theInstance.getAttached()}")
        print("max voltage:", self.theInstance.getMaxVoltage())
        print("min voltage: ", self.theInstance.getMinVoltage())
        return self.theInstance.getVoltage()


def inputVoltage(number, identifier, theArray):
        # could add a wait function here... the identifier is if its Servo or DC
        # the number is the index that is be to used
        print("entered inputVoltage function")
        VHubSerial_motors = 697178
        print("vint serial for motors entered")
        # its either number or identifier
        instance = Singleton(number)
        start_time = time.time()
        while True:
            print("Entered once because of", id(instance))
            instance.createInstance()
            # Check if 5 seconds have passed
            # if time.time() - start_time >= 5:
            #     break  # Break the loop if 5 seconds have passed

            second = instance.useThatInstance()
            if(identifier == 2):
                if not(22 <= second <= 26):
                    inputDC[number] = False
                else:
                    inputDC[number] = True

            elif(identifier == 1):
                if not(11.5 <= second <= 12.5):
                    inputS[number] = False
                else:
                    inputS[number] = True


# the two other functions you need to see if there is a change or not
def turnedOnConnectionServo(number, motorsArray):
        motors_S = motorsArray
        prev = connectionS[number]
        if motors_S[number].getAttached():
            print("The Servo motor #%d is attached"% number)
            if motors_S[number].getIsOpen():
                print("The Servo motor #%d is open"% number)
            if motors_S[number].getIsOpen():
                connectionS[number] = True
                if prev != connectionS[number]: CDetected = True
                
            else:
                print("The Servo motor #%d is not open" % number)
                motors_S[number].openWaitForAttachment(1000)
                connectionS[number] = False
                if prev != connectionS[number]: CDetected = True
            inputVoltage(number, 1, motorsArray)
            
        else: 
            connectionS[number] = False
            if prev != connectionDC[number]: CDetected = True

def turnedOnConnectionDC(number, motorsArray):
        # prev = connectionDC[number]
        motors = motorsArray
        print("boolean ", motors[number].getAttached())
        if motors[number].getAttached():
            print("The DC motor #%d is attached"% number)
            # if motors[number].getIsOpen():
            #     print("The DC motor #%d is open"% number)
            #     connectionDC[number] = True
            #     # if prev != connectionDC[number]: CDetected = True
            # else:
            #     print("The DC motor #%d is not open" % number)
            #     motors[number].openWaitForAttachment(1000)
            #     connectionDC[number] = False
                # if prev != connectionDC[number]: CDetected = True
            inputVoltage(number, 2, motorsArray)
        else: 
            connectionDC[number] = False
            print("It is not attached !!! ")
            # if prev != connectionDC[number]: CDetected = True
            
def printer(): 
        print("DC MOTOR STATS: ")
        for x in range(sizeDC):
            print("DC MOTOR #",x)
            print("---------------")
            print("Input voltage status: " + ("FAULTY!!!!!!" if inputDC[x] == False else "VALID"))
            print("Connection status:"+ (" FAILED " if connectionDC[x] == False else " SUCCESS"))

        for y in range(sizeS):
            print("Servo MOTOR #",y)
            print("---------------")
            print("Input voltage status: " + ("FAULTY!!!!!!" if inputS[y] == False else "VALID"))
            print("Connection status:" + (" FAILED " if connectionS[y] == False else " SUCCESS"))
        time.sleep(1)


def pollerSystem(initalizedMotors):
    #first case is does it enter the pollerSystem?
    print("entering the poller system")
    # could do a while statement in here that continously loops 
    time.sleep(1)
    turnedOnConnectionDC(1, initalizedMotors)

# inputVoltage(1, 0, [])
# time.sleep(5)  # Wait for 5 second
# inputVoltage(1, 0, [])


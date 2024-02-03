from motor__init import *
import threading
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

#when the identifer is 1 then it is a servo, 2 is dc motor

def inputVoltage(number, identifier, theArray):
        second = theArray[number].getVoltage()
        print("Voltage statement: it is ", second)
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
    # this is the code for debugging
    turnedOnConnectionDC(1, initalizedMotors)
    
    # cant test the servo ones yet because it is not working in the original one  
    #  turnedOnConnectionServo(1, initalizedMotors)
    
    # this is the final code for everything
    # time.sleep(1)
    # while True:
    #     #  clear the terminal
    #     os.system('cls' if os.name == 'nt' else 'clear')

    #     # threads_servo = [threading.Thread(target=turnedOnConnectionServo, args=(x, initalizedMotors)) for x in range(len(motors_S))]
    #     # for threadS in threads_servo:
    #     #     threadS.start()

    #     threads_dc = [threading.Thread(target=turnedOnConnectionDC, args=(y, initalizedMotors)) for y in range(len(motors))]
    #     for thread in threads_dc:
    #         thread.start()

    #     # for threadSS in threads_servo:
    #     #     threadSS.join()

    #     for threadd in threads_dc:
    #         threadd.join()

    #     printer()

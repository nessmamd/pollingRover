from motor__init import *
import threading
import os

sizeS = len(motors_S)
sizeDC = len(motors)

inputDC = [False]*sizeDC
inputS = [False]*sizeS
connectionDC = [False]*sizeDC
connectionS = [False]*sizeS
groundDC = [False]*sizeDC
groundS = [False]*sizeS

def inputVoltage(number, type):
    try:
        first = type[number].getVoltage()
        time.sleep(1)
        second = type[number].getVoltage()
        # driving motor is 22-26 and arm is 11.5-12.5
        if(type == motors):
            if abs(second - first < 1) and not(22 <= second <= 26):
                inputDC[number] = False
        else if(type == motors_S):
            if abs(second - first < 1) and not(11.5 <= second <= 12.5):
                inputS[number] = False

    except AttributeError:
        if type == motors:
            inputDC[number] = True
        else:
            inputS[number] = True

def turnedOnConnectionServo(number):
    try:
        # the if statement to check, if its connected or not
        if motors_S[number].getAttached():
            # print("The Servo motor #%d is attached"% number)
            if motors_S[number].getIsOpen():
                # print("The Servo motor #%d is open"% number)
                connectionS[number] = True
            else:
                # print("The Servo motor #%d is not open" % number)
                motors_S[number].openWaitForAttachment(1000)
                connectionS[number] = False
            inputVoltage(number, motors_S)
            groundVoltage(number, motors_S)

    except AttributeError:
         connectionS[number] = False

def turnedOnConnectionDC(number):
    try:
        # the if statement to check, if its connected or not
        if motors[number].getAttached():
            # print("The DC motor #%d is attached"% number)
            if motors[number].getIsOpen():
                # print("The DC motor #%d is open"% number)
                connectionDC[number] = True

            else:
                # print("The DC motor #%d is not open" % number)
                motors[number].openWaitForAttachment(1000)
                connectionDC[number] = False
            inputVoltage(number, motors)
            groundVoltage(number,motors)

    except AttributeError:
        connectionDC[number] = False

def groundVoltage(number,volt):
    x = 1 


while True:
    #  clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    threads_servo = [threading.Thread(target=turnedOnConnectionServo, args=(x,)) for x in range(len(motors_S))]
    for threadS in threads_servo:
        threadS.start()

    threads_dc = [threading.Thread(target=turnedOnConnectionDC, args=(y,)) for y in range(len(motors))]
    for thread in threads_dc:
        thread.start()

    for threadSS in threads_servo:
        threadSS.join()

    for threadd in threads_dc:
        threadd.join()

    time.sleep(1)

    print("DC MOTOR STATS: ")
    for x in range(sizeDC):
        print("DC MOTOR #"+x)
        print("---------------")
        print("Input voltage status: " + ("FAULTY!!!!!!" if inputDC[x] == False else "@5"))
        print("Connection status:"+ (" FAILED " if connectionDC[x] == False else " SUCCESS"))

    for y in range(sizeS):
        print("Servo MOTOR #"+ y)
        print("---------------")
        print("Input voltage status: " + ("FAULTY!!!!!!" if inputS[x] == False else "@5"))
        print("Connection status:" + (" FAILED " if connectionS[x] == False else " SUCCESS"))

    time.sleep(1)


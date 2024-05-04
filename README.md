***Motor Initialization and Monitoring System***

This script initializes and monitors motors connected to a system, providing feedback on their connection status and input voltage.

The script includes functions for initializing motors, monitoring their connection status and input voltage, and printing the status of each motor.

Functions:
    def inputVoltage(number, identifier, theArray):
        Initializes a VoltageInput object for a motor and continuously monitors its input voltage.
    
    def turnedOnConnectionServo(number, motorsArray):
        Monitors the connection status of a Servo motor and updates the connection status and input voltage arrays accordingly.

    def turnedOnConnectionDC(number, motorsArray):
        Monitors the connection status of a DC motor and updates the connection status and input voltage arrays accordingly.

    def printer():
        Prints the status of each DC and Servo motor, including their input voltage status and connection status.

    def pollerSystem(initializedMotors):
        Continuously polls the system to monitor the connection status and input voltage of the motors.

Global Variables:
    sizeS: int
        Size of the Servo motors array.

    sizeDC: int
        Size of the DC motors array.

    inputDC: list
        Array to store the input voltage status of DC motors.

    inputS: list
        Array to store the input voltage status of Servo motors.

    connectionDC: list
        Array to store the connection status of DC motors.

    connectionS: list
        Array to store the connection status of Servo motors.

    groundDC: list
        Array to store the ground status of DC motors.

    groundS: list
        Array to store the ground status of Servo motors.

    mapping: dict
        Dictionary mapping motor indices to port numbers.

    SingletonMeta: metaclass
        Metaclass for implementing the Singleton design pattern.

    Singleton: class
        Class implementing the Singleton design pattern for creating a single instance of a VoltageInput object for each motor.

    motors_S: list
        List of Servo motors.

    motors: list
        List of DC motors.
'''

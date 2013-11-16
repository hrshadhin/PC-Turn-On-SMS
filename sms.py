
import serial
import time

#function for sending
def Sending(message, sender):
    SerialPort = serial.Serial("/dev/ttyUSB1",115200)
    SerialPort.write('AT+CMGF=1\r')
    time.sleep(1)
    SerialPort.write('AT+CMGS="'+sender+'"\r\n')
    time.sleep(1)
    SerialPort.write(message+"\x1A")
    time.sleep(1)
    print 'message sent'
    


Sending("Your pc Turn on","+8801554322707")

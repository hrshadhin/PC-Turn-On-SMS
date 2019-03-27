PC-Turn-On-SMS
==============

Simple Python script to send sms on Mobile phone using GSM modem 

Usage script:
=============

SerialPort = serial.Serial("/dev/ttyUSB1",115200)
change "/dev/ttyUSB1" and "115200" as port that modem connected and bound rate as your own on sms.py file.


Sending("Your pc Turn on","+8801554322xxx")
change your message and recipient number at above line on sms.py file.


And make changes to run.sh as you want and make this file to run on startup.

Thats it....

Enjoy:)

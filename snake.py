#!/usr/bin/env python
import RPi.GPIO as GPIO  
import time  

import subprocess
import smtplib
import socket
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import datetime
import urllib2

#blink and servo for snake
GPIO.setmode(GPIO.BOARD)  #to use Raspberry Pi board pin numbers   
GPIO.setup(7,GPIO.OUT) #motor output
GPIO.setup(13,GPIO.IN)#button
GPIO.setup(37, GPIO.OUT) #light 
GPIO.setup(33, GPIO.OUT) #light 2



while True:
    input = GPIO.input(13)
  
    if input == True:
        print ("SSSS!")
        fromaddr = "segoj297@newschool.edu"     
        toaddr = "segoj297@newschool.edu"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg ['Subject'] = "You put the snake to sleep!!!"

        body = "You put the snake to sleep!!!"
        msg.attach(MIMEText(body,'plain'))

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(fromaddr,'Back$traight')
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        break

    if input == True:
        GPIO.output(37,GPIO.LOW) #light 
        GPIO.output(33,GPIO.LOW) #light 2
        p.stop()
        print ("You put the snake to sleep!!!")

    if input == False:
        GPIO.output(37,GPIO.HIGH) #light 
        GPIO.output(33,GPIO.HIGH) #light 2
        p = GPIO.PWM(7,50)
        p.start(2.5)
        p.ChangeDutyCycle(2.5) #0 degrees
        time.sleep(1)
        p.ChangeDutyCycle(7.5) #neutral
        time.sleep(1)
        # p.ChangeDutyCycle(12.5) #180 degrees
        # time.sleep(1)

        print ("The snake is awake!!!")

GPIO.cleanup()



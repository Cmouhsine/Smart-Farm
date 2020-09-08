import RPi.GPIO as GPIO
import time 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

channel = 17
arrosage_on =18
arrosage_off =23

GPIO.setup(channel, GPIO.IN)
GPIO.setup(arrosage_on, GPIO.OUT)
GPIO.setup(arrosage_off, GPIO.OUT)

def callback(channel):  
	if GPIO.input(channel):
		print ("water pump off")
		GPIO.output(23,GPIO.HIGH)
		GPIO.output(18,GPIO.LOW)
		
		
	else:
		print ("water pump on")
		GPIO.output(18,GPIO.HIGH)
		GPIO.output(23,GPIO.LOW)
		
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)



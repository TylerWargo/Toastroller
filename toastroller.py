#Import Python Libraries
import RPi.GPIO as GPIO
import uinput
import time

#(2018) Made by Tyler Wargo

#Set GPIO Pins As Board Reference
GPIO.setmode(GPIO.BOARD)

#Setup / Initialize GPIO PINS
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Set ‘device’ Variable - Set Keys
Device = uinput.Device([uinput.KEY_UP,
			    uinput.KEY_DOWN,
			    uinput.KEY_LEFT,
			    uinput.KEY_RIGHT])

#While Running Loop Execute Code
while True:
	#Check GPIO Status
	if(GPIO.input(11) == True):
            #LEFT ARROW
		print(‘LEFT’)
		device.emit_click(uinput.KEY_LEFT)
		time.sleep(0.2)

	elif(GPIO.input(12) == True):
            #DOWN ARROW
		print(‘DOWN’)
		device.emit_click(uinput.KEY_DOWN)
		time.sleep(0.2)

	elif(GPIO.input(16) == True):
            #RIGHT ARROW
		print(‘RIGHT’)
		device.emit_click(uinput.KEY_RIGHT)
		time.sleep(0.2)

	elif(GPIO.input(22) == True):
            #UP ARROW
		print(‘UP’)
		device.emit_click(uinput.KEY_UP)
		time.sleep(0.2)

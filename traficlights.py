from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware
redLed = LED(17)
yellowLed = LED(27)
greenLed = LED(22)

## GUI Defs
win = Tk()
win.title("Traffic Light Controls")
myFont = tkinter.font.Font(family = 'Helvetica', size = 14, weight = "bold")

## Event functions

def redLedSelect():
	redLed.on()
	yellowLed.off()
	greenLed.off()
def yellowLedSelect():
	yellowLed.on()
	redLed.off()
	greenLed.off()
def greenLedSelect():
	greenLed.on()
	redLed.off()
	yellowLed.off()
def exitGui():
	win.destroy()

## Widgets

redLedButton = Button(win, text = 'Select Red LED', font = myFont, command = redLedSelect, bg = 'red', height = 4, width = 20)
redLedButton.grid(row=0,column=1)

yellowLedButton = Button(win, text = 'Select Yellow LED', font = myFont, command = yellowLedSelect, bg = 'yellow', height = 4, width = 20)
yellowLedButton.grid(row=0,column=2)

greenLedButton = Button(win, text = 'Select Green LED', font = myFont, command = greenLedSelect, bg = 'green', height = 4, width = 20)
greenLedButton.grid(row=0,column=3)

offButton = Button(win, text = 'Exit GUI', font = myFont, command = exitGui, bg = 'gray', height = 4, width = 24)
offButton.grid(row=0,column=4)

win.mainloop()


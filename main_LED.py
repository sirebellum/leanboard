import spidev
import RPi.GPIO as GPIO
from time import sleep
from LED_functions import *
from lean_board_functions import *

def latch_in():
    GPIO.output(latch, GPIO.HIGH)
    GPIO.output(latch, GPIO.LOW)
    
def LED_write(buffer):
    for i in range(0, 36):
        spi.xfer2([buffer[i]])

latch = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(latch, GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0, 1)

buffer = list(0x00 for x in range(0, 36))

GPIO.output(latch, GPIO.HIGH)
GPIO.output(latch, GPIO.LOW)
for i in range(0, 36):
    spi.xfer2([0x00])
GPIO.output(latch, GPIO.HIGH)
GPIO.output(latch, GPIO.LOW)

rooms = ("Ballroom1", "Ballroom2", "Bexar", "Denman", "Harris", "Travis")
room_state = list(0 for x in range(0, 6))
data = 0

try:
    while True:
        
        for i in range(0, 6):
            data = calcTime(timeDelta(getData(rooms[i])[1]))
            print(data)
            if data[0] > 0:
                room_state[i] = 0
            else: room_state[i] = 1
            
        for i in range(0, 6):
            if room_state[i] == 1:
                LED_Toggle(i, buffer)
            else: LED_Off(i, buffer)
            
        LED_write(buffer)
        latch_in()
        
        sleep(1)
        
        
except KeyboardInterrupt:
    GPIO.cleanup()
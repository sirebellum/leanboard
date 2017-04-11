import spidev
import RPi.GPIO as GPIO
from time import sleep
from LED_functions import *

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

try:
    while True:
        
        LED_On(0, buffer)
        LED_On(11, buffer)
        LED_Off(12, buffer)
        LED_Off(23, buffer)
        
        for i in range(0, 36):
            spi.xfer2([buffer[i]])
        
        GPIO.output(latch, GPIO.HIGH)
        GPIO.output(latch, GPIO.LOW)    
        
        sleep(1)
        
        LED_Off(0, buffer)
        LED_Off(11, buffer)
        LED_On(12, buffer)
        LED_On(23, buffer)
        
        for i in range(0, 36):
            spi.xfer2([buffer[i]])
            
        GPIO.output(latch, GPIO.HIGH)
        GPIO.output(latch, GPIO.LOW)
        
        sleep(1)
            
except KeyboardInterrupt:
    GPIO.cleanup()
import spidev
import RPi.GPIO as GPIO
import time

latch = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(latch, GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0, 1)

buffer_1 = list(0x00 for x in range(0, 36))
for x in range(18, 36):
    buffer_1[x] = 0xFF
buffer_2 = list(0xFF for x in range(0, 36))
for x in range(18, 36):
    buffer_2[x] = 0x00

try:
    while True:
        for i in range(0, 36):
            spi.xfer2([buffer_1[i]])
        
        GPIO.output(latch, GPIO.HIGH)
        GPIO.output(latch, GPIO.LOW)    
        
        time.sleep(1)
        
        for i in range(0, 36):
            spi.xfer2([buffer_2[i]])
            
        GPIO.output(latch, GPIO.HIGH)
        GPIO.output(latch, GPIO.LOW)
        
        time.sleep(1)
            
except KeyboardInterrupt:
    GPIO.cleanup()
import spidev
import RPi.GPIO as GPIO
import time

latch = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(latch, GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0, 1)

bufferoff = list(0x00 for x in range(0, 36))
bufferon = list(0xFF for x in range(0, 36))

try:
    while True:
        for i in range(0, 18):
            spi.xfer2([bufferoff[i]])
#        for i in range(18, 36):
#            spi.xfer2([bufferon[i]])
        
        GPIO.output(latch, GPIO.HIGH)
        GPIO.output(latch, GPIO.LOW)    
        
        time.sleep(1)
        
        for i in range(0, 18):
            spi.xfer2([bufferon[i]])
#        for i in range(18, 36):
#            spi.xfer2([bufferoff[i]])
            
        GPIO.output(latch, GPIO.HIGH)
        GPIO.output(latch, GPIO.LOW)
        
        time.sleep(1)
            
except KeyboardInterrupt:
    GPIO.cleanup()
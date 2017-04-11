import spidev
import RPi.GPIO as GPIO
import time

latch = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(latch, GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0, 1)

buffer = list(0x00 for x in range(0, 36))

try:
    while True:
        
        buffer[0]|= 0xFF
        buffer[1]|= 0xF0
        buffer[18]|= 0xFF
        buffer[19]|= 0xF0
        
        buffer[16]&= 0xF0
        buffer[17]&= 0x00
        buffer[34]&= 0xF0
        buffer[35]&= 0x00
        
        for i in range(0, 36):
            spi.xfer2([buffer[i]])
        
        GPIO.output(latch, GPIO.HIGH)
        GPIO.output(latch, GPIO.LOW)    
        
        time.sleep(1)
        
        buffer[16]|= 0x0F
        buffer[17]|= 0xFF
        buffer[34]|= 0x0F
        buffer[35]|= 0xFF
        
        buffer[0]&= 0x00
        buffer[1]&= 0x0F
        buffer[18]&= 0x00
        buffer[19]&= 0x0F
        
        
        for i in range(0, 36):
            spi.xfer2([buffer[i]])
            
        GPIO.output(latch, GPIO.HIGH)
        GPIO.output(latch, GPIO.LOW)
        
        time.sleep(1)
            
except KeyboardInterrupt:
    GPIO.cleanup()
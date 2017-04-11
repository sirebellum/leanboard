def LED_On(LED, buffer):
    
    if (LED % 2) == 0: #even
        i = LED*3/2
        buffer[i]|= 0xFF
        buffer[i+1]|= 0xF0
        return i
        
    elif (LED % 2) != 0: #odd
        i = ((LED-1) * 3/2) + 1
        buffer[i]|= 0x0F
        buffer[i+1]|= 0xFF
        return i

        
def LED_Off(LED, buffer):
    
    if (LED % 2) == 0: #even
        i = LED*3/2
        buffer[i]&= 0x00
        buffer[i+1]&= 0x0F
        return i
        
    elif (LED % 2) != 0: #odd
        i = ((LED-1) * 3/2) + 1
        buffer[i]&= 0xF0
        buffer[i+1]&= 0x00
        return i
#"23 - LED" because SPI LED controller takes most significant LED data first. Serves to reverse the order of data sent to correctly match up buffer index with LED numbers on board

def LED_On(LED, buffer):
    
    if ((23-LED) % 2) == 0: #even
        i = (23 - LED)*3/2
        buffer[i]|= 0xFF
        buffer[i+1]|= 0xF0
        return i
        
    elif ((23-LED) % 2) != 0: #odd
        i = (((23 - LED)-1) * 3/2) + 1
        buffer[i]|= 0x0F
        buffer[i+1]|= 0xFF
        return i


        
def LED_Off(LED, buffer):
    
    if ((23-LED) % 2) == 0: #even
        i = (23 - LED)*3/2
        buffer[i]&= 0x00
        buffer[i+1]&= 0x0F
        return i
        
    elif ((23-LED) % 2) != 0: #odd
        i = (((23 - LED)-1) * 3/2) + 1
        buffer[i]&= 0xF0
        buffer[i+1]&= 0x00
        return i
    
    
    
def LED_Toggle(LED, buffer):
        
    if ((23-LED) % 2) == 0: #even
        i = (23 - LED)*3/2
        buffer[i]^= 0xFF
        buffer[i+1]^= 0xF0
        return i
        
    elif ((23-LED) % 2) != 0: #odd
        i = (((23 - LED)-1) * 3/2) + 1
        buffer[i]^= 0x0F
        buffer[i+1]^= 0xFF
        return i

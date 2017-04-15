#!/usr/bin/python

from lean_board_functions import *
from Adafruit_LED_Backpack import SevenSegment
import datetime
import time as ti
import sys

room = sys.argv[1]

#Determines which 7 segment display to address depending on room specified with command line arg
if room == "Ballroom1":
    segment = SevenSegment.SevenSegment(address=0x70)
    segment.set_invert(1)
elif room == "Ballroom2":
    segment = SevenSegment.SevenSegment(address=0x71)
    segment.set_invert(1)
elif room == "Bexar":
    segment = SevenSegment.SevenSegment(address=0x72)    
elif room == "Denman":
    segment = SevenSegment.SevenSegment(address=0x73)
elif room == "Harris":
    segment = SevenSegment.SevenSegment(address=0x74)
elif room == "Travis":
    segment = SevenSegment.SevenSegment(address=0x75)
    segment.set_invert(1)
else:
    sys.exit("Room did not match an existing room!")


while True:

    init_Seg(segment)

    data = getData(room)
    timestamp = data[0]
    endtime = data[1]
    

#values so that while loop doesn't exit by default
    hours = 1
    minutes = 1
    seconds = 1

#Make sure that submitted event end time is in the future, write "EE-1" error to 7 segment if not
    if calcTime(timeDelta(endtime))[0] < 0:
        segment.clear()
        segment.set_digit(0, "E")
        segment.set_digit(1, "E")
        segment.set_digit(2, "-")
        segment.set_digit(3, "1")
        write_Seg(segment)
        hours = 0     #Ensures while loop never starts
        minutes = 0
        seconds = 0


#Loops until timer's countdown is finished
    while hours+minutes+seconds != 0:

        now = datetime.datetime.now()

        time = calcTime(timeDelta(endtime))

        hours = time[0]
        minutes = time[1]
        seconds = time[2]
        
#Strings to allow iterating over digits to allow easier writing to 7 segment, extra 0 digit to make sure reading 2nd digit from single digit times doesn't go out of array
        if hours < 10: hours_string = "0" + str(hours)
        else: hours_string = str(hours)
    
        if minutes >= 10: minutes_string = str(minutes)
        else: minutes_string = "0" + str(minutes)
        
        if seconds >= 10: seconds_string = str(seconds)
        else: seconds_string = "0" + str(seconds)

#        print hours, minutes, seconds

#Beginning of code block that writes digits to 7 segment depending on time values. Displays hours and minutes if hours exist. Minutes and seconds if hours = 0. "EE99" error code if event is more than 99 hours in the future.
        if hours > 99:
            segment.clear()
            segment.set_digit(0, "E")
            segment.set_digit(1, "E")
            segment.set_digit(2, "9")
            segment.set_digit(3, "9")
            write_Seg(segment)

        elif (hours != 0 and hours <= 99):
            segment.clear()
            segment.set_digit(0, hours_string[0])
            segment.set_digit(1, hours_string[1])
            segment.set_digit(2, minutes_string[0])
            segment.set_digit(3, minutes_string[1])
            segment.set_colon(now.second % 2)
            write_Seg(segment)
        
        elif hours == 0:
            segment.clear()
            segment.set_digit(0, minutes_string[0])
            segment.set_digit(1, minutes_string[1])
            segment.set_digit(2, seconds_string[0])
            segment.set_digit(3, seconds_string[1])
            segment.set_colon(1)
            write_Seg(segment)
    
    
#Exit if newer timestamp detected
        if getData(room)[0] != timestamp:
            segment.clear()
            segment.set_digit(0, "0")
            segment.set_digit(1, "0")
            segment.set_digit(2, "0")
            segment.set_digit(3, "0")
            write_Seg(segment)
            break
    
        ti.sleep(1)
    

#Wait for new data
    while timestamp == getData(room)[0]:
        ti.sleep(1)
    

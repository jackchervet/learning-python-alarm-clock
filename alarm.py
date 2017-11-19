from random import *
from datetime import datetime
import time
import sys
import webbrowser

if len(sys.argv) < 4:
    print('Oops! Invalid number of arguments.')
    print('The arguments should be given in the following format:')
    print('<hour> <minute> <am/pm>')
    print('The arguments recieved were:')
    print(str(sys.argv))
else:
    h = int(sys.argv[1])
    m = int(sys.argv[2])
    mer = str(sys.argv[3]).lower()

    if h < 1 or h > 12:
        print("Invalid argument, expected 'hour' argument between 1 and 12")
        print("Recieved: ", h)
        print("Exiting...")
    elif m < 0 or m > 59:
        print("Invalid argument, expected 'minute' argument between 0 and 59")
        print("Recieved: ", m)
        print("Exiting...")
    elif mer != 'am' and mer != 'pm':
        print("Invalid argument, expected 'am' or 'pm'")
        print("Recieved: ", mer)
        print("Exiting...")
    else:
        if h == 12:
            h = 0
        if mer == 'pm':
            h = h + 12

        currTime = str(datetime.time(datetime.now()))
        ch = int(currTime[:2])
        cm = int(currTime[3:5])

        toSleep = ((h - ch)*60*60) + ((m - cm)*60)
        if toSleep < 0:
            toSleep = toSleep + (24*60*60)

        hours = int(toSleep/(60*60))
        minutes = int((toSleep/60) - (hours*60))

        print("Okay, alarm set for ", hours, " hour(s) and ", minutes, " minute(s) from now.")
        time.sleep(toSleep)

        print("BEEP BEEP BEEP BEEP!")
        vidFile = open("videos.txt", "r")
        vids = vidFile.readlines()
        url = vids[randint(0, (len(vids)-1))]

        webbrowser.open_new(url)

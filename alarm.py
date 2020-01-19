"""
@author: DHRUVIL
"""

import time
from playsound import playsound






print ("What time do you want to wake up?")
print ("Use this format.\nExample: 06:30:00")
Alarm = input("> ")



Time = time.strftime("%H:%M:%S")



while Time != Alarm:
    
    #print ("The time is" + Time)
    
    Time = time.strftime("%H:%M:%S")
    
    
    time.sleep(1)
    
if Time == Alarm:
    
    playsound('C:/Users/DHRUVIL/Downloads/maa.mp3')
    snooze_in = input("Do you want to snooze? press y or n. ")
 

    
    if snooze_in == 'y':
        print("The alarm will start in 5 seconds")
        time.sleep(5)               #snooze for x seconds
        h=time.strftime("%H")
        m=time.strftime("%M")
        s=time.strftime("%S")
        playsound('C:/Users/DHRUVIL/Downloads/maa.mp3')

        #return alarm(h,m,s)

    else:
        exit()          
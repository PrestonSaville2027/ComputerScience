# Blinky

from adafruit_circuitplayground import cp       #Importing cp to allow code in playground to run
import time     #Importing time for code to run on 367ms repetitions


while True:
    cp.pixels.fill((0, 255, 0))
    time.sleep(0.367)
    cp.pixels.fill((0, 0, 0))
    time.sleep(0.367)























# Woosh
 
from adafruit_circuitplayground import cp       #Importing cp to allow code in playground to run
import time     #Importing time for code to run on 367ms repetitions




  


while True:
    if cp.button_a:
        for i in range(0,10):
            cp.pixels[i] = (255, 0, 0) 
            time.sleep(0.1)
            cp.pixels[i] = (0, 0, 0)
        while cp.button_a:  # Wait until button is released
            pass




























# Flip-Flop

from adafruit_circuitplayground import cp




while True:
    if cp.switch == False:
        cp.pixels[0] = (0, 0, 0)   
        cp.pixels[1] = (0, 0, 0)   
        cp.pixels[2] = (0, 0, 0)   
        cp.pixels[3] = (0, 0, 0)   
        cp.pixels[4] = (0, 0, 0)   
        cp.pixels[5] = (0, 255, 0)   
        cp.pixels[6] = (0, 255, 0)   
        cp.pixels[7] = (0, 255, 0)   
        cp.pixels[8] = (0, 255, 0)   
        cp.pixels[9] = (0, 255, 0)   
    elif cp.switch == True:
        cp.pixels[1] = (0, 255, 0)   
        cp.pixels[2] = (0, 255, 0)   
        cp.pixels[3] = (0, 255, 0)   
        cp.pixels[4] = (0, 255, 0)
        cp.pixels[5] = (0, 0, 0)   
        cp.pixels[6] = (0, 0, 0)   
        cp.pixels[7] = (0, 0, 0)   
        cp.pixels[8] = (0, 0, 0)   
        cp.pixels[9] = (0, 0, 0)      
    else:
		     cp.pixels.fill((0,0,0)) # Off









































# Tippy

from adafruit_circuitplayground import cp


while True:
    x, y, z = cp.acceleration  # Get acceleration along X, Y, Z axes
    print("X:", x, "Y:", y, "Z:", z)
    if x > 5: 
        cp.pixels[0] = (0, 0, 0)   
        cp.pixels[1] = (0, 0, 0)   
        cp.pixels[2] = (0, 0, 0)   
        cp.pixels[3] = (0, 0, 0)   
        cp.pixels[4] = (0, 0, 0)   
        cp.pixels[5] = (0, 0, 0)   
        cp.pixels[6] = (0, 255, 0)   
        cp.pixels[7] = (0, 255, 0)   
        cp.pixels[8] = (0, 255, 0)   
        cp.pixels[9] = (0, 0, 0)   
    elif x > -5:
        cp.pixels[1] = (255, 0, 0)   
        cp.pixels[2] = (255, 0, 0)   
        cp.pixels[3] = (255, 0, 0)   
        cp.pixels[4] = (0, 0, 0)   
        cp.pixels[5] = (0, 0, 0)   
        cp.pixels[6] = (0, 0, 0)   
        cp.pixels[7] = (0, 0, 0)   
        cp.pixels[8] = (0, 0, 0)   
        cp.pixels[9] = (0, 0, 0)      
    else:
		     cp.pixels.fill((0,0,0)) # Off

    















# Thermometer

from adafruit_circuitplayground import cp

while True:
    print("Temperature (C):" + cp.temperature)
    temp_c = cp.temperature
    temp_f = (temp_c * 9 / 5) + 32
    print("Temperature (F):" + temp_f)
    if temp_f < 78: 
       cp.pixels[0] = (0, 0, 1)   
       cp.pixels[1] = (0, 0, 0)   
       cp.pixels[2] = (0, 0, 0)   
       cp.pixels[3] = (0, 0, 0)   
       cp.pixels[4] = (0, 0, 0)   
       cp.pixels[5] = (0, 0, 0)   
       cp.pixels[6] = (0, 0, 0)   
       cp.pixels[7] = (0, 0, 0)  
       cp.pixels[8] = (0, 0, 0)   
       cp.pixels[9] = (0, 0, 0)   
    elif temp_f > 78:  
       cp.pixels[0] = (0, 0, 1)   
       cp.pixels[1] = (0, 0, 1)   
       cp.pixels[2] = (0, 0, 0)   
       cp.pixels[3] = (0, 0, 0)   
       cp.pixels[4] = (0, 0, 0)   
       cp.pixels[5] = (0, 0, 0)   
       cp.pixels[6] = (0, 0, 0)   
       cp.pixels[7] = (0, 0, 0)  
       cp.pixels[8] = (0, 0, 0)   
       cp.pixels[9] = (0, 0, 0)   
    elif temp_f > 79:  
       cp.pixels[0] = (0, 0, 1)   
       cp.pixels[1] = (0, 0, 1)   
       cp.pixels[2] = (0, 0, 1)   
       cp.pixels[3] = (0, 0, 0)   
       cp.pixels[4] = (0, 0, 0)   
       cp.pixels[5] = (0, 0, 0)   
       cp.pixels[6] = (0, 0, 0)   
       cp.pixels[7] = (0, 0, 0)  
       cp.pixels[8] = (0, 0, 0)   
       cp.pixels[9] = (0, 0, 0)   
    elif temp_f > 80:  
       cp.pixels[0] = (1, 1, 0)   
       cp.pixels[1] = (1, 1, 0)   
       cp.pixels[2] = (1, 1, 0)   
       cp.pixels[3] = (1, 1, 0)   
       cp.pixels[4] = (0, 0, 0)   
       cp.pixels[5] = (0, 0, 0)   
       cp.pixels[6] = (0, 0, 0)   
       cp.pixels[7] = (0, 0, 0)  
       cp.pixels[8] = (0, 0, 0)   
       cp.pixels[9] = (0, 0, 0)   
    elif temp_f > 81:  
       cp.pixels[0] = (1, 1, 0)   
       cp.pixels[1] = (1, 1, 0)   
       cp.pixels[2] = (1, 1, 0)   
       cp.pixels[3] = (1, 1, 0)   
       cp.pixels[4] = (1, 1, 0)   
       cp.pixels[5] = (0, 0, 0)   
       cp.pixels[6] = (0, 0, 0)   
       cp.pixels[7] = (0, 0, 0)  
       cp.pixels[8] = (0, 0, 0)   
       cp.pixels[9] = (0, 0, 0)   
    elif temp_f > 82:  
       cp.pixels[0] = (1, 1, 0)   
       cp.pixels[1] = (1, 1, 0)   
       cp.pixels[2] = (1, 1, 0)   
       cp.pixels[3] = (1, 1, 0)   
       cp.pixels[4] = (1, 1, 0)   
       cp.pixels[5] = (1, 1, 0)   
       cp.pixels[6] = (0, 0, 0)   
       cp.pixels[7] = (0, 0, 0)  
       cp.pixels[8] = (0, 0, 0)   
       cp.pixels[9] = (0, 0, 0)   
    elif temp_f > 83:  
       cp.pixels[0] = (1, 1, 0)   
       cp.pixels[1] = (1, 1, 0)   
       cp.pixels[2] = (1, 1, 0)   
       cp.pixels[3] = (1, 1, 0)   
       cp.pixels[4] = (1, 1, 0)   
       cp.pixels[5] = (1, 1, 0)   
       cp.pixels[6] = (1, 1, 0)   
       cp.pixels[7] = (0, 0, 0)  
       cp.pixels[8] = (0, 0, 0)   
       cp.pixels[9] = (0, 0, 0)   
    elif temp_f > 84:  
       cp.pixels[0] = (1, 0, 0)   
       cp.pixels[1] = (1, 0, 0)   
       cp.pixels[2] = (1, 0, 0)   
       cp.pixels[3] = (1, 0, 0)   
       cp.pixels[4] = (1, 0, 0)   
       cp.pixels[5] = (1, 0, 0)   
       cp.pixels[6] = (1, 0, 0)   
       cp.pixels[7] = (1, 0, 0)  
       cp.pixels[8] = (0, 0, 0)   
       cp.pixels[9] = (0, 0, 0)   
    elif temp_f > 85:  
       cp.pixels[0] = (1, 0, 0)   
       cp.pixels[1] = (1, 0, 0)   
       cp.pixels[2] = (1, 0, 0)   
       cp.pixels[3] = (1, 0, 0)   
       cp.pixels[4] = (1, 0, 0)   
       cp.pixels[5] = (1, 0, 0)   
       cp.pixels[6] = (1, 0, 0)   
       cp.pixels[7] = (1, 0, 0)  
       cp.pixels[8] = (1, 0, 0)   
       cp.pixels[9] = (0, 0, 0)   
    elif temp_f > 86:  
       cp.pixels[0] = (1, 0, 0)   
       cp.pixels[1] = (1, 0, 0)   
       cp.pixels[2] = (1, 0, 0)   
       cp.pixels[3] = (1, 0, 0)   
       cp.pixels[4] = (1, 0, 0)   
       cp.pixels[5] = (1, 0, 0)   
       cp.pixels[6] = (1, 0, 0)   
       cp.pixels[7] = (1, 0, 0)  
       cp.pixels[8] = (1, 0, 0)   
       cp.pixels[9] = (1, 0, 0)   
   






















# Police Simulator

from adafruit_circuitplayground import cp       #Importing cp to allow code in playground to run
import time     #Importing time for code to run on 367ms repetitions



  


while True:
    cp.pixels.fill((255, 0, 0))
    time.sleep(0.500)
    cp.pixels.fill((0, 0, 255))
    time.sleep(0.500)
    cp.pixels.fill((255, 0, 0))
    time.sleep(0.500)
    cp.pixels.fill((0, 0, 255))
    time.sleep(0.500)
    cp.pixels.fill((255, 0, 0))
    time.sleep(0.500)
    cp.pixels.fill((0, 0, 255))
    time.sleep(0.500)
    cp.pixels.fill((255, 0, 0))
    time.sleep(0.500)
    cp.pixels.fill((0, 0, 255))
    time.sleep(0.500)

    notes = [(500, 0.5), (900, 0.5), (500, 0.5), (900, 0.5)]  

    for frequency, duration in notes:
        cp.play_tone(frequency, duration)
    time.sleep(0.75)  






















# Randomizer

from adafruit_circuitplayground import cp       #Importing cp to allow code in playground to run

import random

while True:
    x, y, z = cp.acceleration
    shake_threshold = 10.0
    if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:
        for i in range (0,10):
            cp.pixels[i] = random.randint(0,255,0), random.randint(0,255,0), random.randint(0,255,0)






















# Dice

from adafruit_circuitplayground import cp       #Importing cp to allow code in playground to run

import random

while True:
    roll = random.randint(0,10)
    if cp.button_a:
        for i in range (0, roll):
            cp.pixels[i] = (0, 0, 255)
    elif cp.button_b:
        cp.pixels.fill((0, 0, 0))









    








# Counter

from adafruit_circuitplayground import cp     #Importing cp to allow code in playground to run
import time     #Import time for program to be able to run on time durations


presses = 0
while True:
    if cp.button_a:    
        if presses < 10:
            cp.pixels[presses] = (1,0,0)       
            presses = presses + 1       
            time.sleep(0.25)
              


    if cp.button_b:     
        if presses > -1:
            cp.pixels[presses] = (0,0,0)       
            presses = presses  - 1
            time.sleep(0.25)




# I didn't do light meter
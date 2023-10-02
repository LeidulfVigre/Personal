#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:57:13 2023

@author: leidulfvigre
"""

import turtle as tl

# Funksjon som lager en haug med fi
def firkanter(antall, storrelse = 5):
    
    tilt = 0     # Starter med 0 graders tilt og endrer med 30 grader senere
    endring1 = 5 # Starter med en endring på 5 piksler
                 # OBS! Viktig at endringen alltid er dobbelt så stor som 
                 # startsstørrelsen! Da blir jo kvadratet dobbelt så stort!
    
    endring2 = 5 # Bruker denne størrelsen to ganger :P
    
    # Setter opp vinduet
    tl.setup(400, 400, 400, 400)
    tl.speed(0)
    tl.Screen().bgcolor('black')
    
    # Antall firkanter en vil lage:
    for i in range(antall):
        
        # Flytter pila til riktig posisjon for hver runde med kvadrater
        tl.penup()
        tl.goto(0,0)
        tl.left(90)
        tl.forward(endring2)
        tl.left(90)
        tl.forward(storrelse/2)
        tl.right(180)
        tl.pendown()
        
       # tl.right(tilt)
        
        # Lager en individuell firkant:
        for j in range(4):
            
            # Endrer fargen på linja på et litt klønete vis
            # FIKS MEG! Kan nok gjøres på en mer elegant måte!!
            if(j == 0):
                tl.color('red')
            elif(j == 1):
                tl.color('yellow')
            elif(j == 2):
                tl.color('green')
            elif(j == 3):
                tl.color('blue')
            
            tl.forward(storrelse)
            tl.right(90)
        
        tl.setheading(0) # Setter retningen til pila mot originalretningen som
                         # den startet med!
        
        tilt += 5 # Øker tilt med 30 grader
        tl.right(tilt)
        
        # Til slutt endres størrelsen med 10 pikler og setter pennen ned
        storrelse += (endring1*2) # Dette er bra! Vil at størrelsen skal være slik.
        
        # Endring må bli større med 5 hver gang slik at endringen for 
        # hvert kvadrat er like stort
        endring2 += 5
        
    # Avslutter programmet
    tl.done()
    
firkanter(50)


#Tracy Sawe
#October 18
#Dartboard Pi

#library
import random

#user's input
squareSize=int(input("What is the size of the square?"))
iterations=int(input("How many iterations?"))
grid=int(input("Print the grid (1=yes, 0=no)?"))

#variables
radius=int(squareSize/2)
hits=0

#number of runs
for i in range (iterations):
#chosing random x,y corrdinates
    dartx=random.uniform(-radius,radius)
    darty=random.uniform(-radius,radius)
    print("the dart lands at(",dartx,",",darty,")")
#calculating hit or miss
    if (dartx**2+darty**2<=radius**2):
        hits=hits+1
        print("hit")
    else:
        print("miss")
#calculating pi
    pi=(hits/iterations)*4
    print("Pi approximation:",pi)
    
#board
    if grid==1:
        print(" *"*(squareSize+2))
        for y in range(radius,-radius-2,-1):
            print("*", end="")
            for x in range(-radius,radius+2):
                print(" ",end="")
#circle equation
                curve=x*x+y*y-radius*radius
                if curve<=radius and curve>=-radius:
                    print(".",end="")
                elif x==(int(dartx)) and y==(int(darty)):
#causes slight displacement of dart 
                    print("<",end="")
                else:
                    print(" ",end="")
            print("*")
        print(" *"*(squareSize+2))


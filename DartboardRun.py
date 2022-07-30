#Tracy Sawe
#october 20
#DartboardPi Run



import random
squareSize=int(input("What is the size of the square?"))
iterations=int(input("How many iterations?"))
grid=int(input("Print the grid (1=yes, 0=no)?"))
radius=int(squareSize/2)
hits=0

for i in range (iterations):
    dartx=random.uniform(-radius,radius)
    darty=random.uniform(-radius,radius)
    print("The dart lands at (",dartx,",",darty,")")
    if (dartx**2+darty**2<=radius**2):
            hits=hits+1
            print("hit")
    else:
        print("miss")

    pi=(hits/iterations)*4
    print("Pi approximation:",pi)
    if grid==1:
        print(" *"*(squareSize+2))
        for y in range(radius,-radius-2,-1):
            print("*", end="")
            for x in range (-radius,radius+2):
                print(" ", end="")
                curve=x*x+y*y-radius*radius
                if curve<=radius and curve>=-radius:
                    print(".",end="")
                elif x==(int(dartx))and y==(int(darty)):
                    print("<",end="")
                else:
                    print(" ",end="")
            print("*")
        print(" *"*(squareSize+2))



    

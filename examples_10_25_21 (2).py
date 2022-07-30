    #prompt for a number, tell who divides it
def divisible():
    number=int(input("Enter a number: "))
    for i in range(number):
        #if the number is divisible by i, then
        if number%(i+1)==0:
            print(number,"is divisible by",(i+1))

def biggestoftwo():
    a = int(input("enter number 'a': "))
    b = int(input("enter number 'b': "))
    if a>b:
        print("a is biggest")
    elif a<b:
        print("b is biggest")
    else:
        print("a is equal to b")

def biggestofthree():
    a = int(input("enter number 'a': "))
    b = int(input("enter number 'b': "))
    c = int(input("enter number 'c': "))

    if a>b:
        #a is bigger
        if a>c:
            print("a is biggest")
        else:
            print("c is biggest")
    else:
        #b is bigger
        if b>c:
            print("b is biggest")
        else:
            print("c is biggest")


def biggestoffour():
    a = int(input("enter number 'a': "))
    b = int(input("enter number 'b': "))
    c = int(input("enter number 'c': "))
    d = int(input("enter number 'd': "))
    #identity of first
    biggestsofar="a"
    #size of first
    biggestsofarvalue=a
    
    #check is b is better than best so far?
    if b>biggestsofarvalue:
        #b is bigger
        #adjust our biggest
        biggestsofar="b"
        biggestsofarvalue=b
    # b is smaller: do anything? np: no need for else
    #c
    if c>biggestsofarvalue:
        biggestsofar="c"
        biggestsofarvalue=c
    #d
    if d>biggestsofarvalue:
        biggestsofar="d"
        biggestsofarvalue=d
    print("the biggest is",biggestsofar)

def savings():
    balance=float(input("How much money do you start with?"))
    years=0
    while balance<1000000:
        #handle one year of interest
        interest=balance*.01
        balance=balance+interest
#        print("you have",balance)
        years=years+1
    print("it took you ",years,"years to reach 1 million")

def GPAexample():
    GPA=3.9
    classes=30
    Dcounter=0
    while GPA>=2.0:
    #every time we earn a class, let's average it
        lettergrade=1.0
        GPA=(classes*GPA+lettergrade)/(classes+1)
        Dcounter=Dcounter+1
    print("You can earn ",Dcounter-1,"D's")
GPAexample()

#Tracy Sawe
#November 19
#Minesweaper

#library
import random 


def game():
    #just has dots
    board=makeboard()
    #has dots and bomb
    board=plantmines(board)
    reveal=makereveal()
    while not won(board, reveal):
        y=int(input("Chose a y coordinate?"))
        x=int(input("Chose an x coordinate?"))
        reveal[x][y]=True
        printboard(board, reveal)
        if board[x][y]=="*":
            print("!!!!!!!BOOM!!!!!!!!!!!!!!!!!")
            #restars the game
            return
        
    
def makeboard():
    #makes a list for the board
    board=['.']
    board=board*10
    for i in range (10):
        board[i]=['.']*10
    #returns board list
    return board

def plantmines(board):
    for y in range (10):
        for x in range (10):
            #chooses a random spot from the list to make a mine
            minex=random.random()
            #plants the mine in the list
            if minex<0.1:
                board[y][x]='*'
    #returns list with mine            
    return board

def printboard(board, reveal):
    #shows x cooridinates
    print('  0123456789')
    for y in range (10):
        #y cooridinates 
        if(y > 0):
            print()
        print(str(y) + ' ', end='')
        for x in range (10):
            #reveals the coordinates the user choses
            if reveal[x][y]==True:
                if board[x][y]!="*":
                    board[x][y]='.'
                print(board[x][y], end="")
            #hides everything else
            else:
                board[x][y]='X'
                print(board[x][y], end="")
    print()
    

def makereveal():
    #list that corilates with the board
    reveal=[False]
    reveal=reveal*10
    for i in range (10):
        reveal[i]=[False]*10
    return reveal

#def placenumber(board)

#if board[x-1]==0
#if board[y-1]==0

def won(board, reveal):
    for y in range (10):
        for x in range (10):
            if board[x][y]!='*' and reveal[x][y]==False:
                return False
    return True

game()

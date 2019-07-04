# (C) Copyright: Daniel Rusu #
##############################


######################################################
###################### Imports #######################
######################################################

from sys    import stdin, stdout
from os     import name, system
from time   import sleep

######################################################


namePlayer1     = None          # First name 
namePlayer2     = None          # Second name
isBoxChecked    = ['-'] * 9     # Box values
whoTurnIs       = 1             # Who is at turn

######################################################

######################################################
############### Clear screen function ################
######################################################


def clear_screen():
    if name == 'nt':
        _ = system('cls') # windows
    else:
        _ = system('clear') # mac or linux


######################################################

######################################################
############ Debug function ##########################
######################################################


def debug(*args):
    for x in args:
        print(x, end = ' ')

######################################################

######################################################
#############  Start up countdown function ###########
######################################################

def startUpGame():
    print("Game starts in...")
    for i in range(3, 0, -1):
        print(str(i) + "...")
        sleep(1)
  
    clear_screen()
    print("GO")
    sleep(2)

######################################################

######################################################
############## Table Display #########################
######################################################

def displayTable():
    global isBoxChecked

    position = 0

    for i in range(3):
        for j in range(3):
            print(isBoxChecked[position], end = ' ')
            position += 1
        print("\n")

######################################################

######################################################
############ Prepare the game ########################
######################################################

def readInputData():
    global namePlayer1
    global namePlayer2
    namePlayer1 = input("Name of the first player: ")
    namePlayer2 = input("Name of the second player: ")

    print(namePlayer1 + " will be with X and " + namePlayer2 + " will be with 0. X starts! \n")

    print("The number of each box is as shown down:\n1 2 3\n4 5 6\n7 8 9\n\nGo?[y/n]: ")

    answerQuestion = input()

    while answerQuestion != 'y' and answerQuestion != 'n':
        debug(answerQuestion)
        answerQuestion = input("Please answer only with 'y' or 'n' (y -> yes and n -> no): ")

    if answerQuestion == 'y':
        startUpGame()
        game()
    else:
        print("Exiting game. Restart the program")

######################################################

######################################################
################## Check if is end game ##############
######################################################

def isEnd():
    # 0 - end
    # 1 - player 1 wins
    # 2 - player 2 wins
    # 3 - draw

    global isBoxChecked

    for i in range(3):
        x = 3 * i
        x = int(x)

        if isBoxChecked[x] == isBoxChecked[x + 1] == isBoxChecked[x + 2] and isBoxChecked[x] != '-':
            if isBoxChecked[x] == 'X':
                return 1
            else:
                return 2
        elif isBoxChecked[i] == isBoxChecked[i + 3] == isBoxChecked[i + 6] and isBoxChecked[i] != '-':
            if isBoxChecked[i] == 'X':
                return 1
            else:
                return 2
    
    if isBoxChecked[0] == isBoxChecked[4] == isBoxChecked[8] and isBoxChecked[0] != '-':
        if isBoxChecked[0] == 'X':
            return 1
        else:
            return 2
    
    if isBoxChecked[2] == isBoxChecked[4] == isBoxChecked[6] and isBoxChecked[2] != '-':
        if isBoxChecked[2] == 'X':
            return 1
    
    for i in range(9):
        if isBoxChecked[i] == '-':
            return 0

    return 3

######################################################

######################################################
################### The game #########################
######################################################

def game():
    global isBoxChecked
    global namePlayer1
    global namePlayer2
    global whoTurnIs

    while not(isEnd()):
        clear_screen()
        charToPut = None

        if whoTurnIs == 1:
            print(namePlayer1 + " is at turn\n\n")
            charToPut = 'X'
        else:
            print(namePlayer2 + " is at turn\n\n")
            charToPut = 'O'

        position = 0

        for i in range(3):
            for j in range(3):
                print(isBoxChecked[position], end = ' ')
                position += 1
            print("\n")

        print("\n\n")

        answerBox = input("Please choose a position: ")

        while not(valid(answerBox)):
            print("\n\nThe position you picked isn't correct. You have to choose a position from [1-9] which ")
            print("is not completed before")
            print("The number of each box is as shown down:\n1 2 3\n4 5 6\n7 8 9\n\n'-' is for empty boxes.")
            answerBox = input("Please choose a position: ")

        answerBox = int(answerBox)

        isBoxChecked[answerBox - 1] = charToPut
        whoTurnIs = 3 - whoTurnIs

    clear_screen()

    winner = isEnd()

    if winner == 1:
        print(namePlayer1 + " won!\n\n")
    elif winner == 2:
        print(namePlayer2 + " won!\n\n")
    elif winner == 3:
        print("Is a draw\n\n")

    displayTable()

######################################################

######################################################
################## Box Valid Check ###################
######################################################

def valid(pos):
    global isBoxChecked

    try:
        pos = int(pos)
    except:
        return False

    if pos < 1 or pos > 9:
        return False
    
    if isBoxChecked[pos - 1] != '-':
        return False

    return True

######################################################

######################################################
####################### Game Engine ##################
######################################################

readInputData()

######################################################

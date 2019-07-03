from sys import stdin, stdout
from os import name, system
from time import sleep

def clear_screen():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

def debug(*args):
  for x in args:
    print(x, end = " ")

def startUpGame():
  print("Game starts in...")
  for i in range(3, 0, -1):
    print(str(i) + "...")
    sleep(1)
  
  clear_screen()
  print("GO")

def readInputData():
  global namePlayer1
  global namePlayer2
  namePlayer1 = input("Name of the first player:")
  namePlayer2 = input("Name of the second player:")

  print(namePlayer1 + " will be with X and " + namePlayer2 + " will be with 0. X starts! Go? [y/n]")
  answerQuestion = input()

  while answerQuestion != 'y' and answerQuestion != 'n':
    debug(answerQuestion)
    answerQuestion = input("Please answer only with 'y' or 'n' (y -> yes and n -> no): ")

  if answerQuestion == 'y':
    startUpGame()
  else:
    print("Exiting game. Restart the program")

  exit

# Global Data 
namePlayer1, namePlayer2 = 0, 0

readInputData()
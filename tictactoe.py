from sys import stdin, stdout

def clear_screen():
  print("\n" * 100)

def debug(*args):
  for x in args:
    print(x, end = " ")

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

# Global Data 
namePlayer1, namePlayer2 = 0, 0

readInputData()

debug(namePlayer1, namePlayer2)
#!/usr/bin/env python3
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

def readfile():
  data = []
  datafile = datafilename()
  with open(datafile, 'r') as file:
    for line in file:
      data.append(tuple(line.strip().split(' ')))
  return data

def outcome(a, b):
  if a == 'rock' and b == 'rock':
    return 'tie'
  elif a == 'rock' and b == 'paper':
    return 'lose'
  elif a == 'rock' and b == 'scissors':
    return 'win'
  elif a == 'paper' and b == 'rock':
    return 'win'
  elif a == 'paper' and b == 'paper':
    return 'tie'
  elif a == 'paper' and b == 'scissors':
    return 'lose'
  elif a == 'scissors' and b == 'rock':
    return 'lose'
  elif a == 'scissors' and b == 'paper':
    return 'win'
  elif a == 'scissors' and b == 'scissors':
    return 'tie'
  else:
    print("error in comparison. quitting.")
    quit()

def mymove(theirmove, outcome):
  if theirmove   == 'rock'     and outcome == 'lose':
    return 'scissors'
  elif theirmove == 'paper'    and outcome == 'lose':
    return 'rock'
  elif theirmove == 'scissors' and outcome == 'lose':
    return 'paper'
  elif theirmove == 'rock'     and outcome == 'win':
    return 'paper'
  elif theirmove == 'paper'    and outcome == 'win':
    return 'scissors'
  elif theirmove == 'scissors' and outcome == 'win':
    return 'rock'
  elif outcome   == 'tie':
    return theirmove

theirmoves = {
  'A': 'rock',
  'B': 'paper',
  'C': 'scissors'
}
myoutcomes = {
  'X': 'lose',
  'Y': 'tie',
  'Z': 'win'
}
points = {
  'rock': 1,
  'paper': 2,
  'scissors': 3,
  'win': 6,
  'tie': 3,
  'lose': 0
}
moves=readfile()
totalpoints=0
i=0
for move in moves:
  totalpoints+=points[mymove(theirmoves[move[0]], myoutcomes[move[1]])] + points[myoutcomes[move[1]]]
  i+=1
  print(f"{i}: {totalpoints}")
#print(f"{points[mymoves[readfile()[0][0]]] + points[outcome(mymoves[readfile()[0][0]], theirmoves[readfile()[0][1]])]}")

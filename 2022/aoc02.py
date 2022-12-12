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

mymoves = {
  'A': 'rock',
  'B': 'paper',
  'C': 'scissors'
}
theirmoves = {
  'X': 'rock',
  'Y': 'paper',
  'Z': 'scissors'
}
points = {
  'rock': 1,
  'paper': 2,
  'scissors': 3,
  'win': 6,
  'tie': 3,
  'lose': 0
}
print(f"{points[mymoves[readfile()[0][0]]] + points[outcome(mymoves[readfile()[0][0]], theirmoves[readfile()[0][1]])]}")

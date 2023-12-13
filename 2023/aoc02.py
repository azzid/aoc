#!/usr/bin/env python3
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

def readfile():
  data = {}
  datafile = datafilename()
  with open(datafile, 'r') as file:
    for line in file:
      gameno = int(line.split(':')[0].split(' ')[1])
      data[gameno] = []
      for pullstr in line.split(':')[1].split(';'):
        d = {}
        for colstr in pullstr.split(','):
          color = colstr.strip().split()[1]
          num   = int(colstr.strip().split()[0])
          d[color]=num
        data[gameno].append(d)
  return data

def gameisvalid(game):
  valid = True
  for pull in game:
    for color in pull.keys():
      if pull[color] > bag[color]:
        valid = False
  return valid
  

# Max valid colors - can't pull more than you have in the bag
bag = { 'red': 12, 'green': 13, 'blue': 14 }
games = readfile()
summ = 0
for gameno in games.keys():
  if gameisvalid(games[gameno]): summ += gameno
print(summ)

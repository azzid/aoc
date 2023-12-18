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
      draw = {}
      winner, ticket = line.split(':')[1].split('|')
      draw['winner'] = winner.split()
      draw['ticket'] = ticket.split()
      data.append(draw)
  return data

numberoftickets = {}
for i, draw in enumerate(readfile()):
  numwinnums = len(set(draw['winner']).intersection(set(draw['ticket'])))
  print(f"wins: {numwinnums}")
  for j in range(1,numwinnums+2):
    print(f"i: {i}, j: {j}")
    try:
      multiplier = numberoftickets[i+1]
    except:
      multiplier = 1
    try:
      numberoftickets[i+j] += multiplier
    except:
      numberoftickets[i+j] = multiplier
print(numberoftickets)
print(sum(numberoftickets.values()))

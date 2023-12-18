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
# i starts on 0
for i, draw in enumerate(readfile()):
  n = i+1
  numwinnums = len(set(draw['winner']).intersection(set(draw['ticket'])))
  print(f"wins: {numwinnums}")
  try:
    multiplier = numberoftickets[n]+1
  except:
    multiplier = 1
  for j in range(1,numwinnums+2):
    print(f"n: {n}, j: {j}")
    if j == 1:
      try:
        numberoftickets[i+j] += 1
      except:
        numberoftickets[i+j] = 1
    else:
      try:
        numberoftickets[i+j] += multiplier
      except:
        numberoftickets[i+j] = multiplier
print(numberoftickets)
print(sum(numberoftickets.values()))

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
  for j in range(1,numwinnums+2):
    try:
      numberoftickets[i+j] += 1
    except:
      numberoftickets[i+j] = 1
print(sum(numberoftickets.values()))

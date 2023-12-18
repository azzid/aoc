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

points = 0
for draw in readfile():
  numwinnums = len(set(draw['winner']).intersection(set(draw['ticket'])))
  #print(numwinnums)
  if numwinnums > 0:
    points = points + 2**(numwinnums-1)
print(points)

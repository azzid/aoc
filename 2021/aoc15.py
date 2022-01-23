#!/usr/local/bin/python3
from pathlib import Path
from time import time
from itertools import product
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

def readfile():
  riskmap = []
  datafile = datafilename()
  with open(datafile, 'r') as file:
    for line in file:
      riskmap.append([int(a) for a in list(line.strip())])
  return riskmap

def validnextsteps(pos, riskmap, prevpos=None):
  minX, minY, maxX, maxY = 0, 0, len(riskmap[0])-1, len(riskmap)-1
  posX = pos[0]
  posY = pos[1]
  xrange = range(max(minX, posX-1), min(maxX, posX+1)+1)
  yrange = range(max(minY, posY-1), min(maxY, posY+1)+1)
  square = list(product(xrange, yrange))
  nexsteps = [ point for point in square if
             ( point[0] == pos[0] and point[1] != pos[1] ) or
             ( point[1] == pos[1] and point[0] != pos[0] ) and
               not point == prevpos ]
  return nexsteps

def first():
  starttime = time()
  riskmap = readfile()
  maxX, maxY = len(riskmap[0])-1, len(riskmap)-1
  pos = (0,0)
  goal = (maxX, maxY)
  pathrisk = 0
  print(f"{validnextsteps(pos, riskmap)}")
  quit()
  while pos[0] < goal[0] or pos[1] < goal[1]:
    if pos[0] < goal[0] and pos[1] < goal[1]:
      if riskmap[pos[1]+1][pos[0]] > riskmap[pos[1]][pos[0]+1]:
        pos = (pos[0]+1, pos[1])
      elif riskmap[pos[1]+1][pos[0]] <= riskmap[pos[1]][pos[0]+1]:
        pos = (pos[0], pos[1]+1)
    elif pos[1] == goal[1]:
      pos = (pos[0]+1, pos[1])
    elif pos[0] == goal[0]:
      pos = (pos[0], pos[1]+1)
    else:
      print(f"should probably never get here. quit.")
      quit()
    pathrisk += riskmap[pos[1]][pos[0]]
  print(f"risk: {pathrisk}")

first()

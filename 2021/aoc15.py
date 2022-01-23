#!/usr/local/bin/python3
from pathlib import Path
from time import time
from itertools import product
from copy import deepcopy
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
  paths = []
  for nextstep in validnextsteps(pos, riskmap):
    path = [pos, nextstep]
    paths.append(path)
  unfinishedpaths = [ p for p in paths if p[-1][0] < maxX or p[-1][1] < maxY ]
  print(f"{unfinishedpaths}")

first()

#!/usr/local/bin/python3
from pathlib import Path
from time import time
from itertools import product
from copy import deepcopy
from math import sqrt
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

def validnextsteps(path, riskmap):
  minX, minY, maxX, maxY = 0, 0, len(riskmap[0])-1, len(riskmap)-1
  pos = path[-1]
  posX = pos[0]
  posY = pos[1]
  xrange = range(max(minX, posX-1), min(maxX, posX+1)+1)
  yrange = range(max(minY, posY-1), min(maxY, posY+1)+1)
  square = list(product(xrange, yrange))
  nextsteps = [ point for point in square if (
             ( point[0] == posX and point[1] != posY ) or
             ( point[1] == posY and point[0] != posX )) and
               not point in path ]
  #print(f"pos: {pos}, next: {nextsteps}")
  return nextsteps

def pathcost(path, riskmap):
  cost = 0
  for step in path[1:]:
    cost += riskmap[step[1]][step[0]]
  return cost

def pathdistanceleft(path, goal):
  pos = path[-1]
  diffX = goal[0] - pos[0]
  diffY = goal[1] - pos[1]
  distance = sqrt(diffX ** 2 + diffY ** 2)
  return distance

def first():
  starttime = time()
  riskmap = readfile()
  maxX, maxY = len(riskmap[0])-1, len(riskmap)-1
  startpos = (0,0)
  goal = (maxX, maxY)
  pathrisk = 0
  paths = []
  for nextstep in validnextsteps([startpos], riskmap):
    path = [startpos, nextstep]
    paths.append(path)
  unfinishedpaths = [ p for p in paths if p[-1][0] < maxX or p[-1][1] < maxY ]
  while unfinishedpaths:
    for path in unfinishedpaths[:3]:
      paths.remove(path)
      for nextstep in validnextsteps(path, riskmap):
        newpath = deepcopy(path+[nextstep])
        if pathcost(newpath, riskmap) <= 816:
          paths.append(newpath)
    unfinishedpaths = [ p for p in paths if p[-1][0] < maxX or p[-1][1] < maxY ]
    unfinishedpaths.sort(key=lambda x: pathcost(x, riskmap))
    for path in unfinishedpaths[:3]:
      print(f"cost: {pathcost(path, riskmap)}, distance: {pathdistanceleft(path, goal)}")
    finishedpaths = [ p for p in paths if p[-1][0] == maxX and p[-1][1] == maxY ]
    if finishedpaths:
      print(f"mincost: {min([ pathcost(path, riskmap) for path in finishedpaths ])}")

first()

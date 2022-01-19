#!/usr/local/bin/python3
from pathlib import Path
from collections import Counter
from time import time
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

def first():
  starttime = time()
  riskmap = readfile()
  maxX, maxY = len(riskmap[0])-1, len(riskmap)-1
  pos = [0,0]
  goal = [maxX, maxY]
  pathrisk = 0
  #import code
  #code.interact(local=locals())
  #riskmap[pos[1]][pos[0]]
  #print(f"top left: {riskmap[0][0:3]}, bottom right: {riskmap[-1][-4:-1]}")
  #print(f"lenX: {maxX}, lenY: {maxY}")
  #print(f"goal: {riskmap[maxY][maxX]}")
  while pos[0] < goal[0] or pos[1] < goal[1]:
    if pos[0] < goal[0] and pos[1] < goal[1]:
      if riskmap[pos[1]+1][pos[0]] > riskmap[pos[1]][pos[0]+1]:
        pos[0] += 1
      elif riskmap[pos[1]+1][pos[0]] <= riskmap[pos[1]][pos[0]+1]:
        pos[1] += 1
    elif pos[1] == goal[1]:
      pos[0] += 1
    elif pos[0] == goal[0]:
      pos[1] += 1
    else:
      print(f"should probably never get here. quit.")
      quit()
    pathrisk += riskmap[pos[1]][pos[0]]
  print(f"risk: {pathrisk}")

first()

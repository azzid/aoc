#!/usr/local/bin/python3
from functools import reduce
def readfile():
  data = []
  with open('aoc09.txt', 'r') as file:
    for line in file:
    # list(map(int, hits))
      data.append(list(map(int, list(line.strip()))))
  return data

def islowpoint(x,y,data):
  boolean = True
  xmin = 0
  ymin = 0
  xmax = len(data[0])-1
  ymax = len(data)-1
  
  above = (x, y-1)
  below = (x, y+1)
  right = (x+1, y)
  left  = (x-1, y)

  for direction in [above, below, right, left]:
    if xmin <= direction[0] <= xmax and ymin <= direction[1] <= ymax:
      if data[direction[1]][direction[0]] > data[y][x]:
        boolean = boolean and True
      else:
        boolean = boolean and False

  return boolean
      
def basinset(lowpoint, data, lpbset):
  lpbset.add(lowpoint)

  x = lowpoint[0]
  y = lowpoint[1]
  xmin = 0
  ymin = 0
  xmax = len(data[0])-1
  ymax = len(data)-1
  
  above = (x, y-1)
  below = (x, y+1)
  right = (x+1, y)
  left  = (x-1, y)
  
  for direction in [above, below, right, left]:
    if xmin <= direction[0] <= xmax and ymin <= direction[1] <= ymax:
      if data[direction[1]][direction[0]] < 9 and not direction in lpbset:
        lpbset.update(basinset(direction, data, lpbset))
  return lpbset

def first():
  data = readfile()
  lowpoints = []
  risk = 0
  #x, y = 1, 1
  #print(f"{data[y][x]}")
  for y in range(len(data)):
    for x in range(len(data[0])):
      if islowpoint(x,y,data):
        lowpoints.append((x,y))
  for lp in lowpoints:
    risk += data[lp[1]][lp[0]]+1
  print(f"Risk: {risk}")

def second():
  data = readfile()
  lowpoints = []
  basinsizes = []
  #x, y = 1, 1
  #print(f"{data[y][x]}")
  for y in range(len(data)):
    for x in range(len(data[0])):
      if islowpoint(x,y,data):
        lowpoints.append((x,y))
  for lp in lowpoints:
    lpbset = set()
    basinsizes.append(len(basinset(lp, data, lpbset)))

  basinsizes.sort()

  print(f"Three largest basins multiplied: {reduce((lambda a, b:a*b), basinsizes[-3:])}")

second()

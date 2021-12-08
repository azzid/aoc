#!/usr/local/bin/python3
from functools import reduce

def readfile():
  coordinates = []
  #Example line: 720,475 -> 720,669
  with open('aoc05.txt', 'r') as file:
    for line in file:
      start, stop = line.strip().split(' -> ')
      startx, starty = map(int, start.split(','))
      stopx, stopy   = map(int, stop.split(','))
      coordinates.append([[startx,starty],[stopx,stopy]])
  return coordinates

def first():
  coordinates = readfile()
  # remove diagonal lines
  coordinates = list(filter(lambda line: line[0][0] == line[1][0] or line[0][1] == line[1][1], coordinates))
  maxcoordinate = max(reduce(lambda a, b: a+b, reduce(lambda a, b: a+b, coordinates)))+2
  diagram = []
  for i in range(maxcoordinate):
    diagram.append(maxcoordinate * [0])
  for line in coordinates:
    start, stop = line
    x1, y1 = start
    x2, y2 = stop
    if x1 == x2:
      x = x1
      if y1 < y2:
        for y in range(y1, y2+1):
          diagram[y][x] += 1
      else:
        for y in range(y2, y1+1):
          diagram[y][x] += 1
    elif y1 == y2:
      y = y1
      if x1 < x2:
        for x in range(x1, x2+1):
          diagram[y][x] += 1
      else:
        for x in range(x2, x1+1):
          diagram[y][x] += 1
  print(f"{len(list(filter(lambda z: z > 1, reduce(lambda a, b: a+b, diagram))))}")

def second():
  coordinates = readfile()
  # remove diagonal lines
  coordinates = list(filter(lambda line: line[0][0] == line[1][0] or line[0][1] == line[1][1], coordinates))
  maxcoordinate = max(reduce(lambda a, b: a+b, reduce(lambda a, b: a+b, coordinates)))+2
  diagram = []
  for i in range(maxcoordinate):
    diagram.append(maxcoordinate * [0])
  for line in coordinates:
    start, stop = line
    x1, y1 = start
    x2, y2 = stop
    if x1 == x2:
      x = x1
      for y in range(min(y1,y2), max(y1,y2)+1):
        diagram[y][x] += 1
    elif y1 == y2:
      y = y1
      for x in range(min(x1,x2), max(x1,x2)+1):
        diagram[y][x] += 1
  print(f"{len(list(filter(lambda z: z > 1, reduce(lambda a, b: a+b, diagram))))}")

second()

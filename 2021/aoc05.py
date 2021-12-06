#!/usr/local/bin/python3
def readfile():
  coordinates = []
  #720,475 -> 720,669
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
  coordinates = filter(lambda line: line[0][0] == line[1][0] or line[0][1] == line[1][1], coordinates)

first()

#!/usr/local/bin/python3
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

def readfile():
  points = []
  folds = []
  datafile = datafilename()
  with open(datafile, 'r') as file:
    for line in file:
      if ',' in line:
        strpoint = line.strip().split(',')
        point = tuple((int(strpoint[0]), int(strpoint[1])))
        points.append(point)
      elif '=' in line:
        strfold = line.strip().split()[2].split('=')
        fold = tuple((strfold[0], int(strfold[1])))
        folds.append(fold)
  return points, folds

def makeblankmap(x, y):
  return [[False] * x] * y

def first():
  points, folds = readfile()
  maxX = max([point[0] for point in points])
  maxY = max([point[1] for point in points])
  maparray = makeblankmap(maxX+1, maxY+1)

first()

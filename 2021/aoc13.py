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

def makeblankpaper(x, y):
  line = []
  lines = []
  for i in range(x):
    line.append(False)
  for i in range(y):
    lines.append(line[:])
  return lines

def putpointsonpaper(points, paper):
  for point in points:
    paper[point[1]][point[0]] = True

def foldpaper(paper, fold):
  if fold[0] == 'x':
    print(f"TODO: X-type fold along line {fold[1]}")
  elif fold[0] == 'y':
    print(f"TODO: Y-type fold along line {fold[1]}")
  else:
    print(f"Unidentified fold direction. Error.")
    quit()
  
def first():
  points, folds = readfile()
  maxX = max([point[0] for point in points])
  maxY = max([point[1] for point in points])
  paper = makeblankpaper(maxX+1, maxY+1)
  putpointsonpaper(points, paper)
  foldpaper(paper, folds[0])
  #print(f"{paper}")

first()

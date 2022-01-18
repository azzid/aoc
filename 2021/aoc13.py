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
  foldline = fold[1]
  if fold[0] == 'y':
    # Cut away everything below fold
    newpaper = paper[:foldline]
    # Figure out the size of the flap getting folded up
    foldsize = len(paper[foldline+1:])
    if foldsize > len(newpaper):
      print(f"folded flap longer than remaining paper. error.")
      quit()
    for offset in range(1,foldsize+1):
      #>>> a
      #[True, False, False]
      #>>> b
      #[False, True, False]
      #>>> [tup[0]|tup[1] for tup in zip(a,b)]
      #[True, True, False]
      newpaper[foldline-offset] = [overlap[0]|overlap[1] for overlap in zip(paper[foldline-offset],paper[foldline+offset])]
  elif fold[0] == 'x':
    rotatedpaper = rotatepaperclockwise(paper)
    rotatedpaper = foldpaper(rotatedpaper, ('y', fold[1]))
    newpaper = rotatepaperback(rotatedpaper)
  else:
    print(f"Unidentified fold direction. Error.")
    quit()
  return newpaper

def rotatepaperclockwise(paper):
 return list(list(x)[::-1] for x in zip(*paper)) 

def rotatepaperback(paper):
  return list(map(list, zip(*paper)))[::-1]

def countpointsonpaper(paper):
  # Flatten 2d list
  paperpoints = [j for sub in paper for j in sub]
  # Return count of 'True's
  return paperpoints.count(True)

def displaypaper(paper, xfold=None, yfold=None):
  x = 0
  for line in paper:
    y = 0
    for dot in line:
      if x == yfold and y == xfold:
        print(f"+", end ="")
      elif x == yfold:
        print(f"-", end ="")
      elif y == xfold:
        print(f"|", end ="")
      elif dot:
        print(f"#", end ="")
      else:
        print(f".", end ="")
      y += 1
    print(f"")
    x += 1
  
def first():
  points, folds = readfile()
  maxX = max([point[0] for point in points])
  maxY = max([point[1] for point in points])
  paper = makeblankpaper(maxX+1, maxY+1)
  putpointsonpaper(points, paper)
  for fold in folds:
    paper = foldpaper(paper, fold)
  displaypaper(paper)

first()

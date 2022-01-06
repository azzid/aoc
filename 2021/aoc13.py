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
        point = tuple(line.strip().split(','))
        points.append(point)
      elif '=' in line:
        fold = tuple(line.strip().split()[2].split('='))
        folds.append(fold)
  return points, folds

def first():
  points, folds = readfile()
  maxX = max([int(point[0]) for point in points])
  maxY = max([int(point[1]) for point in points])
  print(f"1st point: {points[0]}, 1st fold: {folds[0]}")
  print(f"last point: {points[-1]}, last fold: {folds[-1]}")
  print(f"#points: {len(points)}, #folds: {len(folds)}")
  print(f"max X:{maxX}, max Y:{maxY}")

first()

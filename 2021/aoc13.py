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
        fold = tuple(line.split()[2].split('='))
        folds.append(fold)
  return points, folds

def first():
  points, folds = readfile()
  print(f"1st point: {points[0]}, 1st fold: {folds[0]}")
  print(f"last point: {points[-1]}, last fold: {folds[-1]}")

first()

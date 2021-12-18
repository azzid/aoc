#!/usr/local/bin/python3
from copy import deepcopy
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

data = []
def readfile():
  global data
  datafile = datafilename()
  with open(datafile, 'r') as file:
    for line in file:
      points = tuple(line.strip().split('-'))
      data.append(tuple((points[0], points[1])))
      data.append(tuple((points[1], points[0])))

def possiblenext(path):
  global data
  # Impossibly clever way to keep track of visited small caves
  visitedsmallcaves = list(set([point for edge in path for point in edge if point.islower()]))
  #print(f"path: {path} has visited {visitedsmallcaves} small caves")
  if not path:
    # Path not started, first edge[0] is 'start' mandatory
    starts = [edge for edge in data if edge[0] == 'start']
    #print(f"path {path} has not started, return starts ({starts})")
    return starts
  elif path[-1][-1] == 'end' or 'DEAD END' in path:
    # Path has reached end. No next step.
    #print(f"Path has reached end. No next step in {path}")
    return []
  else:
    nexts = [edge for edge in data if path[-1][1] == edge[0] and not edge[1] in visitedsmallcaves]
    if nexts:
      #print(f"path {path} can continue via {nexts}")
      return nexts
    else:
      #print(f"path {path} seem to be a dead end")
      return ["DEAD END"]

def first():
  readfile()
  path = []
  paths = []
  # Seed paths with start edges
  for nextstep in possiblenext(path):
    path.append(nextstep)
    paths.append(deepcopy(path))
    path.remove(nextstep)
  unfinishedpaths = deepcopy(paths)
  while unfinishedpaths:
    for path in unfinishedpaths:
      #print(f"current unfinished path: {path}")
      paths.remove(path)
      for nextstep in possiblenext(path):
        path.append(nextstep)
        paths.append(deepcopy(path))
        path.remove(nextstep)
    unfinishedpaths = [path for path in paths if not path[-1][-1] == 'end']
    #print(f"unfinished: {unfinishedpaths}")
  print(f"{len(paths)}")
  
def second():
  data = readfile()

first()

#!/usr/local/bin/python3
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

def readfile():
  data = []
  datafile = datafilename()
  with open(datafile, 'r') as file:
    for line in file:
      data.append(tuple(line.strip().split('-')))
  return data

def possiblenext(path, data):
  # Impossibly clever way to keep track of visited small caves
  visitedsmallcaves = list(set([point for edge in path for point in edge if point.islower()]))
  if not path:
    # Path not started, first edge[0] is 'start' mandatory
    starts = [edge for edge in data if edge[0] == 'start']
    return starts
  if path[-1][1] == 'end':
    # Path has reached end. No next step.
    return []
  else:
    nexts = [edge for edge in data if path[-1][1] == edge[0] and not edge[1] in visitedsmallcaves]
    return nexts

def first():
  data = readfile()
  path = []
  path.append(possiblenext(path, data)[0])
  print(f"{possiblenext(path, data)}")
  

def second():
  data = readfile()

first()

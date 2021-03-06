#!/usr/local/bin/python3
from time import time
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
  if not path:
    # Path not started, first edge[0] is 'start' mandatory
    starts = [edge for edge in data if edge[0] == 'start']
    return starts
  elif path[-1][-1] == 'end' or 'DEAD END' in path:
    # Path has reached end. No next step.
    return []
  else:
    nexts = [edge for edge in data if path[-1][1] == edge[0] and not edge[1] in visitedsmallcaves]
    if nexts:
      return nexts
    else:
      return ["DEAD END"]

def possiblenext2(path):
  global data
  nostartsdata = [edge for edge in data if not 'start' in edge]
  # Impossibly clever way to keep track of visited small caves
  visitedsmallcaves = list(set([point for edge in path for point in edge if point.islower()]))

  # List describing path of small caves
  smallcavepath = [point for edge in path for point in edge if point.islower()]
  # Count occurences in list
  smallcavecounts = {cave:smallcavepath.count(cave) for cave in smallcavepath}
  if len({k:v for (k,v) in smallcavecounts.items() if v > 2}) == 1:
    # Small cave has been visited twice
    smallvisitedtwice = True
  elif len({k:v for (k,v) in smallcavecounts.items() if v > 2}) == 0:
    # No small cave visited twice
    smallvisitedtwice = False
  else:
    # something is wrong
    print(f"more than one cave visited twice [{path}]. error!")
    quit()

  if not path:
    # Path not started, first edge[0] is 'start' mandatory
    starts = [edge for edge in data if edge[0] == 'start']
    return starts
  elif path[-1][-1] == 'end' or 'DEAD END' in path:
    # Path has reached end. No next step.
    return []
  else:
    # more than one cave visited twice [[('start', 'op'), ('op', 'bj'), ('bj', 'op'), ('op', 'bj'), ('bj', 'PF')]]. error!
    if smallvisitedtwice:
      nexts = [edge for edge in nostartsdata if path[-1][-1] == edge[0] and not edge[1] in visitedsmallcaves]
    else:
      nexts = [edge for edge in nostartsdata if path[-1][-1] == edge[0]]
    if nexts:
      return nexts
    else:
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
      paths.remove(path)
      for nextstep in possiblenext(path):
        path.append(nextstep)
        paths.append(deepcopy(path))
        path.remove(nextstep)
    unfinishedpaths = [path for path in paths if not path[-1][-1] == 'end']
  print(f"{len(paths)}")

def checkpath(path):
  for i in list(range(len(path)))[:-1]:
    if not path[i][-1] == path[i+1][0]:
      print(f"invalid path: {path}")
      quit()

def second():
  starttime = time()
  readfile()
  path = []
  paths = []
  i = 0
  # Seed paths with start edges
  for nextstep in possiblenext2(path):
    path.append(nextstep)
    paths.append(deepcopy(path))
    path.remove(nextstep)
  unfinishedpaths = deepcopy(paths)
  while unfinishedpaths:
    if i % 1 == 0:
      print(f"i{i} #{len(unfinishedpaths)} {int(time() - starttime)}s: {unfinishedpaths[-1]}")
    i += 1
    for path in unfinishedpaths:
      paths.remove(path)
      for nextstep in possiblenext2(path):
        checkpath(path)
        path.append(nextstep)
        if not path in paths:
          paths.append(deepcopy(path))
        path.pop()
    #for unfinishedpath in unfinishedpaths:
    #  print(f"pre: {unfinishedpath}")
    unfinishedpaths = deepcopy([path for path in paths if not path[-1][-1] == 'end' and not path[-1][-1] == "DEAD END"])
    #for unfinishedpath in unfinishedpaths:
    #  print(f"pos: {unfinishedpath}")
    #input("Press Enter to continue...")
    #for asd in unfinishedpaths:
    #  print(f"{asd}")
    #input("Press Enter to continue...")
  print(f"{len(paths)}")

second()

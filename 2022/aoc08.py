#!/usr/bin/env python3
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

def readfile():
  datafile = datafilename()
  overview = []
  with open(datafile, 'r') as file:
    for line in file:
      overview.append(list(map(int, list(line.strip()))))
  return(overview)

def visible_from_left(x, y, overview):
  row = overview[y]
  tree = row[x]
  must_be_lower = row[:x]
  if max(must_be_lower, default=0) < tree:
    return True
  else:
    return False

def visible_from_right(x, y, overview):
  pass
def visible_from_top(x, y, overview):
  pass
def visible_from_bottom(x, y, overview):
  pass
overview = readfile()
print(f"{visible_from_left(1, 1, overview)}")

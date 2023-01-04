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
  row = overview[y]
  tree = row[x]
  must_be_lower = row[x+1:]
  if max(must_be_lower, default=0) < tree:
    return True
  else:
    return False

def visible_from_top(x, y, overview):
  row = overview[y]
  tree = row[x]
  must_be_lower = [ r[x] for r in overview[:y] ]
  if max(must_be_lower, default=0) < tree:
    return True
  else:
    return False

def visible_from_bottom(x, y, overview):
  row = overview[y]
  tree = row[x]
  must_be_lower = [ r[x] for r in overview[y+1:] ]
  if max(must_be_lower, default=0) < tree:
    return True
  else:
    return False

def visible_from_edge(x, y, overview):
  return (
    visible_from_left(x, y, overview) or
    visible_from_right(x, y, overview) or
    visible_from_top(x, y, overview) or
    visible_from_bottom(x, y, overview)
  )

overview = readfile()
row_indices = list(range(0, len(overview)))
col_indices = list(range(0, len(overview[0])))
visible_trees = 0
for x in row_indices:
  for y in col_indices:
    if visible_from_edge(x, y, overview):
      visible_trees += 1
print(f"visible trees: {visible_trees}")


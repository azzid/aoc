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

def visible_from(direction, x, y, overview):
  row = overview[y]
  tree = row[x]

  if direction == 'left':
    must_be_lower = row[:x]
  elif direction == 'right':
    must_be_lower = row[x+1:]
  elif direction == 'top':
    must_be_lower = [ r[x] for r in overview[:y] ]
  elif direction == 'bottom':
    must_be_lower = [ r[x] for r in overview[y+1:] ]
  else:
    print(f"ERROR! unknown direction [{direction}]")
    quit()

  # DEBUG
  #if x == 0 and y == 1:
  #  print(f"{max(must_be_lower, default=0) < tree} - from {direction}, tree with height {tree} must tower over {must_be_lower}")
  if max(must_be_lower, default=-1) < tree:
    return True
  else:
    return False

def visible_from_edge(x, y, overview):
  return (
    visible_from('left', x, y, overview) or
    visible_from('right', x, y, overview) or
    visible_from('top', x, y, overview) or
    visible_from('bottom', x, y, overview)
  )

overview = readfile()
row_indices = list(range(0, len(overview)))
col_indices = list(range(0, len(overview[0])))
visible_trees = 0
invisible_trees = 0
for x in row_indices:
  for y in col_indices:
    if visible_from_edge(x, y, overview):
      visible_trees += 1
      #print(f"[{x}][{y}]: True")
    else:
      invisible_trees += 1
      #print(f"[{x}][{y}]: False")
print(f"visible trees: {visible_trees}\ninvisible trees: {invisible_trees}")
#print(overview[col_indices[0]][row_indices[3]])
#[0][1]: False 

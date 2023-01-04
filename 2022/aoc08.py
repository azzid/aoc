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

def viewing_distance(direction, x, y, overview):
  row = overview[y]
  tree = row[x]

  if direction == 'left':
    must_be_lower = row[:x]
    must_be_lower.reverse()
  elif direction == 'right':
    must_be_lower = row[x+1:]
  elif direction == 'top':
    must_be_lower = [ r[x] for r in overview[:y] ]
    must_be_lower.reverse()
  elif direction == 'bottom':
    must_be_lower = [ r[x] for r in overview[y+1:] ]
  else:
    print(f"ERROR! unknown direction [{direction}]")
    quit()

  actually_lower = []
  for i in range(len(must_be_lower)):
    actually_lower.append(must_be_lower[i])
    if must_be_lower[i] >= tree:
      break

  return(len(actually_lower))

def scenic_score(x, y, overview):
  return (
    viewing_distance('left', x, y, overview) *
    viewing_distance('right', x, y, overview) *
    viewing_distance('top', x, y, overview) *
    viewing_distance('bottom', x, y, overview)
  )

overview = readfile()
row_indices = list(range(0, len(overview)))
col_indices = list(range(0, len(overview[0])))
top_scenic_score = 0
for x in row_indices:
  for y in col_indices:
    if scenic_score(x, y, overview) > top_scenic_score:
      top_scenic_score = scenic_score(x, y, overview)
print(f"top scenic score: {top_scenic_score}")

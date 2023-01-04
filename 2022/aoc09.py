#!/usr/bin/env python3
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

def readfile():
  datafile = datafilename()
  movements = []
  with open(datafile, 'r') as file:
    for line in file:
      a = line.strip().split()
      movements.append(tuple((a[0], int(a[1]))))
  return(movements)

for move in readfile():
  print(move)

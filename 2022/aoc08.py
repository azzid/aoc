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

print(f"{readfile()}")

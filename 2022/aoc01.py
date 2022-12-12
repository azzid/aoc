#!/usr/bin/env python3
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

def readfile():
  data = []
  backpack = []
  datafile = datafilename()
  with open(datafile, 'r') as file:
    for line in file:
      if not line.strip():
        data.append(backpack)
        backpack = []
      else:
        backpack.append(int(line.strip()))
  return data


caloriesums = list(map(sum, readfile()))
caloriesums.sort()
print(f"{sum(caloriesums[-3:])}")

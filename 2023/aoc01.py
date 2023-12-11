#!/usr/bin/env python3
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
      nums = [ c for c in line if c.strip().isdigit() ]
      data.append(int(nums[0] + nums[-1]))
  return data

print(sum(readfile()))

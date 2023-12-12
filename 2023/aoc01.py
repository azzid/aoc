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
      digitedline = line.replace('one', 'o1e').replace('two', 't2o').replace('three','t3e').replace('four','f4r').replace('five','f5e').replace('six','s6x').replace('seven','s7n').replace('eight','e8t').replace('nine','n9e')
      nums = [ c for c in digitedline if c.isdigit() ]
      data.append(int(nums[0] + nums[-1]))
  return data

print(sum(readfile()))

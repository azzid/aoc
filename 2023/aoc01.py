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
      digitedline = line.replace('one', '1').replace('two', '2').replace('three','3').replace('four','4').replace('five','5').replace('six','6').replace('seven','7').replace('eight','8').replace('nine','9')
      nums = [ c for c in digitedline if c.isdigit() ]
      data.append(int(nums[0] + nums[-1]))
  return data

print(sum(readfile()))

#!/usr/bin/env python3
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

# 60-60,45-60
#>>> list(range(3, 5+1))
#[3, 4, 5]
#>>> list(map(int, a.split('-')))
#[60, 60]


def readfile():
  data = []
  datafile = datafilename()
  with open(datafile, 'r') as file:
    for line in file:
      a, b = line.split(',')
      astart, astop = map(int, a.split('-'))
      bstart, bstop = map(int, b.split('-'))
      data.append(tuple((range(astart, astop+1), range(bstart, bstop+1))))
  return data

print(f"{readfile()[0]}")

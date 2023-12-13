#!/usr/bin/env python3
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

def readfile():
  data = {}
  datafile = datafilename()
  with open(datafile, 'r') as file:
    for line in file:
      gameno = int(line.split(':')[0].split(' ')[1])
      data[gameno] = []
      for pullstr in line.split(':')[1].split(';'):
        d = {}
        for colstr in pullstr.split(','):
          color = colstr.strip().split()[1]
          num   = int(colstr.strip().split()[0])
          d[color]=num
        data[gameno].append(d)
  return data

print(readfile()[1])

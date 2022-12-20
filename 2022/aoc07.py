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
      if line[0] == '$':   # command
        if line.strip().split()[1] == 'cd' and not line.strip().split()[2] == '..':
          descend(line.strip().split()[2])
        elif line.strip().split()[1] == 'cd':
          ascend()
        elif line.strip().split()[1] == 'ls':
          read_until_next_command()
        else:
          print(f"error, unknown command: {line.strip()}")

  return data

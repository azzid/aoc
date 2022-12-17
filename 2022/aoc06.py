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
      return list(line.strip())

data = readfile()
for i in range(14, len(data)+1):
  chars = data[i-14:i]
  if len(set(chars)) == 14:
    print(f"I founds it I dids!! I founds number {i}")
    quit()

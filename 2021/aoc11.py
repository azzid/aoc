#!/usr/local/bin/python3
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
      data.append(list(map(int, list(line.strip()))))
  return data

def first():
  data = readfile()
  for line in data:
    print(f"{line}")

def second():
  data = readfile()

first()

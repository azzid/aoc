#!/usr/local/bin/python3
from pathlib import Path
from collections import Counter
from time import time
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

def readfile():
  riskmap = []
  datafile = datafilename()
  with open(datafile, 'r') as file:
    for line in file:
      riskmap.append(list(line))
  return riskmap

def first():
  starttime = time()
  riskmap = readfile()
  print(f"top left: {riskmap[0][0:3]}, bottom right: {riskmap[-1][-4:-1]}")

first()

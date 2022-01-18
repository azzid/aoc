#!/usr/local/bin/python3
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

def readfile():
  template = ""
  insertions = []
  datafile = datafilename()
  with open(datafile, 'r') as file:
    for line in file:
      if len(line) > 8:
        template = line.strip()
      elif ' -> ' in line:
        insertion = tuple(line.strip().split(' -> '))
        insertions.append(insertion)
  return template, insertions
  
def first():
  template, insertions = readfile()
  print(f"Template: {template}")
  print(f"first ins: {insertions[0]}")
  print(f"last ins: {insertions[-1]}")
  
first()

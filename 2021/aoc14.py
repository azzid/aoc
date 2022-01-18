#!/usr/local/bin/python3
from pathlib import Path
from collections import Counter
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
  
def getinsertion(pair, insertions):
  for insertion in insertions:
    if insertion[0] == pair:
      return insertion[1]
  return None
  
def makeinsertions(template, insertions):
  newstring = ""
  for i in range(len(template)-1):
    pair = template[i] + template[i+1]
    newstring += template[i] + getinsertion(pair, insertions)
  newstring += pair[-1]
  return newstring
  
def first():
  template, insertions = readfile()
  for i in range(10):
    template = makeinsertions(template, insertions)
  #print(f"after step {i+1} lengt of {template} is {len(template)}")
  counts = Counter(list(template))
  maxchar=max(counts, key=counts.get)
  maxoccur=counts[maxchar]
  minchar=min(counts, key=counts.get)
  minoccur=counts[minchar]
  print(f"difference between number of {maxchar}[{maxoccur}] and {minchar}[{minoccur}] is: {maxoccur-minoccur}")

first()

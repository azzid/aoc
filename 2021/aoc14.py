#!/usr/local/bin/python3
from pathlib import Path
from collections import Counter
from time import time
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

def countpairsinstring(template):
  paircounts = {}
  paircounts['first'] = template[0]
  paircounts['last'] = template[-1]
  
  for i in range(len(template)-1):
    pair = template[i] + template[i+1]
    try:
      paircounts[pair] += 1
    except KeyError:
      paircounts[pair] = 1
  # Remove first/last:
  # {k: paircounts[k] for k in paircounts if len(k) == 2}
  return paircounts
  
def second():
  iterattions = 40
  starttime = time()
  template, insertions = readfile()
  print(f"{countpairsinstring(template)}")
  quit()
  for i in range(iterations):
    template = makeinsertions(template, insertions)
    #print(f"after step {i+1} lengt of template is {len(template)} and {int(time() - starttime)}s has passed since start")
    counts = Counter(list(template))
    #print(counts)
    maxchar=max(counts, key=counts.get)
    maxoccur=counts[maxchar]
    minchar=min(counts, key=counts.get)
    minoccur=counts[minchar]
    print(f"{i+1}: diff {maxchar}[{maxoccur}]-{minchar}[{minoccur}]: {maxoccur-minoccur}")

second()

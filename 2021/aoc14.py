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

def makecounterinsertions(paircounts, insertions):
  # Save first/last char in string to new count dict
  newpaircounts = {k: paircounts[k] for k in paircounts if k == 'first' or k == 'last'}
  # Iterate over all the pairs
  for pair in {k: paircounts[k] for k in paircounts if len(k) == 2}:
    # Get char to insert
    insert = getinsertion(pair, insertions)
    # Create the two new pairs
    pair1 = pair[0] + insert
    pair2 = insert + pair[-1] 
    # Add the count from the old pair to the new ones
    try:
      newpaircounts[pair1] += paircounts[pair]
    except KeyError:
      newpaircounts[pair1]  = paircounts[pair]
    try:
      newpaircounts[pair2] += paircounts[pair]
    except KeyError:
      newpaircounts[pair2]  = paircounts[pair]
  return newpaircounts
  
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

def countcharsinpairs(paircounts):
  charcounts = {}
  for pair in {k: paircounts[k] for k in paircounts if len(k) == 2}:
    try:
      charcounts[pair[0]]  += paircounts[pair]
    except KeyError:
      charcounts[pair[0]]   = paircounts[pair]
    try:
      charcounts[pair[-1]] += paircounts[pair]
    except KeyError:
      charcounts[pair[-1]]  = paircounts[pair]
  charcounts[paircounts['first']] += 1
  charcounts[paircounts['last']] += 1
  # Slice all counts in half as chars has been counted twice
  charcounts = {k: int(charcounts[k]/2) for k in charcounts}
  return charcounts
 
def second():
  iterations = 10
  starttime = time()
  template, insertions = readfile()
  paircounts = countpairsinstring(template)
  for i in range(iterations):
    paircounts = makecounterinsertions(paircounts, insertions)
  counts = countcharsinpairs(paircounts)
  maxchar=max(counts, key=counts.get)
  maxoccur=counts[maxchar]
  minchar=min(counts, key=counts.get)
  minoccur=counts[minchar]
  print(f"difference between number of {maxchar}[{maxoccur}] and {minchar}[{minoccur}] is: {maxoccur-minoccur}")

second()

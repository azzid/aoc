#!/usr/bin/env python3
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

from operator import itemgetter
def readfile():
  stacks = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: []
           }
  #indices = list(range(1, len(line), 4))          # hard-code to prevent opening file twice or computing list for every line in file
  indices = [ 1, 5, 9, 13, 17, 21, 25, 29, 33 ]
  operations = []
  datafile = datafilename()
  with open(datafile, 'r') as file:
    for line in file:
      if not line.strip():
        operations = True
      if operations:
        # do operations stuff
        continue
      else:
        lineobjects = list(itemgetter(*indices)(list(line)))
        for i, x in enumerate(lineobjects):
          if ' ' in x or x in map(str, stacks.keys()):
            #print(f"{i+1} is {x} - skipping")
            continue
          #print(f"{i+1}: {x}")
          stacks[i+1].insert(0, x)
    print(f"{stacks}")

readfile()

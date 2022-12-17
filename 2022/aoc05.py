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
  instruction = []
  operations = False
  datafile = datafilename()
  with open(datafile, 'r') as file:
    for line in file:
      if not line.strip():
        operations = True
        continue
      if operations:
        # do operations stuff
        a = line.strip().split(' ')
        d = { a[0]: a[1], a[2]: a[3], a[4]: a[5] }
        instruction.append(d)
      else:
        lineobjects = list(itemgetter(*indices)(list(line)))
        for i, x in enumerate(lineobjects):
          if ' ' in x or x in map(str, stacks.keys()):
            continue
          stacks[i+1].insert(0, x)
    return(stacks, instruction)

stacks, operations = readfile()
print(f"stack 1: {stacks[1]}")
print(f"operation 1: {operations[1]}")

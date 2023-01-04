#!/usr/bin/env python3
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

def readfile():
  datafile = datafilename()
  with open(datafile, 'r') as file:
    return list(map(str.strip, list(file)))

def process_ops():
  top = {'/': {}}
  curr = top
  for line in readfile():
    if line[0] == '$':
      # commandline
      if line.split()[1] == 'cd':
          curr = curr[line.split()[2]]
      elif line.split()[1] == 'ls':
        # the coming lines will list what's in 'curr'
        # dont think I need to do anything...
        pass
      else:
        print(f"only cd and ls are supported - not {line.split(' ')[1]}")
        quit()
    else:
      # in ls
      if line.split()[0] == 'dir':
        curr[line.split()[1]] = {'..': curr}
      else:
        curr[line.split()[1]] = int(line.split()[0])
  return(top)
    
print(f"{process_ops()}")

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
    
def foldersize(top):
  sizesum=0
  for key in top.keys():
    if key == '..':
      # dont follow circular link
      pass
    elif type(top[key]) is int:
      sizesum+=top[key]
    elif type(top[key]) is dict:
      sizesum+=foldersize(top[key])
  return(sizesum)

def print_foldersizes(top, s=''):
  for key in top.keys():
    if key == '..':
      # dont follow circular link
      pass
    elif type(top[key]) is dict:
      print(f"{s}{key}: {foldersize(top[key])}")
  s = s + '  '
  for key in top.keys():
    if key == '..':
      # dont follow circular link
      pass
    elif type(top[key]) is dict:
      print_foldersizes(top[key], s)

def return_foldersizes(top, notover=100000):
  a = []
  for key in top.keys():
    if key == '..':
      # dont follow circular link
      pass
    elif type(top[key]) is dict:
      size = foldersize(top[key])
      if size < notover: a.append(size)

  for key in top.keys():
    if key == '..':
      # dont follow circular link
      pass
    elif type(top[key]) is dict:
      a = a + return_foldersizes(top[key])
  return(a)

top = process_ops()
#print(f"{foldersize(top)}")
print(f"{return_foldersizes(top)}")

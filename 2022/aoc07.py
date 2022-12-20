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

print(f"{readfile()[0]}")
#>>> a = {}
#>>> a['/'] = {}
#>>> a
#{'/': {}}
#>>> a['/']['bqpslnv'] = 113975
#>>> a['/']['..'] = a['/']
#>>> a
#{'/': {'bqpslnv': 113975, '..': {...}}}

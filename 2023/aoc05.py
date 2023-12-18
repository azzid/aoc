#!/usr/bin/env python3
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

def readfile():
  data = []
  datafile = datafilename()
  source, destination = 'unset', 'unset'
  with open(datafile, 'r') as file:
    for line in file:
      if 'seeds:' in line:
        print(f"seeds: {line.split(':')[1].split()}")
      elif 'map:' in line:
        print(f"{line.split()[0].split('-to-')}")
        source, destination = line.split()[0].split('-to-')
      elif '\n' == line:
        if  not (source, destination) == ('unset', 'unset'):
          a['source'] = source
          a['destination'] = destionation
          data.append(a)
        a = {}
        #pass
        #print(f"empty line, source is {source} - dest is {destination}")
      else: # numbers...
        dststart, srcstart, length = list(map(int, line.split()))
        srclist = list(range(srcstart, srcstart+length))
        dstlist = list(range(dststart, dststart+length))
        for i, srcid in enumerate(srclist):
          a[srcid] = dstlist[i]
        print(dststart, srcstart, length)
        #pass

  return data

print(readfile())

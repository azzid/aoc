#!/usr/bin/env python3
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

def readfile():
  data = []
  datafile = datafilename()
  with open(datafile, 'r') as file:
    for line in file:
      a, b = line.split(',')
      astart, astop = map(int, a.split('-'))
      bstart, bstop = map(int, b.split('-'))
      data.append(tuple((range(astart, astop+1), range(bstart, bstop+1))))
  return data

def does_ranges_overlap(rangetuple):
  rangea = rangetuple[0]
  rangeb = rangetuple[1]
  commonlength = len(set(rangea).intersection(set(rangeb)))
  if commonlength > 0:
    return True
  else:
    return False

def does_one_contain_the_other(rangetuple):
  rangea = rangetuple[0]
  rangeb = rangetuple[1]
  lena = len(rangea)
  lenb = len(rangeb)
  commonlength = len(set(rangea).intersection(set(rangeb)))
  if commonlength == lena or commonlength == lenb:
    return True
  else:
    return False

debug = False
i = 0
for rangetuple in readfile():
  if debug:
    print(f"{rangetuple}: {does_one_contain_the_other(rangetuple)}")
  elif does_ranges_overlap(rangetuple):
    i += 1
print(f"found {i} ranges with overlap")

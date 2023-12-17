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
      data.append(list(line))
  return data

def is_valid(startrow, stoprow, startcol, stopcol):
  miny = max(startrow - 1, 0)
  maxy = min(stoprow + 2, maxrow)
  minx = max(startcol - 1, 0)
  maxx = min(stopcol + 2, maxcol)

  #print(f"minx: {minx}, maxx: {maxx}, miny: {miny}, maxy: {maxy}")
  #twod = [line[minx:maxx] for line in ptmtx[miny:maxy]]
  #print(twod)
  flatset = set([j for i in [line[minx:maxx] for line in ptmtx[miny:maxy]] for j in i])
  #print(flatset)
  if len(flatset.intersection(chars)) > 0:
    return True
  else:
    return False

ptmtx = readfile()
chars = set()
for line in range(len(ptmtx)):
  for column in range(len(ptmtx[line])):
    char = ptmtx[line][column]
    if not ( char in ''.join([ str(i) for i in range(0, 10)]) or char == '.' ):
      chars.add(char)

number = '0'
summ   = 0
startrow, startcol = [140, 140]
stoprow, stopcol = [0, 0]
maxrow = len(ptmtx)
maxcol = len(ptmtx[0])
for line in range(len(ptmtx)):
  for column in range(len(ptmtx[line])):
    char = ptmtx[line][column]
    if char in ''.join([ str(i) for i in range(0, 10)]):
      if number == '0': # just found a new number
        startrow = line
        startcol = column
        number = char
      else:
        number += char
      #print(f"number: {number}, startrow: {startrow}")
    if char in chars.union('.') or column == maxcol:
      if not number == '0': # found end of number
        stoprow = line
      if column == maxcol:
        stopcol = column
      else:
        stopcol = column-1 
    if startcol <= stopcol: # found both ends of number
      if is_valid(startrow, stoprow, startcol, stopcol):
        summ += int(number)
      number = '0'

print(summ)

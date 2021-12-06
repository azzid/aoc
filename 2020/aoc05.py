#!/usr/local/bin/python3
def first():
  maxsid = 0
  with open('aoc05.txt', 'r') as file:
    for line in file:
      row = getrow(line[:7].strip())
      col = getcol(line[7:].strip())
      sid = row * 8 + col
      if sid > maxsid:
        maxsid = sid
      print(f"{line.strip()} is row: {row}, col: {col} (sid: {sid})")
    print(f"Highest seat ID: {maxsid}")

def second():
  seats = []
  with open('aoc05.txt', 'r') as file:
    for line in file:
      row = getrow(line[:7].strip())
      col = getcol(line[7:].strip())
      sid = row * 8 + col
      #print(f"{line.strip()} is row: {row}, col: {col} (sid: {sid})")
      seats.append(sid)
  seats.sort()
  findmissing(seats)
  
def findmissing(listonums):
  for i in list(range(len(listonums)))[20:-20]:
    if listonums[i+1] - listonums[i] == 2:
      print(f"sid before: {listonums[i]}")
      print(f"my seat: {listonums[i]+1}")
      print(f"sid after: {listonums[i+1]}")

def getrow(bfstring):
  rows = list(range(0, 128))
  for bf in list(bfstring):
    half = int(len(rows)/2)
    if 'B' == bf:     # upper half
      rows = rows[half:]
    elif 'F' == bf:   # lower half
      rows = rows[:half]
    else:
      print(f"Expected B or F, found {bf}")
      quit()
  if len(rows) == 1:
    return(rows[0])
  else:
    print(f"Expected to only have on element by now. Failed, rows: {rows}")
    quit()

def getcol(rlstring):
  cols = list(range(0, 8))
  for rl in list(rlstring):
    half = int(len(cols)/2)
    if 'R' == rl:     # upper half
      cols = cols[half:]
    elif 'L' == rl:   # lower half
      cols = cols[:half]
    else:
      print(f"Expected R or L, found {rl}")
      quit()
  if len(cols) == 1:
    return(cols[0])
  else:
    print(f"Expected to only have on element by now. Failed, cols: {cols}")
    quit()
    
second()

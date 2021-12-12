#!/usr/local/bin/python3
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
      data.append(list(map(int, list(line.strip()))))
  return data

def plusone(indata):
  outdata = []
  for line in indata:
    outdata.append(list(map(lambda a: a + 1, line)))
  return outdata

def getninepluses(indata):
  readytoflash = []
  for y in list(range(len(indata))):
    for x in list(range(len(indata[y]))):
      if indata[y][x] > 9:
        readytoflash.append((x,y))
  return readytoflash

def flash(octo, indata):
  x = octo[0]
  y = octo[1]
  xmin = 0
  ymin = 0
  xmax = len(indata[0])-1
  ymax = len(indata)-1
  lsx = max(xmin, x-1)
  lsy = max(ymin, y-1)
  hsx = min(xmax, x+1)
  hsy = min(ymax, y+1)
  #print(f"{lsx} < {x} < {hsx}, {lsy} < {y} < {hsy}")
  for sy in range(lsy, hsy+1):
    #print("")
    for sx in range(lsx, hsx+1):
      if (sx, sy) == octo:
        #print(f"({(sx,sy)})", end='')
        pass
        #indata[sy][sx] = 0
      else:
        #print(f"{(sx,sy)}", end='')
        indata[sy][sx] += 1

  return indata

def nullify(alreadyflashed, indata):
  for octo in alreadyflashed:
    x = octo[0]
    y = octo[1]
    indata[y][x] = 0
  return indata

def first():
  flashes = 0
  data = readfile()

  for i in range(1,101):
    # First, the energy level of each octopus increases by 1.
    data = plusone(data)
    # Then, any octopus with an energy level greater than 9 flashes.
    flashyoctopi = getninepluses(data)
    alreadyflashed = set()
    # This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent.
    # If this causes an octopus to have an energy level greater than 9, it also flashes.
    while flashyoctopi:
      for octo in flashyoctopi:
        flashes += 1
        data = flash(octo, data)
        # An octopus can only flash at most once per step.
        alreadyflashed.add(octo)
      flashyoctopi = getninepluses(data)
      flashyoctopi = list(set(flashyoctopi).difference(alreadyflashed))
    # Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.
    data = nullify(alreadyflashed, data)
    if i == 100:
      print(f"Flashes after step {i}: {flashes}")

def second():
  flashes = 0
  data = readfile()

  for i in range(1,10100):
    data = plusone(data)
    flashyoctopi = getninepluses(data)
    alreadyflashed = set()
    while flashyoctopi:
      for octo in flashyoctopi:
        flashes += 1
        data = flash(octo, data)
        alreadyflashed.add(octo)
      flashyoctopi = getninepluses(data)
      flashyoctopi = list(set(flashyoctopi).difference(alreadyflashed))
    # Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.
    data = nullify(alreadyflashed, data)
    if len(alreadyflashed) == 100:
      print(f"Everybody flashed at once! This happened in step {i}.")
      quit()

second()

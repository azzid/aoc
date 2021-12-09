#!/usr/local/bin/python3
from functools import reduce
def readfile():
  with open('aoc10.txt', 'r') as file:
    return(list(map(lambda x:int(x.strip()), file)))

def first():
  adapters = readfile()
  adapters.sort()
  adapters.append(adapters[-1]+3)
  curr = 0
  ones = 0
  threes = 0
  for i in adapters:
    if i - curr == 1:
      ones += 1
    elif i - curr == 3:
      threes += 1
    curr = i
  print(f"ones: {ones}, threes: {threes}, ones*threes: {ones*threes}")

def countvalidpaths(adapters):
  last = adapters[-1]
  if last == 0:
    return 1
  else:
    rest = adapters[:-1]
    comp = [ x for x in rest if last - x <= 3 ]
    count = 0
    for x in comp:
      i = rest.index(x) + 1
      print(f"{rest[:i]} count: {count}")
      count += countvalidpaths(rest[:i])
    return count

def listisvalid(adapters):
  bool = True
  bool = bool and adapters[0] == 0
  bool = bool and adapters[-1] == 152
  for i in range(len(adapters)-1):
    bool = bool and adapters[i+1] - adapters[i] <= 3
  return bool

def trimmedlists(adapters):
  sublists = []
  for i in range(len(adapters)):
    sublist = adapters[:i] + adapters[i+1:]
    if listisvalid(sublist):
      sublists.append(sublist)
  #for lista in sublists:
  #  print(f"{lista}")
  #quit()
  return sublists

def second():
  adapters = readfile()
  adapters.sort()
  adapters.append(adapters[-1]+3)
  adapters = [0] + adapters
  adapteroptions = []

  for adapter in adapters:
    #print(f"{adapter} has {len([x for x in adapters if adapter < x <= adapter+3])} possible adapters to connect to.")
    adapteroptions.append(len([x for x in adapters if adapter < x <= adapter+3]))
  adapteroptions = [a for a in adapteroptions if a > 0]
  #print(f"{adapteroptions}")
  adaptercombos = reduce(lambda a, b: a*b, adapteroptions)

  print(f"{adaptercombos}")

second()

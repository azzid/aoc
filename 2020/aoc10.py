#!/usr/local/bin/python3
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

#def indexoffork(adapters):
#  for i in range(len(adapters)):
    
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
  valids = []
  if listisvalid(adapters):
    valids.append(adapters)
  shorterlist = trimmedlists(adapters)
  i = 0
  while shorterlist:
    valids = valids + shorterlist
    templist = []
    for lista in shorterlist:
      templist += trimmedlists(lista)
    shorterlist = templist
    i += 1
    print(f"{i}: {len(valids)}")

second()

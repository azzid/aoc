#!/usr/local/bin/python3
def first():
  total = 0
  groupanswers = set({})
  with open('aoc06.txt', 'r') as file:
    i = 0
    for line in file:
      if line.strip():
        for x in list(line.strip()):
          groupanswers.add(x)
      else:
        #print(f"New group! Last group had {len(groupanswers)} ({groupanswers}) answers, total before them was {total}.")
        total += len(groupanswers)
        groupanswers = set({})
      #i += 1
      #if i > 10:
      #  quit()
    # Clean up if last group wasn't terminated by empty line
    if groupanswers:
      total += len(groupanswers)
    print(f"Number: {total}")

def second():
  from functools import reduce
  total = 0
  commonanswers = set({})
  groupanswers = list([])
  with open('aoc06.txt', 'r') as file:
    for line in file:
      useranswers  =  set({})
      if line.strip():
        for x in list(line.strip()):
          useranswers.add(x)
        groupanswers.append(useranswers)
      else:
        #print(f"New group! Last group had {len(groupanswers)} ({groupanswers}) answers, total before them was {total}.")
        commonanswers = reduce(lambda a, b: a.intersection(b), groupanswers)
        total += len(commonanswers)
        groupanswers = list([])
    # Clean up if last group wasn't terminated by empty line
    if groupanswers:
      commonanswers = reduce(lambda a, b: a.intersection(b), groupanswers)
      total += len(commonanswers)
    print(f"Number: {total}")

second()

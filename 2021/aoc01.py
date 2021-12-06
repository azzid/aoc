#!/usr/local/bin/python3
def readfile():
  with open('aoc01.txt', 'r') as file:
    return(list(map(lambda x:int(x.strip()), file)))

def first():
  depths = readfile()
  count = 0
  for i in range(len(depths[:-1])):
    if depths[i] < depths[i+1]:
      count += 1
  print(f"Increases: {count}")

def second():
  depths = readfile()
  count = 0
  for i in range(len(depths[:-3])):
    if depths[i] + depths[i+1] + depths[i+2] < depths[i+1] + depths[i+2] + depths[i+3]:
      count += 1
  print(f"Increases: {count}")
  
second()

#!/usr/local/bin/python3
def readfile():
  fishies = []
  with open('aoc06.txt', 'r') as file:
    fishies = list(map(int, file.read().strip().split(',')))
  return fishies

def first():
  fishies = readfile()
  for day in list(range(81)):
    print(f"Day {day} there are: {len(fishies)} fishies")
    for i in list(range(len(fishies))):
      if fishies[i] == 0:
        fishies.append(8)
        fishies[i] = 7
      fishies[i] -= 1

first()

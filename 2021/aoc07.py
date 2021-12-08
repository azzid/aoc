#!/usr/local/bin/python3
def readfile():
  crabs = []
  with open('aoc07.txt', 'r') as file:
    crabs = list(map(int, file.read().strip().split(',')))
  return crabs

def fuelcost(alignto, crabs):
  fuelconsumed = 0
  for crab in crabs:
    fuelconsumed += max(alignto, crab) - min(alignto, crab)
  return fuelconsumed

def first():
  crabs = readfile()
  fuelcosts = [(pos, fuelcost(pos, crabs)) for pos in range(2000)]
  cheapest = min(fuelcosts,key=lambda fuelcost:fuelcost[1])
  print(f"Cheapest position is {cheapest[0]} which requires {cheapest[1]} units of fuel")

first()

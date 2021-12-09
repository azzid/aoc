#!/usr/local/bin/python3
def readfile():
  data = []
  with open('aoc09.txt', 'r') as file:
    for line in file:
      data.append(list(line.strip()))
  return data

def first():
  data = readfile()
  x, y = 1, 1
  print(f"{data[y][x]}")

def second():
  pass

first()

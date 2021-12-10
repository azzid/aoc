#!/usr/local/bin/python3
def readfile():
  data = []
  with open('aoc10.txt', 'r') as file:
    for line in file:
      data.append(list(map(int, list(line.strip()))))
  return data

def first():
  data = readfile()

def second():
  data = readfile()

first()

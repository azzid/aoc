#!/usr/local/bin/python3
def readfile():
  crabs = []
  with open('aoc07.txt', 'r') as file:
    crabs = list(map(int, file.read().strip().split(',')))
  return crabs

def first():
  crabs = readfile()

first()

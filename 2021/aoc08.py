#!/usr/local/bin/python3
def readfile():
  data = []
  with open('aoc08.txt', 'r') as file:
    for line in file:
      unique_signal_patterns, digit_output_values = line.split(' | ')
      data.append((unique_signal_patterns.split(), digit_output_values.split()))
  return data

def first():
  data = readfile()
  dovs = []
  for i in range(len(data)):
    dovs += data[i][1]
  easydovcount = len([dov for dov in dovs if len(dov) == 2 or len(dov) == 3 or len(dov) == 4 or len(dov) == 7])
  print(f"{easydovcount}")

def second():
  pass

first()

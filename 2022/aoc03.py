#!/usr/bin/env python3
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

def readfile():
  data = []
  datafile = datafilename()
  with open(datafile, 'r') as file:
    for lineno, line in enumerate(file):
      groupid = int(lineno/3)
      elfid = int(lineno%3)
      if elfid == 0:
        data.append([])
      data[groupid].append(set(list(line.strip())))
  return data

def split_string(s):
  a = s[0:int(len(s)/2)]
  b = s[int(len(s)/2):]
  return tuple((list(a), list(b)))

char_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

total = 0
for i, group in enumerate(readfile()):
  common_item = group[0].intersection(group[1]).intersection(group[2]).pop()
  item_value = char_values[common_item]
  total += item_value
  print(f"group {i} has {common_item} in common, valued at {item_value} - added to the total it lands on {total}")


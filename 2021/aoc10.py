#!/usr/local/bin/python3
from pathlib import Path
def datafilename():
  mypath = Path(__file__)
  txtpath = mypath.with_suffix('.txt')
  return txtpath

def readfile():
  data = []
  datafile = datafilename()
  with open(datafile, 'r') as file:
    for line in file:
      data.append(list(map(str, list(line.strip()))))
  return data

def first():
  data = readfile()
  openings = '([{<'
  closings = ')]}>'
  points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
  }
  seen = []
  score = 0
  for line in data:
    for char in line:
      if char in openings:
        seen.append(char)
      elif char in closings:
        checkifmatch = seen.pop()
        if checkifmatch == '(' and char == ')':
          pass
        elif checkifmatch == '[' and char == ']':
          pass
        elif checkifmatch == '{' and char == '}':
          pass
        elif checkifmatch == '<' and char == '>':
          pass
        else:
          score += points[char]
          #print(f"{checkifmatch} does not match {char}, scoring {points[char]} points.")
          #print(f"Line: {''.join(line)} is bust.")
          #quit()
  print(f"Score: {score}")

def second():
  data = readfile()

first()

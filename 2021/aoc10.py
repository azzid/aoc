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
  openings = '([{<'
  closings = ')]}>'
  points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
  }
  seen = []
  totalscores = []
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
          seen = []
          break
          #print(f"{checkifmatch} does not match {char}, scoring {points[char]} points.")
          #print(f"Line: {''.join(line)} is bust.")
          #quit()
    missingclosings = []
    missingopenings = seen[:]
    while seen:
    # Still got unclosed openings, line need to be completed
      opening = seen.pop()
      if opening == '(':
        missingclosings.append(')')
      elif opening == '[':
        missingclosings.append(']')
      elif opening == '{':
        missingclosings.append('}')
      elif opening == '<':
        missingclosings.append('>')
    if missingclosings:
      #print(f"{''.join(missingopenings)}  {''.join(missingclosings)}")
      #quit()
      score = 0
      for c in missingclosings:
        score *= 5
        score += points[c]
      totalscores.append(score)
  totalscores.sort()
  print(f"Score: {totalscores[int((len(totalscores) - 1)/2)]}")

second()

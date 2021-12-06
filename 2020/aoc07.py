#!/usr/local/bin/python3
import re
bagcontent = {}
def first():
  total = 0
  lookfor = 'shiny gold'
  containerpattern = re.compile('^([a-z]+ [a-z]+)')
  contentpattern = re.compile('(?:([0-9]+) ([a-z]+ [a-z]+)+)')
  global bagcontent
  with open('aoc07.txt', 'r') as file:
    for line in file:
      bagcolor = containerpattern.search(line).groups()[0]
      for num, col in contentpattern.findall(line):
        #print(f"'{bagcolor}': '{num}' '{col}'")
        try: bagcontent[bagcolor][col]=num
        except KeyError:
          bagcontent[bagcolor] = {}
          bagcontent[bagcolor][col]=num
  for outer in bagcontent.keys():
    if cancontain(lookfor, outer):
      total += 1
  print(f"Number of bags that can contain {lookfor}: {total}")

def second():
  global bagcontent
  lookfor = 'shiny gold'
  containerpattern = re.compile('^([a-z]+ [a-z]+)')
  contentpattern = re.compile('(?:([0-9]+) ([a-z]+ [a-z]+)+)')
  with open('aoc07.txt', 'r') as file:
    for line in file:
      bagcolor = containerpattern.search(line).groups()[0]
      for num, col in contentpattern.findall(line):
        #print(f"'{bagcolor}': '{num}' '{col}'")
        try: bagcontent[bagcolor][col]=int(num)
        except KeyError:
          bagcontent[bagcolor] = {}
          bagcontent[bagcolor][col]=int(num)
  #print(f"{bagcontent}")
  print(f"Number of bags in a {lookfor} bag is {numberofbagsin(lookfor)}")

def numberofbagsin(lookfor):
  total = 0
  global bagcontent
  try:
    for inner in bagcontent[lookfor].keys():
      count = bagcontent[lookfor][inner]
      containingcount = numberofbagsin(inner)
      total += containingcount*count+count
  except KeyError:
    return 0
  return total

def cancontain(lookfor, outer):
  try:
    if lookfor in list(bagcontent[outer].keys()):
      return True
  except KeyError:
    #print(f"{outer} can contain no bags")
    pass
  try:
    for inner in list(bagcontent[outer].keys()):
      if cancontain(lookfor, inner):
        return True
    else:
      return False
  except KeyError:
    #print(f"{outer} can contain no bags")
    pass

second()

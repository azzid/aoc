#!/usr/local/bin/python3
from functools import reduce
import re
def first():
  passport = []
  validcount = 0
  with open('aoc04.txt', 'r') as file:
    for line in file:
      if len(line.strip()) > 0:
        for prop in line.strip().split(' '):
          passport.append(prop)
      else:   # only works if file ends with a blank line
        if is_valid(passport):
          validcount += 1
        passport = []
  print(f"Number of valids: {validcount}")

def is_valid(listofstrings):
  count = 0
  propisvalid = {
    'byr': False,
    'iyr': False,
    'eyr': False,
    'hgt': False,
    'hcl': False,
    'ecl': False,
    'pid': False
  }
  validcolor = re.compile('^#[a-f0-9]{6}$')
  validpid = re.compile('^[0-9]{9}$')
  for prop in listofstrings:
    propname = prop.split(':')[0]
    propvalue = prop.split(':')[1]
    if propname in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ]: # ignore 'cid'
      count += 1
    if propname == 'byr' and 1920 <= int(propvalue) <= 2002:
      propisvalid['byr'] = True
    elif propname == 'iyr' and 2010 <= int(propvalue) <= 2020:
      propisvalid['iyr'] = True
    elif propname == 'eyr' and 2020 <= int(propvalue) <= 2030:
      propisvalid['eyr'] = True
    elif propname == 'hgt':
      if 'in' in propvalue and 59 <= int(propvalue.strip('in')) <= 76:
        propisvalid['hgt'] = True
      if 'cm' in propvalue and 150 <= int(propvalue.strip('cm')) <= 193:
        propisvalid['hgt'] = True
    elif propname == 'hcl' and validcolor.match(propvalue):
      propisvalid['hcl'] = True
    elif propname == 'ecl' and propvalue in [ 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' ]:
      propisvalid['ecl'] = True
    elif propname == 'pid' and validpid.match(propvalue):
      propisvalid['pid'] = True

  #print(f"{listofstrings} {propisvalid}")
      
  if count >= 7 and reduce(lambda x, y: x and y, propisvalid.values()):
    return True
  else:
    return False
first()

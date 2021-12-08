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
  data = readfile()
  one, two, three, four, five, six, seven, eight, nine = 0,0,0,0,0,0,0,0,0
  stringsum = 0
  for i in range(len(data)):
    string = ''
    dovs = data[i][1]
    usps = data[i][0]
    patterns = usps + dovs
    pattsets = list(map(set, patterns))
    for ps in [dov for dov in pattsets if len(dov) == 2 or len(dov) == 3 or len(dov) == 4 or len(dov) == 7]:
      if len(ps) == 2:
        one = ps
      if len(ps) == 3:
        seven = ps
      if len(ps) == 4:
        four = ps
      if len(ps) == 7:
        eight = ps
    for ps in [dov for dov in pattsets if len(dov) == 5]:
    # patterns 5 long are numbers 2, 3, 5
      if one.issubset(ps):
        three = ps
      if len(ps.difference(four)) == 3:
        two = ps
      if len(ps.difference(four)) == 2:
        five = ps
    for ps in [dov for dov in pattsets if len(dov) == 6]:
    # patterns 6 long are numbers 0, 6, 9
      if not five.issubset(ps):
        zero = ps
      elif one.issubset(ps):
        nine = ps
      else:
        six = ps
    for dov in dovs:
      dov = set(dov)
      if dov == zero:
        string += '0'
      elif dov == one:
        string += '1'
      elif dov == two:
        string += '2'
      elif dov == three:
        string += '3'
      elif dov == four:
        string += '4'
      elif dov == five:
        string += '5'
      elif dov == six:
        string += '6'
      elif dov == seven:
        string += '7'
      elif dov == eight:
        string += '8'
      elif dov == nine:
        string += '9'
    stringsum += int(string)
    print(f"{dovs}: {string}")
  print(f"SUM: {stringsum}")

second()

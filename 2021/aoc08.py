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
  stringsum = 0
  for i in range(len(data)):
    zero, one, two, three, four, five, six, seven, eight, nine = 0,0,0,0,0,0,0,0,0,0
    string = ''
    dovs = data[i][1]
    usps = data[i][0]
    patterns = usps 
    pattsets = list(map(set, patterns))
    if not len(pattsets) == 10:
      print(f"pattset not 10 long: {pattset}")
      quit()
    for ps in [usp for usp in pattsets if len(usp) == 2 or len(usp) == 3 or len(usp) == 4 or len(usp) == 7]:
      if len(ps) == 2:
        one = ps
      if len(ps) == 3:
        seven = ps
      if len(ps) == 4:
        four = ps
      if len(ps) == 7:
        eight = ps
    for ps in [usp for usp in pattsets if len(usp) == 5]:
    # patterns 5 long are numbers 2, 3, 5
      if one.issubset(ps):
        three = ps
      elif len(ps.difference(four)) == 3:
        two = ps
      elif len(ps.difference(four)) == 2:
        five = ps
      else:
        print(f"ps {ps} not recognized")
        quit()
    for ps in [usp for usp in pattsets if len(usp) == 6]:
    # patterns 6 long are numbers 0, 6, 9
      if not five.issubset(ps):
        zero = ps
      elif one.issubset(ps):
        nine = ps
      else:
        six = ps
    while 0 in [zero, one, two, three, four, five, six, seven, eight, nine]:
      for i, s in enumerate([zero, one, two, three, four, five, six, seven, eight, nine]):
        if not type(s) is set:
          print(f"Still no set defined to describe {i} ", end='')
          if i == 6 and type(two) is set and type(three) is set and type(five) is set:
            # We can construct our own 6.
            six = five.union(two.difference(three))
            print(f"constructing my own: {six}")
          else:
            print(f"")
            quit()
    if 0 in [zero, one, two, three, four, five, six, seven, eight, nine]:
      print(f"Error: some pattern not recognized: {[zero, one, two, three, four, five, six, seven, eight, nine]}")
      quit()
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
      else:
        print(f"Number {dov} not recognized. :-(")
        print(f"{usps} | {dovs}")
        print(f"{dovs}: {string}")
        quit()
    stringsum += int(string)
    #print(f"{dovs}: {string}")
  print(f"SUM: {stringsum}")

second()

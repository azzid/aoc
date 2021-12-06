#!/usr/local/bin/python3
def readfile():
  with open('aoc03.txt', 'r') as file:
    return(list(map(lambda x:str(x.strip()), file)))

def first():
  counts = [0,0,0,0,0,0,0,0,0,0,0,0]
  binaries = readfile()
  for instruction in binaries:
    for i in range(len(instruction)):
      #print(f"{instruction[i]}", end=" ")
      if int(instruction[i]) > 0:
        counts[i] += 1
      else:
        counts[i] -= 1
  #print(f"{counts}")
  gamma = ""
  epsilon = ""
  for x in counts:
    if x >= 0:
      gamma += "1"
      epsilon += "0"
    else:
      gamma += "0"
      epsilon += "1"
  print(f"  GAMMA: {gamma} (dec: {int(gamma, 2)})")
  print(f"EPSILON: {epsilon} (dec: {int(epsilon, 2)})")
  print(f"Multiplied: {int(gamma, 2) * int(epsilon, 2)}")
      
def pickonesorzeroes(instructions, pos, pref):
    ones   = [ x for x in instructions if x[pos] == "1" ]
    zeroes = [ x for x in instructions if x[pos] == "0" ]
    #print(f"a one: {ones[0]}, a zero: {zeroes[0]}")
    if pref == "oxy":
      if len(ones) >= len(zeroes):
        return ones
      else:
        return zeroes
    elif pref == "co2":
      if len(zeroes) <= len(ones):
        return zeroes
      else:
        return ones
    else:
      print("Failed.")
      quit()
  
def second():
  binaries = readfile()
  oxy = binaries[:]
  co2 = binaries[:]
  #print(f"{temp[0]}")
  for i in range(len(binaries[0])):
    #print(f"{i}")
    if len(oxy) > 1:
      oxy = pickonesorzeroes(oxy, i, "oxy")
    if len(co2) > 1:
      co2 = pickonesorzeroes(co2, i, "co2")
      #print(f"{len(temp)}")
  print(f"oxy: {oxy}, co2: {co2}")
  print(f"Multiplied: {int(oxy[0], 2) * int(co2[0], 2)}")

second()

#!/usr/local/bin/python3
def readfile():
  with open('aoc09.txt', 'r') as file:
    return(list(map(lambda x:int(x.strip()), file)))

def isvalid(preamble, value):
  for i in range(len(preamble)):
    one = preamble[i]
    rest = preamble[:i] + preamble[i+1:]
    #print(f"value: {value}, one: {one}, rest:     {rest}")
    rest = list(map(lambda x:x+one, rest))
    #print(f"value: {value}, one: {one}, rest+one: {rest}")
    #quit()
    if value in rest: return True
  return False

def first():
  chiper = readfile()
  for i in range(len(chiper)):
    if i > 25:
      if isvalid(chiper[i-25:i], chiper[i]):
        #print(f"{chiper[i-25:i]} {chiper[i]}")
        pass
      else:
        print(f"Found invalid!! {chiper[i]} with index {i}")
        quit()

def second():
  chiper = readfile()
  targetsum = 1930745883
  for i in range(len(chiper)):
    for j in range(i, len(chiper)):
      if sum(chiper[i:j]) == targetsum:
        #print(f"Found range! {chiper[i:j]} which sums up to {targetsum}")
        print(f"Max: {max(chiper[i:j])}, min: {min(chiper[i:j])}, sum: {max(chiper[i:j])+min(chiper[i:j])}")
        quit()
      elif sum(chiper[i:j]) > targetsum:
        break

second()

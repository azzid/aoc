#!/usr/local/bin/python3
karta = []
trees = 0
def printpos(height, strafe):
  prepos  = ''.join(karta[height])[:strafe]
  poschar = karta[height][strafe]
  postpos = ''.join(karta[height])[strafe+1:]
  print(f"{prepos}({poschar}){postpos} - trees hit: {trees}")

def first():
  global karta, trees
  with open('aoc03.txt', 'r') as file:
    for line in file:
      karta.append(list(line.strip()))
  #print(f"[0][0]: {karta[0][0]} [3][1]: {karta[3][1]} [rad=0]: {karta[0]}")
  height = len(karta)
  width = len(karta[0])
  #print(f"height: {height}, width: {width}")
  currheight=0
  currstrafe=0
  printpos(currheight, currstrafe)
  while currheight < height - 1:
    currheight += 1
    currstrafe += 3
    currstrafe = currstrafe % width
    printpos(currheight, currstrafe)
    #print(f"(X: {currstrafe} Y: {currheight}")
    if karta[currheight][currstrafe] == '#':
      trees += 1
  print(f"Trees hit: {trees}")

def second():
  global karta
  with open('aoc03.txt', 'r') as file:
    for line in file:
      karta.append(list(line.strip()))
  print(f"{countpath(1, 1) * countpath(3, 1) * countpath(5, 1) * countpath(7, 1) * countpath(1, 2)}")

def countpath(strafespeed, downspeed):
  global karta, trees
  trees = 0
  #print(f"[0][0]: {karta[0][0]} [3][1]: {karta[3][1]} [rad=0]: {karta[0]}")
  height = len(karta)
  width = len(karta[0])
  #print(f"height: {height}, width: {width}")
  currheight=0
  currstrafe=0
  printpos(currheight, currstrafe)
  while currheight < height - 1:
    currheight += downspeed
    currstrafe += strafespeed
    currstrafe = currstrafe % width
    printpos(currheight, currstrafe)
    #print(f"(X: {currstrafe} Y: {currheight}")
    if karta[currheight][currstrafe] == '#':
      trees += 1
  return trees
#first()
second()

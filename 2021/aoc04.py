#!/usr/local/bin/python3
def readfile():
  with open('aoc04.txt', 'r') as file:
    boards = []
    j = -1
    for i, line in enumerate(file):
      if i == 0:
        draws = line.strip().split(',')
      elif line == "\n":
        j += 1
        boards.append([])
      else:
        boards[j].append(line.strip().split())
  return draws, boards

def iswinner(announced, board):
  announcedset = set(announced)
  for row in board:
    rowset = set(row)
    #print(f"announced: {announcedset}, row: {rowset}, intersect: {announcedset.intersection(rowset)}")
    if len(announcedset.intersection(rowset)) >= 5:
      return True
  return False

def boardscore(announced, board):
  hits = set()
  misses = set()
  announcedset = set(announced)
  for row in board:
    rowset = set(row)
    hits.update(rowset.intersection(announcedset))
    misses.update(rowset.difference(announcedset))
  hits = list(map(int, hits))
  misses = list(map(int, misses))
  #print(f"Board: {board}")
  #print(f"Announced: {announced}")
  #print(f"Misses: {misses}, sum: {sum(misses)}")
  #print(f"Last: {announced[-1]}")
  return sum(misses)*int(announced[-1])

def first():
  score = 0
  announced = []
  winnerfound = False
  draws, boards = readfile()
  #print(f"{draws[-1]}")
  #print(f"{boards[-1]}")
  for draw in draws:
    if not winnerfound:
      announced.append(draw)
      if len(announced) >= 5:
        for board in boards:
          if iswinner(announced, board):
            winnerfound = True
            score = boardscore(announced, board)
  print(f"{score}")

def second():
  draws, boards = readfile()
  winnerboards = []
  winnerannounceds = []
  for board in boards:
    winnerfound = False
    announced = []
    for draw in draws:
      if not winnerfound:
        announced.append(draw)
      if iswinner(announced, board) and not winnerfound:
        winnerboards.append(board)
        winnerannounceds.append(announced)
        winnerfound = True
        #print(f"{winnercall}: {winnerboard[0]} boards left: {len(boards)} calls made: {len(announced)}")
  i = winnerannounceds.index(max(winnerannounceds, key = len))
  #print(f"{winnerboards[i]}")
  #print(f"{winnerannounceds[i]}")
  for i in range(len(winnerannounceds)):
    score = boardscore(winnerannounceds[i], winnerboards[i])
    print(f"{len(winnerannounceds[i])}: {score}")

second()

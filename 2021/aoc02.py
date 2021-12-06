#!/usr/local/bin/python3
def readfile():
  with open('aoc02.txt', 'r') as file:
    a = list(map(lambda line: line.strip().split(' '), file))
  return list(map(lambda array: [array[0], int(array[1])], a))

def first():
  instructions = readfile()
  pos = [0, 0]
  for direction, length in instructions:
    if direction == 'forward':
      pos[0] += length
    elif direction == 'down':
      pos[1] += length
    elif direction == 'up':
      pos[1] -= length
    else:
      print("intredible error")
      quit()
  print(f"We've gone {pos[0]} steps horisontally and {pos[1]} steps down vertically.")
  print(f"Numbers multiplied: {pos[0]*pos[1]}")

def second():
  instructions = readfile()
  # [horisontal, vertical, aim]
  pos = [0, 0, 0]
  for direction, amount in instructions:
    if direction == 'forward':
      pos[0] += amount
      pos[1] += amount * pos[2]
    elif direction == 'down':
      pos[2] += amount
    elif direction == 'up':
      pos[2] -= amount
    else:
      print("incredible error")
      quit()
  print(f"We've gone {pos[0]} steps horisontally and {pos[1]} steps down vertically.")
  print(f"Numbers multiplied: {pos[0]*pos[1]}")

second()

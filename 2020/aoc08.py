#!/usr/local/bin/python3
def first():
  program = []
  number = 0
  pos = 0
  earlierposes = []
  with open('aoc08.txt', 'r') as file:
    for line in file:
      op, val = line.strip().split(' ')
      val = int(val)
      program.append((op, val))
  #print(f"{program[1][1]}")
  while True:
    if pos in earlierposes:
      print(f"Pos: {pos} already visited, stopping. Accumulator is: {number}!")
      quit()
    earlierposes.append(pos)
    if program[pos][0] == 'jmp':
      pos += program[pos][1]
    elif program[pos][0] == 'acc':
      number += program[pos][1]
      pos += 1
    elif program[pos][0] == 'nop':
      pos += 1
    else:
      print(f"Shit's fucked up.")

def second():
  program = []
  with open('aoc08.txt', 'r') as file:
    for line in file:
      op, val = line.strip().split(' ')
      val = int(val)
      program.append((op, val))
  for i in range(len(program)):
    newprogram = toggle(i, program.copy())
    #print(f"Toggling program line {i} from {program[i]} to {newprogram[i]}")
    number = 0
    pos = 0
    earlierposes = []
    while pos < len(program):
      if pos in earlierposes:
        #print(f"Pos: {pos} already visited, stopping. i is: {i}!")
        break
      earlierposes.append(pos)
      if newprogram[pos][0] == 'jmp':
        pos += newprogram[pos][1]
      elif newprogram[pos][0] == 'acc':
        number += newprogram[pos][1]
        pos += 1
      elif newprogram[pos][0] == 'nop':
        pos += 1
      else:
        print(f"Shit's fucked up.")
        quit()
    if pos >= len(program):
      break
  print(f"Pos: {pos} >= {len(program)}, stopping. Accumulator is: {number}! (i was {i})")

def toggle(i, program):
  if program[i][0] == 'nop':
    program[i] = ('jmp', program[i][1])
  elif program[i][0] =='jmp':
    program[i] = ('nop', program[i][1])
  elif program[i][0] =='acc':
    pass
  else:
    print(f"Toggle-shit's fucked up...")
    quit()
  return program.copy()

second()

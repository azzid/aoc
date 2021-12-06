#!/usr/local/bin/python3
def first():
  valid, invalid = 0, 0
  with open('aoc02.txt', 'r') as file:
    for line in file:
      positions, letter, password = line.split()
      start, stop = positions.split('-')
      start, stop = int(start), int(stop)
      letter = letter.strip(':')
      #print(f"{start} {stop} {letter} {password}")
      if start <= password.count(letter) <= stop:
        valid += 1
      else:
        invalid += 1
  print(f"Valid passwords: {valid}")

def second():
  valid, invalid = 0, 0
  with open('aoc02.txt', 'r') as file:
    for line in file:
      positions, letter, password = line.split()
      first, second = positions.split('-')
      first, second = int(first) - 1, int(second) - 1
      letter = letter.strip(':')
      substring = password[first] + password[second]
      print(f"{first} {second} {letter} {substring} {password}")
      if substring.count(letter) == 1:
        valid += 1
      else:
        invalid += 1
  print(f"Valid passwords: {valid}")

second()

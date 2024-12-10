import sys
import re

content = sys.argv[1]

lines = content.splitlines()

starts = []

def isOutOfRange(x, y):
  return x < 0 or y < 0 or y >= len(lines) or x >= len(lines[y])

for lineIndex in range(len(lines)):
  for charIndex in range(len(lines[lineIndex])):
    char = lines[lineIndex][charIndex]
    if char == "0":
      starts.append((charIndex, lineIndex))
score = 0

for start in starts:
  locations = [start]
  for step in range(1, 10):
    newLocations = []
    for location in locations:
      charIndex, lineIndex = location
      for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        newX = charIndex + dx
        newY = lineIndex + dy
        if not isOutOfRange(newX, newY) and str(step) == lines[newY][newX]:
          newLocations.append((newX, newY))
    if len(newLocations) == 0:
      break
    locations = newLocations
  print(start, ":", locations)
  score += len(locations)

print(score)

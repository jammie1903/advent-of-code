# The robots outside the actual bathroom are in a space which is 101 tiles wide and 103 tiles tall
#  (when viewed from above). However, in this example, the robots are in a space which is only
# 11 tiles wide and 7 tiles tall.

import sys
from functools import reduce

content = sys.argv[1]

lines = content.splitlines()

height = 103
width = 101

moveCount = 100

midX = (width - 1) / 2
midY = (height - 1) / 2

robots = []

for line in lines:
  if not line: continue
  parts = line.split()
  # Extract p and v parts
  p_values = parts[0].split('=')[1].split(',')
  v_values = parts[1].split('=')[1].split(',')
  # Convert to integers
  position = tuple(map(int, p_values))
  velocity = tuple(map(int, v_values))

  robots.append((position, velocity))

lowestResult = 10000000000000
lowestIndex = -1

for i in range(0, width * height):
  quadrants = {
    "NE": 0,
    "SE": 0,
    "SW": 0,
    "NW": 0
  }
  for position, velocity in robots:
    finalPos = (
      (position[0] + velocity[0] * i) % width,
      (position[1] + velocity[1] * i) % height
    )

    if finalPos[0] == midX or finalPos[1] == midY: continue

    xSide = "W" if finalPos[0] < midX else "E"
    ySide = "N" if finalPos[1] < midY else "S"
    quadrants[f"{ySide}{xSide}"] += 1

  result = reduce(lambda x, y: x * y, quadrants.values())
  if result < lowestResult:
    lowestResult = result
    lowestIndex = i
print(lowestIndex)

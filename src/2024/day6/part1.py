import sys
import functools

content = sys.argv[1]

lines = content.splitlines()

posX = -1
posY = -1

direction = 3

locations = set()

def isOutOfRange(posX, posY):
  if posX < 0 or posX >= len(lines[0]): return True
  if posY < 0 or posY >= len(lines): return True
  return False

def isObstructed(newPosX, newPosY):
  return not isOutOfRange(newPosX, newPosY) and lines[newPosY][newPosX] == "#"

def recordPosition():
  locations.add(f"{posX},{posY}")

def move():
  global posX, posY, direction
  newPosX = posX
  newPosY = posY
  if direction == 0:
    newPosX += 1
  elif direction == 1:
    newPosY += 1
  elif direction == 2:
    newPosX -= 1
  elif direction == 3:
    newPosY -= 1
  if isObstructed(newPosX, newPosY):
    direction = (direction + 1) % 4
    move()
  else:
    posX = newPosX
    posY = newPosY

for lineIndex in range(1, len(lines) - 1):
  for charIndex in range(1, len(lines[lineIndex]) - 1):
    char = lines[lineIndex][charIndex]
    if char == "^":
      posX = charIndex
      posY = lineIndex
      break
  if(posX >= 0): break

while isOutOfRange(posX, posY) == False:
  recordPosition()
  move()

print(len(locations))

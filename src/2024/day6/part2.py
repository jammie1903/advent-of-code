import sys
import functools

content = sys.argv[1]

lines = content.splitlines()

posX = -1
posY = -1
direction = 3

obstructionX = None
obstructionY = None

locations = set()
tempLocations = set()

validObstructions = set()


def isOutOfRange(posX, posY):
  if posX < 0 or posX >= len(lines[0]): return True
  if posY < 0 or posY >= len(lines): return True
  return False

def isObstructed(newPosX, newPosY):
  return not isOutOfRange(newPosX, newPosY) and (lines[newPosY][newPosX] == "#" or (obstructionX == newPosX and obstructionY == newPosY))

def recordPosition():
  locations.add(f"{posX},{posY}")

def recordTempPosition():
  tempLocations.add(f"{posX},{posY},{direction}")

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
    rotate()
    move()
  else:
    posX = newPosX
    posY = newPosY

def rotate():
  global direction
  direction = (direction + 1) % 4

for lineIndex in range(0, len(lines)):
  for charIndex in range(0, len(lines[lineIndex])):
    char = lines[lineIndex][charIndex]
    if char == "^":
      posX = charIndex
      posY = lineIndex
      break
  if posX >= 0: break

moveCount = 0

while isOutOfRange(posX, posY) == False:
  recordPosition()
  moveCount += 1
  print("moveCount", moveCount)
  sys.stdout.flush()

  currentX = posX
  currentY = posY
  currentDirection = direction
  move()
  canPlaceObstacle = not isOutOfRange(posX, posY) and direction == currentDirection and not f"{posX},{posY}" in locations
  if canPlaceObstacle:
    obstructionX = posX
    obstructionY = posY
  else:
    print("obstacle already in way")
  posX = currentX
  posY = currentY
  direction = currentDirection


  if canPlaceObstacle:
    move()
    loop = False
    while not loop and not isOutOfRange(posX, posY):
      locationString = f"{posX},{posY},{direction}"
      if locationString in tempLocations:
        loop = True
        print("loop")

        for lineIndex in range(0, len(lines)):
          line = ""
          for charIndex in range(0, len(lines[lineIndex])):
            line += (
              "\033[92mO\033[0m" if (obstructionX == charIndex and obstructionY == lineIndex) else
              "\033[92m|\033[0m" if f"{charIndex},{lineIndex},{1}" in tempLocations else
              "\033[92m|\033[0m" if f"{charIndex},{lineIndex},{3}" in tempLocations else
              "\033[92m-\033[0m" if f"{charIndex},{lineIndex},{0}" in tempLocations else
              "\033[92m-\033[0m" if f"{charIndex},{lineIndex},{2}" in tempLocations else
              "+" if f"{charIndex},{lineIndex}" in locations else
              lines[lineIndex][charIndex]
            )
          print (line)

      else:
        recordTempPosition()
        move()
    if loop:
      validObstructions.add(f"{obstructionX},{obstructionY}")
    else: print ("no loop")

  posX = currentX
  posY = currentY
  direction = currentDirection
  obstructionX = None
  obstructionY = None
  tempLocations = set()
  move()

print(len(validObstructions))

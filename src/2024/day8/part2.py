import sys

content = sys.argv[1]

lines = content.splitlines()

height = len(lines)
width = 0

def isInRange(x, y):
  return 0 <= x < width and 0 <= y < height

locations = dict()

antiNodes = set()

def addIfInRange(node: tuple):
  if isInRange(node[0], node[1]):
    antiNodes.add(node)
    return True
  return False

for lineIndex in range(height):
  line = lines[lineIndex]
  width = max(width, len(line))
  for charIndex in range(len(line)):
    char = line[charIndex]
    if not char == ".":
      if not char in locations:
        locations[char] = []
      locations[char].append((charIndex, lineIndex))

values = locations.values()

for valueSet in values:
  for i in range(len(valueSet)):
    for j in range(i + 1, len(valueSet)):
      nodeA = valueSet[i]
      nodeB = valueSet[j]
      diff = (nodeA[0] - nodeB[0], nodeA[1] - nodeB[1])
      addIfInRange(nodeA)
      addIfInRange(nodeB)

      valid = True
      antiNode = nodeA
      while valid:
        antiNode = (antiNode[0] + diff[0], antiNode[1] + diff[1])
        valid = addIfInRange(antiNode)

      valid = True
      antiNode = nodeB
      while valid:
        antiNode = (antiNode[0] - diff[0], antiNode[1] - diff[1])
        valid = addIfInRange(antiNode)

print(len(antiNodes))

for lineIndex in range(height):
  line = lines[lineIndex]
  outputLine = ""
  for charIndex in range(len(line)):
    char = line[charIndex]
    if not char == ".":
      outputLine += char
    elif (charIndex, lineIndex) in antiNodes:
      outputLine += "#"
    else:
      outputLine += char
  print(outputLine)

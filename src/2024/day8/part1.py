import sys

content = sys.argv[1]

lines = content.splitlines()

height = len(lines)
width = 0

def isInRange(x, y):
  return 0 <= x < width and 0 <= y < height

locations = dict()
antiNodes = set()

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
      diff = (valueSet[i][0] - valueSet[j][0], valueSet[i][1] - valueSet[j][1])
      antiNodeA = (valueSet[i][0] + diff[0], valueSet[i][1] + diff[1])
      antiNodeB = (valueSet[j][0] - diff[0], valueSet[j][1] - diff[1])
      if isInRange(antiNodeA[0], antiNodeA[1]):
        antiNodes.add(antiNodeA)
      if isInRange(antiNodeB[0], antiNodeB[1]):
        antiNodes.add(antiNodeB)

print(antiNodes)
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

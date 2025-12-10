import sys
content = sys.argv[1]

lines = content.split("\n")

splitCount = 0
beamIndexes = set()

for line in lines:
  newBeamIndexes = set()
  for i in range(len(line)):
    char = line[i]
    if char == "S":
      newBeamIndexes.add(i)
    elif char == ".":
      if i in beamIndexes:
        newBeamIndexes.add(i)
    elif char == "^":
      if i in beamIndexes:
        newBeamIndexes.add(i - 1)
        newBeamIndexes.add(i + 1)
        splitCount += 1
  beamIndexes = newBeamIndexes

print("splits", splitCount)

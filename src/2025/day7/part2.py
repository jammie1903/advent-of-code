import sys
content = sys.argv[1]

lines = content.split("\n")


beamIndexes = dict()

for line in lines:
  if (not line.strip()):
    continue
  newBeamIndexes = dict()
  for i in range(len(line)):
    char = line[i]
    if char == "S":
      newBeamIndexes[i] = 1
    elif char == ".":
      if i in beamIndexes:
        newBeamIndexes[i] = newBeamIndexes.get(i, 0) + beamIndexes[i]
    elif char == "^":
      if i in beamIndexes:
        newBeamIndexes[i - 1] = newBeamIndexes.get(i - 1, 0) + beamIndexes[i]
        newBeamIndexes[i + 1] = newBeamIndexes.get(i + 1, 0) + beamIndexes[i]
  beamIndexes = newBeamIndexes

print("splits", sum(beamIndexes.values()))

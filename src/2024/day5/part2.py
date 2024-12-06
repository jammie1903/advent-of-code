import sys
import functools

content = sys.argv[1]

lines = content.splitlines()
instructions = []
patternStep = False

def findInstruction(x, y):
  for obj in instructions:
    if obj["x"] == x and obj["y"] == y:
      return obj
  return None

def myCmp(a, b):
  found = findInstruction(a, b)
  if found:
    return -1
  found = findInstruction(b, a)
  if found:
    return 1
  return 0

sum = 0

for line in lines:
  if not line:
    patternStep = True
  elif patternStep:
    unsorted = line.split(",")
    sections = sorted(unsorted,key=functools.cmp_to_key(myCmp))
    if not line == ",".join(sections):
      middle = sections[int(len(sections) / 2)]
      sum += int(middle)
  else:
    x, y = line.split("|")
    instructions.append(dict({ "x": x, "y": y }))

print(sum)

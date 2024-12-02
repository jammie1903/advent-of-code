import sys
content = sys.argv[1]

lines = content.splitlines()

safeCount = 0

def evaluate(values):
  diff = values[0] - values[1]
  ascending = None
  last = values[0]
  for value in values[1:]:
    diff = last - value
    if abs(diff) < 1 or abs(diff) > 3:
      return False
    isAscending = diff > 0
    if ascending == None:
      ascending = isAscending
    elif ascending != isAscending:
      return False
    last = value
  return True

for line in lines:
  rawValues = line.split()
  allValues = [int(x) for x in rawValues]
  prev = safeCount
  for skipIndex in range(len(allValues)):
    values = allValues[:skipIndex] + allValues[skipIndex+1:]
    if evaluate(values):
      safeCount += 1
      break

print("result", safeCount)
sys.stdout.flush()

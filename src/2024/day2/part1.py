import sys
content = sys.argv[1]

lines = content.splitlines()

safeCount = 0

for line in lines:
  rawValues = line.split()
  values = [int(x) for x in rawValues]
  diff = values[0] - values[1]
  ascending = None
  last = values[0]
  safe = True
  for value in values[1:]:
    diff = last - value
    if abs(diff) < 1 or abs(diff) > 3:
      safe = False
      break
    isAscending = diff > 0
    if ascending == None:
      ascending = isAscending
    elif ascending != isAscending:
      safe = False
      break
    last = value
  if safe:
    safeCount += 1


print("result", safeCount)
sys.stdout.flush()

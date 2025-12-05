import sys
content = sys.argv[1]

lines = content.split("\n")
total = 0
ranges = []

def findOverlappingRange(ranges, rangeToCheck):
  for range in ranges:
    if (range[0] <= rangeToCheck[1] and rangeToCheck[0] <= range[1]):
      return range

def combine(range1, range2):
  return (min(range1[0], range2[0]), max(range1[1], range2[1]))

for line in lines:
  if (line == ""): break

  start, end = line.split("-")
  startInt = int(start)
  endInt = int(end)
  ranges.append((startInt, endInt))

finalRanges = []
for range in ranges:
  outputRange = range
  overlap = findOverlappingRange(finalRanges, outputRange)
  while (overlap != None):
    print("overlap", outputRange, overlap)
    finalRanges.remove(overlap)
    outputRange = combine(outputRange, overlap)
    overlap = findOverlappingRange(finalRanges, outputRange)
  finalRanges.append(outputRange)

for range in finalRanges:
  total += 1 + range[1] - range[0]

print("result", total)
sys.stdout.flush()

import sys
content = sys.argv[1]

ranges = content.split(",")
total = 0

for rangeStr in ranges:
  startStr, endStr = rangeStr.split("-")
  start = int(startStr)
  end = int(endStr)

  for value in range(start, end + 1):
    strValue = str(value)
    length = len(strValue)
    if (length % 2) != 0:
      continue
    halfLength = length / 2
    firstHalf = strValue[0:int(halfLength)]
    secondHalf = strValue[int(halfLength):]
    if firstHalf == secondHalf:
      total += value

print("result", total)
sys.stdout.flush()

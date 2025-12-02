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
    halfLength = length / 2

    for i in range(1, int(halfLength) + 1):
      if (length % i != 0): continue
      segments = [strValue[j:j+i] for j in range(0, len(strValue), i)]
      if len(set(segments)) == 1:
        total += value
        break

print("result", total)
sys.stdout.flush()

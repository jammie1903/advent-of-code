import sys
content = sys.argv[1]

lines = content.split("\n")
total = 0
ranges = []

checkingRanges = True
for line in lines:
  if (line == ""): checkingRanges = False

  if (checkingRanges):
    start, end = line.split("-")
    ranges.append((int(start), int(end)))
  elif line != "":
    value = int(line)
    for start, end in ranges:
      if (value >= start and value <= end):
        total += 1
        break

print("result", total)
sys.stdout.flush()

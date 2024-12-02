import sys
content = sys.argv[1]

lines = content.splitlines()
arr = []
counts = {}

for line in lines:
  val1, val2 = line.split()[:2]
  arr.append(val1)
  if val2 in counts:
    counts[val2] += 1
  else:
    counts[val2] = 1

total = 0

for value in arr:
  if value in counts:
    total += int(value) * counts[value]

print("result", total)
sys.stdout.flush()

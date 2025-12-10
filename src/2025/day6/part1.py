import sys
import re
content = sys.argv[1]

lines = content.split("\n")

allSegments = []
operations = None
for line in lines:
  parts = re.split(r'\s+', line.strip())
  print("parts", parts)
  if not (parts[0].isdigit()):
    operations = parts
    break
  else:
    allSegments.append([int(part) for part in parts])
total = 0

print(allSegments)

for i in range(len(operations)):
  operator = operations[i]
  count = allSegments[0][i]
  if operator == "+":
    for j in range(1, len(allSegments)):
      count += allSegments[j][i]
  elif operator == "*":
    for j in range(1, len(allSegments)):
      count *= allSegments[j][i]
  total += count

print ("result", total)
sys.stdout.flush()

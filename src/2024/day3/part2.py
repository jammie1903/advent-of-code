import sys
import re

content = sys.argv[1]

lines = content.splitlines()
total = 0
enabled = True

for line in lines:
  # r prefix - raw string, tells Python not to interpret backslashes as escape characters.
  matches = re.findall(r"(mul\((\d+),(\d+)\))|(do(n't)?\(\))", line)
  for match in matches:
    mulMatch, x, y, otherMatch, dontMatch = match[:5]
    if (dontMatch):
      enabled = False
    elif (otherMatch):
      enabled = True
    elif (mulMatch and enabled):
      total += int(x) * int(y)

print(total)

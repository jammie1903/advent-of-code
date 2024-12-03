import sys
import re

content = sys.argv[1]

lines = content.splitlines()
total = 0

for line in lines:
  # r prefix - raw string, tells Python not to interpret backslashes as escape characters.
  matches = re.findall(r"mul\((\d+),(\d+)\)", line)
  for match in matches:
    x, y = match[:2]
    total += int(x) * int(y)


print(total)

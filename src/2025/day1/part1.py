import sys
content = sys.argv[1]

rows = content.splitlines()

value = 50
zeroCount = 0


for row in rows:
  direction = row[0]
  amount = int(row[1:])
  if (direction == "L"):
    value -= amount
  else:
    value += amount
  value = value % 100
  if value == 0:
    zeroCount += 1


print("result", zeroCount)
sys.stdout.flush()

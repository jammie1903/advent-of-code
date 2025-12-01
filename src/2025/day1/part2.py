import sys
content = sys.argv[1]

rows = content.splitlines()

value = 50
clickCount = 0

for row in rows:
  direction = row[0]
  amount = int(row[1:])

  if (direction == "L" and value == 0 and amount > 0):
    value += 100

  if (direction == "L"):
    value -= amount
  else:
    value += amount

  while value < 0:
    value += 100
    clickCount += 1
    print(".   Adjusting up:", value)
  while value >= 100:
    value -= 100
    clickCount += 1
    print(".   Adjusting down:", value)

  if value == 0 and direction == "L":
    print(".   Value is zero")
    clickCount += 1


print("result", clickCount)
sys.stdout.flush()

import sys
content = sys.argv[1]

lines = content.split("\n")

max_length = max(map(len, lines))

outputLines = [""] * max_length

for line in lines:
  for x in range(max_length):
    char = x >= len(line) and " " or line[x]
    outputLines[x] += char

print (outputLines)

operator = ""
values = []

total = 0

def calculate():
  global operator, values, total
  if (not operator) or (not values):
    return
  if operator == "+":
    total += sum(values)
  elif operator == "*":
    result = 1
    for v in values:
      result *= v
    total += result
  operator = ""
  values = []


for outputLine in outputLines:
  l = outputLine.strip()
  if l == "":
    continue
  if not l.isdigit():
    calculate()
    # find the non-digit character
    for char in l:
      if not char.isdigit() and char != " ":
        operator = char
        l = l.replace(char, " ").strip()
        break
  values.append(int(l))


calculate()

print ("result", total)


sys.stdout.flush()

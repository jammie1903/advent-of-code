import sys
content = sys.argv[1]

rows = content.splitlines()

parsedValues = dict()
outstandingValues = list()

logicMap = {
  "AND": lambda a, b: 1 if a > 0 and b > 0 else 0,
  "OR": lambda a, b: 1 if a > 0 or b > 0 else 0,
  "XOR": lambda a, b: 1 if min(1, a) != min(1, b) else 0
}

for row in rows:
  if ": " in row:
    key, value = row.split(": ")
    parsedValues[key] = int(value)
  if " -> " in row:
    logic, output = row.split(" -> ")
    a, operator, b = logic.split()
    outstandingValues.append((a, operator, b, output))

while len(outstandingValues) > 0:
  a, operator, b, output = outstandingValues.pop(0)
  if a in parsedValues and b in parsedValues:
    aValue = parsedValues[a]
    bValue = parsedValues[b]
    outputValue = logicMap[operator](aValue, bValue)
    parsedValues[output] = outputValue
  else:
    outstandingValues.append((a, operator, b, output))

values = dict()

for key, value in parsedValues.items():
  if key.startswith("z"):
    values[int(key[1:])] = value

output = [None] * len(values)

for i in range(len(output)):
  output[i] = str(values[i])

output.reverse()



print(output, int("".join(output), 2))

import sys

content = sys.argv[1]

values = content.split()

blinkCount = 25


for blink in range(blinkCount):
  newValues = []
  for value in values:
    if value == "0":
      newValues.append("1")
    elif len(value) % 2 == 0:
      # double slash == integer division
      halfPoint = len(value) // 2
      newValues.append(str(int(value[:halfPoint])))
      newValues.append(str(int(value[halfPoint:])))
    else:
      newValues.append(str(int(value) * 2024))
  values = newValues

print(len(values))

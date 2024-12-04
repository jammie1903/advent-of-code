import sys

content = sys.argv[1]

lines = content.splitlines()

lookupString = "MAS"
lookupStringReversed = lookupString[::-1]
matchCount = 0

for lineIndex in range(1, len(lines) - 1):
  for charIndex in range(1, len(lines[lineIndex]) - 1):
    char = lines[lineIndex][charIndex]
    if (char == lookupString[1]):
      line1Char1 = lines[lineIndex + 1][charIndex + 1]
      line1Char3 = lines[lineIndex - 1][charIndex - 1]
      line2Char1 = lines[lineIndex - 1][charIndex + 1]
      line2Char3 = lines[lineIndex + 1][charIndex - 1]

      line1 = line1Char1 + char + line1Char3
      line2 = line2Char1 + char + line2Char3

      if (line1 == lookupString or line1 == lookupStringReversed) and (line2 == lookupString or line2 == lookupStringReversed):
        matchCount+=1

print("Result:", matchCount)

import sys

content = sys.argv[1]

lines = content.splitlines()

lookupString = "XMAS"
matchCount = 0

for lineIndex in range(len(lines)):
  for charIndex in range(len(lines[lineIndex])):
    char = lines[lineIndex][charIndex]
    if (char == lookupString[0]):
      offsets = [-1, 0, 1]
      for lineOffset in offsets:
        for charOffset in offsets:
          if lineOffset == 0 and charOffset == 0: continue
          noMatch = False
          for lookupCharIndex in range(1, len(lookupString)):
            lineLookupIndex = lineIndex + (lineOffset * lookupCharIndex)
            charLookupIndex = charIndex + (charOffset * lookupCharIndex)
            if lineLookupIndex < 0 or lineLookupIndex >= len(lines) or charLookupIndex < 0 or charLookupIndex >= len(lines[lineIndex]):
              noMatch = True
              break
            offsetChar = lines[lineLookupIndex][charLookupIndex]
            if offsetChar != lookupString[lookupCharIndex]:
              noMatch = True
              break
          if not noMatch:
            matchCount+=1

print("Result:", matchCount)



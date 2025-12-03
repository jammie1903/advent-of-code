import sys
content = sys.argv[1]

banks = content.split("\n")
total = 0
digitCount = 12

for bank in banks:
  length = len(bank)
  if length < digitCount:
    continue
  characters = ""
  minIndex = 0
  for i in range(digitCount):
    remainingCharacters = digitCount - i - 1
    substring = bank[minIndex:length - remainingCharacters]
    maxChar = max(substring)
    nextCharacterIndex = minIndex + substring.index(maxChar)
    minIndex = nextCharacterIndex + 1
    characters += maxChar
  total += int(characters)

print("result", total)
sys.stdout.flush()

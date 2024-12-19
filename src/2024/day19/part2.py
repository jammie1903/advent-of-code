import sys

content = sys.argv[1]

lines = content.splitlines()
towels = [x.strip() for x in lines[0].split(",")]

matchCount = 0

for targetPattern in lines[2:]:
  print("targetPattern", targetPattern)
  sys.stdout.flush()
  potentialPatterns = { "": 1 }
  matches = 0
  while len(potentialPatterns) > 0:
    sys.stdout.flush()

    newPatterns = dict()
    for partialPattern, partialPatternCount in potentialPatterns.items():
      for towel in towels:
        newPattern = partialPattern + towel
        if targetPattern == newPattern:
          matches += partialPatternCount
        elif len(newPattern) < len(targetPattern) and targetPattern[:len(newPattern)] == newPattern:
          if newPattern not in newPatterns:
            newPatterns[newPattern] = partialPatternCount
          else:
            newPatterns[newPattern] += partialPatternCount
    potentialPatterns = newPatterns

  matchCount += matches

print(matchCount)

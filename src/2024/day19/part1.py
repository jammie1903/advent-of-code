import sys

content = sys.argv[1]

lines = content.splitlines()
towels = [x.strip() for x in lines[0].split(",")]

matchCount = 0

for targetPattern in lines[2:]:
  print("targetPattern", targetPattern)
  sys.stdout.flush()
  potentialPatterns = [""]
  matchFound = False
  while not matchFound and len(potentialPatterns) > 0:
    sys.stdout.flush()

    newPatterns = set()
    for partialPattern in potentialPatterns:
      for towel in towels:
        newPattern = partialPattern + towel
        if targetPattern == newPattern:
          matchFound = True
          break
        if len(newPattern) < len(targetPattern) and targetPattern[:len(newPattern)] == newPattern:
          newPatterns.add(newPattern)
    potentialPatterns = list(newPatterns)
    if matchFound: break
  if matchFound:
    matchCount += 1

print(matchCount)

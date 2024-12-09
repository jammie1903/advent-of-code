import sys
import re

content = sys.argv[1]

hardDrive = []

nextFileId = 0
nextIsFile = True

for char in content:
  if not re.match(r"[0-9]", char): continue
  size = int(char)
  if nextIsFile:
    hardDrive += [nextFileId] * size
    nextIsFile = False
    nextFileId += 1
  else:
    hardDrive += ["."] * size
    nextIsFile = True

startIndex = 0
endIndex = len(hardDrive) - 1

while startIndex < endIndex:
  swapReady = True
  while hardDrive[startIndex] != ".":
    startIndex += 1
    swapReady = False
  while hardDrive[endIndex] == ".":
    endIndex -= 1
    swapReady = False

  if swapReady:
    temp = hardDrive[startIndex]
    hardDrive[startIndex] = hardDrive[endIndex]
    hardDrive[endIndex] = temp

checksum = 0

for i in range(len(hardDrive)):
  if hardDrive[i] == ".":
    break
  checksum += int(hardDrive[i]) * i

print(checksum)

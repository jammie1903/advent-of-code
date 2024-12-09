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
    hardDrive.append({ "value": str(nextFileId), "size": size })
    nextIsFile = False
    nextFileId += 1
  else:
    hardDrive.append({ "value": ".", "size": size })
    nextIsFile = True

endIndex = len(hardDrive) - 1


while endIndex > 0:
  if hardDrive[endIndex]["value"] != ".":
    startIndex = next((i for i, d in enumerate(hardDrive) if d.get("value") == "." and d.get("size", 0) >= hardDrive[endIndex]["size"]), -1)
    if(startIndex != -1 and startIndex < endIndex):
      if hardDrive[endIndex]["size"] == hardDrive[startIndex]["size"]:
        temp = hardDrive[startIndex]
        hardDrive[startIndex] = hardDrive[endIndex]
        hardDrive[endIndex] = temp
      else:
        remaining = hardDrive[startIndex]["size"] - hardDrive[endIndex]["size"]
        hardDrive[startIndex]["value"] = hardDrive[endIndex]["value"]
        hardDrive[startIndex]["size"] = hardDrive[endIndex]["size"]
        hardDrive[endIndex]["value"] = "."
        hardDrive.insert(startIndex + 1, { "value": ".", "size": remaining })
        endIndex += 1
  endIndex -= 1

checksum = 0

outputArray = []
for val in hardDrive:
  outputArray += [val["value"]] * val["size"]

for i in range(len(outputArray)):
  if outputArray[i] == ".":
    continue
  checksum += int(outputArray[i]) * i

print(checksum)

import sys
import heapq

content = sys.argv[1]

lines = content.split("\n")

def getStraightLineDistance(pointA, pointB):
  return ((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2 + (pointA[2] - pointB[2]) ** 2) ** 0.5

topDistances = []

links = dict()
groups = []

indexA = 0
for line in lines:
  if (not line.strip()):
    continue

  links[indexA] = set()
  links[indexA].add(indexA)
  groups.append(links[indexA])

  point = line.split(",")
  point = (int(point[0]), int(point[1]), int(point[2]))
  indexB = indexA + 1
  for otherLine in lines[indexA + 1:]:
    if (not otherLine.strip()):
      continue
    otherPoint = otherLine.split(",")
    otherPoint = (int(otherPoint[0]), int(otherPoint[1]), int(otherPoint[2]))
    distance = getStraightLineDistance(point, otherPoint)

    # Add to heap
    heapq.heappush(topDistances, (distance, indexA, indexB))

    indexB += 1
  indexA += 1

# sort the heap
topDistances.sort()

for distance, indexA, indexB in topDistances:
  indexAGroup = links.get(indexA)
  indexBGroup = links.get(indexB)

  if indexAGroup == indexBGroup:
    continue
  indexAGroup.update(indexBGroup)
  groups.remove(indexBGroup)
  for index in indexBGroup:
    links[index] = indexAGroup
  if len(groups) == 1:
    indexAX = int(lines[indexA].split(",")[0])
    indexBX = int(lines[indexB].split(",")[0])
    print (indexAX, indexBX, indexAX * indexBX)


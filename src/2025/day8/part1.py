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
    heapq.heappush(topDistances, (-distance, indexA, indexB))

    if len(topDistances) > 1000:
      heapq.heappop(topDistances)
    indexB += 1
  indexA += 1

for distance, indexA, indexB in topDistances:
  indexAGroup = links.get(indexA)
  indexBGroup = links.get(indexB)
  if indexAGroup != None:
    if indexAGroup == indexBGroup:
      continue
    if indexBGroup != None:
      indexAGroup.update(indexBGroup)
      groups.remove(indexBGroup)
      for index in indexBGroup:
        links[index] = indexAGroup
    else:
      indexAGroup.add(indexB)
      links[indexB] = indexAGroup
  elif indexBGroup != None:
    indexBGroup.add(indexA)
    links[indexA] = indexBGroup
  else:
    newGroup = set()
    newGroup.add(indexA)
    newGroup.add(indexB)
    links[indexA] = newGroup
    links[indexB] = newGroup
    groups.append(newGroup)

groups.sort(key=len, reverse=True)

result = 1
for group in groups[0:3]:
    result *= len(group)
print("result", result)

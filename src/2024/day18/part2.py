import math
import sys

class AStar:
  def __init__(self, startNode, goalNode, getNeighbors):
    self.startNode = startNode
    self.goalNode = goalNode
    self.getNeighbors = getNeighbors
    self.openSet = [startNode]
    self.closedSet = set()
    self.cameFrom = dict()
    self.gScore = dict()
    self.gScore[startNode] = 0
    self.fScore = dict()
    self.fScore[startNode] = self.heuristic(startNode, goalNode)

  def distance(self, nodeA, nodeB):
    return 1

  def heuristic(self, nodeA, nodeB):
    xDiff = nodeA[0] - nodeB[0]
    yDiff = nodeA[1] - nodeB[1]

    return math.sqrt(xDiff**2 + yDiff**2)

  def reconstructPath(self, current):
    totalPath = [current]
    while current in self.cameFrom:
      current = self.cameFrom.get(current)
      totalPath.insert(0, current)

    return totalPath

  def getLowestFScoreNode(self):
    lowestNode = None
    lowestFScore = math.inf

    for node in self.openSet:
      fScore = self.fScore.get(node) or math.inf
      if fScore < lowestFScore:
        lowestFScore = fScore
        lowestNode = node

    return lowestNode

  def run(self):
    while len(self.openSet) > 0:
      current = self.getLowestFScoreNode()
      sys.stdout.flush()
      if current == self.goalNode:
        return self.reconstructPath(current)

      # Remove current node from openSet and add it to closedSet
      self.openSet.remove(current)
      self.closedSet.add(current)
      neighbors = self.getNeighbors(current)
      for neighbor in neighbors:
        neighborLocation = neighbor["location"]
        if neighborLocation in self.closedSet:
          continue; # Ignore the neighbor if it's already evaluated

        tentativeGScore = self.gScore.get(current) + self.distance(current, neighborLocation)

        if not neighborLocation in self.openSet:
          self.openSet.append(neighborLocation); # Add neighbor to openSet if not already present

        if not neighborLocation in self.gScore or tentativeGScore < self.gScore.get(neighborLocation):
          # This path to neighbor is better than any previous one
          self.cameFrom[neighborLocation] = current
          self.gScore[neighborLocation] = tentativeGScore
          self.fScore[neighborLocation] = tentativeGScore + self.heuristic(neighborLocation, self.goalNode)


    return None; # No path found


start = (0, 0)
boundSize = 71
target = (boundSize-1, boundSize-1)
readCount = 1024
corrupted = []

def getAdjacentCells(point):
  cells = []
  for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
    nx, ny = point[0] + dx, point[1] + dy
    if 0 <= nx < boundSize and 0 <= ny < boundSize and (nx, ny) not in corrupted:
      cells.append((nx, ny))
  return cells

content = sys.argv[1]

lines = content.splitlines()

for line in lines[:readCount]:
  x, y = line.split(",")
  corrupted.append((int(x), int(y)))

getNeighbors = lambda node: [
  {
    "location": (newX, newY)
  }
  for newX, newY in getAdjacentCells(node)
]
path = []
while path is not None:
  x, y = lines[readCount].split(",")
  readCount += 1
  newCorrupted = (int(x), int(y))
  corrupted.append(newCorrupted)
  if len(path) == 0 or newCorrupted in path:
    aStar = AStar(start, target, getNeighbors)
    path = aStar.run()
print(lines[readCount-1])

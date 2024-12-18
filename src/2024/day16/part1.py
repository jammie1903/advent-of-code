import math
import sys

class AStar:
  def __init__(self, startNode, goalNode, getNeighbors):
    self.startNode = startNode
    startNodeKey = f"{startNode["location"]}:{startNode["direction"]}"
    self.goalNode = goalNode
    self.getNeighbors = getNeighbors
    self.openSet = [startNode]
    self.closedSet = set()
    self.cameFrom = dict()
    self.gScore = dict()
    self.gScore[startNodeKey] = 0
    self.fScore = dict()
    self.fScore[startNodeKey] = self.heuristic(startNode["location"], goalNode)
    # self.costs = dict()
    # self.costs[startNodeKey] = 0

  def heuristic(self, nodeA, nodeB):
    xDiff = nodeA[0] - nodeB[0]
    yDiff = nodeA[1] - nodeB[1]

    return math.sqrt(xDiff**2 + yDiff**2)

  def getLowestFScoreNode(self):
    lowestNode = None
    lowestFScore = math.inf

    for node in self.openSet:
      nodeKey = f"{node["location"]}:{node["direction"]}"
      fScore = self.fScore.get(nodeKey) or math.inf
      if fScore < lowestFScore:
        lowestFScore = fScore
        lowestNode = node

    return lowestNode

  def run(self):
    while len(self.openSet) > 0:
      current = self.getLowestFScoreNode()
      currentKey = f"{current["location"]}:{current["direction"]}"
      if current["location"] == self.goalNode:
        return self.gScore[currentKey]
        # return self.reconstructPath(current)

      # Remove current node from openSet and add it to closedSet
      self.openSet.remove(current)
      self.closedSet.add(currentKey)

      for node in self.getNeighbors(current):
        nodeKey = f"{node["location"]}:{node["direction"]}"
        neighborCost = 1
        if node["direction"] != current["direction"]:
          neighborCost += 1000
        if nodeKey in self.closedSet:
          continue; # Ignore the neighbor if it's already evaluated

        tentativeGScore = self.gScore.get(currentKey) + neighborCost

        if not node in self.openSet:
          self.openSet.append(node); # Add neighbor to openSet if not already present

        if not nodeKey in self.gScore or tentativeGScore < self.gScore.get(nodeKey):
          # This path to neighbor is better than any previous one
          self.cameFrom[nodeKey] = current
          self.gScore[nodeKey] = tentativeGScore
          self.fScore[nodeKey] = tentativeGScore + self.heuristic(node["location"], self.goalNode)
          # self.costs[nodeKey] = self.costs[current] + neighborCost


    return None; # No path found

content = sys.argv[1]

rows = content.splitlines()

wallCells = []
direction = 0

start = {
  "direction": 0,
  "location": (0, 0)
}
end = (0, 0)

for rowIndex in range(len(rows)):
  for cellIndex in range(len(rows[rowIndex])):
    char = rows[rowIndex][cellIndex]
    if char == "#":
      wallCells.append((cellIndex, rowIndex))
    elif char == "E":
      end = (cellIndex, rowIndex)
    elif char == "S":
      start["location"] = (cellIndex, rowIndex)


def getNeighbours(node):
  location = node["location"]
  direction = node["direction"]
  nodes = []
  if direction != 0 and location[0] >= 0:
    newLocation = (location[0] - 1, location[1])
    if newLocation not in wallCells:
      nodes.append({
        "location": newLocation,
        "direction": 2,
      })
  if direction != 2 and location[0] < len(rows[location[1]]):
    newLocation = (location[0] + 1, location[1])
    if newLocation not in wallCells:
      nodes.append({
        "location": newLocation,
        "direction": 0,
      })
  if direction != 1 and location[1] >= 0:
    newLocation = (location[0], location[1] - 1)
    if newLocation not in wallCells:
      nodes.append({
        "location": newLocation,
        "direction": 3,
      })
  if direction != 3 and location[0] < len(rows):
    newLocation = (location[0], location[1] + 1)
    if newLocation not in wallCells:
      nodes.append({
        "location": newLocation,
        "direction": 1,
      })
  return nodes


aStar = AStar(start, end, getNeighbours)
result = aStar.run()

print(result)

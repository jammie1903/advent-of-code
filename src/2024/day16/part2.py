import math
import sys

# I over-engineered this solution entirely, in the hope it would help with teh next part... it did not

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
    self.winningCells = set()
    self.winningScore = -1
    # self.costs = dict()
    # self.costs[startNodeKey] = 0

  def heuristic(self, nodeA, nodeB):
    xDiff = nodeA[0] - nodeB[0]
    yDiff = nodeA[1] - nodeB[1]

    return math.sqrt(xDiff**2 + yDiff**2)

  def reconstructPath(self, current):
    currentKeys = [f"{current["location"]}:{current["direction"]}"]
    totalPath = [f"{current["location"]}:{self.gScore[currentKeys[0]]}"]
    while len(currentKeys) > 0:
      currentKey = currentKeys.pop()
      if currentKey in self.cameFrom:
        currentArr = self.cameFrom.get(currentKey)
        for current in currentArr:
          newKey = f"{current["location"]}:{current["direction"]}"
          totalPath.insert(0, f"{current["location"]}:{self.gScore[newKey]}")
          currentKeys.insert(0, newKey)
    return totalPath

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
      selfGScore = self.gScore[currentKey]
      if current["location"] == self.goalNode:
        if len(self.winningCells) == 0:
          self.winningCells.update(self.reconstructPath(current))
          self.openSet.remove(current)
          self.closedSet.add(currentKey)
          continue
        # else:
        #   entry = f"{current["location"]}:{selfGScore}"
        #   if entry in self.winningCells:
        #     self.winningCells.update(self.reconstructPath(current))
        #     self.openSet.remove(current)
        #     self.closedSet.add(currentKey)
        #     continue

      # Remove current node from openSet and add it to closedSet
      self.openSet.remove(current)
      self.closedSet.add(currentKey)

      for node in self.getNeighbors(current):
        nodeKey = f"{node["location"]}:{node["direction"]}"
        neighborCost = 1
        if node["direction"] != current["direction"]:
          neighborCost += 1000

        tentativeGScore = self.gScore.get(currentKey) + neighborCost

        if nodeKey in self.closedSet:
          entry = f"{node["location"]}:{tentativeGScore}"
          if entry in self.winningCells:
            self.winningCells.update(self.reconstructPath(node))
          continue; # Ignore the neighbor if it's already evaluated


        if not node in self.openSet:
          self.openSet.append(node); # Add neighbor to openSet if not already present

        if not nodeKey in self.gScore or tentativeGScore < self.gScore.get(nodeKey):
          # This path to neighbor is better than any previous one
          self.cameFrom[nodeKey] = [current]
          self.gScore[nodeKey] = tentativeGScore
          self.fScore[nodeKey] = tentativeGScore + self.heuristic(node["location"], self.goalNode)
          # self.costs[nodeKey] = self.costs[current] + neighborCost
        elif nodeKey in self.gScore and tentativeGScore == self.gScore.get(nodeKey):
          self.cameFrom[nodeKey].append(current)

    return len(self.winningCells)

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

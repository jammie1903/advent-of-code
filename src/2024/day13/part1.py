import math
import sys

# I over-engineered this solution entirely, in the hope it would help with teh next part... it did not

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
    self.costs = dict()
    self.costs[startNode] = 0

  def distance(self, nodeA, nodeB):
    xDiff = nodeA[0] - nodeB[0]
    yDiff = nodeA[1] - nodeB[1]

    return math.sqrt(xDiff**2 + yDiff**2)

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
        return self.costs[current]
        # return self.reconstructPath(current)

      # Remove current node from openSet and add it to closedSet
      self.openSet.remove(current)
      self.closedSet.add(current)

      for neighbor in self.getNeighbors(current):
        neighborLocation = neighbor["location"]
        neighborCost = neighbor["cost"]
        if neighborLocation in self.closedSet:
          continue; # Ignore the neighbor if it's already evaluated

        tentativeGScore = self.gScore.get(current) + neighborCost * self.distance(current, neighborLocation)

        if not neighborLocation in self.openSet:
          self.openSet.append(neighborLocation); # Add neighbor to openSet if not already present

        if not neighborLocation in self.gScore or tentativeGScore < self.gScore.get(neighborLocation):
          # This path to neighbor is better than any previous one
          self.cameFrom[neighborLocation] = current
          self.gScore[neighborLocation] = tentativeGScore
          self.fScore[neighborLocation] = tentativeGScore + self.heuristic(neighborLocation, self.goalNode)
          self.costs[neighborLocation] = self.costs[current] + neighborCost


    return None; # No path found

content = sys.argv[1]

rows = content.splitlines()

entries = []

buttons = dict()
target = dict()
for row in rows:
  if not ":" in row: continue
  key, value = row.split(":")
  if key.startswith("Button "):
    buttonId = key.split(" ")[1]
    buttonValues = value.strip().split(",")
    coords = dict()
    for value in buttonValues:
      coord, distance = value.strip().split("+")
      coords[coord] = int(distance)
    buttons[buttonId] = coords
  elif key == "Prize":
    targetValues = value.strip().split(",")
    for value in targetValues:
      coord, distance = value.strip().split("=")
      target[coord] = int(distance)
    entries.append({ "buttons": buttons, "target": target })
    buttons = dict()
    target = dict()
  else:
    raise ImportWarning("Unknown command %s" % key)

start = (0, 0)

total = 0

for entry in entries:
  goal = (entry["target"]["X"], entry["target"]["Y"])
  getNeighbors = lambda node: [
    {
      "location": (newX, newY),
      "cost": 3 if buttonId == "A" else 1
    }
    for buttonId, coords in entry["buttons"].items()
    if (newX := node[0] + coords["X"]) <= goal[0] and (newY := node[1] + coords["Y"]) <= goal[1]
  ]
  aStar = AStar(start, goal, getNeighbors)
  result = aStar.run()
  if result is not None:
    total += result

print(total)

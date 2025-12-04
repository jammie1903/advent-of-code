import sys
content = sys.argv[1]

grid = content.split("\n")
total = 0

def getCellValue(x, y):
  if (y < 0 or y >= len(grid)):
    return None
  if (x < 0 or x >= len(grid[y])):
    return None
  return grid[y][x]

def getAdjacentCellValues(x, y):
  return [
    getCellValue(x - 1, y - 1),
    getCellValue(x - 1, y),
    getCellValue(x - 1, y + 1),
    getCellValue(x, y - 1),
    getCellValue(x, y + 1),
    getCellValue(x + 1, y - 1),
    getCellValue(x + 1, y),
    getCellValue(x + 1, y + 1),
  ]

y = 0
for row in grid:
  max = 0
  for x in range(len(row)):
    cellValue = row[x]
    if (cellValue != "@"): continue
    adjacentCells = getAdjacentCellValues(x, y)
    occupiedCellCount = 0
    for cell in adjacentCells:
      if (cell == "@"): occupiedCellCount += 1
    if (occupiedCellCount < 4):
      total += 1
  y += 1

print("result", total)
sys.stdout.flush()

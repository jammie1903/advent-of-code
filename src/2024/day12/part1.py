import sys

content = sys.argv[1]

rows = content.splitlines()

handled = set()

def getAdjacentCells(point):
  cells = []
  for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
    nx, ny = point[0] + dx, point[1] + dy
    if 0 <= nx < len(rows[y]) and 0 <= ny < len(rows):
      cells.append((nx, ny))
  return cells

total = 0

for y in range(len(rows)):
  for x in range(len(rows[y])):
    if (x, y) in handled: continue
    area = set([(x, y)])
    stack = [(x, y)]
    while len(stack) > 0:
      px, py = stack.pop()
      handled.add((px, py))
      for nx, ny in getAdjacentCells((px, py)):
        if (nx, ny) not in handled and rows[ny][nx] == rows[py][px]:
          area.add((nx, ny))
          stack.append((nx, ny))

    perimeter = 0
    for cell in area:
      adjacentCells = [x for x in getAdjacentCells(cell) if x in area]
      perimeter += 4 - len(adjacentCells)
    print(rows[y][x], "perimeter", perimeter, "area", len(area))
    total += len(area) * perimeter

print(total)

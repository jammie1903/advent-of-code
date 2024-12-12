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

    boundariesByDirection = dict()
    for cell in area:
      for diff in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = cell[0] + diff[0], cell[1] + diff[1]
        isBoundary = False
        if 0 <= nx < len(rows[y]) and 0 <= ny < len(rows):
          if not (nx, ny) in area:
            isBoundary = True
        else:
          isBoundary = True

        if isBoundary:
          if not diff in boundariesByDirection:
            boundariesByDirection[diff] = []
          boundariesByDirection[diff].append(cell)


    segments = 0
    for direction, boundaries in boundariesByDirection.items():
      groupingIndex = 0
      comparisonIndex = 1
      grouping = dict()
      if direction[0] == 0:
        groupingIndex = 1
        comparisonIndex = 0
      for bound in boundaries:
        if not bound[groupingIndex] in grouping:
          grouping[bound[groupingIndex]] = []
        grouping[bound[groupingIndex]].append(bound[comparisonIndex])
      for positions in grouping.values():
        positions.sort()
        last = -2
        for pos in positions:
          if pos - last > 1:
            segments += 1
          last = pos


    print(rows[y][x], "segments", segments, "area", len(area))
    total += len(area) * segments

print(total)

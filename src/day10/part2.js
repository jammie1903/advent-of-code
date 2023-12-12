const fs = require("fs");

const directions = {
  north: ([x, y]) => [x, y - 1],
  south: ([x, y]) => [x, y + 1],
  east: ([x, y]) => [x + 1, y],
  west: ([x, y]) => [x - 1, y]
};

const pipeTypes = {
  "|": [directions.north, directions.south],
  "-": [directions.east, directions.west],
  L: [directions.north, directions.east],
  J: [directions.north, directions.west],
  7: [directions.south, directions.west],
  F: [directions.south, directions.east],
  ".": [],
  S: Object.values(directions)
};

const colorMap = {
  black: "\x1b[30m",
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  blue: "\x1b[34m",
  magenta: "\x1b[35m",
  cyan: "\x1b[36m",
  white: "\x1b[37m",
  gray: "\x1b[90m"
}
const clearColor = "\x1b[0m"

const withColor = (s, color) => `${colorMap[color]}${s}${clearColor}`;

function aStar({ start, getHeuristic = () => 0, getNeighbours, isTarget, onFail = () => {} }) {
  const open = [{ position: start, score: 0, heuristic: 0, parent: null }]
  const closed = []
  while(open.length) {
    const current = open.shift();
    getNeighbours(current.position)
      .filter(n => !closed.find(c => n[0] === c[0] && n[1] === c[1]))
      .forEach(n => {
      const score = current.score + 1;
      const heuristic = getHeuristic(n);
      const openEntry = open.find(o => n[0] === o.position[0] && n[1] === o.position[1]);

      if (openEntry) {
        openEntry.alternativeParents ||= []
        if (openEntry.score + openEntry.heuristic > score + heuristic) {
          openEntry.alternativeParents.push(openEntry.parent);
          openEntry.parent = current;
          openEntry.score = score;
          openEntry.heuristic = heuristic;
        } else {
          openEntry.alternativeParents.push(current);
        }
      } else {
        open.push({ position: n, score, heuristic, parent: current })
      }
    });
    open.sort((a, b) => (a.score = a.heuristic) - (b.score + b.heuristic));
    closed.push(current.position);
    if (isTarget(current)) {
      return current;
    }
  }
  onFail(closed)
}

const pathForEach = (path, action) => {
  let current = path
  while (current) {
    action(current)
    current = current.parent;
  }
}

module.exports = input => {
  const grid = input.split("\n").filter(Boolean);

  function mapCoords(x, y, pipeType, _grid = grid) {
    return pipeTypes[pipeType].map(mapper => mapper([x, y]))
      .filter(([x, y]) => !(x < 0 || y < 0 || x >= _grid[0].length || y >= _grid.length))
  }

  const largerGrid = inputGrid => {
    const grid = [];
    for (let y = 0; y < inputGrid.length; y++) {
      grid.push([], [], [])
      for (let x = 0; x < inputGrid[y].length; x++) {
        const pipeType = inputGrid[y][x];
        const coords = mapCoords(1, 1, pipeType).map(c => c.join(","))
        const enterOccupied = !!coords.length;
        grid[y*3].push(0, coords.includes("1,0"), 0)
        grid[y*3 + 1].push(coords.includes("0,1"), enterOccupied, coords.includes("2,1"))
        grid[y*3 + 2].push(0, coords.includes("1,2"), 0)
      }
    }

    return grid
  }

  const map = [];
  let start;
  for (let y = 0; y < grid.length; y++) {
    map.push([])
    for (let x = 0; x < grid[y].length; x++) {
      const pipeType = grid[y][x]
      map[y].push(mapCoords(x, y, pipeType))
      if (pipeType === "S") {
        start = [x, y]
      }
    }
  }

  const closedPath = aStar({
    start,
    getNeighbours: (position) => {
      const neighbours = map[position[1]][position[0]];
      return neighbours
        .filter(n => {
          const neighboursLinks = map[n[1]][n[0]];
          return neighboursLinks.find(nl => nl[0] === position[0] && nl[1] === position[1])
        })
    },
    isTarget: current => !!current.alternativeParents
  })

  if (!closedPath) {
    throw new Error("No enclosing route found")
  }
  const largeGrid = largerGrid(grid);

  const pathStore = {};
  [closedPath, ...closedPath.alternativeParents].forEach(
    p => pathForEach(p, segment => {
      const pipeType = grid[segment.position[1]][segment.position[0]];
      const pos = [segment.position[0] * 3 + 1, segment.position[1] * 3 + 1]
      const allOccupied = [pos, ...mapCoords(pos[0], pos[1], pipeType, largeGrid)];
      if(allOccupied.length === 1) console.log("HERES AN ISSUE", allOccupied)
      allOccupied.forEach(p => {
        pathStore[p.join(",")] = "blue";
      });
    })
  );

  let containedCells = 0;
  for (let y = 0; y < grid.length; y++) {
    let outputString = "";
    for (let x = 0; x < grid[y].length; x++) {
      pathEntry = pathStore[`${x * 3 + 1},${y * 3 + 1}`];
      if (pathEntry) {
        if(pathEntry === "red") {
          pathStore[`${x * 3 + 1},${y * 3 + 1}`] = "green";
          containedCells++;
        }
      } else {
        const path = aStar({
          start: [x * 3 + 1, y * 3 + 1],
          getNeighbours: (position) => {
            const neighbours = mapCoords(position[0], position[1], "S", largeGrid);
            return neighbours
              .filter(n => {
                return !pathStore[n.join(",")]
              });
          },
          isTarget: current => {
            const state = pathStore[current.position.join(",")]
            if (state != null) {
              return !state;
            }

            return current.position[0] === 0 || current.position[1] === 0
              || (current.position[0] === largeGrid[0].length - 1)
              || (current.position[1] === largeGrid.length - 1)
          },
          getHeuristic: position => {
            const xDist = largeGrid[0].length / 2 - Math.abs(largeGrid[0].length / 2 - position[0]);
            const yDist = largeGrid.length / 2 - Math.abs(largeGrid.length / 2 - position[1])
            return Math.min(xDist, yDist)
          },
          onFail: (closed) => {
            closed.forEach(p => {
              pathStore[p.join(",")] = "red";
            })
          }
        })

        if (path) {
          pathForEach(path, segment => {
            pathStore[segment.position.join(",")] = false;
          })
          outputString += grid[y][x]
        } else {
          containedCells++;
          pathStore[`${x * 3 + 1},${y * 3 + 1}`] = "green";
          outputString += withColor(grid[y][x], "green");
        }
      }
    }
  }

  for (let y = 0; y < largeGrid.length; y++) {
    console.log(
      largeGrid[y].map(v => v ? "□" : "·")
      .map((c, index) => pathStore[`${index},${y}`] ? withColor(c, pathStore[`${index},${y}`]) : c)
      .join("")
    )
  }


  return containedCells;
};

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

module.exports = input => {
  const grid = input.split("\n").filter(Boolean);

  function mapCoords(x, y, pipeType) {
    return pipeTypes[pipeType].map(mapper => mapper([x, y]))
      .filter(([x, y]) => !(x < 0 || y < 0 || x >= grid[0].length || y >= grid.length))
  }

  const map = [];
  let start;
  for (let y = 0; y < grid.length; y++) {
    map.push([])
    for (let x = 0; x < grid[y].length; x++) {
      const pipeType = grid[y][x]
      map[y].push(mapCoords(x, y, grid[y][x]))
      if (pipeType === "S") {
        start = [x, y]
      }
    }
  }
  const open = [{ position: start, score: 0, parent: null }]
  const closed = []
  const closedPaths = []
  while(open.length) {
    const current = open.shift();
    const neighbours = map[current.position[1]][current.position[0]];

    neighbours
      .filter(n => !closed.find(c => n[0] === c[0] && n[1] === c[1]))
      .filter(n => {
        const neighboursLinks = map[n[1]][n[0]];
        return neighboursLinks.find(nl => nl[0] === current.position[0] && nl[1] === current.position[1])
      })
      .forEach(n => {
      const score = current.score + 1;
      const openEntry = open.find(o => n[0] === o.position[0] && n[1] === o.position[1]);

      if (openEntry && openEntry.score > score) {
        openEntry.parent = current;
        openEntry.score = score;
      } else if (!openEntry) {
        open.push({ position: n, score, parent: current })
      }
    });
    open.sort((a, b) => (a.score) - (b.score));
    closed.push(current.position)
    closedPaths.push(current)
  }
  return closedPaths.sort((a, b) => (b.score) - (a.score))[0].score;

};

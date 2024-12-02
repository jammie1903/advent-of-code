
const directions = {
  north: ([x, y]) => [x, y - 1],
  south: ([x, y]) => [x, y + 1],
  east: ([x, y]) => [x + 1, y],
  west: ([x, y]) => [x - 1, y]
};

const sortBy = {
  north: (o1, o2) => o1.y - o2.y,
  south: (o1, o2) => o2.y - o1.y,
  east: (o1, o2) => o2.x - o1.x,
  west: (o1, o2) => o1.x - o2.x
};

function isValidCoordinate([x, y], map) {
  return x >= 0 && y >= 0 && x < map.width && y < map.height
}

class Boulder {
  static char = "#";
  constructor(map, x, y) {
    this.map = map;
    this.setPosition(x, y);
  }

  setPosition(x, y) {
    if (typeof this.x !== "undefined" && typeof this.y !== "undefined") {
      if (this.map[`${this.x},${this.y}`] !== this) {
        throw new Error("Previous space was occupied")
      }
      delete this.map[`${this.x},${this.y}`]
    }
    this.x = x;
    this.y = y;
    if (this.map[`${this.x},${this.y}`] && this.map[`${this.x},${this.y}`] !== this) {
      throw new Error("Space was occupied")
    }
    this.map[`${x},${y}`] = this;
  }

  getAt(x, y) {
    return this.map[`${x},${y}`] || null;
  }
}

class MovingBoulder extends Boulder {
  static char = "O";
  constructor(map, x, y) {
    super(map, x, y)
  }

  roll(direction = "north") {
    let finalLocation = null;
    let location = directions[direction]([this.x, this.y]);
    while (isValidCoordinate(location, this.map)) {
      const occupier = this.getAt(...location);
      if (occupier) {
        break;
      }
      finalLocation = location
      location = directions[direction](location)
    }
    if (finalLocation) {
      this.setPosition(...finalLocation)
    }
  }
}

function getChar(map, x, y) {
  const object = map[`${x},${y}`];
  if (!object) return ".";
  return object.constructor.char;
}

module.exports = input => {
  const grid = input.split("\n").filter(Boolean);
  const map = {
    width: grid[0].length,
    height: grid.length
  };
  const objects = []

  grid.forEach((r, y) => {
    Array.from(r).forEach((c, x) => {
      switch(c) {
        case "#": objects.push(new Boulder(map, x, y)); break
        case "O": objects.push(new MovingBoulder(map, x, y)); break;
      }
    })
  })

  let total = 0;

  const movingBoulders = objects.filter(object => object instanceof MovingBoulder)

  function drawMap() {
    return grid.map((r, y) =>
      Array.from(r).map((c, x) => getChar(map, x, y)).join("")
    ).join("\n")
  }

  let mapStore = {

  }
  let jumped = false;
  for(let i = 0; i < 1000000000; i++) {
    ["north", "west", "south", "east"].forEach(direction => {
      movingBoulders.sort(sortBy[direction])
      movingBoulders.forEach(object => {
        object.roll(direction);
      })
      console.log("--",i,direction,"--");
      console.log(drawMap())
    })

    total = 0;
    movingBoulders
    .forEach(object => {
      total += map.height - object.y - 1;
    })
    console.log("--","total","--");
    console.log("--",total,"--");
    if(total === 64) return

    const drawnMap = drawMap();
    if (!jumped) {
      if (mapStore[drawnMap] != null) {
        console.log(`at index ${i}, the result was the same as index ${mapStore[drawnMap]}`);
        const diff = i - mapStore[drawnMap]
        i = 1000000000 - diff + (i % diff);
        console.log(`new index is ${i}`);
        jumped = true;
      }
    }
    mapStore[drawnMap] = i;
  }

  total = 0;
  movingBoulders
    .forEach(object => {
      total += map.height - object.y - 1;
    })

  console.log("--","final","--");

  console.log(drawMap())


  return total;
}

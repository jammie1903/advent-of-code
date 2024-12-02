
const directions = {
  north: ([x, y]) => [x, y - 1],
  south: ([x, y]) => [x, y + 1],
  east: ([x, y]) => [x + 1, y],
  west: ([x, y]) => [x - 1, y]
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
      delete this.map[`${this.x},${this.y}`]
    }
    this.x = x;
    this.y = y;
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
  const grid = input.split("\n");
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

  objects.filter(object => object instanceof MovingBoulder)
    .forEach(object => {
      object.roll();
      total += map.height - object.y - 1;
    })

  grid.forEach((r, y) => {
    console.log(Array.from(r).map((c, x) => getChar(map, x, y)).join(""))
  })

  return total;
}

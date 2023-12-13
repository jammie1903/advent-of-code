module.exports = input => {
  const grid = input.split("\n").filter(Boolean);

  let stars = []
  for (let y = 0; y < grid.length; y++) {
    for (let x = 0; x < grid[y].length; x++) {
      const isStar = grid[y][x] === "#"
      if (isStar) {
        stars.push({ x, y })
      }
    }
  }
  for (let y = grid.length - 1; y >= 0; y--) {
    const rowHasStar = stars.some(star => star.y === y);
    if(!rowHasStar) {
      console.log(`row ${y} has no stars`)
      stars.filter(star => star.y > y)
        .forEach(star => {
          star.y += 999999;
        })
    }
  }

  for (let x = grid[0].length - 1; x >= 0; x--) {
    const columnHasStar = stars.some(star => star.x === x);
    if(!columnHasStar) {
      console.log(`column ${x} has no stars`)
      stars.filter(star => star.x > x)
        .forEach(star => {
          star.x += 999999;
        })
    }
  }
  let total = 0;
  stars.forEach((star, index) => {
    const remainingStars = stars.slice(index + 1);
    remainingStars.forEach(otherStar => {
      const xDist = Math.abs(star.x - otherStar.x);
      const yDist = Math.abs(star.y - otherStar.y);
      total += xDist + yDist;
    })
  })
  return total;
}

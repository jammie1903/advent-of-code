module.exports = input => {
  const mirrorSets = input.split("\n\n").map(m => m.split("\n"))
  let total = 0

  const verticalCompare = (mirrorSet, i1, i2) =>
    mirrorSet[i1] === mirrorSet[i2]

  const horizontalCompare = (mirrorSet, i1, i2) => {
    const column1 = mirrorSet.map(r => r[i1]).join();
    const column2 = mirrorSet.map(r => r[i2]).join();
    return column1 === column2;
  }

  console.log(mirrorSets.length)
  mirrorSets.forEach((mirrorSet, index) => {
    // console.log(mirrorSet)
    for(let i = 1; i < mirrorSet.length; i++) {
      let diff = 0;
      while (verticalCompare(mirrorSet, i + diff, i - 1 - diff)) {
        diff++;
        if ((i + diff >= mirrorSet.length) || (i - 1 - diff < 0)) {
          console.log(index, "vertical symmetry at indexes", i-1, i)
          total += 100 * i;
          break;
        }
      }
    }

    for(let i = 1; i < mirrorSet[0].length; i++) {
      let diff = 0;
      while (horizontalCompare(mirrorSet, i + diff, i - 1 - diff)) {
        diff++;
        if (i + diff >= mirrorSet[0].length || i - 1 - diff < 0) {
          console.log(index, "horizontal symmetry at indexes", i-1, i)
          total += i;
          break;
        }
      }
    }
  });
  return total;
}

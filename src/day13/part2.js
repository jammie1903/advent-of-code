module.exports = input => {
  const mirrorSets = input.split("\n\n").map(m => m.split("\n"))
  let total = 0

  const verticalDiff = (mirrorSet, i1, i2) =>
    mirrorSet[i1].split("").map((s, index) => s !== mirrorSet[i2][index] ? index : null).filter(i => i !== null)

  const horizontalDiff = (mirrorSet, i1, i2) => {
    const column1 = mirrorSet.map(r => r[i1]);
    const column2 = mirrorSet.map(r => r[i2]);
    return column1.map((s, index) => s !== column2[index] ? index : null).filter(i => i !== null)
  }

  console.log(mirrorSets.length)
  mirrorSets.forEach((mirrorSet, index) => {
    let invalidCell = null

    for(let i = 1; i < mirrorSet.length; i++) {
      let diff = 0;
      while ((i + diff < mirrorSet.length) && (i - 1 - diff >= 0)) {
        const invalidCells = verticalDiff(mirrorSet, i + diff, i - 1 - diff);
        if (invalidCells.length) {
          if(invalidCell || invalidCells.length > 1) {
            invalidCell = null;
            break;
          } else {
            invalidCell = [i + diff, invalidCells[0]]
          }
        }
        diff++;
      }
      if (invalidCell) {
        console.log(index, "new vertical symmetry at indexes", i-1, i)
        total += 100 * i;
        break;
      }
    }

    if (!invalidCell) {
      for(let i = 1; i < mirrorSet[0].length; i++) {
        let diff = 0;
        while ((i + diff < mirrorSet[0].length && i - 1 - diff >= 0)) {
          const invalidCells = horizontalDiff(mirrorSet, i + diff, i - 1 - diff);
          if (invalidCells.length) {
            if (invalidCell || invalidCells.length > 1) {
              invalidCell = null;
              break;
            } else {
              invalidCell = [invalidCells[0], i + diff]
            }
          }
          diff++;
        }
        if (invalidCell) {
          console.log(index, "new horizontal symmetry at indexes", i-1, i)
          total += i;
          break;
        }
      }
    }

    if(!invalidCell) {
      throw new Error(`invalid cell not found for array ${index}`)
    }
  });
  return total;
}

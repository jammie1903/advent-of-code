// Disclaimer: i recovered this code from my chromes console as /i only decided afterwards to preserve it.
// Therefore i cannot check that the solution is correct as its already submitted.
module.exports = input => {
  const lines = input.split("\n").filter(Boolean);
  let total = 0;
  lines.forEach((line, lineNumber) => {
    const regex = /\d+/g;
    let result = regex.exec(line);

    while (result) {
      const minRow = Math.max(0, lineNumber - 1);
      const maxRow = Math.min(lines.length - 1, lineNumber + 1);
      const minColumn = Math.max(0, result.index - 1);
      const maxColumn = Math.min(line.length - 1, result.index + result[0].length + 1);
      let symbolFound = false;
      for (let row = minRow; row <= maxRow; row++) {
        for (let column = minColumn; column <= maxColumn; column++) {
          const value = lines[row][column];
          if (!/[0-9\.]/.test(value)) {
            symbolFound = true;
          }
        }
      }
      if (symbolFound) total += Number(result);
      result = regex.exec(line);
    }
  });
  return total;
};

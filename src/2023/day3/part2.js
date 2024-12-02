// Disclaimer: i recovered this code from my chromes console as /i only decided afterwards to preserve it.
// Therefore i cannot check that the solution is correct as its already submitted.
module.exports = input => {
  const lines = input.split("\n").filter(Boolean);
  const gearMap = {};
  lines.forEach((line, lineNumber) => {
    const regex = /\d+/g;
    let result = regex.exec(line);

    while (result) {
      const minRow = Math.max(0, lineNumber - 1);
      const maxRow = Math.min(lines.length - 1, lineNumber + 1);
      const minColumn = Math.max(0, result.index - 1);
      const maxColumn = Math.min(line.length - 1, result.index + result[0].length);
      for (let row = minRow; row <= maxRow; row++) {
        for (let column = minColumn; column <= maxColumn; column++) {
          const value = lines[row][column];
          if (value === "*") {
            gearMap[`${column},${row}`] ||= [];
            gearMap[`${column},${row}`].push(Number(result[0]));
          }
        }
      }

      result = regex.exec(line);
    }
  });
  return Object.values(gearMap)
    .filter(a => a.length === 2)
    .map(a => a[0] * a[1])
    .reduce((a, b) => a + b);
};

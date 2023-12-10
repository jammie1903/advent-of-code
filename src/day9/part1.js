module.exports = input => {
  const lines = input.split("\n").filter(Boolean)

  return lines.map(line => {
    let data = line.split(" ").map(Number);
    let totals = data[data.length - 1];
    while(data.length && data.some(d => d !== 0)){
      const differences = [];
      for(let i = 0; i < data.length - 1; i++) {
        differences.push(data[i + 1] - data[i])
      }
      data = differences;
      totals += data[data.length - 1];
    }
    return totals;
  }).reduce((a, b) => a + b)
}

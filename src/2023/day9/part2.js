module.exports = input => {
  const lines = input.split("\n").filter(Boolean);

  return lines.map(line => {
    const startingData = line.split(" ").map(Number);
    let data = startingData;
    let stack = [];
    while(data.length && data.some(d => d !== 0)){
      const differences = [];
      for(let i = 0; i < data.length - 1; i++) {
        differences.push(data[i + 1] - data[i]);
      }
      data = differences;
      stack.unshift(data[0]);
    }
    const value = stack.reduce((acc, s) => s - acc);
    return startingData[0] - value;
  }).reduce((a, b) => a + b, 0)
}

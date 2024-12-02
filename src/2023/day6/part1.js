module.exports = input => {
  let [times, distances] = input
    .split("\n")
    .filter(Boolean)
    .map(c => c.split(/\s+/g).slice(1).map(Number));

  const races = times.map((time, index) => ({
    time,
    distance: distances[index]
  }));

  const allWins = races.map(({ time, distance }) => {
    let wins = 0;
    for(let i = 0; i <= time; i++) {
      if (i * (time - i) > distance) wins++;
    }
    return wins;
  });

  return allWins.reduce((a, b) => a * b);
};

module.exports = input => {
  let [time, distance] = input
    .split("\n")
    .filter(Boolean)
    .map(c => Number(c.split(/\s+/g).slice(1).join("")));

  let wins = 0;
  for(let i = 0; i <= time; i++) {
    if (i * (time - i) > distance) wins++;
  }
  return wins;
};

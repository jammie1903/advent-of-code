// Disclaimer: i recovered this code from my chromes console as /i only decided afterwards to preserve it.
// Therefore i cannot check that the solution is correct as its already submitted.
module.exports = input => {
  const cardCounts = {};
  input.split("\n")
    .filter(Boolean)
    .map((s, index) => {
      cardCounts[index] ||= 0;
      cardCounts[index]++;
      const winScore = cardCounts[index];
      let [winners, numbers] = s
        .substring(s.indexOf(":") + 1)
        .split("|")
        .map(a => a.split(/\s+/).filter(Boolean));
      const wins = numbers.filter(n => winners.includes(n)).length;
      for (let i = index + 1; i <= index + wins; i++) {
        cardCounts[i] ||= 0;
        cardCounts[i] += winScore;
      }
    });
    return Object.values(cardCounts).reduce((a,b) => a + b);
};

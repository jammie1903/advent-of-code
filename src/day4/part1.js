// Disclaimer: i recovered this code from my chromes console as /i only decided afterwards to preserve it.
// Therefore i cannot check that the solution is correct as its already submitted.
module.exports = input => {
  let total = 0;
  input
    .split("\n")
    .filter(Boolean)
    .map(s => {
      let [winners, numbers] = s
        .substring(s.indexOf(":") + 1)
        .split("|")
        .map(a => a.split(/\s+/).filter(Boolean));
      const matches = numbers.filter(n => winners.includes(n));
      const score = matches.length ? Math.pow(2, matches.length - 1) : 0;
      total += score;
    });
  return total;
};

// Disclaimer: i recovered this code from my chromes console as /i only decided afterwards to preserve it.
// Therefore i cannot check that the solution is correct as its already submitted.
module.exports = input => {
  let total = 0;

  input
    .split("\n")
    .filter(Boolean)
    .map(s => {
      let [id, picks] = s.split(":");
      picks = picks.split(";");
      picks = picks.flatMap(p => p.split(",").map(c => c.trim().split(" ")));
      id = id.substring(5);
      return { id, picks };
    })
    .forEach(({ id, picks }) => {
      const totals = {};
      picks.forEach(([count, type]) => {
        totals[type] = Math.max(totals[type] || 0, Number(count));
      });

      console.log(id, totals);
      total += Object.values(totals).reduce((a, b) => a * b);
    });
    return total;
};

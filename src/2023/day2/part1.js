// Disclaimer: i recovered this code from my chromes console as /i only decided afterwards to preserve it.
// Therefore i cannot check that the solution is correct as its already submitted.
module.exports = input => {
  const limits = { red: 12, green: 13, blue: 14 };
  let validTotal = 0;

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
      const invalid = picks.find(([count, type]) => {
        return limits[type] < Number(count);
      });
      if (!invalid) validTotal += Number(id);
    });
  return validTotal;
};

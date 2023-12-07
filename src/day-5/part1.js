module.exports = input => {
  let [seeds, ...maps] = input
    .split("\n\n")
    .filter(Boolean)
    .map(c => c.split("\n").filter(Boolean));

  seeds = seeds[0]
    .substring(seeds[0].indexOf(":") + 1)
    .trim()
    .split(" ")
    .map(Number);

  maps = maps.map(map => {
    const [, source, target] = /(\w+)-to-(\w+)/.exec(map[0]);
    const entries = map.slice(1).map(s => {
      const [destinationRangeStart, sourceRangeStart, rangeLength] = s.split(" ").map(Number);
      return {
        sourceMin: sourceRangeStart,
        sourceMax: sourceRangeStart + rangeLength - 1,
        change: destinationRangeStart - sourceRangeStart
      };
    });
    return {
      matches: ({ type }) => type === source,
      process: ({ type, value }) => {
        const matchingEntry = entries.find(e => e.sourceMin <= value && e.sourceMax >= value);
        return {
          type: target,
          value: value + (matchingEntry?.change || 0),
          matchingEntry
        };
      }
    };
  });

  const processor = seedValue => {
    let data = [{ value: seedValue, type: "seed" }];
    while (data[0].type !== "location") {
      const processor = maps.find(m => m.matches(data[0]));
      if (!processor) throw new Error("no processor found");
      data.unshift(processor.process(data[0]));
    }
    console.log(data);
    return data[0].value;
  };

  return seeds.map(processor).reduce((a, b) => (a < b ? a : b));
};

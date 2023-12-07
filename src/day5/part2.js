module.exports = input => {
  let [seeds, ...maps] = input
    .split("\n\n")
    .filter(Boolean)
    .map(c => c.split("\n").filter(Boolean));

  seeds = seeds[0]
    .substring(seeds[0].indexOf(":") + 1)
    .trim()
    .split(" ")
    .map(Number)
    .reduce((acc, v) => {
      if(!acc.length || "end" in acc[0]) {
        acc.unshift({ start: v });
      } else {
        acc[0].end =  acc[0].start + v - 1;
      }
      return acc
    }, []);


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
      process: (input) => {
        let queue = [...input.data];
        let output = []
        while(queue.length) {
          const data = queue.pop();
          const matchingEntry = entries.find(e => e.sourceMin <= data.end && e.sourceMax >= data.start);
          if(!matchingEntry) {
            output.push(data);
            continue;
          }
          const overlap = { start: Math.max(data.start, matchingEntry.sourceMin), end: Math.min(data.end, matchingEntry.sourceMax)  }
          if(overlap.start > data.start) {
            queue.push({ start: data.start, end: overlap.start - 1 })
          }
          if (overlap.end < data.end) {
            queue.push({ start: overlap.end + 1, end: data.end })
          }
          output.push({
            start: overlap.start + matchingEntry.change,
            end: overlap.end + matchingEntry.change
          })
        }
        return { type: target, data: output }
      }
    };
  });

  const runProcessors = seedValues => {
    let data = { data: seedValues, type: "seed" };
    while (data.type !== "location") {
      const processor = maps.find(m => m.matches(data));
      if (!processor) throw new Error("no processor found");
      data = processor.process(data);
    }
    return data.data;
  };

  const locations = runProcessors(seeds)
  return locations.map(l => l.start ).reduce((a, b) => (a < b ? a : b));
};

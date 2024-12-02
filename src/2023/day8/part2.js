module.exports = input => {
  const [directions, rawNodes] = input.split("\n\n");
  const nodes = rawNodes.split("\n").filter(Boolean).reduce((acc, rawNode) => {
    const [, input, L, R] = /(\w+) = \((\w+), (\w+)\)/.exec(rawNode)
    acc[input] = { L, R }
    return acc;
  }, {})

  let positions = Object.keys(nodes).filter(k => k.endsWith("A"));
  const patterns = positions.map((position) => {
    let count = 0;
    let hits = []
    while(hits.length < 2) {
      position = nodes[position][directions[count % directions.length]]
      count++;
      if(position.endsWith("Z")) {
        hits.push(count)
      }
    }
    return { offset: hits[0], repeat: hits[1] }
  });
  const largestPattern = patterns.reduce((p1, p2) => p1.repeat > p2.repeat ? p1 : p2)
  console.log(patterns);
  let n;
  for(n = largestPattern.offset; patterns.some(p => !Number.isInteger((n - p.offset) / p.repeat)); n += largestPattern.repeat) {

  }
  return n;
}

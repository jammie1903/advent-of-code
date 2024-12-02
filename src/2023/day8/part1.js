module.exports = input => {
  const [directions, rawNodes] = input.split("\n\n");
  const nodes = rawNodes.split("\n").filter(Boolean).reduce((acc, rawNode) => {
    const [, input, L, R] = /(\w+) = \((\w+), (\w+)\)/.exec(rawNode)
    acc[input] = { L, R }
    return acc;
  }, {})

  let position = "AAA"
  let count = 0;
  while(position !== "ZZZ") {
    position = nodes[position][directions[count % directions.length]]
    count++;
  }
  return count;
}

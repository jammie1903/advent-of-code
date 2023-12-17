module.exports = input => {
  const lines = input
    .split("\n")
    .filter(Boolean)
    .map(line => {
      const [data, pattern] = line.split(" ");
      return {
        data: Array(5).fill(data).join("?"),
        pattern: Array(5).fill(pattern).join(",")
      };
    });
  let total = 0;
  lines.forEach(({ data, pattern }) => {
    const possibleSpringGroups = data.split(/\.+/).filter(Boolean);
    const highestGroupSize = pattern.split(",").map(Number).reduce((a, b) => Math.max(a, b))
    let comparison = "startsWith"
    const sequentialGroups = possibleSpringGroups.reduce((acc, group) => {
      let possibilities = { "": 1 }
      group.split("").forEach(char => {
        const newPoss = {};

        const process = (sequence, count) => {
          const endsInNumber = /\d/.test(sequence[sequence.length - 1])
          if (endsInNumber && Number(sequence[sequence.length - 1]) > highestGroupSize) return;
          const str = sequence.join("");
          const compString = str.substring(0, str.length - 1);
          if (pattern[comparison](compString)) {
            newPoss[str] ||= 0;
            newPoss[str] += count;
          }
        }

        Object.entries(possibilities).forEach(([p, count]) => {
          const arr = p.split("");
          let endsInNumber = /\d/.test(arr[arr.length - 1])
          if (char === "?") {
            const copy = [...arr];
            if (endsInNumber) {
              copy.push(",")
            }
            process(copy, count);
          }

          if (endsInNumber) {
            arr[arr.length - 1] = Number(arr[arr.length - 1]) + 1;
          } else {
            arr.push(1)
            endsInNumber = true
          }
          process(arr, count);
        })
        possibilities = newPoss;
      });

      possibilities = Object.entries(possibilities).reduce((acc, [sequence, count]) => {
        const trimmedSequence = sequence.endsWith(",") ? sequence.substring(0, sequence.length - 1) : sequence;
        acc[trimmedSequence] ||= 0;
        acc[trimmedSequence] += count;
        return acc;
      }, {})

      if(Object.keys(acc).length === 0) {
        acc[""] = 1;
      }
      const returnObject = {};
      Object.entries(acc).forEach(([partialPattern, count]) => {
        Object.entries(possibilities).forEach(([possibilityPattern, count2]) => {
          const combinedPattern = [partialPattern, possibilityPattern].filter(Boolean).join(",");
          if (pattern.startsWith(combinedPattern)) {
            returnObject[combinedPattern] ||= 0;
            returnObject[combinedPattern] += count * count2;
          }
        })
      })
      comparison = "includes"
      return returnObject
    }, { });
    console.log("result", sequentialGroups)
    console.log("result", sequentialGroups[pattern])
    total += sequentialGroups[pattern] || 0;
    // total += possibilities.filter(p =>
    //   p.split(/\.+/).filter(Boolean).map(s => s.length).join(",") === pattern
    // ).length
  });
  return total;
};
